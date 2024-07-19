import inspect
from typing import Any, Callable, Dict, List, Union

import regex

from .transformers import none

# Non-English characters range
NON_ENGLISH_CHARS = (
    "\u3040-\u30ff"  # Japanese characters
    "\u3400-\u4dbf"  # Chinese characters
    "\u4e00-\u9fff"  # Chinese characters
    "\uf900-\ufaff"  # CJK Compatibility Ideographs
    "\uff66-\uff9f"  # Halfwidth Katakana Japanese characters
    "\u0400-\u04ff"  # Cyrillic characters (Russian)
    "\u0600-\u06ff"  # Arabic characters
    "\u0750-\u077f"  # Arabic characters
    "\u0c80-\u0cff"  # Kannada characters
    "\u0d00-\u0d7f"  # Malayalam characters
    "\u0e00-\u0e7f"  # Thai characters
)

CURLY_BRACKETS = ["{", "}"]
SQUARE_BRACKETS = ["[", "]"]
PARENTHESES = ["(", ")"]
BRACKETS = [CURLY_BRACKETS, SQUARE_BRACKETS, PARENTHESES]

RUSSIAN_CAST_REGEX = regex.compile(r"\([^)]*[\u0400-\u04ff][^)]*\)$|(?<=\/.*)\(.*\)$")
ALT_TITLES_REGEX = regex.compile(rf"[^/|(]*[{NON_ENGLISH_CHARS}][^/|]*[/|]|[/|][^/|(]*[{NON_ENGLISH_CHARS}][^/|]*")
NOT_ONLY_NON_ENGLISH_REGEX = regex.compile(rf"(?<=[a-zA-Z][^{NON_ENGLISH_CHARS}]+)[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}]|[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}](?=[^{NON_ENGLISH_CHARS}]+[a-zA-Z])")
NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#[【★]+|[ \-:/\\[|{{(#$&^]+$")
REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#]+|]$")

DEBUG_HANDLER = False


def extend_options(options: Dict[str, Any] = None) -> Dict[str, Any]:
    """
    Extend the options dictionary with default values.

    :param options: The original options dictionary.
    :return: The extended options dictionary.
    """
    default_options = {
        "skipIfAlreadyFound": True,
        "skipFromTitle": False,
        "skipIfFirst": False,
        "remove": False,
    }
    if options is None:
        options = {}
    for key, value in default_options.items():
        options.setdefault(key, value)
    return options


def create_handler_from_regexp(name: str, reg_exp: regex.Pattern, transformer: Callable, options: Dict[str, Any]) -> Callable:
    """
    Create a handler function from a regular expression pattern.

    :param name: The name of the handler.
    :param reg_exp: The regular expression pattern.
    :param transformer: The transformer function to process the match.
    :param options: Additional options for the handler.
    :return: The handler function.
    """

    def handler(context: Dict[str, Any]) -> Union[Dict[str, Any], None]:
        title = context["title"]
        result = context["result"]
        matched = context["matched"]

        if name in result and options.get("skipIfAlreadyFound", False):
            return None

        match = reg_exp.search(title)
        if match:
            raw_match = match.group(0)
            clean_match = match.group(1) if len(match.groups()) >= 1 else raw_match
            sig = inspect.signature(transformer)
            param_count = len(sig.parameters)
            transformed = transformer(clean_match or raw_match, *([result.get(name)] if param_count > 1 else []))
            if type(transformed) is str:
                transformed = transformed.strip()

            before_title_match = regex.match(r"^\[([^[\]]+)]", title)
            is_before_title = before_title_match is not None and raw_match in before_title_match.group(1)

            other_matches = {k: v for k, v in matched.items() if k != name}
            is_skip_if_first = options.get("skipIfFirst", False) and other_matches and all(match.start() < other_matches[k]["match_index"] for k in other_matches)

            if transformed is not None and not is_skip_if_first:
                matched[name] = matched.get(name, {"raw_match": raw_match, "match_index": match.start()})
                result[name] = options.get("value", transformed)
                return {"raw_match": raw_match, "match_index": match.start(), "remove": options.get("remove", False), "skip_from_title": is_before_title or options.get("skipFromTitle", False)}
        return None

    handler.__name__ = name
    handler.handler_name = name
    return handler


def clean_title(raw_title: str) -> str:
    """
    Clean up a title string by removing unwanted characters and patterns.

    :param raw_title: The raw title string.
    :return: The cleaned title string.
    """
    cleaned_title = raw_title

    if " " not in cleaned_title and "." in cleaned_title:
        cleaned_title = regex.sub(r"\.", " ", cleaned_title)

    cleaned_title = regex.sub(r"_", " ", cleaned_title)
    cleaned_title = regex.sub(r"[[(]movie[)\]]", "", cleaned_title, flags=regex.IGNORECASE)
    cleaned_title = NOT_ALLOWED_SYMBOLS_AT_START_AND_END.sub("", cleaned_title)
    cleaned_title = RUSSIAN_CAST_REGEX.sub("", cleaned_title)
    cleaned_title = regex.sub(r"^[[【★].*[\]】★][ .]?(.+)", r"\1", cleaned_title)
    cleaned_title = regex.sub(r"(.+)[ .]?[[【★].*[\]】★]$", r"\1", cleaned_title)
    cleaned_title = ALT_TITLES_REGEX.sub("", cleaned_title)
    cleaned_title = NOT_ONLY_NON_ENGLISH_REGEX.sub("", cleaned_title)
    cleaned_title = REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END.sub("", cleaned_title)

    # Remove brackets if only one is present
    for brackets in BRACKETS:
        only_one_bracket = not all(bracket in cleaned_title for bracket in brackets)
        if only_one_bracket:
            for bracket in brackets:
                cleaned_title = cleaned_title.replace(bracket, "")

    if " " not in cleaned_title and "." in cleaned_title:
        cleaned_title = regex.sub(r"\.", " ", cleaned_title)

    cleaned_title = cleaned_title.strip()
    return cleaned_title


class Parser:
    """
    A parser that can parse release titles using a set of handlers.

    The parser can be used to parse release titles using a set of handlers. Each handler is a function that takes a
    title and returns a dictionary with the parsed data. The parser will iterate over all handlers and return the first
    non-None result.

    The parser can be extended with new handlers using the add_handler method. The handler can be a function or a
    regular expression pattern. If a regular expression pattern is used, the parser will use the first group as the
    match to be transformed by the transformer function.

    Example:
        >>> parser = Parser()
        >>> parser.add_handler("seasons", r"Season (\\d+)", int)
        >>> parser.add_handler("episodes", r"Episode (\\d+)", int)
        >>> parser.add_handler("languages", r"(English|Spanish|French)", str)
        >>> result = parser.parse("The Simpsons Season 1 Episode 1 English")
        >>> print(result)
    """

    def __init__(self):
        self.handlers: List[Callable] = []

    def add_handler(self, handler_name: str, handler: Union[Callable, regex.Pattern] = None, transformer: Callable = None, options: Dict[str, Any] = None):
        """
        Add a handler to the parser. The handler can be a function or a regular expression pattern.

        :param handler_name: The name of the handler.
        :param handler: The handler function or regex pattern.
        :param transformer: The transformer function to process the match.
        :param options: Additional options for the handler.
        """
        if handler is None and callable(handler_name):
            handler = handler_name
            handler.handler_name = handler_name.__name__ if hasattr(handler_name, "__name__") else "unknown"
        elif isinstance(handler_name, str) and isinstance(handler, regex.Pattern):
            transformer = transformer if callable(transformer) else none
            options = extend_options(options if isinstance(options, dict) else {})
            handler = create_handler_from_regexp(handler_name, handler, transformer, options)
        elif isinstance(handler_name, str) and callable(handler):
            handler.handler_name = handler_name
        else:
            raise ValueError(f"Handler for {handler_name} should be either a regex pattern or a function. Got {type(handler)}")

        self.handlers.append(handler)

    def parse(self, title: str) -> Dict[str, Any]:
        """
        Parse a release title and return the parsed data as a dictionary.

        :param title: The release title to parse.
        :return: A dictionary containing the parsed data.
        """
        title = regex.sub(r"_+", " ", title)
        result: Dict[str, Any] = {}
        matched: Dict[str, Any] = {}
        end_of_title = len(title)

        for handler in self.handlers:
            match_result = handler({"title": title, "result": result, "matched": matched})

            if DEBUG_HANDLER is True or (type(DEBUG_HANDLER) is str and DEBUG_HANDLER in handler.handler_name):
                print(handler.handler_name, match_result, title)

            if match_result is None:
                continue

            match_index = match_result.get("match_index")
            raw_match = match_result.get("raw_match", "")
            remove = match_result.get("remove", False)
            skip_from_title = match_result.get("skip_from_title", False)

            if remove:
                title = title[:match_index] + title[match_index + len(raw_match) :]
            if not skip_from_title and match_index and match_index < end_of_title:
                end_of_title = match_index
            if remove and skip_from_title and match_index < end_of_title:
                end_of_title -= len(raw_match)

        result.setdefault("episodes", [])
        result.setdefault("seasons", [])
        result.setdefault("languages", [])

        # Clean the title up to end_of_title before further processing.
        title = title[:end_of_title]
        result["title"] = clean_title(title)
        return result
