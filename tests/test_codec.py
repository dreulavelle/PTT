import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_codec, expected_bitDepth", [
    ("Nocturnal Animals 2016 VFF 1080p BluRay DTS HEVC-HD2", "hevc", None),
    ("doctor_who_2005.8x12.death_in_heaven.720p_hdtv_x264-fov", "x264", None),
    ("The Vet Life S02E01 Dunk-A-Doctor 1080p ANPL WEB-DL AAC2 0 H 264-RTN", "h264", None),
    ("Gotham S03E17 XviD-AFG", "xvid", None),
    ("Jimmy Kimmel 2017 05 03 720p HDTV DD5 1 MPEG2-CTL", "mpeg2", None),
    ("[Anime Time] Re Zero kara Hajimeru Isekai Seikatsu (Season 2 Part 1) [1080p][HEVC10bit x265][Multi Sub]", "hevc",
     "10bit"),
    ("[naiyas] Fate Stay Night - Unlimited Blade Works Movie [BD 1080P HEVC10 QAACx2 Dual Audio]", "hevc", "10bit"),
    ("[DB]_Bleach_264_[012073FE].avi", None, None),  # Test case to ensure "264" isn't wrongly detected as a codec
    ("[DB]_Bleach_265_[B4A04EC9].avi", None, None),  # Test case to ensure "265" isn't wrongly detected as a codec
])
def test_codec_detection(parser, release_name, expected_codec, expected_bitDepth):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_codec:
        assert "codec" in result, f"Codec key missing in result for {release_name}"
        assert result["codec"] == expected_codec, f"Incorrect codec detected for {release_name}"
        if expected_bitDepth:
            assert "bitDepth" in result, f"bitDepth key missing in result for {release_name}"
            assert result["bitDepth"] == expected_bitDepth, f"Incorrect bitDepth detected for {release_name}"
    else:
        assert "codec" not in result, f"Unexpected codec detection for {release_name}"
