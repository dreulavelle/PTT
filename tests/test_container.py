import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_container", [
    ("Kevin Hart What Now (2016) 1080p BluRay x265 6ch -Dtech mkv", "mkv"),
    ("The Gorburger Show S01E05 AAC MP4-Mobile", "mp4"),
    ("[req]Night of the Lepus (1972) DVDRip XviD avi", "avi"),
])
def test_container_detection(parser, release_name, expected_container):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    assert "container" in result, f"Container key missing in result for {release_name}"
    assert result["container"] == expected_container, f"Incorrect container detected for {release_name}"
