import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_remastered", [
    ("The Fifth Element 1997 REMASTERED MULTi 1080p BluRay HDLight AC3 x264 Zone80", True),
    ("Predator 1987 REMASTER MULTi 1080p BluRay x264 FiDELiO", True),
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", False),
])
def test_remastered_detection(parser, release_name, expected_remastered):
    result = parser.parse(release_name)
    assert ("remastered" in result) == expected_remastered, f"Expected 'remastered' detection to be {expected_remastered} for {release_name}"
