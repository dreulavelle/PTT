# Example of adding handlers, you should replace this with your actual handlers
# parser = Parser()
# parser.add_handler("resolution", regex.compile(r"\b4k\b", regex.IGNORECASE), value("4K"), {"remove": True})

import pytest
import regex
from PTT.parse import Parser
from PTT.transformers import value

@pytest.fixture
def parser():
    parser = Parser()
    parser.add_defaults()
    return parser

def test_parse(parser):
    result = parser.parse("Movie Title [ABC12345] 4K 2160p 2021-01-01 EXTENDED CONVERT HC PROPER REPACK Retail Remastered Unrated R1 CAM 10-bit")
    assert isinstance(result, dict)
    # assert result["title"] == "Movie Title"
    assert result["resolution"] == "4K"
    assert result["extended"] is True
    assert result["convert"] is True
    assert result["hardcoded"] is True
    assert result["proper"] is True
    assert result["repack"] is True
    assert result["retail"] is True
    assert result["remastered"] is True
    assert result["unrated"] is True
    assert result["region"] == "R1"

def test_add_custom_handler(parser):
    parser.add_handler("custom", regex.compile(r"(\[[A-C1-5]*\])", regex.IGNORECASE), value("4K"), {"remove": False})
    result = parser.parse("Movie Title [ABC12345] 4K 2160p 2021-01-01 EXTENDED CONVERT HC PROPER REPACK Retail Remastered Unrated R1 CAM 10-bit")
    assert result["custom"] == "4K"
