import regex
from .transformers import none


NON_ENGLISH_CHARS = "\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f\u0400-\u04ff"
RUSSIAN_CAST_REGEX = regex.compile(r"\([^)]*[\u0400-\u04ff][^)]*\)$|(?<=\/.*)\(.*\)$")
ALT_TITLES_REGEX = regex.compile(rf"[^/|(]*[{NON_ENGLISH_CHARS}][^/|]*[/|]|[/|][^/|(]*[{NON_ENGLISH_CHARS}][^/|]*", regex.IGNORECASE)
NOT_ONLY_NON_ENGLISH_REGEX = regex.compile(rf"(?<=[a-zA-Z][^{NON_ENGLISH_CHARS}]+)[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}]|[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}](?=[^{NON_ENGLISH_CHARS}]+[a-zA-Z])", regex.IGNORECASE)
NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#[【★]+|[ \-:/\\[|{{(#$&^]+$", regex.IGNORECASE)
REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#]+|]$", regex.IGNORECASE)


def extend_options(options=None):
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

def create_handler_from_regexp(name, reg_exp, transformer=None, options=None):
    options = extend_options(options)

    def handler(context):
        title, result, matched = context["title"], context["result"], context["matched"]
        if name in result and options["skipIfAlreadyFound"]:
            return None

        match = reg_exp.search(title)
        if match:
            raw_match = match.group(0)
            clean_match = match.group(1) if len(match.groups()) >= 1 else raw_match
            transformed = transformer(clean_match, result.get(name)) if transformer else clean_match
            before_title_match = regex.match(r"^\[([^\[\]]+)]", title)
            is_before_title = bool(before_title_match) and raw_match in before_title_match.group(1)
            other_matches = {k: v for k, v in matched.items() if k != name}
            is_skip_if_first = options["skipIfFirst"] and other_matches and all(
                match.start() < v["matchIndex"] for v in other_matches.values()
            )
            if transformed and not is_skip_if_first:
                matched[name] = {"rawMatch": raw_match, "matchIndex": match.start()}
                result[name] = transformed
                return {
                    "rawMatch": raw_match,
                    "matchIndex": match.start(),
                    "remove": options["remove"],
                    "skipFromTitle": is_before_title or options["skipFromTitle"],
                }
        return None
    return handler

def clean_title(raw_title):
    cleaned_title = raw_title.replace(".", " ") if " " not in raw_title and "." in raw_title else raw_title
    cleaned_title = regex.sub(r"_(movie)_", "", cleaned_title, flags=regex.IGNORECASE)
    cleaned_title = NOT_ALLOWED_SYMBOLS_AT_START_AND_END.sub("", cleaned_title)
    cleaned_title = RUSSIAN_CAST_REGEX.sub("", cleaned_title)
    cleaned_title = ALT_TITLES_REGEX.sub("", cleaned_title)
    cleaned_title = NOT_ONLY_NON_ENGLISH_REGEX.sub("", cleaned_title)
    cleaned_title = REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END.sub("", cleaned_title)
    return cleaned_title.strip()

class Parser:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler_name, pattern, transformer=None, options=None):
        # Ensure the pattern is compiled into a regex pattern for efficiency.
        compiled_pattern = regex.compile(pattern)
        self.handlers.append({
            "name": handler_name,
            "pattern": compiled_pattern,
            "transformer": transformer,
            "options": options or {}
        })

    def parse(self, title):
        title = title.replace("_", " ")
        result = {}
        matched = {}

        for handler in self.handlers:
            options = handler["options"]
            match = handler["pattern"].search(title)
            if match:
                raw_match = match.group(0)
                clean_match = match.group(1) if len(match.groups()) >= 1 else None
                # Adjust title if necessary, based on handler options
                if options.get("remove", False):
                    title = title[:match.start()] + title[match.end():]
                # Process transformation if transformer is provided
                # If there's no capturing group, pass the whole match; otherwise, pass the capturing group.
                transformed_match = raw_match if clean_match is None else clean_match
                if handler["transformer"]:
                    transformed = handler["transformer"](transformed_match)
                else:
                    transformed = transformed_match
                result[handler["name"]] = transformed
                matched[handler["name"]] = {"raw_match": raw_match, "match_index": match.start()}

        # Clean and finalize the title based on handlers' actions
        result["title"] = clean_title(title)
        return result

    @staticmethod
    def clean_title(title):
        # Your cleanTitle logic here
        # For example:
        cleaned_title = title.strip()
        # Add any specific cleaning logic required
        return cleaned_title