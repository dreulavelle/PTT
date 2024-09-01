import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_complete, expected_title", [
    ("[Furi] Avatar - The Last Airbender [720p] (Full 3 Seasons + Extr", True, None),
    ("Harry.Potter.Complete.Collection.2001-2011.1080p.BluRay.DTS-ETRG", True, None),
    ("Game of Thrones All 7 Seasons 1080p ~∞~ .HakunaMaKoko", True, None),
    ("Avatar: The Last Airbender Full Series 720p", True, "Avatar: The Last Airbender"),
    ("Dora the Explorer - Ultimate Collection", True, None),
    ("Mr Bean Complete Pack (Animated, Tv series, 2 Movies) DVDRIP (WA", True, None),
    ("American Pie - Complete set (8 movies) 720p mkv - YIFY", True, None),
    ("Charlie Chaplin - Complete Filmography (87 movies)", True, None),
    ("Monster High Movies Complete 2014", True, None),
    ("Harry Potter All Movies Collection 2001-2011 720p Dual KartiKing", True, None),
    ("The Clint Eastwood Movie Collection", True, None),
    ("Clint Eastwood Collection - 15 HD Movies", True, None),
    ("Official  IMDb  Top  250  Movies  Collection  6/17/2011", True, None),
    ("The Texas Chainsaw Massacre Collection (1974-2017) BDRip 1080p", True, None),
    ("Snabba.Cash.I-II.Duology.2010-2012.1080p.BluRay.x264.anoXmous", True, None),
    ("Star Wars Original Trilogy 1977-1983 Despecialized 720p", True, None),
    ("The.Wong.Kar-Wai.Quadrology.1990-2004.1080p.BluRay.x264.AAC.5.1-", True, None),
    ("Lethal.Weapon.Quadrilogy.1987-1992.1080p.BluRay.x264.anoXmous", True, None),
    ("X-Men.Tetralogy.BRRip.XviD.AC3.RoSubbed-playXD", True, None),
    ("Mission.Impossible.Pentalogy.1996-2015.1080p.BluRay.x264.AAC.5.1", True, None),
    ("Mission.Impossible.Hexalogy.1996-2018.SweSub.1080p.x264-Justiso", True, None),
    ("American.Pie.Heptalogy.SWESUB.DVDRip.XviD-BaZZe", True, "American Pie"),
    ("The Exorcist 1, 2, 3, 4, 5 - Complete Horror Anthology 1973-2005", True, None),
    ("Harry.Potter.Complete.Saga. I - VIII .1080p.Bluray.x264.anoXmous", True, None),
    # This last test ensures that the collection is recognized but also retains the title appropriately.
    ("[Erai-raws] Ninja Collection - 05 [720p][Multiple Subtitle].mkv", True, "Ninja Collection"),
    ("Furiosa - A Mad Max Saga (2024) 2160p H265 HDR10 D V iTA EnG AC3 5 1 Sub iTA EnG NUiTA NUEnG AsPiDe-MIRCrew mkv", True, "Furiosa - A Mad Max Saga"),
    ("[Judas] Vinland Saga (Season 2) [1080p][HEVC x265 10bit][Multi-Subs]", True, "Vinland Saga"),
])
def test_complete_collection_detection(parser, release_name, expected_complete, expected_title):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    assert result.get("complete") == expected_complete, f"Incorrect 'complete' detection for {release_name}"
    if expected_title is not None:
        assert result.get("title") == expected_title, f"Incorrect title detected for {release_name}"
