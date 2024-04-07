import regex

from PTT.parse import Parser
from PTT.transformers import (
    none, value, integer, boolean, lowercase, uppercase, date,
    range_func, year_range, array, uniq_concat
)


def add_defaults(parser: Parser):
    # Episode code
    parser.add_handler("episodeCode", regex.compile(r"\[(\w{8})\](?=\.\w{1,5}$|$)"), uppercase, {"remove": True})
    parser.add_handler("episodeCode", regex.compile(r"\[([A-Z0-9]{8})\]"), uppercase, {"remove": True})

    # Resolution
    parser.add_handler("resolution", regex.compile(r"\b(?:\[\]?4k[\])?]?)\b", regex.IGNORECASE), value("4k"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"21600?[pi]", regex.IGNORECASE), value("4k"), {"skipIfAlreadyFound": False, "remove": True})
    parser.add_handler("resolution", regex.compile(r"\[\]?3840x\d{4}[\])?]?", regex.IGNORECASE), value("4k"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\[\]?1920x\d{3,4}[\])?]?", regex.IGNORECASE), value("1080p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\[\]?1280x\d{3}[\])?]?", regex.IGNORECASE), value("720p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\[\]?(\d{3,4}x\d{3,4})[\])?]?", regex.IGNORECASE), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(480|720|1080)0[pi]", regex.IGNORECASE), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:BD|HD|M)(720|1080|2160)"), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(480|576|720|1080|2160)[pi]", regex.IGNORECASE), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:^|\D)(\d{3,4})[pi]", regex.IGNORECASE), value("$1p"), {"remove": True})

    # Date
    parser.add_handler("date", regex.compile(r"(?<=\W|^)(?:\[\]?(?:19[6-9]|20[01])[0-9]([. \-/\\])(?:0[1-9]|1[012])\1(?:0[1-9]|[12][0-9]|3[01])[\])]?)(?=\W|$)"), date("YYYY MM DD"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?<=\W|^)(?:\[\]?(?:0[1-9]|[12][0-9]|3[01])([. \-/\\])(?:0[1-9]|1[012])\1(?:19[6-9]|20[01])[0-9][\])]?)(?=\W|$)"), date("DD MM YYYY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?<=\W)(?:\[\]?(?:0[1-9]|1[012])([. \-/\\])(?:0[1-9]|[12][0-9]|3[01])\1(?:[0][1-9]|[0126789][0-9])[\])]?)(?=\W|$)"), date("MM DD YY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?<=\W)(?:\[\]?(?:0[1-9]|[12][0-9]|3[01])([. \-/\\])(?:0[1-9]|1[012])\1(?:[0][1-9]|[0126789][0-9])[\])]?)(?=\W|$)"), date("DD MM YY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?<=\W|^)(?:\[\]?(?:0?[1-9]|[12][0-9]|3[01])[. ]?(?:st|nd|rd|th)?([. \-/\\])(?:feb(?:ruary)?|jan(?:uary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\1(?:19[7-9]|20[01])[0-9][\])]?)(?=\W|$)", regex.IGNORECASE), date("DD MMM YYYY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?<=\W|^)(?:\[\]?(?:0?[1-9]|[12][0-9]|3[01])[. ]?(?:st|nd|rd|th)?([. \-/\\])(?:feb(?:ruary)?|jan(?:uary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\1(?:0[1-9]|[0126789][0-9])[\])]?)(?=\W|$)", regex.IGNORECASE), date("DD MMM YY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?<=\W|^)(?:\[\]?20[01][0-9](?:0[1-9]|1[012])(?:0[1-9]|[12][0-9]|3[01])[\])]?)(?=\W|$)"), date("YYYYMMDD"), {"remove": True})

    # Year
    parser.add_handler("year", regex.compile(r"[([]?[ .]?((?:19\d|20[012])\d[ .]?-[ .]?(?:19\d|20[012])\d)[ .]?[)\]]?"), year_range, { "remove": True })
    parser.add_handler("year", regex.compile(r"[([][ .]?((?:19\d|20[012])\d[ .]?-[ .]?\d{2})[ .]?[)\]]"), year_range, { "remove": True })
    parser.add_handler("year", regex.compile(r"[([]?(?!^)(?<!\d|Cap[. ]?)((?:19\d|20[012])\d)(?!\d|kbps)[)\]]?", regex.IGNORECASE), integer, { "remove": True })
    parser.add_handler("year", regex.compile(r"^[([]?((?:19\d|20[012])\d)(?!\d|kbps)[)\]]?", regex.IGNORECASE), integer, { "remove": True })

    # Extended
    parser.add_handler("extended", regex.compile(r"EXTENDED"), boolean)

    # Convert
    parser.add_handler("convert", regex.compile(r"CONVERT"), boolean)

    # Hardcoded
    parser.add_handler("hardcoded", regex.compile(r"HC|HARDCODED"), boolean)

    # Proper
    parser.add_handler("proper", regex.compile(r"(?:REAL.)?PROPER"), boolean)

    # Repack
    parser.add_handler("repack", regex.compile(r"REPACK|RERIP"), boolean)

    # Retail
    parser.add_handler("retail", regex.compile(r"\bRetail\b", regex.IGNORECASE), boolean)

    # Remastered
    parser.add_handler("remastered", regex.compile(r"\bRemaster(?:ed)?\b", regex.IGNORECASE), boolean)

    # Unrated
    parser.add_handler("unrated", regex.compile(r"\bunrated|uncensored\b", regex.IGNORECASE), boolean)

    # Region
    parser.add_handler("region", regex.compile(r"R\d\b"), none, { "skipIfFirst": True })

    # Source
    parser.add_handler("source", regex.compile(r"\b(?:H[DQ][ .-]*)?CAM(?:H[DQ])?(?:[ .-]*Rip)?\b", regex.IGNORECASE), value("CAM"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\b(?:H[DQ][ .-]*)?S[ .-]*print", regex.IGNORECASE), value("CAM"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\b(?:HD[ .-]*)?T(?:ELE)?S(?:YNC)?(?:Rip)?\b", regex.IGNORECASE), value("TeleSync"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\b(?:HD[ .-]*)?T(?:ELE)?C(?:INE)?(?:Rip)?\b"), value("TeleCine"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bBlu[ .-]*Ray\b(?=.*remux)", regex.IGNORECASE), value("BluRay REMUX"), {"remove": True})
    parser.add_handler("source", regex.compile(r"(?:BD|BR|UHD)[- ]?remux", regex.IGNORECASE), value("BluRay REMUX"), {"remove": True})
    parser.add_handler("source", regex.compile(r"(?<=remux.*)\bBlu[ .-]*Ray\b", regex.IGNORECASE), value("BluRay REMUX"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bBlu[ .-]*Ray\b(?![ .-]*Rip)", regex.IGNORECASE), value("BluRay"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bUHD[ .-]*Rip\b", regex.IGNORECASE), value("UHDRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bHD[ .-]*Rip\b", regex.IGNORECASE), value("HDRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bMicro[ .-]*HD\b", regex.IGNORECASE), value("HDRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\b(?:BR|Blu[ .-]*Ray)[ .-]*Rip\b", regex.IGNORECASE), value("BRRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bBD[ .-]*Rip\b|\bBDR\b|\bBD-RM\b|[[(]BD[\]) .,-]", regex.IGNORECASE), value("BDRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\b(?:HD[ .-]*)?DVD[ .-]*Rip\b", regex.IGNORECASE), value("DVDRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bVHS[ .-]*Rip\b", regex.IGNORECASE), value("DVDRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\b(?:DVD?|BD|BR)?[ .-]*Scr(?:eener)?\b", regex.IGNORECASE), value("SCR"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bP(?:re)?DVD(?:Rip)?\b", regex.IGNORECASE), value("SCR"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bDVD(?:R\d?)?\b", regex.IGNORECASE), value("DVD"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bVHS\b", regex.IGNORECASE), value("DVD"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bPPVRip\b", regex.IGNORECASE), value("PPVRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bHD[ .-]*TV(?:Rip)?\b", regex.IGNORECASE), value("HDTV"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bDVB[ .-]*(?:Rip)?\b", regex.IGNORECASE), value("HDTV"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bSAT[ .-]*Rips?\b", regex.IGNORECASE), value("SATRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bTVRips?\b", regex.IGNORECASE), value("TVRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bR5\b", regex.IGNORECASE), value("R5"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bWEB[ .-]*DL(?:Rip)?\b", regex.IGNORECASE), value("WEB-DL"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\bWEB[ .-]*Rip\b", regex.IGNORECASE), value("WEBRip"), {"remove": True})
    parser.add_handler("source", regex.compile(r"\b(?:DL|WEB|BD|BR)MUX\b", regex.IGNORECASE), none, {"remove": True})
    parser.add_handler("source", regex.compile(r"\b(DivX|XviD)\b"), none, {"remove": True})

    # Video depth
    parser.add_handler("bitDepth", regex.compile(r"(?:8|10|12)[- ]?bit", regex.IGNORECASE), lowercase, {"remove": True})
    parser.add_handler("bitDepth", regex.compile(r"\bhevc\s?10\b", regex.IGNORECASE), value("10bit"))
    parser.add_handler("bitDepth", regex.compile(r"\bhdr10\b", regex.IGNORECASE), value("10bit"))
    parser.add_handler("bitDepth", regex.compile(r"\bhi10\b", regex.IGNORECASE), value("10bit"))

    # HDR
    parser.add_handler("hdr", regex.compile(r"\bDV\b|dolby.?vision|\bDoVi\b", regex.IGNORECASE), uniq_concat(value("DV")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("hdr", regex.compile(r"HDR10(?:\+|plus)", regex.IGNORECASE), uniq_concat(value("HDR10+")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("hdr", regex.compile(r"\bHDR(?:10)?\b", regex.IGNORECASE), uniq_concat(value("HDR")), {"remove": True, "skipIfAlreadyFound": False})

    # Codec
    parser.add_handler("codec", regex.compile(r"\b[xh][-. ]?26[45]", regex.IGNORECASE), lowercase, {"remove": True})
    parser.add_handler("codec", regex.compile(r"\bhevc(?:\s?10)?\b", regex.IGNORECASE), value("hevc"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("codec", regex.compile(r"\b(?:dvix|mpeg2|divx|xvid|avc)\b", regex.IGNORECASE), lowercase, {"remove": True, "skipIfAlreadyFound": False})
