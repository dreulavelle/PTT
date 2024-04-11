import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_convert", [
    ("Better.Call.Saul.S03E04.CONVERT.720p.WEB.h264-TBS", True),
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", False),
])
def test_convert_detection(parser, release_name, expected_convert):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_convert:
        assert result.get(
            "convert") == expected_convert, f"Failed to detect 'convert' flag correctly for {release_name}"
    else:
        assert "convert" not in result, f"Incorrectly detected 'convert' flag for {release_name}"
