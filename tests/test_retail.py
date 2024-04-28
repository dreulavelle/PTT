import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_retail", [
    ("MONSTER HIGH: ELECTRIFIED (2017) Retail PAL DVD9 [EAGLE]", True),
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", False),
])
def test_retail_detection(parser, release_name, expected_retail):
    result = parser.parse(release_name)
    assert ("retail" in result) == expected_retail, f"Expected 'retail' detection to be {expected_retail} for {release_name}"
