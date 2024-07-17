from .handlers import add_defaults
from .parse import Parser

_parser = Parser()
add_defaults(_parser)


def parse(raw_title: str) -> dict:
    """
    Parse the given input string using the initialized parser instance.
    :param raw_title: The input raw torrent title to parse.
    :return: A dictionary with the parsed results.
    """
    return _parser.parse(raw_title)


__all__ = ["Parser", "add_defaults", "parse", "parse_title", "handlers", "transformers"]