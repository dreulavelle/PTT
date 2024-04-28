import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_extended", [
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", True),
    ("Better.Call.Saul.S03E04.CONVERT.720p.WEB.h264-TBS", False),
])
def test_extended_detection(parser, release_name, expected_extended):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_extended:
        assert result.get("extended") == expected_extended, f"Failed to detect 'extended' correctly for {release_name}"
    else:
        assert "extended" not in result, f"Incorrectly detected 'extended' for {release_name}"
