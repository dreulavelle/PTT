import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


# Initialize a parser instance and add default handlers
@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p

def test_parsed_output(parser):
    test_case = "The.Matrix.1999.1080p.BluRay.x264"
    result = parser.parse(test_case)
    assert isinstance(result, dict)
    print(result)

def test_resolution(parser):
    test_case = "The.Matrix.1999.1080p.BluRay.x264"
    result = parser.parse(test_case)
    assert result["resolution"] == "1080p"
    assert result["title"] == "The Matrix"

def test_year(parser):
    test_case = "The.Matrix.1999.1080p.BluRay.x264"
    result = parser.parse(test_case)
    assert result["year"] == 1999
