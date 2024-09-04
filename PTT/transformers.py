from typing import Callable, List, Optional, Union

import arrow
import regex


def none(input_value: str) -> str:
    """
    Return the input value without any transformation.

    :param input_value: The input string.
    :return: The unmodified input string.
    """
    return input_value


def value(val: Union[str, int, Callable[[str], Union[str, int]]]) -> Callable[[str], Union[str, int]]:
    """
    Return a transformer that replaces the input value with a predefined value.

    :param val: The predefined value or a callable to generate the value.
    :return: The transformer function.
    """

    def inner(input_value: str, existing_value: Optional[Union[str, int]] = None) -> Union[str, int]:
        if isinstance(val, str) and isinstance(input_value, str):
            return val.replace("$1", input_value)
        if callable(val):
            return val(input_value)
        return val

    return inner


def integer(input_value: str) -> Optional[int]:
    """
    Convert the input value to an integer.

    :param input_value: The input string.
    :return: The integer value or None if conversion fails.
    """
    try:
        return int(input_value)
    except ValueError:
        return None


def boolean(*args, **kwargs) -> bool:
    """
    Return True for any input, used for boolean flags.

    :return: True
    """
    return True


def lowercase(input_value: str) -> str:
    """
    Convert the input value to lowercase.

    :param input_value: The input string.
    :return: The lowercase string.
    """
    return input_value.lower()


def uppercase(input_value: str) -> str:
    """
    Convert the input value to uppercase.

    :param input_value: The input string.
    :return: The uppercase string.
    """
    return input_value.upper()


month_mapping = {
    r"\bJanu\b": "Jan",
    r"\bFebr\b": "Feb",
    r"\bMarc\b": "Mar",
    r"\bApri\b": "Apr",
    r"\bMay\b": "May",
    r"\bJune\b": "Jun",
    r"\bJuly\b": "Jul",
    r"\bAugu\b": "Aug",
    r"\bSept\b": "Sep",
    r"\bOcto\b": "Oct",
    r"\bNove\b": "Nov",
    r"\bDece\b": "Dec",
}


def convert_months(date_str: str) -> str:
    """
    Convert long month names to their shortened forms.

    :param date_str: The input date string.
    :return: The date string with shortened month names.
    """
    for month, shortened in month_mapping.items():
        date_str = regex.sub(month, shortened, date_str, flags=regex.IGNORECASE)
    return date_str


def date(date_format: Union[str, List[str]]) -> Callable[[str], Optional[str]]:
    """
    Return a transformer that parses dates using the specified format(s).

    :param date_format: The date format(s) to use for parsing.
    :return: The transformer function.
    """

    def inner(input_value: str) -> Optional[str]:
        sanitized = regex.sub(r"\W+", " ", input_value).strip()
        sanitized = convert_months(sanitized)
        formats = [date_format] if not isinstance(date_format, list) else date_format
        for fmt in formats:
            try:
                return arrow.get(sanitized, fmt).format("YYYY-MM-DD")
            except Exception:
                continue
        return None

    return inner


def range_func(input_str: str) -> Optional[List[int]]:
    """
    Parse a range of numbers from the input string.

    :param input_str: The input string.
    :return: A list of integers representing the range, or None if invalid.
    """
    numbers = [int(x) for x in regex.findall(r"\d+", input_str)]

    if len(numbers) == 2 and numbers[0] < numbers[1]:
        return list(range(numbers[0], numbers[1] + 1))
    if len(numbers) > 2 and all(numbers[i] + 1 == numbers[i + 1] for i in range(len(numbers) - 1)):
        return numbers
    if len(numbers) == 1:
        return numbers

    return None


def year_range(input_value: str) -> Optional[str]:
    """
    Parse a range of years from the input string.

    :param input_value: The input string.
    :return: The year range as a string, or None if invalid.
    """
    parts = regex.findall(r"\d+", input_value)
    if not parts:
        return None

    try:
        start = int(parts[0])
        end = int(parts[1]) if len(parts) > 1 else None
    except ValueError:
        return None

    if not end:
        return str(start)

    if end < 100:
        end += start - start % 100

    if end <= start:
        return None

    return f"{start}-{end}"


def array(chain: Optional[Callable[[str], Union[str, int]]] = None) -> Callable[[str], List[Union[str, int]]]:
    """
    Return a transformer that wraps the input value in a list.

    :param chain: An optional transformer to apply to the input value.
    :return: The transformer function.
    """

    def inner(input_value: str) -> List[Union[str, int]]:
        return [chain(input_value) if chain else input_value]

    return inner


def uniq_concat(chain: Callable[[str], Union[str, int]]) -> Callable[[str, Optional[List[Union[str, int]]]], List[Union[str, int]]]:
    """
    Return a transformer that appends unique values to a list.

    :param chain: The transformer to apply to the input value.
    :return: The transformer function.
    """

    def inner(input_value: str, result: Optional[List[Union[str, int]]] = None) -> List[Union[str, int]]:
        if result is None:
            result = []
        output_value = chain(input_value)
        if output_value not in result:
            result.append(output_value)
        return result

    return inner


def transform_resolution(input_value: str) -> str:
    """
    Transform the resolution string to a standardized format.

    :param input_value: The input resolution string.
    :return: The standardized resolution string.
    """

    input_value = lowercase(input_value)

    if "2160" in input_value or "4k" in input_value:
        return "2160p"
    if "1440" in input_value or "2k" in input_value:
        return "1440p"
    if "1080" in input_value:
        return "1080p"
    if "720" in input_value:
        return "720p"
    if "480" in input_value:
        return "480p"
    if "360" in input_value:
        return "360p"
    if "240" in input_value:
        return "240p"
    return input_value
