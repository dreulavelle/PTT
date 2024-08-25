import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p

@pytest.mark.parametrize("release_name, expected_unrated", [
    ("Identity.Thief.2013.Vostfr.UNRATED.BluRay.720p.DTS.x264-Nenuko", True),
    ("Charlie.les.filles.lui.disent.merci.2007.UNCENSORED.TRUEFRENCH.DVDRiP.AC3.Libe", True),
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", False),
])
def test_unrated_detection(parser, release_name, expected_unrated):
    result = parser.parse(release_name)
    assert ("unrated" in result) == expected_unrated, f"Expected 'unrated' detection to be {expected_unrated} for {release_name}"
