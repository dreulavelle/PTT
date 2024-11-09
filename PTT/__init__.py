from .handlers import add_defaults
from .parse import Parser
from .anime import anime_handler

_parser = Parser()
add_defaults(_parser)


def parse_title(raw_title: str, translate_languages: bool = False, parse_anime: bool = False) -> dict:
    """
    Parse the given input string using the initialized parser instance.

    :param raw_title: The input raw torrent title to parse.
    :param translate_languages: Whether to translate language codes to language names or short codes (default: False returns short codes)
    :param parse_anime: Whether to parse anime title (default: False)
    :return: A dictionary with the parsed results.

    Note:
        If `parse_anime` is True, the anime handlers will be added to the parser instance.
        This can add more time to the parsing process.
    """
    if parse_anime:
        anime_handler(_parser)  # add anime handlers to the parser instance
    return _parser.parse(raw_title, translate_languages)


__all__ = ["Parser", "add_defaults", "parse", "parse_title", "handlers", "transformers"]
