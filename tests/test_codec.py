import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_codec, expected_bit_depth", [
    ("Nocturnal Animals 2016 VFF 1080p BluRay DTS HEVC-HD2", "hevc", None),
    ("doctor_who_2005.8x12.death_in_heaven.720p_hdtv_x264-fov", "avc", None),
    ("The Vet Life S02E01 Dunk-A-Doctor 1080p ANPL WEB-DL AAC2 0 H 264-RTN", "avc", None),
    ("Gotham S03E17 XviD-AFG", "xvid", None),
    ("Jimmy Kimmel 2017 05 03 720p HDTV DD5 1 MPEG2-CTL", "mpeg", None),
    ("[Anime Time] Re Zero kara Hajimeru Isekai Seikatsu (Season 2 Part 1) [1080p][HEVC10bit x265][Multi Sub]", "hevc", "10bit"),
    ("[naiyas] Fate Stay Night - Unlimited Blade Works Movie [BD 1080P HEVC10 QAACx2 Dual Audio]", "hevc", "10bit"),
    ("[DB]_Bleach_264_[012073FE].avi", None, None),
    ("[DB]_Bleach_265_[B4A04EC9].avi", None, None),
    ("Mad.Max.Fury.Road.2015.1080p.BluRay.DDP5.1.x265.10bit-GalaxyRG265[TGx]", "hevc", "10bit"),
])
def test_codec_detection(parser, release_name, expected_codec, expected_bit_depth):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_codec:
        assert "codec" in result, f"Codec key missing in result for {release_name}"
        assert result["codec"] == expected_codec, f"Incorrect codec detected for {release_name}"
        if expected_bit_depth:
            assert "bit_depth" in result, f"bit_depth key missing in result for {release_name}"
            assert result["bit_depth"] == expected_bit_depth, f"Incorrect bitDepth detected for {release_name}"
    else:
        assert "codec" not in result, f"Unexpected codec found: {result['codec']} in {release_name}"
