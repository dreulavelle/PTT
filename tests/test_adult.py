import pytest

from PTT import parse_title


@pytest.mark.parametrize("release_name, expected_adult, expected_title", [
    ("Wicked 24 02 23 Liz Jordan And Xxlayna Marie Phantasia XXX 1080p HEVC x265 PRT", True, "Wicked"),
])
def test_random_anime_parse(release_name, expected_adult, expected_title):
    result = parse_title(release_name)
    if expected_adult:
        assert result["adult"] == expected_adult, f"Got {result['adult']} instead of {expected_adult}"
    assert result["title"] == expected_title, f"Got {result['title']} instead of {expected_title}"
