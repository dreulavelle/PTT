import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize(
    "release_name, expected",
    [
        (
            "UFC.239.PPV.Jones.Vs.Santos.HDTV.x264-PUNCH[TGx]",
            {
                "title": "UFC 239 Jones Vs Santos",
                "seasons": [],
                "episodes": [],
                "languages": [],
                "quality": "HDTV",
                "codec": "x264",
                "group": "PUNCH",
                "ppv": True,
            },
        ),
        (
            "UFC.Fight.Night.158.Cowboy.vs.Gaethje.WEB.x264-PUNCH[TGx]",
            {
                "title": "UFC Fight Night 158 Cowboy vs Gaethje",
                "seasons": [],
                "episodes": [],
                "languages": [],
                "quality": "WEB-DL",
                "codec": "x264",
                "group": "PUNCH",
                "ppv": True,
            },
        ),
        (
            "UFC 226 PPV Miocic vs Cormier HDTV x264-Ebi [TJET]",
            {
                "title": "UFC 226 Miocic vs Cormier",
                "seasons": [],
                "episodes": [],
                "languages": [],
                "quality": "HDTV",
                "codec": "x264",
                "ppv": True,
            },
        ),
    ],
)
def test_random_sports_parse(parser, release_name, expected):
    assert parser.parse(release_name) == expected
