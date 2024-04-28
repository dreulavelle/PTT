import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_repack", [
    ("Silicon Valley S04E03 REPACK HDTV x264-SVA", True),
    ("Expedition Unknown S03E14 Corsicas Nazi Treasure RERIP 720p HDTV x264-W4F", True),
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", False),
])
def test_repack_detection(parser, release_name, expected_repack):
    result = parser.parse(release_name)
    assert ("repack" in result) == expected_repack, f"Expected 'repack' detection to be {expected_repack} for {release_name}"
