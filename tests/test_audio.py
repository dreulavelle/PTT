import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_audio", [
    ("Nocturnal Animals 2016 VFF 1080p BluRay DTS HEVC-HD2", ["truehd"]),
    ("Gold 2016 1080p BluRay DTS-HD MA 5 1 x264-HDH", ["truehd"]),
    ("Rain Man 1988 REMASTERED 1080p BRRip x264 AAC-m2g", ["aac"]),
    ("The Vet Life S02E01 Dunk-A-Doctor 1080p ANPL WEB-DL AAC2 0 H 264-RTN", ["aac"]),
    ("Jimmy Kimmel 2017 05 03 720p HDTV DD5 1 MPEG2-CTL", ["dd5.1"]),
    ("A Dog's Purpose 2016 BDRip 720p X265 Ac3-GANJAMAN", ["ac3"]),
    ("Retroactive 1997 BluRay 1080p AC-3 HEVC-d3g", ["ac3"]),
    ("Tempete 2016-TrueFRENCH-TVrip-H264-mp3", None),
    ("Detroit.2017.BDRip.MD.GERMAN.x264-SPECTRE", None),
    ("The Blacklist S07E04 (1080p AMZN WEB-DL x265 HEVC 10bit EAC-3 5.1)[Bandi]", ["eac3"]),
    ("Condor.S01E03.1080p.WEB-DL.x265.10bit.EAC3.6.0-Qman[UTR].mkv", ["eac3"]),
    ("The 13 Ghosts of Scooby-Doo (1985) S01 (1080p AMZN Webrip x265 10bit EAC-3 2.0 - Frys) [TAoE]", ["eac3"]),
    ("[Thund3r3mp3ror] Attack on Titan - 23.mp4", None),  # Test case to ensure "mp3" isn't detected inside a word
    ("Buttobi!! CPU - 02 (DVDRip 720x480p x265 HEVC AC3x2 2.0x2)(Dual Audio)[sxales].mkv", ["ac3"]),
    ("[naiyas] Fate Stay Night - Unlimited Blade Works Movie [BD 1080P HEVC10 QAACx2 Dual Audio]", ["aac"]),
    ("Sakura Wars the Movie (2001) (BDRip 1920x1036p x265 HEVC FLACx2, AC3 2.0+5.1x2)(Dual Audio)[sxales].mkv", ["flac", "ac3"]),
    ("Spider-Man.No.Way.Home.2021.2160p.BluRay.REMUX.HEVC.TrueHD.7.1.Atmos-FraMeSToR", ["atmos"]),
    
])
def test_audio_detection(parser, release_name, expected_audio):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    if expected_audio:
        assert result.get("audio") == expected_audio, f"Failed for {release_name}"
    else:
        assert "audio" not in result, f"Unexpected audio detection for {release_name}"

@pytest.mark.parametrize("release_name, expected_audio", [
    ("Macross ~ Do You Remember Love (1984) (BDRip 1920x1036p x265 HEVC DTS-HD MA, FLAC, AC3x2 5.1+2.0x3)(Dual Audio)[sxales].mkv", ["truehd", "ac3"]),
    ("Escaflowne (2000) (BDRip 1896x1048p x265 HEVC TrueHD, FLACx3, AC3 5.1x2+2.0x3)(Triple Audio)[sxales].mkv", ["truehd", "ac3"]),
    ("[SAD] Inuyasha - The Movie 4 - Fire on the Mystic Island [BD 1920x1036 HEVC10 FLAC2.0x2] [84E9A4A1].mkv", ["flac"]),
])
def test_audio_detection_without_episode(parser, release_name, expected_audio):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    if expected_audio:
        assert result.get("audio") == expected_audio, f"Failed for {release_name}"
    else:
        assert "audio" not in result, f"Unexpected audio detection for {release_name}"
    assert result.get("episodes") == [], f"Unexpected episode detection for {release_name}"

@pytest.mark.parametrize("release_name, expected_audio, expected_episode", [
    ("Outlaw Star - 23 (BDRip 1440x1080p x265 HEVC AC3, FLACx2 2.0x3)(Dual Audio)[sxales].mkv", ["flac", "ac3"], [23]),
])
def test_audio_detection_with_episode(parser, release_name, expected_audio, expected_episode):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    if expected_audio and expected_episode:
        assert result.get("audio") == expected_audio, f"Failed for {release_name}"
        assert result.get("episodes") == expected_episode, f"Failed for {release_name}"
    else:
        assert "audio" not in result, f"Unexpected audio detection for {release_name}"