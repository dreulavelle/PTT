import regex
from .transformers import (
    none, value, integer, boolean, lowercase, uppercase, date,
    range as range_function, year_range, array, uniq_concat
)

def add_defaults(parser):
    # Episode code
    parser.add_handler("episodeCode", regex.compile(r"\[[(]([a-zA-Z0-9]{8})[\])](?=\.[a-zA-Z0-9]{1,5}$|$)\]"), uppercase, {"remove": True})
    parser.add_handler("episodeCode", regex.compile(r"\[([A-Z0-9]{8})\]"), uppercase, {"remove": True})

    # Resolution
    parser.add_handler("resolution", regex.compile(r"\b4k\b", regex.IGNORECASE), value("4k"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"21600?[pi]"), value("4k"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\b(?:\[|\()?4k(?:\]|\))?\b", regex.IGNORECASE), value("4k"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"2160[pi]", regex.IGNORECASE), value("4k"), {"skipIfAlreadyFound": False, "remove": True})
    parser.add_handler("resolution", regex.compile(r"\b(?:\[|\()?(3840x2160)(?:\]|\))?\b", regex.IGNORECASE), value("4k"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\b(?:\[|\()?(1920x(1080|1200))(?:\]|\))?\b", regex.IGNORECASE), value("1080p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\b(?:\[|\()?(1280x720)(?:\]|\))?\b", regex.IGNORECASE), value("720p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\b(?:\[|\()?(?P<width>\d{3,4})x(?P<height>\d{3,4})(?:\]|\))?\b", regex.IGNORECASE), lambda match, result: value(f"{match.group('height')}p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(480|720|1080)0[pi]", regex.IGNORECASE), lambda match, result: value(f"{match.group(1)}p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\b(?:BD|HD|M)(720|1080|2160)\b"), lambda match, result: value(f"{match.group(1)}p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(480|576|720|1080|2160)[pi]", regex.IGNORECASE), lambda match, result: value(f"{match.group(1)}p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?<!\d)(\d{3,4})[pi]", regex.IGNORECASE), lambda match, result: value(f"{match.group(1)}p"), {"remove": True})

    # Date
    parser.add_handler("date", regex.compile(r"(19[6-9]|20[0-2])\d([.\-/])(0[1-9]|1[0-2])\2(0[1-9]|[12][0-9]|3[01])"), date("YYYY-MM-DD"), {"remove": True})
    # Additional date patterns...

    # Year
    parser.add_handler("year", regex.compile(r"\b(19\d{2}|20[01]\d)\b"), integer, {"remove": True})
    # Additional year patterns...

    # Extended, Convert, Hardcoded, etc.
    parser.add_handler("extended", regex.compile(r"EXTENDED"), boolean)
    parser.add_handler("convert", regex.compile(r"CONVERT"), boolean)
    # More patterns...

    # Audio
    parser.add_handler("audio", regex.compile(r"7\.1[ .]?Atmos"), value("7.1 Atmos"), {"remove": True})
    # More audio patterns...

    # Languages
    parser.add_handler("languages", regex.compile(r"\bmulti(?:ple)?[ .-]*(?:su?$|sub\w*|dub\w*)\b|msub"), uniq_concat(value("multi subs")), {"remove": True})
    # More language patterns...

    # Custom handler example for complex logic
    def custom_bit_depth_logic(result):
        if result.get("bitDepth"):
            result["bitDepth"] = result["bitDepth"].replace(" ", "").replace("-", "")
    parser.add_handler("bitDepth", regex.compile(r"(8|10|12)[- ]?bit"), lowercase, {"custom_logic": custom_bit_depth_logic, "remove": True})
    # More custom logic handlers...

    # HDR
    parser.add_handler("hdr", regex.compile(r"\bDV\b|dolby.?vision|\bDoVi\b"), uniq_concat(value("DV")), {"remove": True})
    # More HDR patterns...

    # Codec
    parser.add_handler("codec", regex.compile(r"\b[xh][-. ]?26[45]"), lowercase, {"remove": True})
    # More codec patterns...

    # Note: Continue in the same vein for all other handlers specified in the JavaScript source.

# To use this function, instantiate your Parser and then call add_defaults(parser) with it.
