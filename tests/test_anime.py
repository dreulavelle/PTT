import pytest

from PTT import parse_title


@pytest.mark.parametrize("release_name, expected", [
    ("Sword.Art.Online.Alternative.S01.v2.1080p.Blu-Ray.10-Bit.Dual-Audio.LPCM.x265-iAHD", {
        "title": "Sword Art Online Alternative",
        "seasons": [1],
        "episodes": [],
        "languages": [],
        "bit_depth": "10bit",
        "dubbed": True,
        "quality": "BluRay",
        "codec": "hevc",
        "resolution": "1080p",
        "group": "iAHD"
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
        "extension": "mkv"
    }),
    ("[Erai-raws] Tearmoon Teikoku Monogatari - 01 [1080p][Multiple Subtitle] [ENG][POR-BR][SPA-LA][SPA][ARA][FRE][GER][ITA][RUS]", {
        "title": "Tearmoon Teikoku Monogatari",
        "seasons": [],
        "episodes": [1],
        "languages": ["en", "fr", "es", "pt", "it", "de", "ru", "ar"],
        "resolution": "1080p",
        "group": "Erai-raws",
        "subbed": True
    }),
    ("Hunter x Hunter (2011) - 01 [1080p][Multiple Subtitle] [ENG][POR-BR][SPA-LA][SPA][ARA][FRE][GER][ITA][RUS]", {
        "title": "Hunter x Hunter",
        "seasons": [],
        "episodes": [1],
        "languages": ["en", "fr", "es", "pt", "it", "de", "ru", "ar"],
        "resolution": "1080p",
        "year": 2011,
        "subbed": True
    }),
    ("[SubsPlease] Fairy Tail - 100 Years Quest - 05 (1080p) [1107F3A9].mkv", {
        "title": "Fairy Tail",
        "seasons": [],
        "episodes": [5],
        "languages": [],
        "episode_code": "1107F3A9",
        "extension": "mkv",
        "container": "mkv",
        "resolution": "1080p",
        "group": "SubsPlease"
    }),
    ("Naruto Shippuden (001-500) [Complete Series + Movies] (Dual Audio)", {
        "title": "Naruto Shippuden",
        "seasons": [],
        "episodes": list(range(1, 501)),
        "languages": [],
        "dubbed": True,
        "complete": True,
    }),
    ("[Erai-raws] Sword Art Online Alternative - Gun Gale Online - 10 [720p][Multiple Subtitle].mkv", {
        "title": "Sword Art Online Alternative - Gun Gale Online",
        "seasons": [],
        "episodes": [10],
        "languages": [],
        "resolution": "720p",
        "group": "Erai-raws",
        "container": "mkv",
        "extension": "mkv",
        "subbed": True,
    }),
    ("One.Piece.S01E1116.Lets.Go.Get.It!.Buggys.Big.Declaration.2160p.B-Global.WEB-DL.JPN.AAC2.0.H.264.MSubs-ToonsHub.mkv", {
        "title": "One Piece",
        "seasons": [1],
        "episodes": [1116],
        "languages": ["ja"],
        "resolution": "2160p",
        "quality": "WEB-DL",
        "audio": ["AAC"],
        "codec": "avc",
        "group": "ToonsHub",
        "container": "mkv",
        "extension": "mkv",
        "subbed": True
    }),
    ("[Erai-raws] 2-5 Jigen no Ririsa - 08 [480p][Multiple Subtitle][972D0669].mkv", {
        "title": "2-5 Jigen no Ririsa",
        "seasons": [],
        "episodes": [8],
        "languages": [],
        "resolution": "480p",
        "group": "Erai-raws",
        "episode_code": "972D0669",
        "container": "mkv",
        "extension": "mkv",
        "subbed": True,
    }),
    ("[Exiled-Destiny]_Tokyo_Underground_Ep02v2_(41858470).mkv", {
        "title": "Tokyo Underground",
        "seasons": [],
        "episodes": [2],
        "languages": [],
        "group": "Exiled-Destiny",
        "episode_code": "41858470",
        "container": "mkv",
        "extension": "mkv",
    }),
])
def test_random_anime_parse(release_name, expected):
    result = parse_title(release_name)
    assert result == expected
