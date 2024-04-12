import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_region, should_have_region", [
    ("Welcome to New York 2014 R5 XviD AC3-SUPERFAST", "R5", True),
    ("[Coalgirls]_Code_Geass_R2_06_(1920x1080_Blu-ray_FLAC)_[F8C7FE25].mkv", None, False),
])
def test_region_detection(parser, release_name, expected_region, should_have_region):
    result = parser.parse(release_name)
    if should_have_region:
        assert result.get('region') == expected_region, f"Expected region to be {expected_region} for {release_name}"
    else:
        assert 'region' not in result, f"Region should not be detected in {release_name}"
