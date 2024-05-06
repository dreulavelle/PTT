import inspect
from typing import Any
import regex

from .transformers import none

NON_ENGLISH_CHARS = "\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f\u0400-\u04ff"
RUSSIAN_CAST_REGEX = regex.compile(r"\([^)]*[\u0400-\u04ff][^)]*\)$|(?<=\/.*)\(.*\)$")
ALT_TITLES_REGEX = regex.compile(rf"[^/|(]*[{NON_ENGLISH_CHARS}][^/|]*[/|]|[/|][^/|(]*[{NON_ENGLISH_CHARS}][^/|]*")
NOT_ONLY_NON_ENGLISH_REGEX = regex.compile(
    rf"(?<=[a-zA-Z][^{NON_ENGLISH_CHARS}]+)[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}]|[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}](?=[^{NON_ENGLISH_CHARS}]+[a-zA-Z])")
NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#[【★]+|[ \-:/\\[|{{(#$&^]+$")
REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#]+|]$")

DEBUG_HANDLER = "seasons"


def extend_options(options=None):
    """Extend the options dictionary with default values."""
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


def create_handler_from_regexp(name, reg_exp, transformer, options):
    """Create a handler function from a regular expression pattern."""
    def handler(context):
        title = context['title']
        result = context['result']
        matched = context['matched']

        if name in result and options.get('skipIfAlreadyFound', False):
            return None

        # if name == DEBUG_HANDLER:
        #     print(f"Regexp Pattern: {reg_exp.pattern}")
        #     print(f"Title: {title}")

        match = reg_exp.search(title)
        # if name == DEBUG_HANDLER:
        #     print(f"Match: {match}")
        if match:
            raw_match = match.group(0)
            clean_match = match.group(1) if len(match.groups()) >= 1 else raw_match
            sig = inspect.signature(transformer)
            param_count = len(sig.parameters)
            transformed = transformer(clean_match or raw_match, *([result.get(name)] if param_count > 1 else []))

            before_title_match = regex.match(r'^\[([^[\]]+)]', title) # or '^\[([^\[\]]+)]'
            is_before_title = before_title_match is not None and raw_match in before_title_match.group(1)

            other_matches = {k: v for k, v in matched.items() if k != name}
            # if name == DEBUG_HANDLER:
            #     print(f"Other Matches: {other_matches}")
            is_skip_if_first = options.get('skipIfFirst', False) and other_matches and all(
                match.start() < other_matches[k]['match_index'] for k in other_matches
            )
            # is_skip_if_first = False

            if transformed is not None and not is_skip_if_first:
                matched[name] = matched.get(name, {'raw_match': raw_match, 'match_index': match.start()})
                result[name] = options.get('value', transformed)
                return {
                    'raw_match': raw_match,
                    'match_index': match.start(),
                    'remove': options.get('remove', False),
                    'skip_from_title': is_before_title or options.get('skipFromTitle', False)
                }
        return None

    handler.__name__ = name
    handler.handler_name = name
    return handler


def clean_title(raw_title):
    """Clean up a title string by removing unwanted characters and patterns."""
    cleaned_title = raw_title

    if " " not in cleaned_title and "." in cleaned_title:
        cleaned_title = regex.sub(r"\.", " ", cleaned_title)

    cleaned_title = regex.sub(r"_", " ", cleaned_title)
    cleaned_title = regex.sub(r"[[(]movie[)\]]", "", cleaned_title, flags=regex.IGNORECASE)
    cleaned_title = NOT_ALLOWED_SYMBOLS_AT_START_AND_END.sub("", cleaned_title)
    cleaned_title = RUSSIAN_CAST_REGEX.sub("", cleaned_title)
    # maybe [\[\[【★].*[\]】★][ .]?(.+)
    cleaned_title = regex.sub(r"^[[【★].*[\]】★][ .]?(.+)", r"\1", cleaned_title)
    cleaned_title = regex.sub(r"(.+)[ .]?[[【★].*[\]】★]$", r"\1", cleaned_title)
    cleaned_title = ALT_TITLES_REGEX.sub("", cleaned_title)
    cleaned_title = NOT_ONLY_NON_ENGLISH_REGEX.sub("", cleaned_title)
    cleaned_title = REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END.sub("", cleaned_title)

    # Trim the resulting title
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
        self.handlers: list = []

    def add_handler(self, handler_name, handler, transformer=None, options=None):

        if not handler and callable(handler_name):
            handler = handler_name
            handler.handler_name = "unknown"
        elif type(handler_name) == str and type(handler) == regex.Pattern:
            transformer = transformer if callable(transformer) else none
            options = extend_options(transformer if type(transformer) == dict else options)
            handler = create_handler_from_regexp(handler_name, handler, transformer, options)
        elif type(handler_name) == str and callable(handler):
            handler.handler_name = handler_name
        else:
            raise ValueError(
                f"Handler for {handler_name} should be either a regex pattern or a function. Got {type(handler)}")

        self.handlers.append(handler)

    def parse(self, title: str) -> dict: # type: ignore
        """Parse a release title and return the parsed data as a dictionary."""
        title: str = regex.sub(r"_+", " ", title)
        result: dict[str, Any] = {}
        matched: dict[str, Any] = {}
        end_of_title: int = len(title)

        for handler in self.handlers:
            match_result = handler(
                {
                    "title": title,
                    "result": result,
                    "matched": matched
                }
            )

            # if handler.handler_name == DEBUG_HANDLER:
            #     print(f"Result: {match_result}")
            #
            # if DEBUG_HANDLER:
            #     print(handler.handler_name)
            #     print("Title before: " + title)

            if match_result is None:
                # if DEBUG_HANDLER:
                #     print("Title after: " + title)
                #     print(end_of_title)
                continue

            if match_result.get('remove', False):
                title = title[:match_result['match_index']] + title[match_result['match_index'] + len(
                    match_result['raw_match']):]
            if not match_result.get('skip_from_title') and match_result.get('match_index') and match_result[
                'match_index'] < end_of_title:
                end_of_title = match_result['match_index']
            if match_result.get('remove') and match_result.get('skip_from_title') and match_result[
                'match_index'] < end_of_title:
                # adjust title index in case part of it should be removed and skipped
                end_of_title -= len(match_result.get("raw_match", ""))

            # if DEBUG_HANDLER:
            #     print("Title after: " + title)
            #     print(end_of_title)

        if not result.get("episodes"):
            result["episodes"] = []
        if not result.get("seasons"):
            result["seasons"] = []
        if not result.get("languages"):
            result["languages"] = []

        # Clean the title up to end_of_title before further processing.
        title: str = title[:end_of_title]
        result["title"] = clean_title(title)
        return result
