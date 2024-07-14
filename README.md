# parsett - Parse Torrent Titles

parsett (Parse Torrent Titles) is a flexible and powerful toolkit for parsing and transforming torrent titles. It provides a robust mechanism to define custom parsing handlers and transformers, making it ideal for extracting meaningful information from torrent file names.

**Note:** This library is a Python port of the `parse-torrent-title` library from [TheBeastLT](https://github.com/TheBeastLT/parse-torrent-title).

## Features

- Easy-to-use interface for parsing torrent titles.
- Supports custom handlers and transformers.
- Built-in default handlers for common patterns in torrent titles.
- Extensible and customizable.

## Installation

To install parsett, you can use pip:

```bash
pip install parsett
```

## Quick Start

### Basic Usage

To parse a torrent title using the default handlers, simply call `parsett.parse()`:

```python
import PTT

result = PTT.parse_title("The Simpsons S01E01 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole")
print(result)
```

### Sample Parsed Data

Here are some examples of parsed torrent titles:

#### Example 1

**Title:** `The Simpsons S01E01 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole`

**Parsed Result:**

```json
{
    "resolution": "1080p",
    "source": "BluRay",
    "bit_depth": "10bit",
    "codec": "hevc",
    "audio": "aac",
    "seasons": [1],
    "episodes": [1],
    "languages": [],
    "title": "The Simpsons"
}
```

#### Example 2

**Title:** `www.Tamilblasters.party - The Wheel of Time (2021) Season 01 EP(01-08) [720p HQ HDRip - [Tam + Tel + Hin] - DDP5.1 - x264 - 2.7GB - ESubs]`

**Parsed Result:**

```json
{
    "resolution": "720p",
    "year": 2021,
    "source": "HDRip",
    "codec": "x264",
    "seasons": [1],
    "episodes": [1, 2, 3, 4, 5, 6, 7, 8],
    "languages": ["hindi", "telugu", "tamil"],
    "site": "www.Tamilblasters.party",
    "title": "The Wheel of Time"
}
```

#### Example 3

**Title:** `The.Walking.Dead.S06E07.SUBFRENCH.HDTV.x264-AMB3R.mkv`

**Parsed Result:**

```json
{
    "source": "HDTV",
    "codec": "x264",
    "group": "AMB3R",
    "container": "mkv",
    "seasons": [6],
    "episodes": [7],
    "languages": ["french"],
    "extension": "mkv",
    "title": "The Walking Dead"
}
```

## Supported Fields

Here are the fields that are currently supported by the default handlers, along with their types:

- `title`: `str`
- `resolution`: `str`
- `date`: `str`
- `year`: `int`
- `extended`: `bool`
- `convert`: `bool`
- `hardcoded`: `bool`
- `proper`: `bool`
- `repack`: `bool`
- `retail`: `bool`
- `remastered`: `bool`
- `unrated`: `bool`
- `region`: `str`
- `source`: `str`
- `bit_depth`: `str`
- `hdr`: `str`
- `codec`: `str`
- `audio`: `str`
- `group`: `str`
- `container`: `str`
- `volumes`: `list[int]`
- `seasons`: `list[int]`
- `episodes`: `list[int]`
- `episode_code`: `str`
- `complete`: `bool`
- `languages`: `list[str]`
- `dubbed`: `bool`
- `site`: `str`
- `extension`: `str`

## Advanced Usage

You can create and customize your own parser instance if needed:

```python
from PTT import Parser, add_defaults

# Create a new parser instance
parser = Parser()

# Add default handlers
add_defaults(parser)

# Parse a torrent title
result = parser.parse("The Simpsons S01E01 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole")
print(result)
```

## Adding Custom Handlers

parsett allows you to add custom handlers to extend the parsing capabilities. Here’s how you can do it:

### Define a Custom Handler

A handler is a function that processes a specific pattern in the input string. Here’s an example of a custom handler that extracts hashtags from a string:

```python
import regex
from PTT.parse import Parser

def hashtag_handler(input_string):
    hashtags = regex.findall(r"#(\w+)", input_string)
    return {"hashtags": hashtags}

# Create a new parser instance
parser = Parser()

# Add the custom handler
parser.add_handler("hashtags", regex.compile(r"#(\w+)"), hashtag_handler)

# Parse a string
result = parser.parse("This is a test string with #hashtags and #morehashtags.")
print(result)
```

## Built-in Transformers

parsett comes with several built-in transformers to manipulate the extracted data. These include:

- `none`: Returns the input value without any transformation.
- `value`: Replaces the input value with a predefined value.
- `integer`: Converts the input value to an integer.
- `boolean`: Returns `True` for any input.
- `lowercase`: Converts the input value to lowercase.
- `uppercase`: Converts the input value to uppercase.
- `date`: Parses dates using specified format(s).
- `range_func`: Parses a range of numbers from the input string.
- `year_range`: Parses a range of years from the input string.
- `array`: Wraps the input value in a list.
- `uniq_concat`: Appends unique values to a list.

### Example Usage of Transformers

```python
from parsett.transformers import lowercase, uppercase

# Add a handler with a transformer
parser.add_handler("lowercase_example", regex.compile(r"[A-Z]+"), lowercase)
parser.add_handler("uppercase_example", regex.compile(r"[a-z]+"), uppercase)

result = parser.parse("This is a MIXED case STRING.")
print(result)
```

## Options in add_handler

The `add_handler` function allows you to specify options to control the behavior of the handler. The available options are:

```python
default_options = {
    "skipIfAlreadyFound": True,
    "skipFromTitle": False,
    "skipIfFirst": False,
    "remove": False,
}
```

### Option Details

- `skipIfAlreadyFound`: If `True`, the handler will not process the input if the field has already been found.
- `skipFromTitle`: If `True`, the matched pattern will be excluded from the title.
- `skipIfFirst`: If `True`, the handler will not process the input if it is the first handler.
- `remove`: If `True`, the matched pattern will be removed from the input string.

### Example Usage of Options

```python
parser.add_handler("custom_handler", regex.compile(r"\bexample\b", regex.IGNORECASE), lambda x: "example_value", {
    "skipIfAlreadyFound": False,
    "skipFromTitle": True,
    "skipIfFirst": True,
    "remove": True,
})
```

## Extending the Parser

To extend the parser with additional functionality, you can create new transformers and handlers.

### Creating a New Transformer

A transformer is a function that processes the extracted value. Here’s an example of a custom transformer that reverses a string:

```python
def reverse(input_value):
    return input_value[::-1]

# Add a handler with the custom transformer
parser.add_handler("reverse_example", regex.compile(r"\w+"), reverse)

result = parser.parse("Reverse this string.")
print(result)
```

### Creating a Custom Handler for Torrent Titles

Let's create a custom handler to extract the uploader name from a torrent title:

```python
def uploader_handler(input_string):
    match = regex.search(r"Uploader: ([\w\s]+)", input_string)
    if match:
        return {"uploader": match.group(1)}
    return {}

# Add the custom handler
parser.add_handler("uploader", regex.compile(r"Uploader: ([\w\s]+)"), uploader_handler)

# Parse a string
result = parser.parse("Anatomia De Grey - Temporada 19 [HDTV][Cap.1905][Castellano][www.AtomoHD.nu].avi Uploader: JohnDoe")
print(result)
```

## Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
