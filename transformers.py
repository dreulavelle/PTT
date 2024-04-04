import re
from typing import Any, Callable, Union, Optional, List
from datetime import datetime

def none(input: str) -> str:
    return input

def value(val: Union[str, Callable[[str], str]]) -> Callable[[str], str]:
    if isinstance(val, str):
        return lambda input: val.replace("$1", input)
    return val

def integer(input: str) -> Optional[int]:
    try:
        return int(input)
    except ValueError:
        return None

def boolean(_) -> bool:
    return True

def lowercase(input: str) -> str:
    return input.lower()

def uppercase(input: str) -> str:
    return input.upper()

def date(date_format: str) -> Callable[[str], Optional[str]]:
    def transformer(input: str) -> Optional[str]:
        try:
            parsed_date = datetime.strptime(input, date_format)
            return parsed_date.strftime("%Y-%m-%d")
        except ValueError:
            return None
    return transformer

def range_transform(input: str) -> Optional[List[int]]:
    array = [int(x) for x in re.sub(r"\D+", " ", input).strip().split() if x.isdigit()]
    if len(array) >= 2 and all(array[i] < array[i + 1] for i in range(len(array) - 1)):
        return array
    return None

def year_range(input: str) -> Optional[str]:
    parts = input.split("-")
    if len(parts) == 2 and all(part.isdigit() for part in parts):
        start, end = map(int, parts)
        if start < end:
            return f"{start}-{end}"
    return None

def array(chain: Optional[Callable[[str], Any]] = None) -> Callable[[str], List[Any]]:
    def transformer(input: str) -> List[Any]:
        return [chain(input)] if chain else [input]
    return transformer

def uniq_concat(chain: Optional[Callable[[str], Any]] = None) -> Callable[[str, Optional[List[Any]]], List[Any]]:
    def transformer(input: str, result: Optional[List[Any]] = None) -> List[Any]:
        result = result or []
        item = chain(input) if chain else input
        if item not in result:
            result.append(item)
        return result
    return transformer
