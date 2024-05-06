import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_seasons", [
    ("The Simpsons S28E21 720p HDTV x264-AVS", [28]),
    ("breaking.bad.s01e01.720p.bluray.x264-reward", [1]),
    ("S011E16.mkv", [11]),
    ("Dragon Ball Super S01 E23 French 1080p HDTV H264-Kesni", [1]),
    ("The Twilight Zone 1985 S01E23a Shadow Play.mp4", [1]),
    ("Mash S10E01b Thats Show Biz Part 2 1080p H.264 (moviesbyrizzo upload).mp4", [10]),
    ("The Twilight Zone 1985 S01E22c The Library.mp4", [1]),
    ("Desperate.Housewives.S0615.400p.WEB-DL.Rus.Eng.avi", [6]),
    ("Doctor.Who.2005.8x11.Dark.Water.720p.HDTV.x264-FoV", [8]),
    ("Orange Is The New Black Season 5 Episodes 1-10 INCOMPLETE (LEAKED)", [5]),
    ("Smallville (1x02 Metamorphosis).avi", [1]),
    ("The.Man.In.The.High.Castle1x01.HDTV.XviD[www.DivxTotaL.com].avi", [1]),
    ("clny.3x11m720p.es[www.planetatorrent.com].mkv", [3]),
    ("Game Of Thrones Complete Season 1,2,3,4,5,6,7 406p mkv + Subs", list(range(1, 8))),
    ("Futurama Season 1 2 3 4 5 6 7 + 4 Movies - threesixtyp", list(range(1, 8))),
    ("Breaking Bad Complete Season 1 , 2 , 3, 4 ,5 ,1080p HEVC", list(range(1, 6))),
    ("True Blood Season 1, 2, 3, 4, 5 & 6 + Extras BDRip TSV", list(range(1, 7))),
    ("How I Met Your Mother Season 1, 2, 3, 4, 5, & 6 + Extras DVDRip", list(range(1, 7))),
    ("The Simpsons Season 20 21 22 23 24 25 26 27 - threesixtyp", list(range(20, 28))),
    ("Perdidos: Lost: Castellano: Temporadas 1 2 3 4 5 6 (Serie Com", list(range(1, 7))),
    ("The Boondocks Season 1, 2 & 3", list(range(1, 4))),
    ("Boondocks, The - Seasons 1 + 2", list(range(1, 3))),
    ("The Boondocks Seasons 1-4 MKV", list(range(1, 5))),
    ("The Expanse Complete Seasons 01 & 02 1080p", list(range(1, 3))),
    ("Friends.Complete.Series.S01-S10.720p.BluRay.2CH.x265.HEVC-PSA", list(range(1, 11))),
    ("Stargate Atlantis ALL Seasons - S01 / S02 / S03 / S04 / S05", list(range(1, 6))),
    ("Stargate Atlantis Complete (Season 1 2 3 4 5) 720p HEVC x265", list(range(1, 6))),
    ("Skam.S01-S02-S03.SweSub.720p.WEB-DL.H264", list(range(1, 4))),
    ("Игра престолов / Game of Thrones [S1-8] (2011-2019) Blu-Ray Remux 2160p | 4K | HEVC | HDR | Dolby Vision | D, P", list(range(1, 9))),
    ("Игра престолов / Game of Thrones (2011-2019) BDRemux [H.264/1080p] (S1-8E1-73 of 73) AlexFilm, LostFilm, FoxLife, Ren-TV, Kravec, Jaskier, FocusStudio, NewStudio, FOX, AMS, OmskBird", list(range(1, 9))),
    ("Game.of.Thrones.S01-07.LostFilm.AlexFilm.Dub.Eng.BDRip.1080p", list(range(1, 8))),
    ("Game.of.Thrones.S01.2160p.UHD.BluRay.x265-SpaceHD13", [1]),
    ("Game_Of_Thrones_Season 01", [1]),
    ("Game.of.Thrones.S01.e01-02.2160p.UHD.BluRay.x265-Morpheus", [1]),
    ("Spongebob Squarepants Season 1-8 DvdRip", list(range(1, 9))),
    ("[DBDRaws][海绵宝宝 第一季spongebob squarepants Season 1][0120TV][1080P][WebRip][HEVC10bit][AC3][MKV]", [1]),
    ("Supernatural_s15_LostFilm_1080p", [15]),
    ("Supernatural (2005) Season 15 S15 (1080p BluRay x265 HEVC 10bit AAC 5.1 Silence)", [15]),
    ("Supernatural Season 1-10 1 2 3 4 5 6 7 8 9 10 Complete HD {KURD}", list(range(1, 11))),
    ("Breaking Bad - Complete Season 1,2,3,4,5 + Extras - BluRay 1080p", list(range(1, 6))),
    ("Breaking Bad Season 1, 2 & 3 + Extras Blu-ray BDRip TSV", list(range(1, 4))),
    ("Silo.Season.1.2160p.DV.H265-MIXED", [1]),
    ("Stranger.Things.S01-S04.1080p.WEB-DL.DDP5.1.x264-AOC", list(range(1, 5))),
    ("Stranger.Things.Netflix.S01 S04.Complete.1080p 720p.MKV.MP4.AAC.WEB-DL [62.1GB]", list(range(1, 5))),
])
def test_season_detection(parser, release_name, expected_seasons):
    result = parser.parse(release_name)
    assert "seasons" in result, f"Season key missing in result for {release_name}"
    assert set(result.get("seasons", [])) == set(expected_seasons), f"Incorrect seasons detected for {release_name}"
