import pytest

from PTT import parse_title


@pytest.mark.parametrize("release_name, expected", [
    ("Sword.Art.Online.Alternative.S01.v2.1080p.Blu-Ray.10-Bit.Dual-Audio.LPCM.x265-iAHD", {
        "title": "Sword Art Online Alternative",
        "seasons": [1],
        "episodes": [],
        "languages": ["dual audio"],
        "bit_depth": "10bit",
        "dubbed": True,
        "quality": "BluRay",
        "codec": "x265",
        "resolution": "1080p",
        "group": "iAHD",
    }),
    ("[SubsPlease] Tearmoon Teikoku Monogatari - 01 (1080p) [15ADAE00].mkv", {
        "title": "Tearmoon Teikoku Monogatari",
        "seasons": [],
        "episodes": [1],
        "episode_code": "15ADAE00",
        "languages": [],
        "resolution": "1080p",
        "group": "SubsPlease",
        "container": "mkv",
        "extension": "mkv",
    }),
    ("[Erai-raws] Tearmoon Teikoku Monogatari - 01 [1080p][Multiple Subtitle] [ENG][POR-BR][SPA-LA][SPA][ARA][FRE][GER][ITA][RUS]", {
        "title": "Tearmoon Teikoku Monogatari",
        "seasons": [],
        "episodes": [1],
        "languages": ["multi subs", "english", "french", "spanish", "portuguese", "italian", "german", "russian", "arabic"],
        "resolution": "1080p",
        "group": "Erai-raws",
    }),
    ("Hunter x Hunter (2011) - 01 [1080p][Multiple Subtitle] [ENG][POR-BR][SPA-LA][SPA][ARA][FRE][GER][ITA][RUS]", {
        "title": "Hunter x Hunter",
        "seasons": [],
        "episodes": [1],
        "languages": ["multi subs", "english", "french", "spanish", "portuguese", "italian", "german", "russian", "arabic"],
        "resolution": "1080p",
        "year": 2011,
    }),
])
def test_random_anime_parse(release_name, expected):
    result = parse_title(release_name)
    assert result == expected
