import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_extras", [
    ("Madame Web 2024 1080p WEBRip 1400MB DD 5.1 x264 Sample-GalaxyRG[TGx]", ["Sample"]),
    ("Madame Web Sample 2024 1080p WEBRip 1400MB DD 5.1 x264-GalaxyRG[TGx]", None),
    ("Madame Web Sample 1080p WEBRip 1400MB DD 5.1 x264-GalaxyRG[TGx]", ["Sample"]),
    ("AVATAR.Featurette.Creating.the.World.of.Pandora.1080p.H264.ITA.AC3.ENGAAC.PappaMux.mkv", ["Featurette"])
])
def test_proper_detection(parser, release_name, expected_extras):
    result = parser.parse(release_name)
    if expected_extras:
        assert result["extras"] == expected_extras, f"Expected 'extras' to be {expected_extras} for {release_name}"
    else:
        assert "extras" not in result, f"Expected 'extras' to not be present for {release_name}"
