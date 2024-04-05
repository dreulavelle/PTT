import regex

# Importing transformations from transformers.py
from .transformers import none

# Constants
NON_ENGLISH_CHARS = "\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f\u0400-\u04ff"
RUSSIAN_CAST_REGEX = regex.compile(r"\([^)]*[\u0400-\u04ff][^)]*\)$|(?<=\/.*)\(.*\)$")
ALT_TITLES_REGEX = regex.compile(rf"[^/|(]*[{NON_ENGLISH_CHARS}][^/|]*[/|]|[/|][^/|(]*[{NON_ENGLISH_CHARS}][^/|]*", regex.IGNORECASE)
NOT_ONLY_NON_ENGLISH_REGEX = regex.compile(rf"(?<=[a-zA-Z][^{NON_ENGLISH_CHARS}]+)[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}]|[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}](?=[^{NON_ENGLISH_CHARS}]+[a-zA-Z])", regex.IGNORECASE)
NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#[【★]+|[ \-:/\\[|{{(#$&^]+$", regex.IGNORECASE)
REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#]+|]$", regex.IGNORECASE)

def extend_options(options):
    default_options = {
        'skipIfAlreadyFound': True,
        'skipFromTitle': False,
        'skipIfFirst': False,
        'remove': False
    }
    for key, value in default_options.items():
        options.setdefault(key, value)
    return options

def create_handler_from_regex(name, reg_exp, transformer=none, options=None):
    if options is None:
        options = {}
    options = extend_options(options)

    def handler(title, result, matched):
        if name in result and options['skipIfAlreadyFound']:
            return None

        match = reg_exp.search(title)
        if match:
            raw_match, clean_match = match.group(0), match.group(0)
            transformed = transformer(clean_match, result.get(name))
            is_before_title = bool(regex.match(r"^\[([^[\]]+)]", title) and raw_match in title)
            other_matches = [(k, v) for k, v in matched.items() if k != name]
            is_skip_if_first = options['skipIfFirst'] and other_matches and all(match.start() < m[1]['matchIndex'] for m in other_matches)

            if transformed and not is_skip_if_first:
                matched[name] = {'rawMatch': raw_match, 'matchIndex': match.start()}
                result[name] = options.get('value') or transformed
                return {
                    'rawMatch': raw_match,
                    'matchIndex': match.start(),
                    'remove': options['remove'],
                    'skipFromTitle': is_before_title or options['skipFromTitle']
                }
        return None

    handler.__name__ = name
    return handler

def clean_title(raw_title):
    cleaned_title = raw_title.replace(".", " ") if " " not in raw_title and "." in raw_title else raw_title
    cleaned_title = (cleaned_title.replace("_", " ")
                     .replace(regex.compile(r"\[(movie)\]", regex.IGNORECASE), "")
                     .replace(NOT_ALLOWED_SYMBOLS_AT_START_AND_END, "")
                     .replace(RUSSIAN_CAST_REGEX, "")
                     .replace(regex.compile(r"^[[【★].*[\]】★][ .]?(.+)", regex.IGNORECASE), r"\1")
                     .replace(regex.compile(r"(.+)[ .]?[[【★].*[\]】★]$", regex.IGNORECASE), r"\1")
                     .replace(ALT_TITLES_REGEX, "")
                     .replace(NOT_ONLY_NON_ENGLISH_REGEX, "")
                     .replace(REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END, "")
                     .strip())
    return cleaned_title

class Parser:
    def __init__(self):
        self.handlers = []

    def add_handler(self, handler_name, handler=None, transformer=None, options=None):
        if handler is None and callable(handler_name):
            # If no name is provided and a function handler is directly given
            handler = handler_name
            handler.__name__ = "unknown"
        elif isinstance(handler_name, str) and isinstance(handler, regex.Pattern):
            # If the handler provided is a regular expression
            transformer = transformer if callable(transformer) else none
            options = extend_options(transformer if isinstance(transformer, dict) else options)
            handler = create_handler_from_regex(handler_name, handler, transformer, options)
        elif callable(handler):
            # If the handler is a function
            handler.__name__ = handler_name
        else:
            # If the handler is neither a function nor a regular expression, throw an error
            raise ValueError(f"Handler for {handler_name} should be a regex.Pattern or a function. Got: {type(handler)}")

        self.handlers.append(handler)

    def parse(self, title):
        title = title.replace("_", " ")
        result = {}
        matched = {}
        end_of_title = len(title)

        for handler in self.handlers:
            match_result = handler(title, result, matched)
            if match_result and match_result['remove']:
                title = title[:match_result['matchIndex']] + title[match_result['matchIndex'] + len(match_result['rawMatch']):]
            if match_result and not match_result.get('skipFromTitle') and match_result.get('matchIndex', 0) < end_of_title:
                end_of_title = match_result['matchIndex']
            if match_result and match_result['remove'] and match_result.get('skipFromTitle') and match_result.get('matchIndex', 0) < end_of_title:
                end_of_title -= len(match_result['rawMatch'])

        result['title'] = clean_title(title[:end_of_title])

        return result
