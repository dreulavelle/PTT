from .handlers import add_defaults
from .parse import Parser

_parser = Parser()
add_defaults(_parser)


def parse_title(input_string: str) -> dict:
    """
    Parse the given input string using the initialized parser instance.

    :param input_string: The input string to parse.
    :return: A dictionary with the parsed results.
    """
    return _parser.parse(input_string)


__all__ = ["Parser", "add_defaults", "parse"]
