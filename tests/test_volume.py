import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser

@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p

@pytest.mark.parametrize("release_name, expected", [
    ("[MTBB] Sword Art Onlineː Alicization - Volume 2 (BD 1080p)", {'volumes': [2]}),
    ("[Neutrinome] Sword Art Online Alicization Vol.2 - VOSTFR [1080p BDRemux] + DDL", {'volumes': [2]}),
    ("[Mr. Kimiko] Oh My Goddess! - Vol. 7 [Kobo][2048px][CBZ]", {'volumes': [7]}),
    ("[MTBB] Cross Game - Volume 1-3 (WEB 720p)", {'volumes': [1, 2, 3]}),
    ("PIXAR SHORT FILMS COLLECTION - VOLS. 1 & 2 + - BDrip 1080p", {'volumes': [1, 2]}),
    ("Altair - A Record of Battles Vol. 01-08 (Digital) (danke-Empire)", {'volumes': [1, 2, 3, 4, 5, 6, 7, 8]}),
    ("Guardians of the Galaxy Vol. 2 (2017) 720p HDTC x264 MKVTV", {'title': "Guardians of the Galaxy Vol. 2", 'volumes': None}),
    ("Kill Bill: Vol. 1 (2003) BluRay 1080p 5.1CH x264 Ganool", {'title': "Kill Bill: Vol. 1", 'volumes': None}),
    ("[Valenciano] Aquarion EVOL - 22 [1080p][AV1 10bit][FLAC][Eng sub].mkv", {'title': "Aquarion EVOL", 'volumes': None}),
])
def test_volume_detection(parser, release_name, expected):
    result = parser.parse(release_name)
    for key, value in expected.items():
        if value is not None:
            assert key in result and result[key] == value, f"Expected {key} to be {value} for {release_name}"
        else:
            assert key not in result, f"Expected {key} not to be present for {release_name}"
