import regex

from PTT.parse import Parser
from PTT.transformers import (
    array,
    boolean,
    date,
    integer,
    lowercase,
    none,
    range_func,
    transform_resolution,
    uniq_concat,
    uppercase,
    value,
)


def add_defaults(parser: Parser):
    """
    Adds default handlers to the provided parser for various patterns such as episode codes, resolution,
    date formats, year ranges, etc. The handlers use regular expressions to match patterns and transformers
    to process the matched values.

    :param parser: The parser instance to which handlers will be added.
    """
    # Torrent extension
    parser.add_handler("torrent", regex.compile(r"\.torrent$"), boolean, {"remove": True})

    # Extras (This stuff can be trashed)
    parser.add_handler("extras", regex.compile(r"\bNCED\b", regex.IGNORECASE), uniq_concat(value("NCED")), {"remove": True})
    parser.add_handler("extras", regex.compile(r"\bNCOP\b", regex.IGNORECASE), uniq_concat(value("NCOP")), {"remove": True})
    parser.add_handler("extras", regex.compile(r"\b(?:Deleted[ .-]*)?Scene(?:s)?\b", regex.IGNORECASE), uniq_concat(value("Deleted Scene")), {"remove": False})
    parser.add_handler("extras", regex.compile(r"(?:(?<=\b(?:19\d{2}|20\d{2})\b.*)\b(?:Featurettes?)\b|\bFeaturettes?\b(?!.*\b(?:19\d{2}|20\d{2})\b))", regex.IGNORECASE), uniq_concat(value("Featurette")), {"skipFromTitle": True, "remove": False})
    parser.add_handler("extras", regex.compile(r"(?:(?<=\b(?:19\d{2}|20\d{2})\b.*)\b(?:Sample)\b|\b(?:Sample)\b(?!.*\b(?:19\d{2}|20\d{2})\b))", regex.IGNORECASE), uniq_concat(value("Sample")), {"skipFromTitle": True, "remove": False})
    parser.add_handler("extras", regex.compile(r"(?:(?<=\b(?:19\d{2}|20\d{2})\b.*)\b(?:Trailers?)\b|\bTrailers?\b(?!.*\b(?:19\d{2}|20\d{2}|.(Park|And))\b))", regex.IGNORECASE), uniq_concat(value("Trailer")), {"skipFromTitle": True, "remove": False})

    # PPV
    parser.add_handler("ppv", regex.compile(r"\bPPV\b", regex.IGNORECASE), boolean, {"skipFromTitle": True, "remove": True})
    parser.add_handler("ppv", regex.compile(r"\b\W?Fight.?Nights?\W?\b", regex.IGNORECASE), boolean, {"skipFromTitle": True, "remove": False})

    # Site before languages to get rid of domain name with country code.
    parser.add_handler("site", regex.compile(r"^(www?[\.,][\w-]+\.[\w-]+(?:\.[\w-]+)?)\s+-\s*", regex.IGNORECASE), options={"skipFromTitle": True, "remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("site", regex.compile(r"^((?:www?[\.,])?[\w-]+\.[\w-]+(?:\.[\w-]+)*?)\s+-\s*", regex.IGNORECASE), options={"skipIfAlreadyFound": False})

    # Episode code
    parser.add_handler("episode_code", regex.compile(r"[[(]([a-zA-Z0-9]{8})[\])](?=\.[a-zA-Z0-9]{1,5}$|$)"), uppercase, {"remove": True})
    parser.add_handler("episode_code", regex.compile(r"\[([A-Z0-9]{8})]"), uppercase, {"remove": True})

    # Resolution
    parser.add_handler("resolution", regex.compile(r"\[?\]?3840x\d{4}[\])?]?", regex.IGNORECASE), value("2160p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\[?\]?1920x\d{3,4}[\])?]?", regex.IGNORECASE), value("1080p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\[?\]?1280x\d{3}[\])?]?", regex.IGNORECASE), value("720p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\[?\]?(\d{3,4}x\d{3,4})[\])?]?p?", regex.IGNORECASE), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(480|720|1080)0[pi]", regex.IGNORECASE), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:QHD|QuadHD|WQHD|2560(\d+)?x(\d+)?1440p?)", regex.IGNORECASE), value("1440p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:Full HD|FHD|1920(\d+)?x(\d+)?1080p?)", regex.IGNORECASE), value("1080p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:BD|HD|M)(2160p?|4k)", regex.IGNORECASE), value("2160p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:BD|HD|M)1080p?", regex.IGNORECASE), value("1080p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:BD|HD|M)720p?", regex.IGNORECASE), value("720p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:BD|HD|M)480p?", regex.IGNORECASE), value("480p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\b(?:4k|2160p|1080p|720p|480p)(?!.*\b(?:4k|2160p|1080p|720p|480p)\b)", regex.IGNORECASE), transform_resolution, {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\b4k|21600?[pi]\b", regex.IGNORECASE), value("2160p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(\d{3,4})[pi]", regex.IGNORECASE), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(240|360|480|576|720|1080|2160|3840)[pi]", regex.IGNORECASE), lowercase, {"remove": True})

    # Trash (Equivalent to RTN auto-trasher) - DO NOT REMOVE HERE!
    # This one is pretty strict, but it removes a lot of the garbage
    # parser.add_handler("trash", regex.compile(r"\b(\w+rip|hc|((h[dq]|clean)(.+)?)?cam.?(rip|rp)?|(h[dq])?(ts|tc)(?:\d{3,4})?|tele(sync|cine)?|\d+[0o]+([mg]b)|\d{3,4}tc)\b"), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\b(?:H[DQ][ .-]*)?CAM(?!.?(S|E|\()\d+)(?:H[DQ])?(?:[ .-]*Rip|Rp)?\b", regex.IGNORECASE), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\b(?:H[DQ][ .-]*)?S[ \.\-]print\b", regex.IGNORECASE), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\b(?:HD[ .-]*)?T(?:ELE)?(C|S)(?:INE|YNC)?(?:Rip)?\b", regex.IGNORECASE), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\bPre.?DVD(?:Rip)?\b", regex.IGNORECASE), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\b(?:DVD?|BD|BR)?[ .-]*Scr(?:eener)?\b", regex.IGNORECASE), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\bDVB[ .-]*(?:Rip)?\b", regex.IGNORECASE), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\bSAT[ .-]*Rips?\b", regex.IGNORECASE), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\bLeaked\b", regex.IGNORECASE), boolean, {"remove": True})
    parser.add_handler("trash", regex.compile(r"threesixtyp", regex.IGNORECASE), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\bR5|R6\b", regex.IGNORECASE), boolean, {"remove": False})
    parser.add_handler("trash", regex.compile(r"\b(?:Deleted[ .-]*)?Scene(?:s)?\b", regex.IGNORECASE), boolean, {"remove": True})
    parser.add_handler("trash", regex.compile(r"\bHQ.?(Clean)?.?(Aud(io)?)?\b", regex.IGNORECASE), boolean, {"remove": True})

    # Date
    parser.add_handler("date", regex.compile(r"(?:\W|^)([[(]?(?:19[6-9]|20[012])[0-9]([. \-/\\])(?:0[1-9]|1[012])\2(?:0[1-9]|[12][0-9]|3[01])[])]?)(?:\W|$)"), date("YYYY MM DD"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?:\W|^)(\[?\]?(?:0[1-9]|[12][0-9]|3[01])([. \-/\\])(?:0[1-9]|1[012])\2(?:19[6-9]|20[01])[0-9][\])]?)(?:\W|$)"), date("DD MM YYYY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?:\W)(\[?\]?(?:0[1-9]|1[012])([. \-/\\])(?:0[1-9]|[12][0-9]|3[01])\2(?:[0][1-9]|[0126789][0-9])[\])]?)(?:\W|$)"), date("MM DD YY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?:\W)(\[?\]?(?:0[1-9]|[12][0-9]|3[01])([. \-/\\])(?:0[1-9]|1[012])\2(?:[0][1-9]|[0126789][0-9])[\])]?)(?:\W|$)"), date("DD MM YY"), {"remove": True})
    parser.add_handler(
        "date",
        regex.compile(r"(?:\W|^)([([]?(?:0?[1-9]|[12][0-9]|3[01])[. ]?(?:st|nd|rd|th)?([. \-/\\])(?:feb(?:ruary)?|jan(?:uary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\2(?:19[7-9]|20[012])[0-9][)\]]?)(?=\W|$)", regex.IGNORECASE),
        date(["DD MMM YYYY", "Do MMM YYYY", "Do MMMM YYYY"]),
        {"remove": True},
    )
    parser.add_handler(
        "date",
        regex.compile(r"(?:\W|^)(\[?\]?(?:0?[1-9]|[12][0-9]|3[01])[. ]?(?:st|nd|rd|th)?([. \-\/\\])(?:feb(?:ruary)?|jan(?:uary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\2(?:0[1-9]|[0126789][0-9])[\])]?)(?:\W|$)", regex.IGNORECASE),
        date("DD MMM YY"),
        {"remove": True},
    )
    parser.add_handler("date", regex.compile(r"(?:\W|^)(\[?\]?20[012][0-9](?:0[1-9]|1[012])(?:0[1-9]|[12][0-9]|3[01])[\])]?)(?:\W|$)"), date("YYYYMMDD"), {"remove": True})

    # Complete
    parser.add_handler("complete", regex.compile(r"\b((?:19\d|20[012])\d[ .]?-[ .]?(?:19\d|20[012])\d)\b"), boolean, {"remove": True})  # year range
    parser.add_handler("complete", regex.compile(r"[([][ .]?((?:19\d|20[012])\d[ .]?-[ .]?\d{2})[ .]?[)\]]"), boolean, {"remove": True})  # year range

    # Bit Rate
    parser.add_handler("bitrate", regex.compile(r"\b\d+[kmg]bps\b", regex.IGNORECASE), lowercase, {"remove": True})

    # Year
    parser.add_handler("year", regex.compile(r"\b(20[0-9]{2}|2100)(?!\D*\d{4}\b)"), integer, {"remove": True})
    parser.add_handler("year", regex.compile(r"[([]?(?!^)(?<!\d|Cap[. ]?)((?:19\d|20[012])\d)(?!\d|kbps)[)\]]?", regex.IGNORECASE), integer, {"remove": True})
    parser.add_handler("year", regex.compile(r"^[([]?((?:19\d|20[012])\d)(?!\d|kbps)[)\]]?", regex.IGNORECASE), integer, {"remove": True})

    # Edition
    parser.add_handler("edition", regex.compile(r"\b\d{2,3}(th)?[\.\s\-\+_\/(),]Anniversary[\.\s\-\+_\/(),](Edition|Ed)?\b", regex.IGNORECASE), value("Anniversary Edition"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\bUltimate[\.\s\-\+_\/(),]Edition\b", regex.IGNORECASE), value("Ultimate Edition"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\bExtended[\.\s\-\+_\/(),]Director\"?s\b", regex.IGNORECASE), value("Directors Cut"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\b(custom.?)?Extended\b", regex.IGNORECASE), value("Extended Edition"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\bDirector\"?s[\.\s\-\+_\/(),]Cut\b", regex.IGNORECASE), value("Directors Cut"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\bCollector\"?s\b", regex.IGNORECASE), value("Collectors Edition"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\bTheatrical\b", regex.IGNORECASE), value("Theatrical"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\bUncut\b", regex.IGNORECASE), value("Uncut"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\bIMAX\b", regex.IGNORECASE), value("IMAX"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\bDiamond\b", regex.IGNORECASE), value("Diamond Edition"), {"remove": True})
    parser.add_handler("edition", regex.compile(r"\bRemaster(?:ed)?\b", regex.IGNORECASE), value("Remastered"), {"remove": True, "skipIfAlreadyFound": True})

    # Upscaled
    parser.add_handler("upscaled", regex.compile(r"\b(?:AI.?)?(Upscaled?|Enhanced?)\b", regex.IGNORECASE), boolean)
    parser.add_handler("upscaled", regex.compile(r"\b(?:iris2|regrade|ups(uhd|fhd|hd|4k))\b", regex.IGNORECASE), boolean)
    parser.add_handler("upscaled", regex.compile(r"\b\.AI\.\b", regex.IGNORECASE), boolean)

    # Convert
    parser.add_handler("convert", regex.compile(r"\bCONVERT\b", regex.IGNORECASE), boolean)

    # Hardcoded
    parser.add_handler("hardcoded", regex.compile(r"\bHC|HARDCODED\b", regex.IGNORECASE), boolean)

    # Proper
    parser.add_handler("proper", regex.compile(r"\b(?:REAL.)?PROPER\b", regex.IGNORECASE), boolean)

    # Repack
    parser.add_handler("repack", regex.compile(r"\bREPACK|RERIP\b", regex.IGNORECASE), boolean)

    # Retail
    parser.add_handler("retail", regex.compile(r"\bRetail\b", regex.IGNORECASE), boolean)

    # Remastered
    parser.add_handler("remastered", regex.compile(r"\bRemaster(?:ed)?\b", regex.IGNORECASE), boolean)

    # Documentary
    parser.add_handler("documentary", regex.compile(r"\bDOCU(?:menta?ry)?\b", regex.IGNORECASE), boolean)

    # Unrated
    parser.add_handler("unrated", regex.compile(r"\bunrated|uncensored\b", regex.IGNORECASE), boolean)

    # Region
    parser.add_handler("region", regex.compile(r"R\d\b"), none, {"skipIfFirst": True})

    # Quality
    parser.add_handler("quality", regex.compile(r"\b(?:HD[ .-]*)?T(?:ELE)?S(?:YNC)?(?:Rip)?\b", regex.IGNORECASE), value("TeleSync"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\b(?:HD[ .-]*)?T(?:ELE)?C(?:INE)?(?:Rip)?\b"), value("TeleCine"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\b(?:DVD?|BD|BR)?[ .-]*Scr(?:eener)?\b", regex.IGNORECASE), value("SCR"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bP(?:RE)?-?(HD|DVD)(?:Rip)?\b", regex.IGNORECASE), value("SCR"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bBlu[ .-]*Ray\b(?=.*remux)", regex.IGNORECASE), value("BluRay REMUX"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"(?:BD|BR|UHD)[- ]?remux", regex.IGNORECASE), value("BluRay REMUX"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"(?<=remux.*)\bBlu[ .-]*Ray\b", regex.IGNORECASE), value("BluRay REMUX"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bremux\b", regex.IGNORECASE), value("REMUX"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bBlu[ .-]*Ray\b(?![ .-]*Rip)", regex.IGNORECASE), value("BluRay"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bUHD[ .-]*Rip\b", regex.IGNORECASE), value("UHDRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bHD[ .-]*Rip\b", regex.IGNORECASE), value("HDRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bMicro[ .-]*HD\b", regex.IGNORECASE), value("HDRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\b(?:BR|Blu[ .-]*Ray)[ .-]*Rip\b", regex.IGNORECASE), value("BRRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bBD[ .-]*Rip\b|\bBDR\b|\bBD-RM\b|[[(]BD[\]) .,-]", regex.IGNORECASE), value("BDRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\b(?:HD[ .-]*)?DVD[ .-]*Rip\b", regex.IGNORECASE), value("DVDRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bVHS[ .-]*Rip?\b", regex.IGNORECASE), value("VHSRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bDVD(?:R\d?|.*Mux)?\b", regex.IGNORECASE), value("DVD"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bVHS\b", regex.IGNORECASE), value("VHS"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bPPVRip\b", regex.IGNORECASE), value("PPVRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bHD.?TV.?Rip\b", regex.IGNORECASE), value("HDTVRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bHD.?TV\b", regex.IGNORECASE), value("HDTV"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bDVB[ .-]*(?:Rip)?\b", regex.IGNORECASE), value("HDTV"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bSAT[ .-]*Rips?\b", regex.IGNORECASE), value("SATRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bTVRips?\b", regex.IGNORECASE), value("TVRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bR5\b", regex.IGNORECASE), value("R5"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\b(?:DL|WEB|BD|BR)MUX\b", regex.IGNORECASE), value("WEBMux"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bWEB[ .-]*Rip\b", regex.IGNORECASE), value("WEBRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bWEB[ .-]?DL[ .-]?Rip\b", regex.IGNORECASE), value("WEB-DLRip"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\bWEB[ .-]*(DL|.BDrip|.DLRIP)\b", regex.IGNORECASE), value("WEB-DL"), {"remove": True})
    parser.add_handler("quality", regex.compile(r"\b(?<!\w.)WEB\b|\bWEB(?!([ \.\-\(\],]+\d))\b", regex.IGNORECASE), value("WEB"), {"remove": True, "skipFromTitle": True})  #
    parser.add_handler("quality", regex.compile(r"\b(?:H[DQ][ .-]*)?CAM(?!.?(S|E|\()\d+)(?:H[DQ])?(?:[ .-]*Rip|Rp)?\b", regex.IGNORECASE), value("CAM"), {"remove": True, "skipFromTitle": True})  # can appear in a title as well, check it last
    parser.add_handler("quality", regex.compile(r"\b(?:H[DQ][ .-]*)?S[ \.\-]print", regex.IGNORECASE), value("CAM"), {"remove": True, "skipFromTitle": True})  # can appear in a title as well, check it last
    parser.add_handler("quality", regex.compile(r"\bPDTV\b", regex.IGNORECASE), value("PDTV"), {"remove": True})

    # Video depth
    parser.add_handler("bit_depth", regex.compile(r"\bhevc\s?10\b", regex.IGNORECASE), value("10bit"))
    parser.add_handler("bit_depth", regex.compile(r"(?:8|10|12)[-\.]?(?=bit)", regex.IGNORECASE), value("$1bit"), {"remove": True})
    parser.add_handler("bit_depth", regex.compile(r"\bhdr10\b", regex.IGNORECASE), value("10bit"))
    parser.add_handler("bit_depth", regex.compile(r"\bhi10\b", regex.IGNORECASE), value("10bit"))

    def handle_bit_depth(context):
        result = context["result"]
        if "bit_depth" in result:
            # Replace hyphens and spaces with nothing (effectively removing them)
            result["bit_depth"] = result["bit_depth"].replace(" ", "").replace("-", "")

    parser.add_handler("bit_depth", handle_bit_depth)

    # HDR
    parser.add_handler("hdr", regex.compile(r"\bDV\b|dolby.?vision|\bDoVi\b", regex.IGNORECASE), uniq_concat(value("DV")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("hdr", regex.compile(r"HDR10(?:\+|plus)", regex.IGNORECASE), uniq_concat(value("HDR10+")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("hdr", regex.compile(r"\bHDR(?:10)?\b", regex.IGNORECASE), uniq_concat(value("HDR")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("hdr", regex.compile(r"\bSDR\b", regex.IGNORECASE), uniq_concat(value("SDR")), {"remove": True, "skipIfAlreadyFound": False})

    # Codec
    parser.add_handler("codec", regex.compile(r"\b[hx][\. \-]?264\b", regex.IGNORECASE), value("avc"), {"remove": True})
    parser.add_handler("codec", regex.compile(r"\b[hx][\. \-]?265\b", regex.IGNORECASE), value("hevc"), {"remove": True})
    parser.add_handler("codec", regex.compile(r"\bHEVC10(bit)?\b|\b[xh][\. \-]?265\b", regex.IGNORECASE), value("hevc"), {"remove": True})
    parser.add_handler("codec", regex.compile(r"\bhevc(?:\s?10)?\b", regex.IGNORECASE), value("hevc"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("codec", regex.compile(r"\bdivx|xvid\b", regex.IGNORECASE), value("xvid"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("codec", regex.compile(r"\bavc\b", regex.IGNORECASE), value("avc"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("codec", regex.compile(r"\bav1\b", regex.IGNORECASE), value("av1"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("codec", regex.compile(r"\b(?:mpe?g\d*)\b", regex.IGNORECASE), value("mpeg"), {"remove": True, "skipIfAlreadyFound": False})

    def handle_space_in_codec(context):
        if context["result"].get("codec"):
            context["result"]["codec"] = regex.sub("[ .-]", "", context["result"]["codec"])

    parser.add_handler("codec", handle_space_in_codec)

    # Channels
    parser.add_handler("channels", regex.compile(r"\bDDP?5[ \.\_]1\b", regex.IGNORECASE), uniq_concat(value("5.1")), {"remove": False})
    parser.add_handler("channels", regex.compile(r"\b5\.1(ch)?\b", regex.IGNORECASE), uniq_concat(value("5.1")), {"remove": False})
    parser.add_handler("channels", regex.compile(r"\b7[\.\- ]1(.?ch(annel)?)?\b", regex.IGNORECASE), uniq_concat(value("7.1")), {"remove": False})
    parser.add_handler("channels", regex.compile(r"\b2\.0\b", regex.IGNORECASE), uniq_concat(value("2.0")), {"remove": False})
    parser.add_handler("channels", regex.compile(r"\bstereo\b", regex.IGNORECASE), uniq_concat(value("stereo")), {"remove": False})
    parser.add_handler("channels", regex.compile(r"\bmono\b", regex.IGNORECASE), uniq_concat(value("mono")), {"remove": False})
    parser.add_handler("channels", regex.compile(r"\b(?:x[2-4]|5[\W]1(?:x[2-4])?)\b", regex.IGNORECASE), uniq_concat(value("5.1")), {"remove": True})
    parser.add_handler("channels", regex.compile(r"\b2\.0(?:x[2-4])\b", regex.IGNORECASE), uniq_concat(value("2.0")), {"remove": True})

    # Audio
    parser.add_handler("audio", regex.compile(r"\bDDP5[ \.\_]1\b", regex.IGNORECASE), uniq_concat(value("Dolby Digital Plus")), {"remove": True, "skipIfFirst": True})
    parser.add_handler("audio", regex.compile(r"\b(?!.+HR)(DTS.?HD.?Ma(ster)?|DTS.?X)\b", regex.IGNORECASE), uniq_concat(value("DTS Lossless")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\bDTS(?!(.?HD.?Ma(ster)?|.X)).?(HD.?HR|HD)?\b", regex.IGNORECASE), uniq_concat(value("DTS Lossy")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\b(Dolby.?)?Atmos\b", regex.IGNORECASE), uniq_concat(value("Atmos")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\b(TrueHD|\.True\.)\b", regex.IGNORECASE), uniq_concat(value("TrueHD")), {"remove": True, "skipIfAlreadyFound": False, "skipFromTitle": True})
    parser.add_handler("audio", regex.compile(r"\bTRUE\b"), uniq_concat(value("TrueHD")), {"remove": True, "skipIfAlreadyFound": False, "skipFromTitle": True})
    parser.add_handler("audio", regex.compile(r"\bFLAC(?:\+?2\.0)?(x[2-4])?\b", regex.IGNORECASE), uniq_concat(value("FLAC")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\bEAC-?3(?:[. -]?[256]\.[01])?\b", regex.IGNORECASE), uniq_concat(value("EAC3")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\bAC-?3(x2)?(?:[ .-](5\.1)?[x+]2\.?0?x?3?)?\b", regex.IGNORECASE), uniq_concat(value("AC3")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\b5\.1(ch)?\b", regex.IGNORECASE), uniq_concat(value("AC3")), {"remove": True, "skipIfAlreadyFound": True})
    parser.add_handler("audio", regex.compile(r"\b(DD2?[\+p]2?(.?5.1)?|DD Plus|Dolby Digital Plus)\b", regex.IGNORECASE), uniq_concat(value("Dolby Digital Plus")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\b(DD|Dolby.?Digital.?)2?(5.?1)?(?!.?(Plus|P|\+))\b", regex.IGNORECASE), uniq_concat(value("Dolby Digital")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\bQ?Q?AAC(x?2)?\b", regex.IGNORECASE), uniq_concat(value("AAC")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\b(H[DQ])?.?(Clean.?Aud(io)?)\b", regex.IGNORECASE), uniq_concat(value("HQ Clean Audio")), {"remove": True, "skipIfAlreadyFound": False})

    # Group
    parser.add_handler("group", regex.compile(r"- ?(?!\d+$|S\d+|\d+x|ep?\d+|[^[]+]$)([^\-. []+[^\-. [)\]\d][^\-. [)\]]*)(?:\[[\w.-]+])?(?=\.\w{2,4}$|$)", regex.IGNORECASE), none, {"remove": False})

    # Container
    parser.add_handler("container", regex.compile(r"\.?[\[(]?\b(MKV|AVI|MP4|WMV|MPG|MPEG)\b[\])]?", regex.IGNORECASE), lowercase)

    # Volume
    parser.add_handler("volumes", regex.compile(r"\bvol(?:s|umes?)?[. -]*(?:\d{1,2}[., +/\\&-]+)+\d{1,2}\b", regex.IGNORECASE), range_func, {"remove": True})

    def handle_volumes(context):
        title = context["title"]
        result = context["result"]
        matched = context["matched"]

        start_index = matched.get("year", {}).get("match_index", 0)
        match = regex.search(r"\bvol(?:ume)?[. -]*(\d{1,2})", title[start_index:], regex.IGNORECASE)

        if match:
            matched["volumes"] = {"match": match.group(0), "match_index": match.start()}
            result["volumes"] = [int(match.group(1))]
            return {"raw_match": match.group(0), "match_index": match.start() + start_index, "remove": True}
        return None

    parser.add_handler("volumes", handle_volumes)

    # Pre-Language
    parser.add_handler("languages", regex.compile(r"\b(temporadas?|completa)\b", regex.IGNORECASE), uniq_concat(value("es")), {"skipIfAlreadyFound": False})

    # Complete
    parser.add_handler("complete", regex.compile(r"(?:\bthe\W)?(?:\bcomplete|collection|dvd)?\b[ .]?\bbox[ .-]?set\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"(?:\bthe\W)?(?:\bcomplete|collection|dvd)?\b[ .]?\bmini[ .-]?series\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"(?:\bthe\W)?(?:\bcomplete|full|all)\b.*\b(?:series|seasons|collection|episodes|set|pack|movies)\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"\b(?:series|seasons|movies?)\b.*\b(?:complete|collection)\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"(?:\bthe\W)?\bultimate\b[ .]\bcollection\b", regex.IGNORECASE), boolean, {"skipIfAlreadyFound": False})
    parser.add_handler("complete", regex.compile(r"\bcollection\b.*\b(?:set|pack|movies)\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"\bcollection\b", regex.IGNORECASE), boolean, {"skipFromTitle": True})
    parser.add_handler("complete", regex.compile(r"duology|trilogy|quadr[oi]logy|tetralogy|pentalogy|hexalogy|heptalogy|anthology", regex.IGNORECASE), boolean, {"skipIfAlreadyFound": False})
    parser.add_handler("complete", regex.compile(r"\bcompleta\b", regex.IGNORECASE), boolean, {"remove": True})
    parser.add_handler("complete", regex.compile(r"\bsaga\b", regex.IGNORECASE), boolean, {"skipFromTitle": True, "skipIfAlreadyFound": True})

    # Seasons
    parser.add_handler("seasons", regex.compile(r"(?:complete\W|seasons?\W|\W|^)((?:s\d{1,2}[., +/\\&-]+)+s\d{1,2}\b)", regex.IGNORECASE), range_func, {"remove": True})
    parser.add_handler("seasons", regex.compile(r"(?:complete\W|seasons?\W|\W|^)[([]?(s\d{2,}-\d{2,}\b)[)\]]?", regex.IGNORECASE), range_func, {"remove": True})
    parser.add_handler("seasons", regex.compile(r"(?:complete\W|seasons?\W|\W|^)[([]?(s[1-9]-[2-9])[)\]]?", regex.IGNORECASE), range_func, {"remove": True})
    parser.add_handler("seasons", regex.compile(r"\d+ª(?:.+)?(?:a.?)?\d+ª(?:(?:.+)?(?:temporadas?))", regex.IGNORECASE), range_func, {"remove": True})
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?(?:seasons?|[Сс]езони?|temporadas?)[. ]?[-:]?[. ]?[([]?((?:\d{1,2}[., /\\&]+)+\d{1,2}\b)[)\]]?", regex.IGNORECASE), range_func, {"remove": True})
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?(?:seasons?|[Сс]езони?|temporadas?)[. ]?[-:]?[. ]?[([]?((?:\d{1,2}[.-]+)+[1-9]\d?\b)[)\]]?", regex.IGNORECASE), range_func, {"remove": True})
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?season[. ]?[([]?((?:\d{1,2}[. -]+)+[1-9]\d?\b)[)\]]?(?!.*\.\w{2,4}$)", regex.IGNORECASE), range_func, {"remove": True})
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?\bseasons?\b[. -]?(\d{1,2}[. -]?(?:to|thru|and|\+|:)[. -]?\d{1,2})\b", regex.IGNORECASE), range_func, {"remove": True})
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?(?:saison|seizoen|season|series|temp(?:orada)?):?[. ]?(\d{1,2})\b", regex.IGNORECASE), array(integer))
    parser.add_handler("seasons", regex.compile(r"(\d{1,2})(?:-?й)?[. _]?(?:[Сс]езон|sez(?:on)?)(?:\W?\D|$)", regex.IGNORECASE), array(integer))
    parser.add_handler("seasons", regex.compile(r"[Сс]езон:?[. _]?№?(\d{1,2})(?!\d)", regex.IGNORECASE), array(integer))
    parser.add_handler("seasons", regex.compile(r"(?:\D|^)(\d{1,2})Â?[°ºªa]?[. ]*temporada", regex.IGNORECASE), array(integer), {"remove": True})
    parser.add_handler("seasons", regex.compile(r"t(\d{1,3})(?:[ex]+|$)", regex.IGNORECASE), array(integer), {"remove": True})
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete)?(?:\W|^)s(\d{1,3})(?:[\Wex]|\d{2}\b|$)", regex.IGNORECASE), array(integer), {"skipIfAlreadyFound": False})
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?(?:\W|^)(\d{1,2})[. ]?(?:st|nd|rd|th)[. ]*season", regex.IGNORECASE), array(integer))
    parser.add_handler("seasons", regex.compile(r"(?<=S)\d{2}(?=E\d+)"), array(integer))
    parser.add_handler("seasons", regex.compile(r"(?:\D|^)(\d{1,2})[xх]\d{1,3}(?:\D|$)"), array(integer))
    parser.add_handler("seasons", regex.compile(r"\bSn([1-9])(?:\D|$)"), array(integer))
    parser.add_handler("seasons", regex.compile(r"[[(](\d{1,2})\.\d{1,3}[)\]]"), array(integer))
    parser.add_handler("seasons", regex.compile(r"-\s?(\d{1,2})\.\d{2,3}\s?-"), array(integer))
    parser.add_handler("seasons", regex.compile(r"(?:^|\/)(\d{1,2})-\d{2}\b(?!-\d)"), array(integer))
    parser.add_handler("seasons", regex.compile(r"[^\w-](\d{1,2})-\d{2}(?=\.\w{2,4}$)"), array(integer))
    parser.add_handler("seasons", regex.compile(r"(?<!\bEp?(?:isode)? ?\d+\b.*)\b(\d{2})[ ._]\d{2}(?:.F)?\.\w{2,4}$"), array(integer))
    parser.add_handler("seasons", regex.compile(r"\bEp(?:isode)?\W+(\d{1,2})\.\d{1,3}\b", regex.IGNORECASE), array(integer))

    # Episodes
    parser.add_handler("episodes", regex.compile(r"(?:[\W\d]|^)e[ .]?[([]?(\d{1,3}(?:[ .-]*(?:[&+]|e){1,2}[ .]?\d{1,3})+)(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"(?:[\W\d]|^)ep[ .]?[([]?(\d{1,3}(?:[ .-]*(?:[&+]|ep){1,2}[ .]?\d{1,3})+)(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"(?:[\W\d]|^)\d+[xх][ .]?[([]?(\d{1,3}(?:[ .]?[xх][ .]?\d{1,3})+)(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"(?:[\W\d]|^)(?:episodes?|[Сс]ерии:?)[ .]?[([]?(\d{1,3}(?:[ .+]*[&+][ .]?\d{1,3})+)(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"[([]?(?:\D|^)(\d{1,3}[ .]?ao[ .]?\d{1,3})[)\]]?(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"(?:[\W\d]|^)(?:e|eps?|episodes?|[Сс]ерии:?|\d+[xх])[ .]*[([]?(\d{1,3}(?:-\d{1,3})+)(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"(?:\W|^)[st]\d{1,2}[. ]?[xх-]?[. ]?(?:e|x|х|ep|-|\.)[. ]?(\d{1,4})(?:[abc]|v0?[1-4]|\D|$)", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"\b[st]\d{2}(\d{2})\b", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?:\W|^)(\d{1,3}(?:[ .]*~[ .]*\d{1,3})+)(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"-\s(\d{1,3}[ .]*-[ .]*\d{1,3})(?!-\d)(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"s\d{1,2}\s?\((\d{1,3}[ .]*-[ .]*\d{1,3})\)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"(?:^|\/)\d{1,2}-(\d{2})\b(?!-\d)"), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<!\d-)\b\d{1,2}-(\d{2})(?=\.\w{2,4}$)"), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<=^\[.+].+)[. ]+-[. ]+(\d{1,4})[. ]+(?=\W)", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<!(?:seasons?|[Сс]езони?)\W*)(?:[ .([-]|^)(\d{1,3}(?:[ .]?[,&+~][ .]?\d{1,3})+)(?:[ .)\]-]|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"(?<!(?:seasons?|[Сс]езони?)\W*)(?:[ .([-]|^)(\d{1,3}(?:-\d{1,3})+)(?:[ .)(\]]|-\D|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"\bEp(?:isode)?\W+\d{1,2}\.(\d{1,3})\b", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?:\b[ée]p?(?:isode)?|[Ээ]пизод|[Сс]ер(?:ии|ия|\.)?|cap(?:itulo)?|epis[oó]dio)[. ]?[-:#№]?[. ]?(\d{1,4})(?:[abc]|v0?[1-4]|\W|$)", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"\b(\d{1,3})(?:-?я)?[ ._-]*(?:ser(?:i?[iyj]a|\b)|[Сс]ер(?:ии|ия|\.)?)", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?:\D|^)\d{1,2}[. ]?[xх][. ]?(\d{1,3})(?:[abc]|v0?[1-4]|\D|$)"), array(integer))  # Fixed: Was catching `1.x265` as episode.
    parser.add_handler("episodes", regex.compile(r"(?<=S\d{2}E)\d+", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"[[(]\d{1,2}\.(\d{1,3})[)\]]"), array(integer))
    parser.add_handler("episodes", regex.compile(r"\b[Ss]\d{1,2}[ .](\d{1,2})\b"), array(integer))
    parser.add_handler("episodes", regex.compile(r"-\s?\d{1,2}\.(\d{2,3})\s?-"), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<=\D|^)(\d{1,3})[. ]?(?:of|из|iz)[. ]?\d{1,3}(?=\D|$)", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"\b\d{2}[ ._-](\d{2})(?:.F)?\.\w{2,4}$"), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<!^)\[(\d{2,3})](?!(?:\.\w{2,4})?$)"), array(integer))
    parser.add_handler("episodes", regex.compile(r"(\d+)(?=.?\[([A-Z0-9]{8})])", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<![xh])\b264\b|\b265\b", regex.IGNORECASE), array(integer), {"remove": True})
    parser.add_handler("episodes", regex.compile(r"(?<!\bMovie\s-\s)(?<=\s-\s)\d+(?=\s[-(\s])"), array(integer), {"remove": True, "skipIfAlreadyFound": True})

    def handle_episodes(context):
        title = context["title"]
        result = context.get("result", {})
        matched = context.get("matched", {})

        if "episodes" not in result:
            start_indexes = [comp.get("match_index") for comp in [matched.get("year"), matched.get("seasons")] if comp and comp.get("match_index", None)]
            end_indexes = [comp["match_index"] for comp in [matched.get("resolution"), matched.get("quality"), matched.get("codec"), matched.get("audio")] if comp and comp.get("match_index", None)]

            start_index = min(start_indexes) if start_indexes else 0
            end_index = min(end_indexes + [len(title)])

            beginning_title = title[:end_index]
            middle_title = title[start_index:end_index]

            matches = regex.search(r"(?<!movie\W*|film\W*|^)(?:[ .]+-[ .]+|[([][ .]*)(\d{1,4})(?:a|b|v\d|\.\d)?(?:\W|$)(?!movie|film|\d+)", beginning_title, regex.IGNORECASE) or regex.search(r"^(?:[([-][ .]?)?(\d{1,4})(?:a|b|v\d)?(?:\W|$)(?!movie|film)", middle_title, regex.IGNORECASE)

            if matches:
                episode_numbers = [int(num) for num in regex.findall(r"\d+", matches.group(1))]
                result["episodes"] = episode_numbers
                return {"match_index": title.index(matches.group(0))}

        return None

    parser.add_handler("episodes", handle_episodes)

    # Country Code
    parser.add_handler("country", regex.compile(r"\b(US|UK)\b"), value("$1"))

    # Languages (ISO 639-1 Standardized)
    parser.add_handler("languages", regex.compile(r"\bengl?(?:sub[A-Z]*)?\b", regex.IGNORECASE), uniq_concat(value("en")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\beng?sub[A-Z]*\b", regex.IGNORECASE), uniq_concat(value("en")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bing(?:l[eéê]s)?\b", regex.IGNORECASE), uniq_concat(value("en")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\besub\b", regex.IGNORECASE), uniq_concat(value("en")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\benglish\W+(?:subs?|sdh|hi)\b", regex.IGNORECASE), uniq_concat(value("en")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\beng?\b", regex.IGNORECASE), uniq_concat(value("en")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\benglish?\b", regex.IGNORECASE), uniq_concat(value("en")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:JP|JAP|JPN)\b", regex.IGNORECASE), uniq_concat(value("ja")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(japanese|japon[eê]s)\b", regex.IGNORECASE), uniq_concat(value("ja")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:KOR|kor[ .-]?sub)\b", regex.IGNORECASE), uniq_concat(value("ko")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(korean|coreano)\b", regex.IGNORECASE), uniq_concat(value("ko")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:traditional\W*chinese|chinese\W*traditional)(?:\Wchi)?\b", regex.IGNORECASE), uniq_concat(value("zh")), {"skipIfAlreadyFound": False, "remove": True})
    parser.add_handler("languages", regex.compile(r"\bzh-hant\b", regex.IGNORECASE), uniq_concat(value("zh")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:mand[ae]rin|ch[sn])\b", regex.IGNORECASE), uniq_concat(value("zh")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"(?<!shang-?)\bCH(?:I|T)\b", regex.IGNORECASE), uniq_concat(value("zh")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(chinese|chin[eê]s)\b", regex.IGNORECASE), uniq_concat(value("zh")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bzh-hans\b", regex.IGNORECASE), uniq_concat(value("zh")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bFR(?:ench|a|e|anc[eê]s)?\b", regex.IGNORECASE), uniq_concat(value("fr")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(VOST(?:FR?|A)?)\b", regex.IGNORECASE), uniq_concat(value("fr")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(VF[FQIB2]?|(TRUE|SUB)?.?FRENCH|(VOST)?FR2?)\b", regex.IGNORECASE), uniq_concat(value("fr")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bspanish\W?latin|american\W*(?:spa|esp?)", regex.IGNORECASE), uniq_concat(value("la")), {"skipFromTitle": True, "skipIfAlreadyFound": False, "remove": True})
    parser.add_handler("languages", regex.compile(r"\b(?:\bla\b.+(?:cia\b))", regex.IGNORECASE), uniq_concat(value("es")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:audio.)?lat(?:in?|ino)?\b", regex.IGNORECASE), uniq_concat(value("la")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:audio.)?(?:ESP|spa|(en[ .]+)?espa[nñ]ola?|castellano)\b", regex.IGNORECASE), uniq_concat(value("es")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bes(?=[ .,/-]+(?:[A-Z]{2}[ .,/-]+){2,})\b", regex.IGNORECASE), uniq_concat(value("es")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?<=[ .,/-]+(?:[A-Z]{2}[ .,/-]+){2,})es\b", regex.IGNORECASE), uniq_concat(value("es")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?<=[ .,/-]+[A-Z]{2}[ .,/-]+)es(?=[ .,/-]+[A-Z]{2}[ .,/-]+)\b", regex.IGNORECASE), uniq_concat(value("es")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bes(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("es")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bspanish\W+subs?\b", regex.IGNORECASE), uniq_concat(value("es")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(spanish|espanhol)\b", regex.IGNORECASE), uniq_concat(value("es")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:p[rt]|en|port)[. (\\/-]*BR\b", regex.IGNORECASE), uniq_concat(value("pt")), {"skipIfAlreadyFound": False, "remove": True})
    parser.add_handler("languages", regex.compile(r"\bbr(?:a|azil|azilian)\W+(?:pt|por)\b", regex.IGNORECASE), uniq_concat(value("pt")), {"skipIfAlreadyFound": False, "remove": True})
    parser.add_handler("languages", regex.compile(r"\b(?:leg(?:endado|endas?)?|dub(?:lado)?|portugu[eèê]se?)[. -]*BR\b", regex.IGNORECASE), uniq_concat(value("pt")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bleg(?:endado|endas?)\b", regex.IGNORECASE), uniq_concat(value("pt")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bportugu[eèê]s[ea]?\b", regex.IGNORECASE), uniq_concat(value("pt")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bPT[. -]*(?:PT|ENG?|sub(?:s|titles?))\b", regex.IGNORECASE), uniq_concat(value("pt")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bpt(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("pt")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bpor\b", regex.IGNORECASE), uniq_concat(value("pt")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b-?ITA\b", regex.IGNORECASE), uniq_concat(value("it")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?<!w{3}\.\w+\.)IT(?=[ .,/-]+(?:[a-zA-Z]{2}[ .,/-]+){2,})\b"), uniq_concat(value("it")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bit(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("it")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bitaliano?\b", regex.IGNORECASE), uniq_concat(value("it")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bgreek[ .-]*(?:audio|lang(?:uage)?|subs?(?:titles?)?)?\b", regex.IGNORECASE), uniq_concat(value("el")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:GER|DEU)\b", regex.IGNORECASE), uniq_concat(value("de")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bde(?=[ .,/-]+(?:[A-Z]{2}[ .,/-]+){2,})\b", regex.IGNORECASE), uniq_concat(value("de")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?<=[ .,/-]+(?:[A-Z]{2}[ .,/-]+){2,})de\b", regex.IGNORECASE), uniq_concat(value("de")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?<=[ .,/-]+[A-Z]{2}[ .,/-]+)de(?=[ .,/-]+[A-Z]{2}[ .,/-]+)\b", regex.IGNORECASE), uniq_concat(value("de")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bde(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("de")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(german|alem[aã]o)\b", regex.IGNORECASE), uniq_concat(value("de")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bRUS?\b", regex.IGNORECASE), uniq_concat(value("ru")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(russian|russo)\b", regex.IGNORECASE), uniq_concat(value("ru")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bUKR\b", regex.IGNORECASE), uniq_concat(value("uk")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bukrainian\b", regex.IGNORECASE), uniq_concat(value("uk")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bhin(?:di)?\b", regex.IGNORECASE), uniq_concat(value("hi")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)tel(?!\W*aviv)|telugu)\b", regex.IGNORECASE), uniq_concat(value("te")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bt[aâ]m(?:il)?\b", regex.IGNORECASE), uniq_concat(value("ta")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)MAL(?:ay)?|malayalam)\b", regex.IGNORECASE), uniq_concat(value("ml")), {"remove": True, "skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)KAN(?:nada)?|kannada)\b", regex.IGNORECASE), uniq_concat(value("kn")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)MAR(?:a(?:thi)?)?|marathi)\b", regex.IGNORECASE), uniq_concat(value("mr")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)GUJ(?:arati)?|gujarati)\b", regex.IGNORECASE), uniq_concat(value("gu")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)PUN(?:jabi)?|punjabi)\b", regex.IGNORECASE), uniq_concat(value("pa")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)BEN(?!.\bThe|and|of\b)(?:gali)?|bengali)\b", regex.IGNORECASE), uniq_concat(value("bn")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?<!YTS\.)LT\b"), uniq_concat(value("lt")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\blithuanian\b", regex.IGNORECASE), uniq_concat(value("lt")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\blatvian\b", regex.IGNORECASE), uniq_concat(value("lv")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bestonian\b", regex.IGNORECASE), uniq_concat(value("et")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)PL|pol)\b", regex.IGNORECASE), uniq_concat(value("pl")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(polish|polon[eê]s|polaco)\b", regex.IGNORECASE), uniq_concat(value("pl")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bCZ[EH]?\b", regex.IGNORECASE), uniq_concat(value("cs")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bczech\b", regex.IGNORECASE), uniq_concat(value("cs")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bslo(?:vak|vakian|subs|[\]_)]?\.\w{2,4}$)\b", regex.IGNORECASE), uniq_concat(value("sk")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bHU\b"), uniq_concat(value("hu")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bHUN(?:garian)?\b", regex.IGNORECASE), uniq_concat(value("hu")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bROM(?:anian)?\b", regex.IGNORECASE), uniq_concat(value("ro")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bRO(?=[ .,/-]*(?:[A-Z]{2}[ .,/-]+)*sub)", regex.IGNORECASE), uniq_concat(value("ro")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bbul(?:garian)?\b", regex.IGNORECASE), uniq_concat(value("bg")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:srp|serbian)\b", regex.IGNORECASE), uniq_concat(value("sr")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:HRV|croatian)\b", regex.IGNORECASE), uniq_concat(value("hr")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bHR(?=[ .,/-]*(?:[A-Z]{2}[ .,/-]+)*sub)\b", regex.IGNORECASE), uniq_concat(value("hr")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bslovenian\b", regex.IGNORECASE), uniq_concat(value("sl")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)NL|dut|holand[eê]s)\b", regex.IGNORECASE), uniq_concat(value("nl")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bdutch\b", regex.IGNORECASE), uniq_concat(value("nl")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bflemish\b", regex.IGNORECASE), uniq_concat(value("nl")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:DK|danska|dansub|nordic)\b", regex.IGNORECASE), uniq_concat(value("da")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(danish|dinamarqu[eê]s)\b", regex.IGNORECASE), uniq_concat(value("da")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bdan\b(?=.*\.(?:srt|vtt|ssa|ass|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("da")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)FI|finsk|finsub|nordic)\b", regex.IGNORECASE), uniq_concat(value("fi")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bfinnish\b", regex.IGNORECASE), uniq_concat(value("fi")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)SE|swe|swesubs?|sv(?:ensk)?|nordic)\b", regex.IGNORECASE), uniq_concat(value("sv")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(swedish|sueco)\b", regex.IGNORECASE), uniq_concat(value("sv")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:NOR|norsk|norsub|nordic)\b", regex.IGNORECASE), uniq_concat(value("no")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(norwegian|noruegu[eê]s|bokm[aå]l|nob|nor(?=[\]_)]?\.\w{2,4}$))\b", regex.IGNORECASE), uniq_concat(value("no")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:arabic|[aá]rabe|ara)\b", regex.IGNORECASE), uniq_concat(value("ar")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\barab.*(?:audio|lang(?:uage)?|sub(?:s|titles?)?)\b", regex.IGNORECASE), uniq_concat(value("ar")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bar(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("ar")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:turkish|tur(?:co)?)\b", regex.IGNORECASE), uniq_concat(value("tr")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(TİVİBU|tivibu|bitturk(.net)?|turktorrent)\b", regex.IGNORECASE), uniq_concat(value("tr")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bvietnamese\b|\bvie(?=[\]_)]?\.\w{2,4}$)", regex.IGNORECASE), uniq_concat(value("vi")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bind(?:onesian)?\b", regex.IGNORECASE), uniq_concat(value("id")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(thai|tailand[eê]s)\b", regex.IGNORECASE), uniq_concat(value("th")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(THA|tha)\b"), uniq_concat(value("th")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:malay|may(?=[\]_)]?\.\w{2,4}$)|(?<=subs?\([a-z,]+)may)\b", regex.IGNORECASE), uniq_concat(value("ms")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bheb(?:rew|raico)?\b", regex.IGNORECASE), uniq_concat(value("he")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(persian|persa)\b", regex.IGNORECASE), uniq_concat(value("fa")), {"skipFromTitle": True, "skipIfAlreadyFound": False})

    parser.add_handler("languages", regex.compile(r"[\u3040-\u30ff]+", regex.IGNORECASE), uniq_concat(value("ja")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # japanese
    parser.add_handler("languages", regex.compile(r"[\u3400-\u4dbf]+", regex.IGNORECASE), uniq_concat(value("zh")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # chinese
    parser.add_handler("languages", regex.compile(r"[\u4e00-\u9fff]+", regex.IGNORECASE), uniq_concat(value("zh")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # chinese
    parser.add_handler("languages", regex.compile(r"[\uf900-\ufaff]+", regex.IGNORECASE), uniq_concat(value("zh")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # chinese
    parser.add_handler("languages", regex.compile(r"[\uff66-\uff9f]+", regex.IGNORECASE), uniq_concat(value("ja")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # japanese
    parser.add_handler("languages", regex.compile(r"[\u0400-\u04ff]+", regex.IGNORECASE), uniq_concat(value("ru")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # russian
    parser.add_handler("languages", regex.compile(r"[\u0600-\u06ff]+", regex.IGNORECASE), uniq_concat(value("ar")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # arabic
    parser.add_handler("languages", regex.compile(r"[\u0750-\u077f]+", regex.IGNORECASE), uniq_concat(value("ar")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # arabic
    parser.add_handler("languages", regex.compile(r"[\u0c80-\u0cff]+", regex.IGNORECASE), uniq_concat(value("kn")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # kannada
    parser.add_handler("languages", regex.compile(r"[\u0d00-\u0d7f]+", regex.IGNORECASE), uniq_concat(value("ml")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # malayalam
    parser.add_handler("languages", regex.compile(r"[\u0e00-\u0e7f]+", regex.IGNORECASE), uniq_concat(value("th")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # thai
    parser.add_handler("languages", regex.compile(r"[\u0900-\u097f]+", regex.IGNORECASE), uniq_concat(value("hi")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # hindi
    parser.add_handler("languages", regex.compile(r"[\u0980-\u09ff]+", regex.IGNORECASE), uniq_concat(value("bn")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # bengali
    parser.add_handler("languages", regex.compile(r"[\u0a00-\u0a7f]+", regex.IGNORECASE), uniq_concat(value("gu")), {"skipFromTitle": True, "skipIfAlreadyFound": False})  # gujarati

    def infer_language_based_on_naming(context):
        title = context["title"]
        result = context["result"]
        matched = context["matched"]
        if "languages" not in result or not any(lang in result["languages"] for lang in ["pt", "es"]):
            # Checking if episode naming convention suggests Portuguese language
            if (matched.get("episodes") and regex.search(r"capitulo|ao", matched["episodes"].get("raw_match", ""), regex.IGNORECASE)) or regex.search(r"dublado", title, regex.IGNORECASE):
                result["languages"] = result.get("languages", []) + ["pt"]

        return None

    parser.add_handler("languages", infer_language_based_on_naming)

    # Subbed
    parser.add_handler("subbed", regex.compile(r"\b(?:Official.*?|Dual-?)?sub(s|bed)?\b", regex.IGNORECASE), boolean, {"remove": True})
    parser.add_handler("subbed", regex.compile(r"\bmulti(?:ple)?[ .-]*(?:su?$|sub\w*|dub\w*)\b|msub", regex.IGNORECASE), boolean, {"skipIfAlreadyFound": False, "remove": True})

    # Dubbed
    parser.add_handler("dubbed", regex.compile(r"\bmulti(?:ple)?[ .-]*(?:lang(?:uages?)?|audio|VF2)?\b", regex.IGNORECASE), boolean, {"skipIfAlreadyFound": False})
    parser.add_handler("dubbed", regex.compile(r"\btri(?:ple)?[ .-]*(?:audio|dub\w*)\b", regex.IGNORECASE), boolean, {"skipIfAlreadyFound": False})
    parser.add_handler("dubbed", regex.compile(r"\bdual[ .-]*(?:au?$|[aá]udio|line)\b", regex.IGNORECASE), boolean, {"skipIfAlreadyFound": False})
    parser.add_handler("dubbed", regex.compile(r"\bdual\b(?![ .-]*sub)", regex.IGNORECASE), boolean, {"skipIfAlreadyFound": False})
    parser.add_handler("dubbed", regex.compile(r"\b(fan\s?dub)\b", regex.IGNORECASE), boolean, {"remove": True, "skipFromTitle": True})
    parser.add_handler("dubbed", regex.compile(r"\b(Fan.*)?(?:DUBBED|dublado|dubbing|DUBS?)\b", regex.IGNORECASE), boolean, {"remove": True})
    parser.add_handler("dubbed", regex.compile(r"\b(?!.*\bsub(s|bed)?\b)([ _\-\[(\.])?(dual|multi)([ _\-\[(\.])?(audio)?\b", regex.IGNORECASE), boolean, {"remove": True})
    parser.add_handler("dubbed", regex.compile(r"\b(JAP?(anese)?|ZH)\+ENG?(lish)?|ENG?(lish)?\+(JAP?(anese)?|ZH)\b", regex.IGNORECASE), boolean, {"remove": True})

    def handle_group(context):
        result = context["result"]
        matched = context["matched"]
        if "group" in matched and matched["group"].get("raw_match", "").startswith("[") and matched["group"]["raw_match"].endswith("]"):
            end_index = matched["group"]["match_index"] + len(matched["group"]["raw_match"]) if "group" in matched else 0

            # Check if there's any overlap with other matched elements
            if any(key != "group" and matched[key]["match_index"] < end_index for key in matched if "match_index" in matched[key]) and "group" in result:
                del result["group"]
        return None

    parser.add_handler("group", handle_group)

    # 3D
    parser.add_handler("3d", regex.compile(r"\b((Half.)?SBS|HSBS)\b", regex.IGNORECASE), boolean, {"remove": False, "skipIfFirst": True})
    parser.add_handler("3d", regex.compile(r"\b3D\b", regex.IGNORECASE), boolean, {"remove": False, "skipIfFirst": True})

    # Size
    parser.add_handler("size", regex.compile(r"\b(\d+(\.\d+)?\s?(MB|GB|TB))\b", regex.IGNORECASE), none, {"remove": True})
    
    # Site
    parser.add_handler("site", regex.compile(r"\[([^\]]+\.[^\]]+)\](?=\.\w{2,4}$|\s)", regex.IGNORECASE), value("$1"), {"remove": True})
    parser.add_handler("site", regex.compile(r"\bwww\.\w*\.\w+\b", regex.IGNORECASE), value("$1"), {"remove": True})

    # Networks
    parser.add_handler("network", regex.compile(r"\bATVP?\b", regex.IGNORECASE), value("Apple TV"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bAMZN\b", regex.IGNORECASE), value("Amazon"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bNF|Netflix\b", regex.IGNORECASE), value("Netflix"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bNICK(elodeon)?\b", regex.IGNORECASE), value("Nickelodeon"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bDSNY?P?\b", regex.IGNORECASE), value("Disney"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bH(MAX|BO)\b", regex.IGNORECASE), value("HBO"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bHULU\b", regex.IGNORECASE), value("Hulu"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bCBS\b", regex.IGNORECASE), value("CBS"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bNBC\b", regex.IGNORECASE), value("NBC"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bAMC\b", regex.IGNORECASE), value("AMC"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bPBS\b", regex.IGNORECASE), value("PBS"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\b(Crunchyroll|[. -]CR[. -])\b", regex.IGNORECASE), value("Crunchyroll"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bVICE\b", regex.IGNORECASE), value("VICE"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bSony\b", regex.IGNORECASE), value("Sony"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bHallmark\b", regex.IGNORECASE), value("Hallmark"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bAdult.?Swim\b", regex.IGNORECASE), value("Adult Swim"), {"remove": True})
    parser.add_handler("network", regex.compile(r"\bAnimal.?Planet|ANPL\b", regex.IGNORECASE), value("Animal Planet"), {"remove": True})

    # Extension
    parser.add_handler("extension", regex.compile(r"\.(3g2|3gp|avi|flv|mkv|mk3d|mov|mp2|mp4|m4v|mpe|mpeg|mpg|mpv|webm|wmv|ogm|divx|ts|m2ts|iso|vob|sub|idx|ttxt|txt|smi|srt|ssa|ass|vtt|nfo|html)$", regex.IGNORECASE), lowercase)
    parser.add_handler("audio", regex.compile(r"\bMP3\b", regex.IGNORECASE), uniq_concat(value("MP3")), {"remove": True, "skipIfAlreadyFound": False})

    # Group
    parser.add_handler("group", regex.compile(r"\(([\w-]+)\)(?:$|\.\w{2,4}$)"))
    parser.add_handler("group", regex.compile(r"\b(?:Erai-raws|Erai-raws\.com)\b", regex.IGNORECASE), value("Erai-raws"), {"remove": True})
    parser.add_handler("group", regex.compile(r"^\[([^[\]]+)]"))

    def handle_group_exclusion(context):
        result = context["result"]
        if "group" in result and result["group"] in ["-", ""]:
            del result["group"]
        return None

    parser.add_handler("group", handle_group_exclusion)

    parser.add_handler("trash", regex.compile(r"acesse o original", regex.IGNORECASE), boolean, {"remove": True})

    # Title (hardcoded cleanup)
    parser.add_handler("title", regex.compile(r"\b100[ .-]*years?[ .-]*quest\b", regex.IGNORECASE), none, {"remove": True}) # episode title
