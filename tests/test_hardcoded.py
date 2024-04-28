import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_hardcoded", [
    ("Ghost In The Shell 2017 1080p HC HDRip X264 AC3-EVO", True),
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", False),
])
def test_hardcoded_detection(parser, release_name, expected_hardcoded):
    result = parser.parse(release_name)
    if expected_hardcoded:
        assert result.get(
            "hardcoded") == expected_hardcoded, f"Failed to detect 'hardcoded' correctly for {release_name}"
    else:
        assert "hardcoded" not in result, f"Incorrectly detected 'hardcoded' for {release_name}"
