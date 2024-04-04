from .transformers import none, value, integer, boolean, lowercase, uppercase, date, range_transform as range, year_range, array, uniq_concat

def add_defaults(parser):
    # Episode Code
    parser.add_handler("episodeCode", r"\[([A-Z0-9]{8})\]", uppercase, {"remove": True})

    # Resolution
    parser.add_handler("resolution", r"\b4k\b", value("4K"), {"remove": True})
    parser.add_handler("resolution", r"2160[pi]", value("4K"), {"remove": True, "skipIfAlreadyFound": False})

    # Date
    parser.add_handler("date", r"(19[6-9]|20[01])\d-[01]\d-[0-3]\d", date("YYYY-MM-DD"), {"remove": True})

    # Year
    parser.add_handler("year", r"\b(19\d{2}|20[01]\d)\b", integer, {"remove": True})

    # Extended
    parser.add_handler("extended", r"EXTENDED", boolean, {"remove": True})

    # Convert
    parser.add_handler("convert", r"CONVERT", boolean, {"remove": True})

    # Hardcoded
    parser.add_handler("hardcoded", r"HC|HARDCODED", boolean, {"remove": True})

    # Proper
    parser.add_handler("proper", r"PROPER", boolean, {"remove": True})

    # Repack
    parser.add_handler("repack", r"REPACK|RERIP", boolean, {"remove": True})

    # Retail
    parser.add_handler("retail", r"\bRetail\b", boolean, {"remove": True})

    # Remastered
    parser.add_handler("remastered", r"\bRemastered\b", boolean, {"remove": True})

    # Unrated
    parser.add_handler("unrated", r"\bUnrated|Uncensored\b", boolean, {"remove": True})

    # Region
    parser.add_handler("region", r"R\d", none, {"skipIfFirst": True})

    # Source
    parser.add_handler("source", r"\bCAM\b", value("CAM"), {"remove": True})

    # Video Depth
    parser.add_handler("bitDepth", r"10[- ]?bit", lowercase, {"remove": True})

    # HDR
    parser.add_handler("hdr", r"\bHDR10\+\b", uniq_concat(value("HDR10+")), {"remove": True, "skipIfAlreadyFound": False})

    # Codec
    parser.add_handler("codec", r"\bH\.264\b", lowercase, {"remove": True})

    # Audio
    parser.add_handler("audio", r"7\.1[ .]?Atmos", value("7.1 Atmos"), {"remove": True})

    # Note: This is a simplified representation. Add more handlers as required by your application's needs.

# Example on how to use it
# parser = Parser()
# add_defaults(parser)
