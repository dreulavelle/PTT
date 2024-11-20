import pytest

from PTT import parse_title


@pytest.mark.parametrize("release_name, expected_adult, expected_title", [
    ("Wicked 24 02 23 Liz Jordan And Xxlayna Marie Phantasia XXX 1080p HEVC x265 PRT", True, "Wicked"),
    ("Wicked.24.11.01.Liz.Jordan.It.Didnt.Have.To.End.This.Way.XXX.1080p.HEVC.x265.PRT.mp4", True, "Wicked"),
    ("The.Sopranos.S04E01.For.All.Debts.Public.and.Private.480p.WEB-DL.x264-Sticky83.mkv", False, "The Sopranos"),
])
def test_random_anime_parse(release_name, expected_adult, expected_title):
    result = parse_title(release_name)
    if expected_adult:
        assert result["adult"] == expected_adult, f"Got {result['adult']} instead of {expected_adult}"
    assert result["title"] == expected_title, f"Got {result['title']} instead of {expected_title}"
