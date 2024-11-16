from .handlers import add_defaults
from .parse import Parser

_parser = Parser()
add_defaults(_parser)


def parse_title(raw_title: str, translate_languages: bool = False) -> dict:
    """
    Parse the given input string using the initialized parser instance.

    :param raw_title: The input raw torrent title to parse.
    :param translate_languages: Whether to translate language codes to language names or short codes (default: False returns short codes)
    :return: A dictionary with the parsed results.
    """
    return _parser.parse(raw_title, translate_languages)


__all__ = ["Parser", "add_defaults", "parse", "parse_title", "handlers", "transformers"]
