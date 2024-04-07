import regex
from datetime import datetime


def none(input_value: str) -> str:
    return input_value

def value(val):
    def inner(input_value, existing_value=None):
        if isinstance(val, str):
            return val.replace("$1", input_value)
        return val
    return inner

def integer(input_value):
    try:
        return int(input_value)
    except ValueError:
        return None

def boolean(*args, **kwargs):
    return True

def lowercase(input_value):
    return input_value.lower()

def uppercase(input_value):
    return input_value.upper()

def date(date_format):
    def inner(input_value):
        sanitized = regex.sub(r"\W+", " ", input_value).strip()
        try:
            # Attempting to parse the date according to the provided format
            date_object = datetime.strptime(sanitized, date_format)
            return date_object.strftime("%Y-%m-%d")
        except ValueError:
            # Handling cases where parsing fails
            return None
    return inner

# def range_func(input):
#     array = [int(x) for x in regex.sub(r"\D+", " ", input).strip().split() if x.isdigit()]
#     if len(array) == 2 and array[0] < array[1]:
#         return list(range(array[0], array[1] + 1))
#     if all(array[i] + 1 == array[i + 1] for i in range(len(array) - 1)):
#         return array
#     return None

def range_func(input_str):
    # Extract numbers from the input string and convert them to integers
    numbers = regex.sub(r"\D+", " ", input_str).strip().split()
    int_nums = [int(x) for x in numbers if x.isdigit()]
    print(int_nums)

    if len(int_nums) == 2 and int_nums[0] < int_nums[1] and int_nums[1] - int_nums[0] == 1:
        return int_nums
    elif len(int_nums) == 2 and int_nums[0] < int_nums[1]:
        return list(range(int_nums[0], int_nums[1] + 1))
    else:
        return int_nums

def year_range(input_value):
    parts = regex.findall(r"\d+", input_value)
    if not parts:
        return None  # Return None if no numeric parts are found

    try:
        start = int(parts[0])
        end = int(parts[1]) if len(parts) > 1 else None
    except ValueError:
        return None  # Return None if conversion to integer fails

    if not end:
        return str(start)  # If there's no end part, return the start as string
    
    if end < 100:
        end += start - start % 100  # Adjust for two-digit years
    
    if end <= start:
        return None  # If the end year is not after the start year, it's not a valid range
    
    return f"{start}-{end}"

def array(chain=None):
    def inner(input_value):
        return [chain(input_value) if chain else input_value]
    return inner

def uniq_concat(chain):
    def inner(input, result=None):
        if result is None:
            result = []
        value = chain(input)
        if value not in result:
            result.append(value)
        return result
    return inner