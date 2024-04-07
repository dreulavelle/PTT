import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


def test_episode_parser(parser):
    test_cases = [
        ("Archer.S02.1080p.BluRay.DTSMA.AVC.Remux", []),
        ("The Simpsons S01E01 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole", [1]),
        ("[F-D] Fairy Tail Season 1 - 6 + Extras [480P][Dual-Audio]", []),
        ("House MD All Seasons (1-8) 720p Ultra-Compressed", []),
        ("Bleach 10º Temporada - 215 ao 220 - [DB-BR]", [215, 216, 217, 218, 219, 220]),
        ("Lost.[Perdidos].6x05.HDTV.XviD.[www.DivxTotaL.com]", [5]),
        ("4-13 Cursed (HD)", [13]),
        ("Dragon Ball Z Movie - 09 - Bojack Unbound - 1080p BluRay x264 DTS 5.1 -DDR", []),  # Correct. This should not match, its a movie.
        ("The Simpsons S28E21 720p HDTV x264-AVS", [21]),
        ("breaking.bad.s01e01.720p.bluray.x264-reward", [1]),
        ("Dragon Ball Super S01 E23 French 1080p HDTV H264-Kesni", [23]),
        ("The.Witcher.S01.07.2019.Dub.AVC.ExKinoRay.mkv", [7]),
        ("Vikings.s02.09.AVC.tahiy.mkv", [9]),
        ("The Twilight Zone 1985 S01E23a Shadow Play.mp4", [23]),
        ("Desperate_housewives_S03E02Le malheur aime la compagnie.mkv", [2]),
        ("Mash S10E01b Thats Show Biz Part 2 1080p H.264 (moviesbyrizzo upload).mp4", [1]),
        ("The Twilight Zone 1985 S01E22c The Library.mp4", [22]),
        ("Desperate.Housewives.S0615.400p.WEB-DL.Rus.Eng.avi", [15]),
        ("Doctor.Who.2005.8x11.Dark.Water.720p.HDTV.x264-FoV.mkv", [11]),
        ("Anubis saison 01 episode 38 tvrip FR", [38]),
        ("Le Monde Incroyable de Gumball - Saison 5 Ep 14 - L'extérieur", [14]),
        ("Smallville (1x02 Metamorphosis).avi", [2]),
        ("The.Man.In.The.High.Castle1x01.HDTV.XviD[www.DivxTotaL.com].avi", [1]),
        ("clny.3x11m720p.es[www.planetatorrent.com].mkv", [11]),
        ("Friends.S07E20.The.One.With.Rachel's.Big.Kiss.720p.BluRay.2CH.x265.HEVC-PSA.mkv", [20]),
        ("Friends - [8x18] - The One In Massapequa.mkv", [18]),
        ("Orange Is The New Black Season 5 Episodes 1-10 INCOMPLETE (LEAKED)", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ("Vikings.Season.05.Ep(01-10).720p.WebRip.2Ch.x265.PSA", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ("Naruto Shippuden Ep 107 - Strange Bedfellows.mkv", [107]),

        ("Friends - [7x23-24] - The One with Monica and Chandler's Wedding + Audio Commentary.mkv", [23, 24]),
        ("Yu-Gi-Oh 3x089 - Awakening of Evil (Part 4).avi", [89]),
        ("611-612 - Desperate Measures, Means & Ends.mp4", [611, 612]),
        ("[TBox] Dragon Ball Z Full 1-291(Subbed Jap Vers)", range(1, 292)),
        ("Naruto Shippuden - 107 - Strange Bedfellows.mkv", [107]),
        ("[AnimeRG] Naruto Shippuden - 107 [720p] [x265] [pseudo].mkv", [107])
    ]

    for test_case, expected in test_cases:
        result = parser.parse(test_case)
        assert isinstance(result, dict)
        assert result["episodes"] == expected, f"Failed for {test_case}"
