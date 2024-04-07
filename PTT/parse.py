from typing import Any, Dict
import regex
from .transformers import none


NON_ENGLISH_CHARS = "\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff\uff66-\uff9f\u0400-\u04ff"
RUSSIAN_CAST_REGEX = regex.compile(r"\([^)]*[\u0400-\u04ff][^)]*\)$|(?<=\/.*)\(.*\)$")
ALT_TITLES_REGEX = regex.compile(rf"[^/|(]*[{NON_ENGLISH_CHARS}][^/|]*[/|]|[/|][^/|(]*[{NON_ENGLISH_CHARS}][^/|]*")
NOT_ONLY_NON_ENGLISH_REGEX = regex.compile(rf"(?<=[a-zA-Z][^{NON_ENGLISH_CHARS}]+)[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}]|[{NON_ENGLISH_CHARS}].*[{NON_ENGLISH_CHARS}](?=[^{NON_ENGLISH_CHARS}]+[a-zA-Z])")
NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#[【★]+|[ \-:/\\[|{{(#$&^]+$")
REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END = regex.compile(rf"^[^\w{NON_ENGLISH_CHARS}#]+|]$")


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

def create_handler_from_regexp(name, reg_exp, transformer, options):
    def handler(context):
        title = context['title']
        result = context['result']
        matched = context['matched']

        if name in result and options.get('skipIfAlreadyFound', False):
            return None

        match = reg_exp.search(title)
        if match:
            raw_match = match.group(0)
            clean_match = match.group(1) if len(match.groups()) >= 1 else raw_match
            transformed = transformer(clean_match, result.get(name, None))
            
            before_title_match = regex.match(r'^\[([^\[\]]+)]', title)
            is_before_title = before_title_match is not None and raw_match in before_title_match.group(1)
            
            other_matches = {k: v for k, v in matched.items() if k != name}
            is_skip_if_first = options.get('skipIfFirst', False) and other_matches and all(
                match.start() < other_matches[k]['match_index'] for k in other_matches
            )

            if transformed is not None and not is_skip_if_first:
                matched[name] = {'raw_match': raw_match, 'match_index': match.start()}
                result[name] = options.get('value', transformed)
                return {
                    'raw_match': raw_match,
                    'match_index': match.start(),
                    'remove': options.get('remove', False),
                    'skip_from_title': is_before_title or options.get('skipFromTitle', False)
                }
        return None
    
    handler.__name__ = name
    return handler

def clean_title(raw_title):
    cleaned_title = raw_title

    if " " not in cleaned_title and "." in cleaned_title:
        cleaned_title = regex.sub(r"\.", " ", cleaned_title)

    cleaned_title = regex.sub(r"_", " ", cleaned_title)
    cleaned_title = regex.sub(r"\[movie\]", "", cleaned_title, flags=regex.IGNORECASE)
    cleaned_title = NOT_ALLOWED_SYMBOLS_AT_START_AND_END.sub("", cleaned_title)
    cleaned_title = RUSSIAN_CAST_REGEX.sub("", cleaned_title)
    cleaned_title = ALT_TITLES_REGEX.sub("", cleaned_title)
    cleaned_title = NOT_ONLY_NON_ENGLISH_REGEX.sub("", cleaned_title)
    cleaned_title = REMAINING_NOT_ALLOWED_SYMBOLS_AT_START_AND_END.sub("", cleaned_title)

    # Trim the resulting title
    cleaned_title = cleaned_title.strip()
    return cleaned_title


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
        title = regex.sub(r"_+", " ", title)
        result: Dict[str, Any] = {"seasons": [], "episodes": [], "languages": []}  # Default values for seasons and episodes
        matched = {}
        end_of_title = len(title)

        for handler in self.handlers:
            options = handler["options"]
            match = handler["pattern"].search(title)
            if match:
                raw_match = match.group(0)
                clean_match = match.group(1) if len(match.groups()) >= 1 else None
                transformed_match = raw_match if clean_match is None else clean_match
                if handler["transformer"]:
                    transformed = handler["transformer"](transformed_match)
                else:
                    transformed = transformed_match
                
                # If the handler demands removal, adjust the title and end_of_title accordingly.
                if options.get("remove", False) and match.start() < end_of_title:
                    title = title[:match.start()] + title[match.end():]
                    end_of_title -= len(raw_match)

                # Save matched data and result.
                matched[handler["name"]] = {"raw_match": raw_match, "match_index": match.start()}
                result[handler["name"]] = transformed

                # If skipping from title, adjust the title and potentially end_of_title.
                if options.get("skipFromTitle", False) and match.start() < end_of_title:
                    title = title.replace(raw_match, "", 1)
                    end_of_title = min(end_of_title, match.start())

        # Clean the title up to end_of_title before further processing.
        title = title[:end_of_title]
        result["title"] = clean_title(title)
        return result


