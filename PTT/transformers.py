import arrow
import regex


def none(input_value: str) -> str:
    return input_value


def value(val):
    def inner(input_value, existing_value=None):
        if isinstance(val, str) and isinstance(input_value, str):
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


def convert_months(date_str):
    for month, shortened in month_mapping.items():
        date_str = regex.sub(month, shortened, date_str, flags=regex.IGNORECASE)
    return date_str

def date(date_format):
    def inner(input_value):
        sanitized = regex.sub(r"\W+", " ", input_value).strip()
        sanitized = convert_months(sanitized)
        print(f"Attempting to parse date: {sanitized}")
        formats = [date_format] if not isinstance(date_format, list) else date_format
        for fmt in formats:
            try:
                return arrow.get(sanitized, fmt).format("YYYY-MM-DD")
            except ValueError as e:
                print(f"Failed to parse date: {input_value} with format: {fmt}")
                print(e)
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
    numbers = [int(x) for x in regex.findall(r'\d+', input_str)]

    # Check if the extracted list of numbers forms a continuous, ascending sequence
    if len(numbers) == 2:
        # If exactly two numbers, generate a range if they form a valid range
        if numbers[0] < numbers[1]:
            return list(range(numbers[0], numbers[1] + 1))
    elif len(numbers) > 2:
        # If more than two numbers, check if they form a continuous, ascending sequence
        if all(numbers[i] + 1 == numbers[i + 1] for i in range(len(numbers) - 1)):
            return numbers
    else:
        # Return the list as-is if it's a single number or empty
        return numbers

    # Return None if the sequence is not continuous or not just a single number
    return None


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
