import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p

@pytest.mark.parametrize("release_name, expected_year, expect_year_presence", [
    ("Dawn.of.the.Planet.of.the.Apes.2014.HDRip.XViD-EVO", 2014, True),
    ("Hercules (2014) 1080p BrRip H264 - YIFY", 2014, True),
    ("One Shot [2014] DVDRip XViD-ViCKY", 2014, True),
    ("2012 2009 1080p BluRay x264 REPACK-METiS", 2009, True),
    ("2008 The Incredible Hulk Feature Film.mp4", 2008, True),
    ("Harry Potter All Movies Collection 2001-2011 720p Dual KartiKing", None, False),
    ("Empty Nest Season 1 (1988 - 89) fiveofseven", None, False),
    ("04. Practice Two (1324mb 1916x1080 50fps 1970kbps x265 deef).mkv", None, False),
    ("Anatomia De Grey - Temporada 19 [HDTV][Cap.1905][Castellano][www.AtomoHD.nu].avi", None, False),
    ("Wonder Woman 1984 (2020) [UHDRemux 2160p DoVi P8 Es-DTSHD AC3 En-AC3].mkv", 2020, True)
])
def test_year_detection(parser, release_name, expected_year, expect_year_presence):
    result = parser.parse(release_name)
    if expect_year_presence:
        assert "year" in result and result["year"] == expected_year, f"Expected year to be {expected_year} for {release_name} - got {result['year']}"
    else:
        assert "year" not in result, f"Expected no year to be present for {release_name}"
