import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_proper", [
    ("Into the Badlands S02E07 PROPER 720p HDTV x264-W4F", True),
    ("Bossi-Reality-REAL PROPER-CDM-FLAC-1999-MAHOU", True),
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", False),
])
def test_proper_detection(parser, release_name, expected_proper):
    result = parser.parse(release_name)
    assert ("proper" in result) == expected_proper, f"Expected 'proper' detection to be {expected_proper} for {release_name}"

