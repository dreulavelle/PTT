import regex

from PTT.parse import Parser
from PTT.transformers import (
    none, value, integer, boolean, lowercase, uppercase, date,
    range_func, year_range, array, uniq_concat
)


def add_defaults(parser: Parser):
    # Episode code
    parser.add_handler("episode_code", regex.compile(r"[[(]([a-zA-Z0-9]{8})[\])](?=\.[a-zA-Z0-9]{1,5}$|$)"), uppercase, {"remove": True})
    parser.add_handler("episode_code", regex.compile(r"\[([A-Z0-9]{8})]"), uppercase, {"remove": True})

    # Resolution
    parser.add_handler("resolution", regex.compile(r"\b(?:\[?\]?4k[\])?]?)\b", regex.IGNORECASE), value("4k"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"21600?[pi]", regex.IGNORECASE), value("4k"), {"skipIfAlreadyFound": False, "remove": True})
    parser.add_handler("resolution", regex.compile(r"\[?\]?3840x\d{4}[\])?]?", regex.IGNORECASE), value("4k"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\[?\]?1920x\d{3,4}[\])?]?", regex.IGNORECASE), value("1080p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\[?\]?1280x\d{3}[\])?]?", regex.IGNORECASE), value("720p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"\[?\]?(\d{3,4}x\d{3,4})[\])?]?", regex.IGNORECASE), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(480|720|1080)0[pi]", regex.IGNORECASE), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:BD|HD|M)(720|1080|2160)"), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(480|576|720|1080|2160)[pi]", regex.IGNORECASE), value("$1p"), {"remove": True})
    parser.add_handler("resolution", regex.compile(r"(?:^|\D)(\d{3,4})[pi]", regex.IGNORECASE), value("$1p"), {"remove": True})

    # Date
    parser.add_handler("date", regex.compile(r"(?:\W|^)([[(]?(?:19[6-9]|20[012])[0-9]([. \-/\\])(?:0[1-9]|1[012])\2(?:0[1-9]|[12][0-9]|3[01])[])]?)(?:\W|$)"), date("YYYY MM DD"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?:\W|^)(\[?\]?(?:0[1-9]|[12][0-9]|3[01])([. \-/\\])(?:0[1-9]|1[012])\2(?:19[6-9]|20[01])[0-9][\])]?)(?:\W|$)"), date("DD MM YYYY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?:\W)(\[?\]?(?:0[1-9]|1[012])([. \-/\\])(?:0[1-9]|[12][0-9]|3[01])\2(?:[0][1-9]|[0126789][0-9])[\])]?)(?:\W|$)"), date("MM DD YY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?:\W)(\[?\]?(?:0[1-9]|[12][0-9]|3[01])([. \-/\\])(?:0[1-9]|1[012])\2(?:[0][1-9]|[0126789][0-9])[\])]?)(?:\W|$)"), date("DD MM YY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?:\W|^)([([]?(?:0?[1-9]|[12][0-9]|3[01])[. ]?(?:st|nd|rd|th)?([. \-/\\])(?:feb(?:ruary)?|jan(?:uary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\2(?:19[7-9]|20[012])[0-9][)\]]?)(?=\W|$)", regex.IGNORECASE), date(["DD MMM YYYY", "Do MMM YYYY", "Do MMMM YYYY"]), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?:\W|^)(\[?\]?(?:0?[1-9]|[12][0-9]|3[01])[. ]?(?:st|nd|rd|th)?([. \-\/\\])(?:feb(?:ruary)?|jan(?:uary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)\2(?:0[1-9]|[0126789][0-9])[\])]?)(?:\W|$)", regex.IGNORECASE), date("DD MMM YY"), {"remove": True})
    parser.add_handler("date", regex.compile(r"(?:\W|^)(\[?\]?20[012][0-9](?:0[1-9]|1[012])(?:0[1-9]|[12][0-9]|3[01])[\])]?)(?:\W|$)"), date("YYYYMMDD"), {"remove": True})

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
    parser.add_handler("source", regex.compile(r"\b(DivX|XviD)\b"), none, {"remove": True}) # TODO: In the js implementation it's true. But then a test case fails in our implementation and i'm not sure why

    # Video depth
    parser.add_handler("bit_depth", regex.compile(r"\bhevc\s?10\b", regex.IGNORECASE), value("10bit"))
    parser.add_handler("bit_depth", regex.compile(r"(?:8|10|12)[- ]?bit", regex.IGNORECASE), lowercase, {"remove": True})
    parser.add_handler("bit_depth", regex.compile(r"\bhdr10\b", regex.IGNORECASE), value("10bit"))
    parser.add_handler("bit_depth", regex.compile(r"\bhi10\b", regex.IGNORECASE), value("10bit"))
    def handle_bit_depth(context):
        result = context['result']
        if 'bitDepth' in result:
            # Replace hyphens and spaces with nothing (effectively removing them)
            result['bit_depth'] = result['bit_depth'].replace(" ", "").replace("-", "")
    parser.add_handler("bit_depth", handle_bit_depth)

    # HDR
    parser.add_handler("hdr", regex.compile(r"\bDV\b|dolby.?vision|\bDoVi\b", regex.IGNORECASE), uniq_concat(value("DV")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("hdr", regex.compile(r"HDR10(?:\+|plus)", regex.IGNORECASE), uniq_concat(value("HDR10+")), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("hdr", regex.compile(r"\bHDR(?:10)?\b", regex.IGNORECASE), uniq_concat(value("HDR")), {"remove": True, "skipIfAlreadyFound": False})

    # Codec
    parser.add_handler("codec", regex.compile(r"\b[xh][-. ]?26[45]", regex.IGNORECASE), lowercase, {"remove": True})
    parser.add_handler("codec", regex.compile(r"\bhevc(?:\s?10)?\b", regex.IGNORECASE), value("hevc"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("codec", regex.compile(r"\b(?:dvix|mpeg2|divx|xvid|avc)\b", regex.IGNORECASE), lowercase, {"remove": True, "skipIfAlreadyFound": False})
    def handle_space_in_codec(context):
        if context["result"].get("codec"):
            context["result"]["codec"] = regex.sub("[ .-]", "", context["result"]["codec"])
    parser.add_handler("codec", handle_space_in_codec)

    # Audio
    parser.add_handler("audio", regex.compile(r"7\.1[. ]?Atmos\b", regex.IGNORECASE), value("7.1 Atmos"), {"remove": True})
    parser.add_handler("audio", regex.compile(r"\b(?:mp3|Atmos|DTS(?:-HD)?|TrueHD)\b", regex.IGNORECASE), lowercase)
    parser.add_handler("audio", regex.compile(r"\bFLAC(?:\+?2\.0)?(?:x[2-4])?\b", regex.IGNORECASE), value("flac"), {"remove": True})
    parser.add_handler("audio", regex.compile(r"\bEAC-?3(?:[. -]?[256]\.[01])?", regex.IGNORECASE), value("eac3"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\bAC-?3(?:[.-]5\.1|x2\.?0?)?\b", regex.IGNORECASE), value("ac3"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\b5\.1(?:x[2-4]+)?\+2\.0(?:x[2-4])?\b", regex.IGNORECASE), value("2.0"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\b2\.0(?:x[2-4]|\+5\.1(?:x[2-4])?)\b", regex.IGNORECASE), value("2.0"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\b5\.1ch\b", regex.IGNORECASE), value("ac3"), {"remove": True, "skipIfAlreadyFound": False})
    parser.add_handler("audio", regex.compile(r"\bDD5[. ]?1\b", regex.IGNORECASE), value("dd5.1"), {"remove": True})
    parser.add_handler("audio", regex.compile(r"\bQ?AAC(?:[. ]?2[. ]0|x2)?\b", regex.IGNORECASE), value("aac"), {"remove": True})

    # Group
    parser.add_handler("group", regex.compile(r"- ?(?!\d+$|S\d+|\d+x|ep?\d+|[^[]+]$)([^\-. []+[^\-. [)\]\d][^\-. [)\]]*)(?:\[[\w.-]+])?(?=\.\w{2,4}$|$)", regex.IGNORECASE), none, {"remove": True})

    # Container
    parser.add_handler("container", regex.compile(r"\.?[\[(]?\b(MKV|AVI|MP4|WMV|MPG|MPEG)\b[\])]?", regex.IGNORECASE), lowercase)

    # Volume
    parser.add_handler("volumes", regex.compile(r"\bvol(?:s|umes?)?[. -]*(?:\d{1,2}[., +/\\&-]+)+\d{1,2}\b", regex.IGNORECASE), range_func, {"remove": True})
    # parser.add_handler("volumes", regex.compile(r"\bvol(?:s|umes?)?[. -]*(\d{1,2})\b", regex.IGNORECASE), integer, {"remove": True})
    def handle_volumes(context):
        title = context['title']
        result = context['result']
        matched = context['matched']

        # Determine the start index based on whether the year is matched
        start_index = matched.get('year', {}).get('match_index', 0)

        # Regular expression to find volume numbers
        match = regex.search(r'\bvol(?:ume)?[. -]*(\d{1,2})', title[start_index:], regex.IGNORECASE)

        if match:
            # Update the matched information for volumes
            matched['volumes'] = {'match': match.group(0), 'match_index': match.start()}

            # Convert the captured group to an integer and store it in the result
            result['volumes'] = [int(match.group(1))]

            # Return a dictionary with details of the raw match and its index
            return {
                'raw_match': match.group(0),
                'match_index': match.start() + start_index,
                'remove': True
            }
        return None
    parser.add_handler("volumes", handle_volumes)

    # Seasons
    parser.add_handler("seasons", regex.compile(r"(?:complete\W|seasons?\W|\W|^)((?:s\d{1,2}[., +/\\&-]+)+s\d{1,2}\b)", regex.IGNORECASE), range_func, { "remove": True })
    parser.add_handler("seasons", regex.compile(r"(?:complete\W|seasons?\W|\W|^)[([]?(s\d{2,}-\d{2,}\b)[)\]]?", regex.IGNORECASE), range_func, { "remove": True })
    parser.add_handler("seasons", regex.compile(r"(?:complete\W|seasons?\W|\W|^)[([]?(s[1-9]-[2-9]\b)[)\]]?", regex.IGNORECASE), range_func, { "remove": True })
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?(?:seasons?|[Сс]езони?|temporadas?)[. ]?[-:]?[. ]?[([]?((?:\d{1,2}[., /\\&]+)+\d{1,2}\b)[)\]]?", regex.IGNORECASE), range_func, { "remove": True })
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?(?:seasons|[Сс]езони?|temporadas?)[. ]?[-:]?[. ]?[([]?((?:\d{1,2}[. -]+)+[1-9]\d?\b)[)\]]?", regex.IGNORECASE), range_func, { "remove": True })
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?season[. ]?[([]?((?:\d{1,2}[. -]+)+[1-9]\d?\b)[)\]]?(?!.*\.\w{2,4}$)", regex.IGNORECASE), range_func, { "remove": True })
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?\bseasons?\b[. -]?(\d{1,2}[. -]?(?:to|thru|and|\+|:)[. -]?\d{1,2})\b", regex.IGNORECASE), range_func, { "remove": True })
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?(?:saison|seizoen|season|series|temp(?:orada)?):?[. ]?(\d{1,2})", regex.IGNORECASE), array(integer))
    parser.add_handler("seasons", regex.compile(r"(\d{1,2})(?:-?й)?[. _]?(?:[Сс]езон|sez(?:on)?)(?:\W?\D|$)", regex.IGNORECASE), array(integer))
    parser.add_handler("seasons", regex.compile(r"[Сс]езон:?[. _]?№?(\d{1,2})(?!\d)", regex.IGNORECASE), array(integer))
    parser.add_handler("seasons", regex.compile(r"(?:\D|^)(\d{1,2})Â?[°ºªa]?[. ]*temporada", regex.IGNORECASE), array(integer), { "remove": True })
    parser.add_handler("seasons", regex.compile(r"t(\d{1,3})(?:[ex]+|$)", regex.IGNORECASE), array(integer), { "remove": True })
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete)?(?:\W|^)s(\d{1,3})(?:[\Wex]|\d{2}\b|$)", regex.IGNORECASE), array(integer), { "skipIfAlreadyFound": False })
    parser.add_handler("seasons", regex.compile(r"(?:(?:\bthe\W)?\bcomplete\W)?(?:\W|^)(\d{1,2})[. ]?(?:st|nd|rd|th)[. ]*season", regex.IGNORECASE), array(integer))
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
    parser.add_handler("episodes", regex.compile(r"(?:\W|^)[st]\d{1,2}[. ]?[xх-]?[. ]?(?:e|x|х|ep|-|\.)[. ]?(\d{1,3})(?:[abc]|v0?[1-4]|\D|$)", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"\b[st]\d{2}(\d{2})\b", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?:\W|^)(\d{1,3}(?:[ .]*~[ .]*\d{1,3})+)(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"-\s(\d{1,3}[ .]*-[ .]*\d{1,3})(?!-\d)(?:\W|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"s\d{1,2}\s?\((\d{1,3}[ .]*-[ .]*\d{1,3})\)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"(?:^|\/)\d{1,2}-(\d{2})\b(?!-\d)"), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<!\d-)\b\d{1,2}-(\d{2})(?=\.\w{2,4}$)"), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<!(?:seasons?|[Сс]езони?)\W*)(?:[ .([-]|^)(\d{1,3}(?:[ .]?[,&+~][ .]?\d{1,3})+)(?:[ .)\]-]|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"(?<!(?:seasons?|[Сс]езони?)\W*)(?:[ .([-]|^)(\d{1,3}(?:-\d{1,3})+)(?:[ .)(\]]|-\D|$)", regex.IGNORECASE), range_func)
    parser.add_handler("episodes", regex.compile(r"\bEp(?:isode)?\W+\d{1,2}\.(\d{1,3})\b", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?:\b[ée]p?(?:isode)?|[Ээ]пизод|[Сс]ер(?:ии|ия|\.)?|cap(?:itulo)?|epis[oó]dio)[. ]?[-:#№]?[. ]?(\d{1,4})(?:[abc]|v0?[1-4]|\W|$)", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"\b(\d{1,3})(?:-?я)?[ ._-]*(?:ser(?:i?[iyj]a|\b)|[Сс]ер(?:ии|ия|\.)?)", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?:\D|^)\d{1,2}[. ]?[xх][. ]?(\d{1,3})(?:[abc]|v0?[1-4]|\D|$)"), array(integer)) # Fixed: Was catching `1.x265` as episode.
    parser.add_handler("episodes", regex.compile(r"[[(]\d{1,2}\.(\d{1,3})[)\]]"), array(integer))
    parser.add_handler("episodes", regex.compile(r"\b[Ss]\d{1,2}[ .](\d{1,2})\b"), array(integer))
    parser.add_handler("episodes", regex.compile(r"-\s?\d{1,2}\.(\d{2,3})\s?-"), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<=\D|^)(\d{1,3})[. ]?(?:of|из|iz)[. ]?\d{1,3}(?=\D|$)", regex.IGNORECASE), array(integer))
    parser.add_handler("episodes", regex.compile(r"\b\d{2}[ ._-](\d{2})(?:.F)?\.\w{2,4}$"), array(integer))
    parser.add_handler("episodes", regex.compile(r"(?<!^)\[(\d{2,3})](?!(?:\.\w{2,4})?$)"), array(integer))
    def handle_episodes(context):
        title = context['title']
        result = context.get('result', {})
        matched = context.get('matched', {})

        if 'episodes' not in result:
            # Gather start indexes from relevant matched fields
            start_indexes = [comp.get('match_index') for comp in [matched.get('year'), matched.get('seasons')] if comp and comp.get('match_index', None)]
            end_indexes = [comp['match_index'] for comp in
                           [matched.get('resolution'), matched.get('source'), matched.get('codec'),
                            matched.get('audio')] if comp and comp.get('match_index', None)]

            # Define the range of the title to search based on detected components
            start_index = min(start_indexes) if start_indexes else 0
            end_index = min(end_indexes + [len(title)])

            # Extract relevant parts of the title for detailed scanning
            beginning_title = title[:end_index]
            middle_title = title[start_index:end_index]

            # Regex patterns to capture episode information, avoiding common prefixes like "movie" or "film"
            regex_patterns = [
                r'(?<!movie\W*|film\W*|^)(?:[ .]+-[ .]+|[([][ .]*)(\d{1,4})(?:a|b|v\d)?(?:\W|$)(?!movie|film)',
                r'^(?:[([-][ .]?)?(\d{1,4})(?:a|b|v\d)?(?:\W|$)(?!movie|film)'
            ]

            # Attempt to match episodes within the defined sections of the title
            for pattern in regex_patterns:
                matches = regex.search(pattern, beginning_title, regex.IGNORECASE) or regex.search(pattern, middle_title,
                                                                                          regex.IGNORECASE)
                if matches:
                    # Extract episode numbers, remove non-digits and convert to integers
                    episode_numbers = [int(num) for num in regex.findall(r'\d+', matches.group(1))]
                    result['episodes'] = episode_numbers
                    return {'match_index': title.index(matches.group(0))}

        return None
    parser.add_handler("episodes", handle_episodes)

    # Complete
    parser.add_handler("complete", regex.compile(r"(?:\bthe\W)?(?:\bcomplete|collection|dvd)?\b[ .]?\bbox[ .-]?set\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"(?:\bthe\W)?(?:\bcomplete|collection|dvd)?\b[ .]?\bmini[ .-]?series\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"(?:\bthe\W)?(?:\bcomplete|full|all)\b.*\b(?:series|seasons|collection|episodes|set|pack|movies)\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"\b(?:series|seasons|movies?)\b.*\b(?:complete|collection)\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"(?:\bthe\W)?\bultimate\b[ .]\bcollection\b", regex.IGNORECASE), boolean, { "skipIfAlreadyFound": False })
    parser.add_handler("complete", regex.compile(r"\bcollection\b.*\b(?:set|pack|movies)\b", regex.IGNORECASE), boolean)
    parser.add_handler("complete", regex.compile(r"\bcollection\b", regex.IGNORECASE), boolean, { "skipFromTitle": True })
    parser.add_handler("complete", regex.compile(r"duology|trilogy|quadr[oi]logy|tetralogy|pentalogy|hexalogy|heptalogy|anthology|saga", regex.IGNORECASE), boolean, { "skipIfAlreadyFound": False })

    # Languages
    parser.add_handler("languages", regex.compile(r"\bmulti(?:ple)?[ .-]*(?:su?$|sub\w*|dub\w*)\b|msub", regex.IGNORECASE), uniq_concat(value("multi subs")), {"skipIfAlreadyFound": False, "remove": True})
    parser.add_handler("languages", regex.compile(r"\bmulti(?:ple)?[ .-]*(?:lang(?:uages?)?|audio|VF2)?\b", regex.IGNORECASE), uniq_concat(value("multi audio")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\btri(?:ple)?[ .-]*(?:audio|dub\w*)\b", regex.IGNORECASE), uniq_concat(value("multi audio")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bdual[ .-]*(?:au?$|[aá]udio|line)\b", regex.IGNORECASE), uniq_concat(value("dual audio")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bdual\b(?![ .-]*sub)", regex.IGNORECASE), uniq_concat(value("dual audio")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bengl?(?:sub[A-Z]*)?\b", regex.IGNORECASE), uniq_concat(value("english")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\beng?sub[A-Z]*\b", regex.IGNORECASE), uniq_concat(value("english")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bing(?:l[eéê]s)?\b", regex.IGNORECASE), uniq_concat(value("english")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\benglish\W+(?:subs?|sdh|hi)\b", regex.IGNORECASE), uniq_concat(value("english")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bEN\b", regex.IGNORECASE), uniq_concat(value("english")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\benglish?\b", regex.IGNORECASE), uniq_concat(value("english")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:JP|JAP|JPN)\b", regex.IGNORECASE), uniq_concat(value("japanese")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(japanese|japon[eê]s)\b", regex.IGNORECASE), uniq_concat(value("japanese")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:KOR|kor[ .-]?sub)\b", regex.IGNORECASE), uniq_concat(value("korean")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(korean|coreano)\b", regex.IGNORECASE), uniq_concat(value("korean")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:traditional\W*chinese|chinese\W*traditional)(?:\Wchi)?\b", regex.IGNORECASE), uniq_concat(value("taiwanese")), {"skipIfAlreadyFound": False, "remove": True})
    parser.add_handler("languages", regex.compile(r"\bzh-hant\b", regex.IGNORECASE), uniq_concat(value("taiwanese")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(?:mand[ae]rin|ch[sn])\b", regex.IGNORECASE), uniq_concat(value("chinese")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bCH[IT]\b", regex.IGNORECASE), uniq_concat(value("chinese")), {"skipFromTitle": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(chinese|chin[eê]s|chi)\b", regex.IGNORECASE), uniq_concat(value("chinese")), {"skipIfFirst": True, "skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bzh-hans\b", regex.IGNORECASE), uniq_concat(value("chinese")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bFR(?:ench|a|e|anc[eê]s)?\b", regex.IGNORECASE), uniq_concat(value("french")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(Truefrench|VF[FI])\b", regex.IGNORECASE), uniq_concat(value("french")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\b(VOST(?:FR?|A)?|SUBFRENCH)\b", regex.IGNORECASE), uniq_concat(value("french")), {"skipIfAlreadyFound": False})
    parser.add_handler("languages", regex.compile(r"\bspanish\W?latin|american\W*(?:spa|esp?)", regex.IGNORECASE), uniq_concat(value("latino")), { "skipFromTitle": True, "skipIfAlreadyFound": False, "remove": True })
    parser.add_handler("languages", regex.compile(r"\b(?:audio.)?lat(?:i|ino)?\b", regex.IGNORECASE), uniq_concat(value("latino")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:audio.)?(?:ESP|spa|(en[ .]+)?espa[nñ]ola?|castellano)\b", regex.IGNORECASE), uniq_concat(value("spanish")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bes(?=[ .,/-]+(?:[A-Z]{2}[ .,/-]+){2,})\b", regex.IGNORECASE), uniq_concat(value("spanish")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?<=[ .,/-]+(?:[A-Z]{2}[ .,/-]+){2,})es\b", regex.IGNORECASE), uniq_concat(value("spanish")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?<=[ .,/-]+[A-Z]{2}[ .,/-]+)es(?=[ .,/-]+[A-Z]{2}[ .,/-]+)\b", regex.IGNORECASE), uniq_concat(value("spanish")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bes(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("spanish")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bspanish\W+subs?\b", regex.IGNORECASE), uniq_concat(value("spanish")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(spanish|espanhol)\b", regex.IGNORECASE), uniq_concat(value("spanish")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:p[rt]|en|port)[. (\\/-]*BR\b", regex.IGNORECASE), uniq_concat(value("portuguese")), { "skipIfAlreadyFound": False, "remove": True })
    parser.add_handler("languages", regex.compile(r"\bbr(?:a|azil|azilian)\W+(?:pt|por)\b", regex.IGNORECASE), uniq_concat(value("portuguese")), { "skipIfAlreadyFound": False, "remove": True })
    parser.add_handler("languages", regex.compile(r"\b(?:leg(?:endado|endas?)?|dub(?:lado)?|portugu[eèê]se?)[. -]*BR\b", regex.IGNORECASE), uniq_concat(value("portuguese")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bleg(?:endado|endas?)\b", regex.IGNORECASE), uniq_concat(value("portuguese")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bportugu[eèê]s[ea]?\b", regex.IGNORECASE), uniq_concat(value("portuguese")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bPT[. -]*(?:PT|ENG?|sub(?:s|titles?))\b", regex.IGNORECASE), uniq_concat(value("portuguese")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bpt(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("portuguese")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bpor\b", regex.IGNORECASE), uniq_concat(value("portuguese")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bITA\b", regex.IGNORECASE), uniq_concat(value("italian")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?<!w{3}\.\w+\.)IT(?=[ .,/-]+(?:[a-zA-Z]{2}[ .,/-]+){2,})\b"), uniq_concat(value("italian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bit(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("italian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bitaliano?\b", regex.IGNORECASE), uniq_concat(value("italian")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bgreek[ .-]*(?:audio|lang(?:uage)?|subs?(?:titles?)?)?\b", regex.IGNORECASE), uniq_concat(value("greek")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:GER|DEU)\b", regex.IGNORECASE), uniq_concat(value("german")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bde(?=[ .,/-]+(?:[A-Z]{2}[ .,/-]+){2,})\b", regex.IGNORECASE), uniq_concat(value("german")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?<=[ .,/-]+(?:[A-Z]{2}[ .,/-]+){2,})de\b", regex.IGNORECASE), uniq_concat(value("german")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?<=[ .,/-]+[A-Z]{2}[ .,/-]+)de(?=[ .,/-]+[A-Z]{2}[ .,/-]+)\b", regex.IGNORECASE), uniq_concat(value("german")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bde(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("german")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(german|alem[aã]o)\b", regex.IGNORECASE), uniq_concat(value("german")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bRUS?\b", regex.IGNORECASE), uniq_concat(value("russian")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(russian|russo)\b", regex.IGNORECASE), uniq_concat(value("russian")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bUKR\b", regex.IGNORECASE), uniq_concat(value("ukrainian")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bukrainian\b", regex.IGNORECASE), uniq_concat(value("ukrainian")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bhin(?:di)?\b", regex.IGNORECASE), uniq_concat(value("hindi")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)tel(?!\W*aviv)|telugu)\b", regex.IGNORECASE), uniq_concat(value("telugu")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bt[aâ]m(?:il)?\b", regex.IGNORECASE), uniq_concat(value("tamil")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?<!YTS\.)LT\b"), uniq_concat(value("lithuanian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\blithuanian\b", regex.IGNORECASE), uniq_concat(value("lithuanian")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\blatvian\b", regex.IGNORECASE), uniq_concat(value("latvian")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bestonian\b", regex.IGNORECASE), uniq_concat(value("estonian")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)PL|pol)\b", regex.IGNORECASE), uniq_concat(value("polish")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(polish|polon[eê]s|polaco)\b", regex.IGNORECASE), uniq_concat(value("polish")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bCZ[EH]?\b", regex.IGNORECASE), uniq_concat(value("czech")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bczech\b", regex.IGNORECASE), uniq_concat(value("czech")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bslo(?:vak|vakian|subs|[\]_)]?\.\w{2,4}$)\b", regex.IGNORECASE), uniq_concat(value("slovakian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bHU\b"), uniq_concat(value("hungarian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bHUN(?:garian)?\b", regex.IGNORECASE), uniq_concat(value("hungarian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bROM(?:anian)?\b", regex.IGNORECASE), uniq_concat(value("romanian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bRO(?=[ .,/-]*(?:[A-Z]{2}[ .,/-]+)*sub)", regex.IGNORECASE), uniq_concat(value("romanian")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bbul(?:garian)?\b", regex.IGNORECASE), uniq_concat(value("bulgarian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:srp|serbian)\b", regex.IGNORECASE), uniq_concat(value("serbian")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:HRV|croatian)\b", regex.IGNORECASE), uniq_concat(value("croatian")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bHR(?=[ .,/-]*(?:[A-Z]{2}[ .,/-]+)*sub)\b", regex.IGNORECASE), uniq_concat(value("croatian")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bslovenian\b", regex.IGNORECASE), uniq_concat(value("slovenian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)NL|dut|holand[eê]s)\b", regex.IGNORECASE), uniq_concat(value("dutch")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bdutch\b", regex.IGNORECASE), uniq_concat(value("dutch")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bflemish\b", regex.IGNORECASE), uniq_concat(value("dutch")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:DK|danska|dansub|nordic)\b", regex.IGNORECASE), uniq_concat(value("danish")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(danish|dinamarqu[eê]s)\b", regex.IGNORECASE), uniq_concat(value("danish")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bdan\b(?=.*\.(?:srt|vtt|ssa|ass|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("danish")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)FI|finsk|finsub|nordic)\b", regex.IGNORECASE), uniq_concat(value("finnish")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bfinnish\b", regex.IGNORECASE), uniq_concat(value("finnish")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:(?<!w{3}\.\w+\.)SE|swe|swesubs?|sv(?:ensk)?|nordic)\b", regex.IGNORECASE), uniq_concat(value("swedish")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(swedish|sueco)\b", regex.IGNORECASE), uniq_concat(value("swedish")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:NOR|norsk|norsub|nordic)\b", regex.IGNORECASE), uniq_concat(value("norwegian")), { "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(norwegian|noruegu[eê]s|bokm[aå]l|nob|nor(?=[\]_)]?\.\w{2,4}$))\b", regex.IGNORECASE), uniq_concat(value("norwegian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:arabic|[aá]rabe|ara)\b", regex.IGNORECASE), uniq_concat(value("arabic")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\barab.*(?:audio|lang(?:uage)?|sub(?:s|titles?)?)\b", regex.IGNORECASE), uniq_concat(value("arabic")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bar(?=\.(?:ass|ssa|srt|sub|idx)$)", regex.IGNORECASE), uniq_concat(value("arabic")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:turkish|tur(?:co)?)\b", regex.IGNORECASE), uniq_concat(value("turkish")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bvietnamese\b|\bvie(?=[\]_)]?\.\w{2,4}$)", regex.IGNORECASE), uniq_concat(value("vietnamese")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bind(?:onesian)?\b", regex.IGNORECASE), uniq_concat(value("indonesian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(thai|tailand[eê]s)\b", regex.IGNORECASE), uniq_concat(value("thai")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(THA|tha)\b"), uniq_concat(value("thai")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(?:malay|may(?=[\]_)]?\.\w{2,4}$)|(?<=subs?\([a-z,]+)may)\b", regex.IGNORECASE), uniq_concat(value("malay")), { "skipIfFirst": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\bheb(?:rew|raico)?\b", regex.IGNORECASE), uniq_concat(value("hebrew")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    parser.add_handler("languages", regex.compile(r"\b(persian|persa)\b", regex.IGNORECASE), uniq_concat(value("persian")), { "skipFromTitle": True, "skipIfAlreadyFound": False })
    def infer_language_based_on_naming(context):
        title = context['title']
        result = context['result']
        matched = context['matched']
        if 'languages' not in result or not any(lang in result['languages'] for lang in ['portuguese', 'spanish']):
            # Checking if episode naming convention suggests Portuguese language
            if (matched.get('episodes') and regex.search(r'capitulo|ao', matched['episodes'].get('raw_match', ''),
                                                         regex.IGNORECASE)) or \
                    regex.search(r'dublado', title, regex.IGNORECASE):
                result['languages'] = result.get('languages', []) + ['portuguese']

        return {'match_index': 0}
    parser.add_handler("languages", infer_language_based_on_naming)

    # Dubbed
    parser.add_handler("dubbed", regex.compile(r"\b(?:DUBBED|dublado|dubbing|DUBS?)\b", regex.IGNORECASE), boolean)
    def handle_dubbed(context):
        result = context['result']
        if 'languages' in result and any(lang in ['multi audio', 'dual audio'] for lang in result['languages']):
            result['dubbed'] = True
        return {'match_index': 0}
    parser.add_handler("dubbed", handle_dubbed)

    # Group
    parser.add_handler("group", regex.compile(r"^\[([^[\]]+)]"))
    parser.add_handler("group", regex.compile(r"\(([\w-]+)\)(?:$|\.\w{2,4}$)"))
    def handle_group(context):
        result = context['result']
        matched = context['matched']
        if 'group' in matched and matched['group'].get('raw_match', '').startswith('[') and matched['group']['raw_match'].endswith(']'):
            end_index = matched['group']['match_index'] + len(matched['group']['raw_match']) if 'group' in matched else 0

            # Check if there's any overlap with other matched elements
            if any(key != 'group' and matched[key]['match_index'] < end_index for key in matched if
                   'match_index' in matched[key]):
                if 'group' in result:
                    del result['group']
        return {'match_index': 0}
    parser.add_handler("group", handle_group)

    # Extension
    parser.add_handler("extension", regex.compile(r"\.(3g2|3gp|avi|flv|mkv|mk3d|mov|mp2|mp4|m4v|mpe|mpeg|mpg|mpv|webm|wmv|ogm|divx|ts|m2ts|iso|vob|sub|idx|ttxt|txt|smi|srt|ssa|ass|vtt|nfo|html)$", regex.IGNORECASE), lowercase)
