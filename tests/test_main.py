import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected", [
    ("sons.of.anarchy.s05e10.480p.BluRay.x264-GAnGSteR", {
        'title': 'sons of anarchy',
        'resolution': '480p',
        'seasons': [5],
        'episodes': [10],
        'source': 'BluRay',
        'codec': 'x264',
        'group': 'GAnGSteR',
        'languages': []
    }),
    ("Color.Of.Night.Unrated.DC.VostFR.BRrip.x264", {
        'title': 'Color Of Night',
        'unrated': True,
        'languages': ['french'],
        'source': 'BRRip',
        'codec': 'x264',
        'seasons': [],
        'episodes': []
    }),
    ("Da Vinci Code DVDRip", {
        'title': 'Da Vinci Code',
        'source': 'DVDRip',
        'languages': [],
        'seasons': [],
        'episodes': []
    }),
    ("Some.girls.1998.DVDRip", {
        'title': 'Some girls',
        'source': 'DVDRip',
        'year': 1998,
        'languages': [],
        'seasons': [],
        'episodes': []
    }),
    ("Ecrit.Dans.Le.Ciel.1954.MULTI.DVDRIP.x264.AC3-gismo65", {
        'title': 'Ecrit Dans Le Ciel',
        'source': 'DVDRip',
        'year': 1954,
        'languages': ['multi audio'],
        'dubbed': True,
        'codec': 'x264',
        'audio': 'ac3',
        'group': 'gismo65',
        'seasons': [],
        'episodes': []
    }),
    ("2019 After The Fall Of New York 1983 REMASTERED BDRip x264-GHOULS", {
        'title': '2019 After The Fall Of New York',
        'source': 'BDRip',
        'remastered': True,
        'year': 1983,
        'codec': 'x264',
        'group': 'GHOULS',
        'languages': [],
        'seasons': [],
        'episodes': []
    }),
    ("Ghost In The Shell 2017 720p HC HDRip X264 AC3-EVO", {
        'title': 'Ghost In The Shell',
        'source': 'HDRip',
        'hardcoded': True,
        'year': 2017,
        'resolution': '720p',
        'codec': 'x264',
        'audio': 'ac3',
        'group': 'EVO',
        'languages': [],
        'seasons': [],
        'episodes': []
    }),
    ("Rogue One 2016 1080p BluRay x264-SPARKS", {
        'title': 'Rogue One',
        'source': 'BluRay',
        'year': 2016,
        'resolution': '1080p',
        'codec': 'x264',
        'group': 'SPARKS',
        'languages': [],
        'seasons': [],
        'episodes': []
    }),
    ("Desperation 2006 Multi Pal DvdR9-TBW1973", {
        'title': 'Desperation',
        'source': 'DVD',
        'year': 2006,
        'languages': ['multi audio'],
        'dubbed': True,
        'region': 'R9',
        'group': 'TBW1973',
        'seasons': [],
        'episodes': []
    }),
    ("Maman, j'ai raté l'avion 1990 VFI 1080p BluRay DTS x265-HTG", {
        'title': "Maman, j'ai raté l'avion",
        'source': 'BluRay',
        'year': 1990,
        'audio': 'dts',
        'resolution': '1080p',
        'languages': ['french'],
        'codec': 'x265',
        'group': 'HTG',
        'seasons': [],
        'episodes': []
    }),
    ("Game of Thrones - The Complete Season 3 [HDTV]", {
        'title': 'Game of Thrones',
        'seasons': [3],
        'source': 'HDTV',
        'languages': [],
        'episodes': []
    }),
    ("The Sopranos: The Complete Series (Season 1,2,3,4,5&6) + Extras", {
        'title': 'The Sopranos',
        'seasons': [1, 2, 3, 4, 5, 6],
        'complete': True,
        'languages': [],
        'episodes': []
    }),
    ("Skins Season S01-S07 COMPLETE UK Soundtrack 720p WEB-DL", {
        'seasons': [1, 2, 3, 4, 5, 6, 7],
        'title': 'Skins',
        'resolution': '720p',
        'source': 'WEB-DL',
        'languages': [],
        'episodes': []
    }),
    ("Futurama.COMPLETE.S01-S07.720p.BluRay.x265-HETeam", {
        'title': 'Futurama',
        'seasons': [1, 2, 3, 4, 5, 6, 7],
        'resolution': '720p',
        'source': 'BluRay',
        'codec': 'x265',
        'group': 'HETeam',
        'languages': [],
        'episodes': []
    }),
    ("You.[Uncut].S01.SweSub.1080p.x264-Justiso", {
        'title': 'You',
        'seasons': [1],
        'languages': ['swedish'],
        'resolution': '1080p',
        'codec': 'x264',
        'group': 'Justiso',
        'episodes': []
    }),
    ("Stephen Colbert 2019 10 25 Eddie Murphy 480p x264-mSD [eztv]", {
        'title': 'Stephen Colbert',
        'date': '2019-10-25',
        'resolution': '480p',
        'codec': 'x264',
        'languages': [],
        'seasons': [],
        'episodes': []
    }),
    ("House MD Season 7 Complete MKV", {
        'title': 'House MD',
        'seasons': [7],
        'container': 'mkv',
        'languages': [],
        'episodes': []
    }),
    ("2008 The Incredible Hulk Feature Film.mp4", {
        'title': 'The Incredible Hulk Feature Film',
        'year': 2008,
        'container': 'mp4',
        'extension': 'mp4',
        'languages': [],
        'seasons': [],
        'episodes': []
    }),
    ("【4月/悠哈璃羽字幕社】[UHA-WINGS][不要输！恶之军团][Makeruna!! Aku no Gundan!][04][1080p AVC_AAC][简繁外挂][sc_tc]", {
        'title': 'Makeruna!! Aku no Gundan!',
        'episodes': [4],
        'resolution': '1080p',
        'codec': 'avc',
        'audio': 'aac',
        'languages': [],
        'seasons': [],
    }),
    ("[GM-Team][国漫][西行纪之集结篇][The Westward Ⅱ][2019][17][AVC][GB][1080P]", {
        'title': 'The Westward Ⅱ',
        'year': 2019,
        'episodes': [17],
        'resolution': '1080p',
        'codec': 'avc',
        'group': 'GM-Team',
        'languages': [],
        'seasons': [],
    }),
    ("Черное зеркало / Black Mirror / Сезон 4 / Серии 1-6 (6) [2017, США, WEBRip 1080p] MVO + Eng Sub", {
        'title': 'Black Mirror',
        'year': 2017,
        'seasons': [4],
        'episodes': [1, 2, 3, 4, 5, 6],
        'languages': ['english'],
        'resolution': '1080p',
        'source': 'WEBRip',
    }),
    ("[neoHEVC] Student Council's Discretion / Seitokai no Ichizon [Season 1] [BD 1080p x265 HEVC AAC]", {
        'title': "Student Council's Discretion / Seitokai no Ichizon",
        'seasons': [1],
        'resolution': '1080p',
        'source': 'BDRip',
        'audio': 'aac',
        'codec': 'hevc',
        'group': 'neoHEVC',
        'languages': [],
        'episodes': []
    }),
    ("[Commie] Chihayafuru 3 - 21 [BD 720p AAC] [5F1911ED].mkv", {
        'title': "Chihayafuru 3",
        'episodes': [21],
        'resolution': '720p',
        'source': 'BDRip',
        'audio': 'aac',
        'container': 'mkv',
        'extension': 'mkv',
        'episode_code': "5F1911ED",
        'group': "Commie",
        'languages': [],
        'seasons': [],
    }),
    ("[DVDRip-ITA]The Fast and the Furious: Tokyo Drift [CR-Bt]", {
        'title': "The Fast and the Furious: Tokyo Drift",
        'source': 'DVDRip',
        'languages': ['italian'],
        'seasons': [],
        'episodes': []
    }),
    ("[BluRay Rip 720p ITA AC3 - ENG AC3 SUB] Hostel[2005]-LIFE[ultimafrontiera]", {
        'title': "Hostel",
        'year': 2005,
        'resolution': '720p',
        'source': 'BRRip',
        'audio': 'ac3',
        'languages': ['english', 'italian'],
        'group': "LIFE",
        'seasons': [],
        'episodes': []
    }),
    ("[OFFICIAL ENG SUB] Soul Land Episode 121-125 [1080p][Soft Sub][Web-DL][Douluo Dalu][斗罗大陆]", {
        'title': "Soul Land",
        'episodes': [121, 122, 123, 124, 125],
        'resolution': '1080p',
        'source': 'WEB-DL',
        'languages': ['english'],
        'seasons': [],
    }),
    ("[720p] The God of Highschool Season 1", {
        'title': "The God of Highschool",
        'seasons': [1],
        'resolution': '720p',
        'languages': [],
        'episodes': []
    }),
    ("Heidi Audio Latino DVDRip [cap. 3 Al 18]", {
        'title': "Heidi",
        'episodes': [3],
        'source': 'DVDRip',
        'languages': ['latino'],
        'seasons': [],
    })
])
def test_random_releases_parse(parser, release_name, expected):
    assert parser.parse(release_name) == expected

