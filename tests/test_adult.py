import pytest

from PTT import parse_title


@pytest.mark.parametrize("release_name, expected_adult", [
    ("Wicked 24 02 23 Liz Jordan And Xxlayna Marie Phantasia XXX 1080p HEVC x265 PRT", True),
    ("Wicked.24.11.01.Liz.Jordan.It.Didnt.Have.To.End.This.Way.XXX.1080p.HEVC.x265.PRT.mp4", True),
    ("The.Sopranos.S04E01.For.All.Debts.Public.and.Private.480p.WEB-DL.x264-Sticky83.mkv", False),
    ("Redhead Nami from One Piece Rough Fucks and Deepthroats in Tight Jeans 2160p", True),
])
def test_random_anime_parse(release_name, expected_adult):
    result = parse_title(release_name)
    assert result.get("adult", False) == expected_adult, f"Expected 'adult' detection to be {expected_adult} for {release_name}"
