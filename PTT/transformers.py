from datetime import datetime

import regex

def none(input):
    return input

def value(val):
    def inner(input):
        if isinstance(val, str):
            return val.replace("$1", input)
        return val
    return inner

def integer(input):
    try:
        return int(input)
    except ValueError:
        return None

def boolean(input):
    return True

def lowercase(input):
    return input.lower()

def uppercase(input):
    return input.upper()

def date(date_format):
    def inner(input):
        sanitized = regex.sub(r"\W+", " ", input).strip()
        try:
            date = datetime.strptime(sanitized, date_format)
            return date.strftime("%Y-%m-%d")
        except ValueError:
            return None
    return inner

def range_func(input):
    array = [int(x) for x in regex.sub(r"\D+", " ", input).strip().split() if x.isdigit()]
    if len(array) == 2 and array[0] < array[1]:
        return list(range(array[0], array[1] + 1))
    if all(array[i] + 1 == array[i + 1] for i in range(len(array) - 1)):
        return array
    return None

def year_range(input):
    parts = regex.split(r"\D+", input)
    start = int(parts[0]) if parts[0].isdigit() else None
    end = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else None
    if not end:
        return str(start)
    if end < 100:
        end += start - start % 100 # type: ignore
    if end <= start: # type: ignore
        return None
    return f"{start}-{end}"

def array(chain):
    def inner(input):
        return [chain(input)] if chain else [input]
    return inner

def uniq_concat(chain):
    def inner(input, result=None):
        new_result = result if result is not None else []
        value = chain(input)
        return new_result if value in new_result else new_result + [value]
    return inner
