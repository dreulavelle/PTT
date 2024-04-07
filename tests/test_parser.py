import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p

def test_parsed_output(parser):
    test_case = "[Golumpa] Fairy Tail - 214 [FuniDub 720p x264 AAC] [5E46AC39]"
    result = parser.parse(test_case)
    assert isinstance(result, dict)
    assert "title" in result
    assert "episodeCode" in result
    assert "resolution" in result
    assert "codec" in result
    assert "audio" in result

def test_basic_parsed(parser):
    test_case = "The.Matrix.1999.1080p.BluRay.x264"
    result = parser.parse(test_case)
    assert isinstance(result, dict)
    assert result["title"] == "The Matrix"
    assert result["resolution"] == "1080p"
    assert result["year"] == 1999
    assert result["source"] == "BluRay"
    assert result["codec"] == "x264"

def test_season_parser(parser):
    test_cases = [
        ("Archer.S02.1080p.BluRay.DTSMA.AVC.Remux", [2]),
        ("The Simpsons S01E01 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole", [1]),
        ("[F-D] Fairy Tail Season 1 - 6 + Extras [480P][Dual-Audio]", [1, 2, 3, 4, 5, 6]),
        ("House MD All Seasons (1-8) 720p Ultra-Compressed", [1, 2, 3, 4, 5, 6, 7, 8]),
        ("Bleach 10º Temporada - 215 ao 220 - [DB-BR]", [10]),
        ("Lost.[Perdidos].6x05.HDTV.XviD.[www.DivxTotaL.com]", [6]),
        ("4-13 Cursed (HD)", [4]),
        ("Dragon Ball Z Movie - 09 - Bojack Unbound - 1080p BluRay x264 DTS 5.1 -DDR", []),  # Correct. This should not match, its a movie.
        ("BoJack Horseman [06x01-08 of 16] (2019-2020) WEB-DLRip 720p", [6]),
        ("[HR] Boku no Hero Academia 87 (S4-24) [1080p HEVC Multi-Subs] HR-GZ", [4]),
        ("The Simpsons S28E21 720p HDTV x264-AVS", [28])
    ]

    for test_case, expected in test_cases:
        result = parser.parse(test_case)
        assert isinstance(result, dict)
        assert result["seasons"] == expected, f"Failed for {test_case}"

def test_episode_code(parser):
    test_case = "[Golumpa] Fairy Tail - 214 [FuniDub 720p x264 AAC] [5E46AC39]"
    result = parser.parse(test_case)
    assert result["episodeCode"] == "5E46AC39"

# def test_languages_parser(parser):
#     test_cases = [
#         ("Deadpool 2016 1080p BluRay DTS Rus Ukr 3xEng HDCL", ["ukrainian", "russian"]),
#         ("VAIANA: MOANA (2017) NL-Retail [2D] EAGLE", ["dutch"]),
#         ("South.Park.S21E10.iTALiAN.FiNAL.AHDTV.x264-NTROPiC", ["italian"]),
#         ("Red Riding 1974 [2009 PAL DVD][En Subs[Sv.No.Fi]", ["english", "finnish", "swedish"]),
#         ("Men in Black International 2019 (inglês português)", ["english", "portuguese"]),
#     ]

#     for test_case, expected in test_cases:
#         result = parser.parse(test_case)
#         assert isinstance(result, dict)
#         assert result["languages"] == expected