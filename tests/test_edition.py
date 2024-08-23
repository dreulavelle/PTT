import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_edition", [
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", "Extended Edition"),
    ("Mary.Poppins.1964.50th.ANNIVERSARY.EDITION.REMUX.1080p.Bluray.AVC.DTS-HD.MA.5.1-LEGi0N", "Anniversary Edition"),
    ("The.Lord.of.the.Rings.The.Fellowship.of.the.Ring.2001.EXTENDED.2160p.UHD.BluRay.x265.10bit.HDR.TrueHD.7.1.Atmos-BOREDOR", "Extended Edition"),
    ("The.Lord.of.the.Rings.The.Motion.Picture.Trilogy.Extended.Editions.2001-2003.1080p.BluRay.x264.DTS-WiKi", "Extended Edition"),
    ("Better.Call.Saul.S03E04.CONVERT.720p.WEB.h264-TBS", None),
    ("The Fifth Element 1997 REMASTERED MULTi 1080p BluRay HDLight AC3 x264 Zone80", "Remastered"),
    ("Predator 1987 REMASTER MULTi 1080p BluRay x264 FiDELiO", "Remastered"),
    ("Have I Got News For You S53E02 EXTENDED 720p HDTV x264-QPEL", "Extended Edition"),
])
def test_extended_detection(parser, release_name, expected_edition):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_edition:
        assert result.get("edition") == expected_edition, f"Failed to detect 'edition' correctly for {release_name}"
    else:
        assert "edition" not in result, f"Incorrectly detected 'edition' for {release_name}"
