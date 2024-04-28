import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_dubbed", [
    ("Yo-Kai Watch S01E71 DUBBED 720p HDTV x264-W4F", True),
    ("[Golumpa] Kochoki - 11 (Kochoki - Wakaki Nobunaga) [English Dub] [FuniDub 720p x264 AAC] [MKV] [4FA0D898]", True),
    ("[Aomori-Raws] Juushinki Pandora (01-13) [Dubs & Subs]", True),
    ("[LostYears] Tsuredure Children (WEB 720p Hi10 AAC) [Dual-Audio]", True),
    ("[DB] Gamers! [Dual Audio 10bit 720p][HEVC-x265]", True),
    ("[DragsterPS] Yu-Gi-Oh! S02 [480p] [Multi-Audio] [Multi-Subs]", True),
    ("A Freira (2018) Dublado HD-TS 720p", True),
    ("Toy.Story.1080p.BluRay.x264-HD[Dubbing PL].mkv", True),
    ("Fame (1980) [DVDRip][Dual][Ac3][Eng-Spa]", True),
    # Test cases to ensure the parser does not incorrectly detect dubbed when not applicable
    ("[Hakata Ramen] Hoshiai No Sora (Stars Align) 01 [1080p][HEVC][x265][10bit][Dual-Subs] HR-DR", False),
    ("[IceBlue] Naruto (Season 01) - [Multi-Dub][Multi-Sub][HEVC 10Bits] 800p BD", True),
])
def test_dubbed_detection(parser, release_name, expected_dubbed):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_dubbed:
        assert result.get("dubbed") == expected_dubbed, f"Failed to detect 'dubbed' correctly for {release_name}"
    else:
        assert "dubbed" not in result, f"Incorrectly detected 'dubbed' for {release_name}"
