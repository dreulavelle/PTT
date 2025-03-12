import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_output", [
    ("sons.of.anarchy.s05e10.480p.BluRay.x264-GAnGSteR", {
        "title": "sons of anarchy",
        "resolution": "480p",
        "seasons": [5],
        "episodes": [10],
        "quality": "BluRay",
        "codec": "avc",
        "group": "GAnGSteR",
        "languages": []
    }),
    ("Color.Of.Night.Unrated.DC.VostFR.BRrip.x264", {
        "title": "Color Of Night",
        "unrated": True,
        "languages": ["fr"],
        "quality": "BRRip",
        "codec": "avc",
        "seasons": [],
        "episodes": []
    }),
    ("Da Vinci Code DVDRip", {
        "title": "Da Vinci Code",
        "quality": "DVDRip",
        "languages": [],
        "seasons": [],
        "episodes": []
    }),
    ("Some.girls.1998.DVDRip", {
        "title": "Some girls",
        "quality": "DVDRip",
        "year": 1998,
        "languages": [],
        "seasons": [],
        "episodes": []
    }),
    ("Ecrit.Dans.Le.Ciel.1954.MULTI.DVDRIP.x264.AC3-gismo65", {
        "title": "Ecrit Dans Le Ciel",
        "quality": "DVDRip",
        "year": 1954,
        "languages": [],
        "dubbed": True,
        "codec": "avc",
        "audio": ["AC3"],
        "group": "gismo65",
        "seasons": [],
        "episodes": []
    }),
    ("2019 After The Fall Of New York 1983 REMASTERED BDRip x264-GHOULS", {
        "title": "2019 After The Fall Of New York",
        "quality": "BDRip",
        "edition": "Remastered",
        "year": 1983,
        "codec": "avc",
        "group": "GHOULS",
        "languages": [],
        "seasons": [],
        "episodes": []
    }),
    ("Ghost In The Shell 2017 720p HC HDRip X264 AC3-EVO", {
        "title": "Ghost In The Shell",
        "quality": "HDRip",
        "hardcoded": True,
        "year": 2017,
        "resolution": "720p",
        "codec": "avc",
        "audio": ["AC3"],
        "group": "EVO",
        "languages": [],
        "seasons": [],
        "episodes": []
    }),
    ("Rogue One 2016 1080p BluRay x264-SPARKS", {
        "title": "Rogue One",
        "quality": "BluRay",
        "year": 2016,
        "resolution": "1080p",
        "codec": "avc",
        "group": "SPARKS",
        "languages": [],
        "seasons": [],
        "episodes": []
    }),
    ("Desperation 2006 Multi Pal DvdR9-TBW1973", {
        "title": "Desperation",
        "quality": "DVD",
        "year": 2006,
        "languages": [],
        "dubbed": True,
        "region": "R9",
        "group": "TBW1973",
        "seasons": [],
        "episodes": [],
        "dubbed": True
    }),
    ("Maman, j'ai raté l'avion 1990 VFI 1080p BluRay DTS x265-HTG", {
        "title": "Maman, j'ai raté l'avion",
        "quality": "BluRay",
        "year": 1990,
        "audio": ["DTS Lossy"],
        "resolution": "1080p",
        "languages": ["fr"],
        "codec": "hevc",
        "group": "HTG",
        "seasons": [],
        "episodes": []
    }),
    ("Game of Thrones - The Complete Season 3 [HDTV]", {
        "title": "Game of Thrones",
        "seasons": [3],
        "quality": "HDTV",
        "languages": [],
        "episodes": [],
        "complete": True
    }),
    ("The Sopranos: The Complete Series (Season 1,2,3,4,5&6) + Extras", {
        "title": "The Sopranos",
        "seasons": [1, 2, 3, 4, 5, 6],
        "complete": True,
        "languages": [],
        "episodes": [],
    }),
    ("Skins Season S01-S07 COMPLETE UK Soundtrack 720p WEB-DL", {
        "seasons": [1, 2, 3, 4, 5, 6, 7],
        "title": "Skins",
        "country": "UK",
        "resolution": "720p",
        "quality": "WEB-DL",
        "languages": [],
        "episodes": [],
        "complete": True
    }),
    ("Futurama.COMPLETE.S01-S07.720p.BluRay.x265-HETeam", {
        "title": "Futurama",
        "seasons": [1, 2, 3, 4, 5, 6, 7],
        "resolution": "720p",
        "quality": "BluRay",
        "codec": "hevc",
        "group": "HETeam",
        "languages": [],
        "episodes": [],
        "complete": True
    }),
    ("You.[Uncut].S01.SweSub.1080p.x264-Justiso", {
        "title": "You",
        "edition": "Uncut",
        "seasons": [1],
        "languages": ["sv"],
        "resolution": "1080p",
        "codec": "avc",
        "group": "Justiso",
        "episodes": []
    }),
    ("Stephen Colbert 2019 10 25 Eddie Murphy 480p x264-mSD [eztv]", {
        "title": "Stephen Colbert",
        "date": "2019-10-25",
        "resolution": "480p",
        "codec": "avc",
        "languages": [],
        "seasons": [],
        "episodes": []
    }),
    ("House MD Season 7 Complete MKV", {
        "title": "House MD",
        "seasons": [7],
        "container": "mkv",
        "languages": [],
        "episodes": [],
        "complete": True
    }),
    ("2008 The Incredible Hulk Feature Film.mp4", {
        "title": "The Incredible Hulk Feature Film",
        "year": 2008,
        "container": "mp4",
        "extension": "mp4",
        "languages": [],
        "seasons": [],
        "episodes": []
    }),
    ("【4月/悠哈璃羽字幕社】[UHA-WINGS][不要输！恶之军团][Makeruna!! Aku no Gundan!][04][1080p AVC_AAC][简繁外挂][sc_tc]", {
        "title": "Makeruna!! Aku no Gundan!",
        "episodes": [4],
        "resolution": "1080p",
        "codec": "avc",
        "audio": ["AAC"],
        "languages": ["zh"],
        "seasons": [],
        "trash": True
    }),
    ("[GM-Team][国漫][西行纪之集结篇][The Westward Ⅱ][2019][17][AVC][GB][1080P]", {
        "title": "The Westward Ⅱ",
        "year": 2019,
        "episodes": [17],
        "resolution": "1080p",
        "codec": "avc",
        "group": "GM-Team",
        "languages": ["zh"],
        "seasons": [],
    }),
    ("Черное зеркало / Black Mirror / Сезон 4 / Серии 1-6 (6) [2017, США, WEBRip 1080p] MVO + Eng Sub", {
        "title": "Black Mirror",
        "year": 2017,
        "seasons": [4],
        "episodes": [1, 2, 3, 4, 5, 6],
        "languages": ["en", "ru"],
        "resolution": "1080p",
        "quality": "WEBRip",
        "subbed": True
    }),
    ("[neoHEVC] Student Council's Discretion / Seitokai no Ichizon [Season 1] [BD 1080p x265 HEVC AAC]", {
        "title": "Student Council's Discretion / Seitokai no Ichizon",
        "seasons": [1],
        "resolution": "1080p",
        "quality": "BDRip",
        "audio": ["AAC"],
        "codec": "hevc",
        "group": "neoHEVC",
        "languages": [],
        "episodes": []
    }),
    ("[Commie] Chihayafuru 3 - 21 [BD 720p AAC] [5F1911ED].mkv", {
        "title": "Chihayafuru 3",
        "episodes": [21],
        "resolution": "720p",
        "quality": "BDRip",
        "audio": ["AAC"],
        "container": "mkv",
        "extension": "mkv",
        "episode_code": "5F1911ED",
        "group": "Commie",
        "languages": [],
        "seasons": [],
    }),
    ("[DVDRip-ITA]The Fast and the Furious: Tokyo Drift [CR-Bt]", {
        "title": "The Fast and the Furious: Tokyo Drift",
        "quality": "DVDRip",
        "languages": ["it"],
        "seasons": [],
        "episodes": []
    }),
    ("[BluRay Rip 720p ITA AC3 - ENG AC3 SUB] Hostel[2005]-LIFE[ultimafrontiera]", {
        "title": "Hostel",
        "year": 2005,
        "resolution": "720p",
        "quality": "BRRip",
        "audio": ["AC3"],
        "languages": ["en", "it"],
        "group": "LIFE",
        "seasons": [],
        "episodes": [],
        "subbed": True
    }),
    ("[OFFICIAL ENG SUB] Soul Land Episode 121-125 [1080p][Soft Sub][Web-DL][Douluo Dalu][斗罗大陆]", {
        "title": "Soul Land",
        "seasons": [],
        "episodes": [121, 122, 123, 124, 125],
        "languages": ["en", "zh"],
        "resolution": "1080p",
        "quality": "WEB-DL",
        "subbed": True
    }),
    ("[720p] The God of Highschool Season 1", {
        "title": "The God of Highschool",
        "seasons": [1],
        "resolution": "720p",
        "languages": [],
        "episodes": []
    }),
    ("Heidi Audio Latino DVDRip [cap. 3 Al 18]", {
        "title": "Heidi",
        "episodes": [3],
        "quality": "DVDRip",
        "languages": ["la"],
        "seasons": [],
    }),
    ("Anatomia De Grey - Temporada 19 [HDTV][Castellano][www.AtomoHD.nu].avi", {
        "title": "Anatomia De Grey",
        "seasons": [19],
        "episodes": [],
        "container": "avi",
        "extension": "avi",
        "languages": ["es"],
        "quality": "HDTV",
        "site": "www.AtomoHD.nu",
    }),
    ("Sprint.2024.S01.COMPLETE.1080p.WEB.h264-EDITH[TGx]", {
        "title": "Sprint",
        "year": 2024,
        "seasons": [1],
        "episodes": [],
        "languages": [],
        "quality": "WEB",
        "resolution": "1080p",
        "scene": True,
        "codec": "avc",
        "group": "EDITH",
        "complete": True
    }),
    ("Madame Web 2024 UHD BluRay 2160p TrueHD Atmos 7 1 DV HEVC REMUX-FraMeSToR", {
        "title": "Madame Web",
        "year": 2024,
        "quality": "BluRay REMUX",
        "resolution": "2160p",
        "channels": ["7.1"],
        "audio": ["Atmos", "TrueHD"],
        "codec": "hevc",
        "languages": [],
        "seasons": [],
        "episodes": [],
        "hdr": ["DV"],
        "group": "FraMeSToR"
    }),
    ("The.Witcher.US.S01.INTERNAL.1080p.WEB.x264-STRiFE", {
        "title": "The Witcher",
        "seasons": [1],
        "episodes": [],
        "languages": [],
        "country": "US",
        "quality": "WEB",
        "resolution": "1080p",
        "scene": True,
        "codec": "avc",
        "group": "STRiFE"
    }),
    ("Madame Web (2024) 1080p HINDI ENGLISH 10bit AMZN WEBRip DDP5 1 x265 HEVC - PSA Shadow", {
        "title": "Madame Web",
        "year": 2024,
        "languages": ["en", "hi"],
        "quality": "WEBRip",
        "resolution": "1080p",
        "bit_depth": "10bit",
        "audio": ["Dolby Digital Plus"],
        "channels": ["5.1"],
        "codec": "hevc",
        "seasons": [],
        "episodes": [],
        "network": "Amazon"
    }),
    ("The Simpsons S01E01 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole", {
        "title": "The Simpsons",
        "seasons": [1],
        "episodes": [1],
        "languages": [],
        "resolution": "1080p",
        "quality": "BluRay",
        "codec": "hevc",
        "bit_depth": "10bit",
        "audio": ["AC3", "AAC"],
        "channels": ["5.1"]
    }),
    ("[DB]_Bleach_264_[012073FE].avi", {
        "title": "Bleach",
        "container": "avi",
        "extension": "avi",
        "episode_code": "012073FE",
        "seasons": [],
        "episodes": [264],
        "languages": [],
        "group": "DB"
    }),
    ("[SubsPlease] One Piece - 1111 (480p) [2E05E658].mkv", {
        "title": "One Piece",
        "container": "mkv",
        "resolution": "480p",
        "extension": "mkv",
        "episode_code": "2E05E658",
        "seasons": [],
        "episodes": [1111],
        "languages": [],
        "group": "SubsPlease"
    }),
    ("One Piece S01E1056 VOSTFR 1080p WEB x264 AAC -Tsundere-Raws (CR) mkv", {
        "title": "One Piece",
        "seasons": [1],
        "episodes": [1056],
        "languages": ["fr"],
        "container": "mkv",
        "resolution": "1080p",
        "scene": True,
        "quality": "WEB",
        "codec": "avc",
        "audio": ["AAC"],
    }),
    ("Mary.Poppins.1964.50th.ANNIVERSARY.EDITION.REMUX.1080p.Bluray.AVC.DTS-HD.MA.5.1-LEGi0N", {
        "title": "Mary Poppins",
        "year": 1964,
        "seasons": [],
        "episodes": [],
        "languages": [],
        "edition": "Anniversary Edition",
        "quality": "BluRay REMUX",
        "resolution": "1080p",
        "audio": ["DTS Lossless"],
        "channels": ["5.1"],
        "codec": "avc",
        "group": "LEGi0N"
    }),
    ("The.Lord.of.the.Rings.The.Fellowship.of.the.Ring.2001.EXTENDED.2160p.UHD.BluRay.x265.10bit.HDR.TrueHD.7.1.Atmos-BOREDOR", {
        "title": "The Lord of the Rings The Fellowship of the Ring",
        "year": 2001,
        "resolution": "2160p",
        "edition": "Extended Edition",
        "languages": [],
        "seasons": [],
        "episodes": [],
        "quality": "BluRay",
        "codec": "hevc",
        "bit_depth": "10bit",
        "audio": ["Atmos", "TrueHD"],
        "channels": ["7.1"],
        "hdr": ["HDR"],
        "group": "BOREDOR"
    }),
    ("Escaflowne (2000) (BDRip 1896x1048p x265 HEVC TrueHD, FLACx3, AC3 5.1x2+2.0x3)(Triple Audio)[sxales].mkv", {
        "title": "Escaflowne",
        "year": 2000,
        "languages": [],
        "seasons": [],
        "episodes": [],
        "quality": "BDRip",
        "codec": "hevc",
        "resolution": "1896x1048p",  # this needs to be 1080p instead probably
        "audio": ["TrueHD", "FLAC", "AC3"],
        "channels": ["5.1"],
        # "group": "sxales",
        "dubbed": True,
        "container": "mkv",
        "extension": "mkv"
    }),
    ("[www.1TamilMV.pics]_The.Great.Indian.Suicide.2023.Tamil.TRUE.WEB-DL.4K.SDR.HEVC.(DD+5.1.384Kbps.&.AAC).3.2GB.ESub.mkv", {
        "title": "The Great Indian Suicide",
        "year": 2023,
        "languages": ["en", "ta"],
        "seasons": [],
        "episodes": [],
        "quality": "WEB-DL",
        "resolution": "2160p",
        "hdr": ["SDR"],
        "codec": "hevc",
        "site": "www.1TamilMV.pics",
        "size": "3.2GB",
        "container": "mkv",
        "extension": "mkv",
        "bitrate": "384kbps",
        "audio": ["TrueHD", "Dolby Digital Plus", "AAC"],
        "channels": ["5.1"],
    }),
    ("www.5MovieRulz.show - Khel Khel Mein (2024) 1080p Hindi DVDScr - x264 - AAC - 2.3GB.mkv", {
        "title": "Khel Khel Mein",
        "year": 2024,
        "languages": ["hi"],
        "seasons": [],
        "episodes": [],
        "quality": "SCR",
        "codec": "avc",
        "audio": ["AAC"],
        "resolution": "1080p",
        "container": "mkv",
        "extension": "mkv",
        "size": "2.3GB",
        "site": "www.5MovieRulz.show",
        "trash": True
    }),
    ("超能警探.Memorist.S01E01.2160p.WEB-DL.H265.AAC-FLTTH.mkv", {
        "title": "Memorist",
        "seasons": [1],
        "episodes": [1],
        "languages": ["zh"],
        "quality": "WEB-DL",
        "codec": "hevc",
        "audio": ["AAC"],
        "resolution": "2160p",
        "container": "mkv",
        "extension": "mkv",
        "group": "FLTTH",
    }),
    ("Futurama.S08E03.How.the.West.Was.1010001.1080p.HULU.WEB-DL.DDP5.1.H.264-FLUX.mkv", {
        "title": "Futurama",
        "seasons": [8],
        "episodes": [3],
        "languages": [],
        "network": "Hulu",
        "codec": "avc",
        "container": "mkv",
        "extension": "mkv",
        "audio": ["Dolby Digital Plus"],
        "channels": ["5.1"],
        "quality": "WEB-DL",
        "resolution": "1080p",
        "group": "FLUX"
    }),
    ("V.H.S.2 [2013] 1080p BDRip x265 DTS-HD MA 5.1 Kira [SEV].mkv", {
        "title": "V H S 2",
        "year": 2013,
        "languages": [],
        "seasons": [],
        "episodes": [],
        "quality": "BDRip",
        "codec": "hevc",
        "audio": ["DTS Lossless"],
        "channels": ["5.1"],
        "container": "mkv",
        "extension": "mkv",
        "resolution": "1080p"
    }),
    ("{WWW.BLUDV.TV} Love, Death & Robots - 1ª Temporada Completa 2019 (1080p) Acesse o ORIGINAL WWW.BLUDV.TV", {
        "title": "Love, Death & Robots",
        "seasons": [1],
        "episodes": [],
        "languages": ["es"],
        "resolution": "1080p",
        "year": 2019,
        "complete": True,
        "site": "WWW.BLUDV.TV",
        "trash": True
    }),
    ("www.MovCr.to - Bikram Yogi, Guru, Predator (2019) 720p WEB_DL x264 ESubs [Dual Audio]-[Hindi + Eng] - 950MB - MovCr.mkv", {
        "title": "Bikram Yogi, Guru, Predator",
        "year": 2019,
        "languages": ["en", "hi"],
        "quality": "WEB-DL",
        "resolution": "720p",
        "codec": "avc",
        "container": "mkv",
        "extension": "mkv",
        "site": "www.MovCr.to",
        "dubbed": True,
        "episodes": [],
        "group": "MovCr",
        "seasons": [],
        "size": "950MB"
    }),
    ("28.days.2000.1080p.bluray.x264-mimic.mkv", {
        "title": "28 days",
        "year": 2000,
        "resolution": "1080p",
        "quality": "BluRay",
        "codec": "avc",
        "container": "mkv",
        "extension": "mkv",
        "group": "mimic",
        "episodes": [],
        "languages": [],
        "seasons": []
    }),
    ("4.20.Massacre.2018.1080p.BluRay.x264.AAC-[YTS.MX].mp4", {
        "title": "4 20 Massacre",
        "year": 2018,
        "resolution": "1080p",
        "quality": "BluRay",
        "codec": "avc",
        "audio": ["AAC"],
        "container": "mp4",
        "extension": "mp4",
        "languages": [],
        "episodes": [],
        "seasons": [],
        "site": "YTS.MX"
    }),
    ("inside.out.2.2024.d.ru.ua.ts.1o8op.mkv", {
        "title": "inside out 2",
        "year": 2024,
       # "resolution": "1080p", - this is correct. we dont want it to parse the resolution here.
        "quality": "TeleSync",
        "container": "mkv",
        "extension": "mkv",
        "languages": ["ru"],
        "episodes": [],
        "seasons": [],
        "trash": True
    }),
    ("I.S.S.2023.P.WEB-DL.1O8Op.mkv", {
        "title": "I S S",
        "year": 2023,
        "quality": "WEB-DL",
        "container": "mkv",
        "extension": "mkv",
        "languages": [],
        "episodes": [],
        "seasons": []
    }),
    ("Skazka.2022.Pa.WEB-DL.1O8Op.mkv", {
        "title": "Skazka",
        "year": 2022,
        "quality": "WEB-DL",
        "container": "mkv",
        "extension": "mkv",
        "languages": [],
        "episodes": [],
        "seasons": []
    }),
    ("Spider-Man.Across.the.Spider-Verse.2023.Dt.WEBRip.1O8Op.mkv", {
        "title": "Spider-Man Across the Spider-Verse",
        "year": 2023,
        "quality": "WEBRip",
        "container": "mkv",
        "extension": "mkv",
        "languages": [],
        "episodes": [],
        "seasons": []
    }),
    ("Civil.War.2024.D.WEB-DL.1O8Op.mkv", {
        "title": "Civil War",
        "year": 2024,
        "quality": "WEB-DL",
        "container": "mkv",
        "extension": "mkv",
        "languages": [],
        "episodes": [],
        "seasons": []
    }),
    ("Dune.Part.Two.2024.2160p.WEB-DL.DDP5.1.Atmos.DV.HDR.H.265-FLUX[TGx]", {
        "title": "Dune Part Two",
        "year": 2024,
        "resolution": "2160p",
        "quality": "WEB-DL",
        "codec": "hevc",
        "audio": ["Dolby Digital Plus", "Atmos"],
        "channels": ["5.1"],
        "group": "FLUX",
        "episodes": [],
        "hdr": ["DV", "HDR"],
        "languages": [],
        "seasons": []
    }),
    ("Saw.3D.2010.1080p.ITA-ENG.BluRay.x265.AAC-V3SP4EV3R.mkv", {
        "title": "Saw 3D",
        "year": 2010,
        "seasons": [],
        "episodes": [],
        "languages": ["en", "it"],
        "resolution": "1080p",
        "quality": "BluRay",
        "codec": "hevc",
        "audio": ["AAC"],
        "container": "mkv",
        "extension": "mkv",
        "group": "V3SP4EV3R"
    }),
    ("Dead Before Dawn 3D (2012) [3D.BLU-RAY] [1080p 3D] [BluRay] [HSBS] [YTS.MX]", {
        "title": "Dead Before Dawn 3D",
        "year": 2012,
        "languages": [],
        "seasons": [],
        "episodes": [],
        "resolution": "1080p",
        "quality": "BluRay",
        "3d": True
    }),
    ("Wonder.Woman.1984.2020.3D.1080p.BluRay.x264-SURCODE[rarbg]", {
        "title": "Wonder Woman 1984",
        "year": 2020,
        "seasons": [],
        "episodes": [],
        "languages": [],
        "resolution": "1080p",
        "scene": True,
        "quality": "BluRay",
        "codec": "avc",
        "group": "SURCODE",
        "3d": True
    }),
    ("The.Last.of.Us.S01E08.1080p.WEB.H264-CAKES[TGx]", {
        "title": "The Last of Us",
        "seasons": [1],
        "episodes": [8],
        "languages": [],
        "resolution": "1080p",
        "scene": True,
        "quality": "WEB",
        "codec": "avc",
        "group": "CAKES"
    }),
    ("The.Office.UK.S01.1080P.BLURAY.REMUX.AVC.DD5.1-NOGRP", {
        "title": "The Office",
        "seasons": [1],
        "episodes": [],
        "languages": [],
        "country": "UK",
        "quality": "BluRay REMUX",
        "resolution": "1080p",
        "audio": ["Dolby Digital"],
        "channels": ["5.1"],
        "codec": "avc",
        "group": "NOGRP"
    }),
    ("The.Office.US.S01-09.COMPLETE.SERIES.1080P.BLURAY.X265-HIQVE", {
        "title": "The Office",
        "seasons": [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "episodes": [],
        "country": "US",
        "languages": [],
        "quality": "BluRay",
        "resolution": "1080p",
        "codec": "hevc",
        "complete": True,
        "group": "HIQVE"
    }),
    ("Hard Knocks 2001 S23E01 1080p MAX WEB-DL DDP2 0 x264-NTb[EZTVx.to].mkv", {
        "title": "Hard Knocks",
        "year": 2001,
        "seasons": [23],
        "episodes": [1],
        "languages": [],
        "quality": "WEB-DL",
        "resolution": "1080p",
        "codec": "avc",
        "audio": ["Dolby Digital Plus"],
        # "channels": ["2.0"],
        "group": "NTb",
        "extension": "mkv",
        "container": "mkv",
        "site": "EZTVx.to"
    }),
    ("Fallout.S01E03.The.Head.2160p.DV.HDR10Plus.Ai-Enhanced.H265.DDP.5.1.MULTI.RIFE.4.15v2-60fps-DirtyHippie.mkv", {
        "title": "Fallout",
        "seasons": [1],
        "episodes": [3],
        "languages": [],
        "resolution": "2160p",
        "codec": "hevc",
        "audio": ["AC3", "Dolby Digital Plus"],
        "channels": ["5.1"],
        "group": "DirtyHippie",
        "container": "mkv",
        "dubbed": True,
        "extension": "mkv",
        "hdr": ["DV", "HDR10+"],
        "upscaled": True
    }),
    ("BoJack Horseman [06x01-08 of 16] (2019-2020) WEB-DLRip 720p", {
        "title": "BoJack Horseman",
        "seasons": [6],
        "episodes": [1, 2, 3, 4, 5, 6, 7, 8],
        "languages": [],
        "resolution": "720p",
        "quality": "WEB-DLRip",
        "complete": True  # this is not correct, but not a big deal either..
    }),
    ("Трон: Наследие / TRON: Legacy (2010) WEB-DL 1080p | D | Open Matte", {
        "title": "TRON: Legacy",
        "year": 2010,
        "seasons": [],
        "episodes": [],
        "languages": ["ru"],
        "resolution": "1080p",
        "quality": "WEB-DL",
    }),
    ("Wentworth.S08E06.PDTV.AAC2.0.x264-BTN", {
        "title": "Wentworth",
        "seasons": [8],
        "episodes": [6],
        "languages": [],
        "quality": "PDTV",
        "codec": "avc",
        "audio": ["AAC"],
        "group": "BTN"
    }),
    ("www.1Tamilblasters.co - Guardians of the Galaxy Vol. 3 (2023) [4K IMAX UHD HEVC - BDRip - [Tam + Mal + Tel + Hin + Eng] - x264 - DDP5.1 (192Kbps) - 8.3GB - ESub].mkv", {
        "title": "Guardians of the Galaxy Vol. 3",
        "year": 2023,
        "seasons": [],
        "episodes": [],
        "languages": ["en", "hi", "te", "ta", "ml"],
        "quality": "BDRip",
        "codec": "hevc",
        "audio": ["Dolby Digital Plus"],
        "channels": ["5.1"],
        "resolution": "2160p",
        "container": "mkv",
        "extension": "mkv",
        "site": "www.1Tamilblasters.co",
        "bitrate": "192kbps",
        "edition": "IMAX",
        "size": "8.3GB"
    }),
    ("【高清影视之家发布 www.hdbthd.com】奥本海默 杜比视界版本 高码版 国英多音轨 中文字幕 .oppenheimer.2023.2160p.hq.web-dl.h265.dv.ddp5.1.2audio-dreamhd", {
        "title": "高清影视之家发布",
        "year": 2023,
        "languages": ["zh"],
        "quality": "WEB-DL",
        "codec": "hevc",
        "audio": ["Dolby Digital Plus"],
        "channels": ["5.1"],
        "resolution": "2160p",
        "site": "www.hdbthd.com",
        "episodes": [],
        "group": "dreamhd",
        "hdr": ["DV"],
        "seasons": [],
        "trash": True
    }),
    ("Venom (2018) HD-TS 720p Hindi Dubbed (Clean Audio) x264", {
        "title": "Venom",
        "year": 2018,
        "seasons": [],
        "episodes": [],
        "languages": ["hi"],
        "quality": "TeleSync",
        "resolution": "720p",
        "codec": "avc",
        "audio": ["HQ Clean Audio"],
        "dubbed": True,
        "trash": True
    }),
    ("www.Tamilblasters.party - The Wheel of Time (2021) Season 01 EP(01-08) [720p HQ HDRip - [Tam + Tel + Hin] - DDP5.1 - x264 - 2.7GB - ESubs]", {
        "title": "The Wheel of Time",
        "year": 2021,
        "seasons": [1],
        "episodes": [1, 2, 3, 4, 5, 6, 7, 8],
        "languages": ["hi", "te", "ta"],
        "quality": "HDRip",
        "resolution": "720p",
        "codec": "avc",
        "audio": ["Dolby Digital Plus"],
        "channels": ["5.1"],
        "site": "www.Tamilblasters.party",
        "size": "2.7GB",
        "trash": True
    }),
    ("The.Walking.Dead.S06E07.SUBFRENCH.HDTV.x264-AMB3R.mkv", {
        # should detect french language and subbed
        "title": "The Walking Dead",
        "seasons": [6],
        "episodes": [7],
        "languages": ["fr"],
        "quality": "HDTV",
        "codec": "avc",
        "group": "AMB3R",
        "extension": "mkv",
        "container": "mkv"
    }),
    ("The Walking Dead S05E03 720p Remux x264-ASAP[ettv]", {
        "title": "The Walking Dead",
        "seasons": [5],
        "episodes": [3],
        "languages": [],
        "quality": "REMUX",
        "resolution": "720p",
        "codec": "avc",
        "group": "ASAP"
    }),
    ("www.TamilBlasters.vip - Shang-Chi (2021) [720p BDRip - [Tamil + Telugu + Hindi + Eng] - x264 - DDP5.1 (192 Kbps) - 1.4GB - ESubs].mkv", {
        # should not find "Shang-Chi" as chinese language
        "title": "Shang-Chi",
        "year": 2021,
        "seasons": [],
        "episodes": [],
        "languages": ["en", "hi", "te", "ta"],
        "quality": "BDRip",
        "resolution": "720p",
        "codec": "avc",
        "audio": ["Dolby Digital Plus"],
        "channels": ["5.1"],
        "site": "www.TamilBlasters.vip",
        "size": "1.4GB",
        "extension": "mkv",
        "container": "mkv"
    }),
    ("Game of Thrones 1ª a 8ª Temporada Completa [720p-1080p] [BluRay] [DUAL]", {
        "title": "Game of Thrones",
        "seasons": [1, 2, 3, 4, 5, 6, 7, 8],
        "episodes": [],
        "languages": ["es"],
        "resolution": "1080p",
        "quality": "BluRay",
        "complete": True,
        "dubbed": True
    }),
    ("Kill.2024.REPACK.1080p.AMZN.WEB-DL.DDP5.1.Atmos.H.264-XEBEC.mkv", {
        "title": "Kill",
        "year": 2024,
        "seasons": [],
        "episodes": [],
        "languages": [],
        "resolution": "1080p",
        "quality": "WEB-DL",
        "codec": "avc",
        "audio": ["Dolby Digital Plus", "Atmos"],
        "channels": ["5.1"],
        "group": "XEBEC",
        "container": "mkv",
        "extension": "mkv",
        "network": "Amazon",
        "repack": True
    }),
    ("Mad.Max.Fury.Road.2015.1080p.BluRay.DDP5.1.x265.10bit-GalaxyRG265[TGx]", {
        "title": "Mad Max Fury Road",
        "year": 2015,
        "seasons": [],
        "episodes": [],
        "languages": [],
        "resolution": "1080p",
        "codec": "hevc",
        "bit_depth": "10bit",
        "audio": ["Dolby Digital Plus"],
        "channels": ["5.1"],
        "group": "GalaxyRG265",
        "quality": "BluRay"
    }),
    ("Властелин колец: Кольца власти (S1E1-8 of 8) / The Lord of the Rings: The Rings of Power (2022) WEB-DL", {
        "title": "Властелин колец: Кольца власти",  # The Lord of the Rings: The Rings of Power  - We probably want the US title instead here
        "year": 2022,
        "seasons": [1],
        "episodes": [1, 2, 3, 4, 5, 6, 7, 8],
        "languages": ["ru"],
        "quality": "WEB-DL"
    }),
    ("抓娃娃 Successor.2024.TC1080P.国语中字", {
        "title": "Successor",
        "year": 2024,
        "seasons": [],
        "episodes": [],
        "languages": ["zh"],
        "resolution": "1080p",
        "quality": "TeleCine",
        "trash": True
    }),
    ("True.Detective.S03E02.720p.WEB.x265-MiNX[eztv].mkv", {
        "title": "True Detective",
        "seasons": [3],
        "episodes": [2],
        "languages": [],
        "resolution": "720p",
        "scene": True,
        "quality": "WEB",
        "codec": "hevc",
        "group": "MiNX",
        "extension": "mkv",
        "container": "mkv"
    }),
    ("True.Grit.1969.720p.WEB.x265-MiNX[eztv].mkv", {
        "title": "True Grit",
        "year": 1969,
        "seasons": [],
        "episodes": [],
        "languages": [],
        "resolution": "720p",
        "scene": True,
        "quality": "WEB",
        "codec": "hevc",
        "group": "MiNX",
        "extension": "mkv",
        "container": "mkv"
    }),
    ("Free Samples (2012) [BluRay] [1080p] [YTS.AM]", {
        "title": "Free Samples",
        "year": 2012,
        "seasons": [],
        "episodes": [],
        "languages": [],
        "resolution": "1080p",
        "quality": "BluRay"
    }),
    ("Trailer Park Boys S01-S10 + Movies + Specials + Extras [Ultimate Collection]-CAPTAiN", {
        "title": "Trailer Park Boys",
        "seasons": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "episodes": [],
        "languages": [],
        "complete": True,
        "group": "CAPTAiN"
    }),
    ("Adbhut (2024) Hindi 1080p HDTVRip x264 AAC 5.1 [2.2GB] - QRips", {
        "title": "Adbhut",
        "year": 2024,
        "seasons": [],
        "episodes": [],
        "languages": ["hi"],
        "resolution": "1080p",
        "quality": "HDTVRip",
        "codec": "avc",
        "audio": ["AC3", "AAC"],
        "channels": ["5.1"],
        "group": "QRips",
        "size": "2.2GB"
    }),
    ("Blood Diamond (2006) 1080p BluRay H264 DolbyD 5 1 + nickarad mp4", {
        "title": "Blood Diamond",
        "year": 2006,
        "seasons": [],
        "episodes": [],
        "languages": [],
        "resolution": "1080p",
        "quality": "BluRay",
        "codec": "avc",
        "audio": ["Dolby Digital"],
        "channels": ["5.1"],
        "container": "mp4"
    }),
    ("The Lockerbie Bombing (2013) Documentary HDTVRIP", {
        "title": "The Lockerbie Bombing",
        "year": 2013,
        "documentary": True,
        "seasons": [],
        "episodes": [],
        "languages": [],
        "quality": "HDTVRip"
    }),
    ("STEVE.martin.a.documentary.in.2.pieces.S01.COMPLETE.1080p.WEB.H264-SuccessfulCrab[TGx]", {
        "title": "STEVE martin a documentary in 2 pieces",
        "seasons": [1],
        "episodes": [],
        "languages": [],
        "quality": "WEB",
        "codec": "avc",
        "group": "SuccessfulCrab",
        "resolution": "1080p",
        "documentary": True,
        "scene": True,
        "complete": True
    }),
    ("The New Frontier S01E10 720p WEB H264-INFLATE[eztv] mkv", {
        "title": "The New Frontier",
        "seasons": [1],
        "episodes": [10],
        "languages": [],
        "quality": "WEB",
        "container": "mkv",
        "codec": "avc",
        "group": "INFLATE",
        "resolution": "720p",
        "scene": True
    }),
    ("[BEST-TORRENTS.COM] The.Penguin.S01E07.MULTi.1080p.AMZN.WEB-DL.H264.DDP5.1.Atmos-K83", {
        "title": "The Penguin",
        "seasons": [1],
        "episodes": [7],
        "languages": [],
        "resolution": "1080p",
        "quality": "WEB-DL",
        "network": "Amazon",
        "codec": "avc",
        "dubbed": True,
        "audio": ["Dolby Digital Plus", "Atmos"],
        "channels": ["5.1"],
        # "group": "K83",
        "site": "BEST-TORRENTS.COM"
    }),
    ("[ Torrent911.my ] The.Penguin.S01E07.FRENCH.WEBRip.x264.mp4", {
        "title": "The Penguin",
        "seasons": [1],
        "episodes": [7],
        "languages": ["fr"],
        "quality": "WEBRip",
        "codec": "avc",
        "site": "Torrent911.my",
        "container": "mp4",
        "extension": "mp4"
    }),
    ("The.O.C.Seasons.01-04.AMZN.1080p.10bit.x265.hevc-Bearfish", {
        "title": "The O C",
        "seasons": [1, 2, 3, 4],
        "episodes": [],
        "languages": [],
        "resolution": "1080p",
        "network": "Amazon",
        "codec": "hevc",
        "bit_depth": "10bit",
        "group": "Bearfish"
    }),
    ("The Adam Project 2022 2160p NF WEB-DL DDP 5 1 Atmos DoVi HDR HEVC-SiC mkv", {
        "title": "The Adam Project",
        "year": 2022,
        "seasons": [],
        "episodes": [],
        "languages": [],
        "resolution": "2160p",
        "quality": "WEB-DL",
        "network": "Netflix",
        "codec": "hevc",
        "container": "mkv",
        "audio": [
            "Atmos",
            "Dolby Digital Plus"
        ],
        "channels": [
            "5.1"
        ],
        "hdr": [
            "DV",
            "HDR"
        ]
    }),
    ("1923 S02E01 The Killing Season 1080p AMZN WEB-DL DDP5 1 H 264-FLUX[TGx]", {
        "title": "1923",
        "seasons": [2],
        "episodes": [1],
        "languages": [],
        "resolution": "1080p",
        "quality": "WEB-DL",
        "network": "Amazon",
        "codec": "avc",
        "audio": ["Dolby Digital Plus"],
        "channels": ["5.1"],
        "group": "FLUX"
    }),
    ("1883.S01E01.1883.2160p.WEB-DL.DDP5.1.H.265-NTb.mkv", {
        "title": "1883",
        "seasons": [1],
        "episodes": [1],
        "languages": [],
        "resolution": "2160p",
        "quality": "WEB-DL",
        "codec": "hevc",
        "audio": ["Dolby Digital Plus"],
        "channels": ["5.1"],
        "group": "NTb",
        "extension": "mkv",
        "container": "mkv"
    }),
    ("1923 S02E01 1080p WEB H264-SuccessfulCrab", {
        "title": "1923",
        "seasons": [2],
        "episodes": [1],
        "languages": [],
        "resolution": "1080p",
        "quality": "WEB",
        "codec": "avc",
        "scene": True,
        "group": "SuccessfulCrab"
    }),
    ("[Anime Time] Naruto - 116 - 360 Degrees of Vision The Byakugan's Blind Spot.mkv", {
        "title": "Naruto",
        "seasons": [],
        "episodes": [116],
        "languages": [],
        "group": "Anime Time",
        "extension": "mkv",
        "container": "mkv"
    }),
    ("[DKB] Blue Lock - (Season 01) [1080p][HEVC x265 10bit][Multi-Subs]", {
        "title": "Blue Lock",
        "seasons": [1],
        "episodes": [],
        "languages": [],
        "resolution": "1080p",
        "bit_depth": "10bit",
        "codec": "hevc",
        "subbed": True,
        "group": "DKB"
    }),
    ("Fallout.S01E03.The.Head.2160p.DV.HDR10Plus.Ai-Enhanced.H265.DDP.5.1.MULTI.RIFE.4.15v2-60fps-DirtyHippie.mkv", {
        "title": "Fallout",
        "seasons": [1],
        "episodes": [3],
        "languages": [],
        "resolution": "2160p",
        "audio": ["AC3", "Dolby Digital Plus"],
        "channels": ["5.1"],
        "codec": "hevc",
        "container": "mkv",
        "extension": "mkv",
        "group": "DirtyHippie",
        "hdr": ["DV", "HDR10+"],
        "upscaled": True,
        "dubbed": True
    }),
    ("[JySzE] Naruto [v2] [R2J] [VFR] [Dual Audio] [Complete] [Extras] [x264]", {
        "title": "Naruto",
        "seasons": [],
        "episodes": [],
        "languages": ["fr"],
        "codec": "avc",
        "dubbed": True,
        "group": "JySzE",
        "complete": True,
        "region": "R2J"
    }),
    ("[JySzE] Naruto [v2] [R2J] [VFR] [Dual Audio] [Complete] [Extras] [x264]", {
        "title": "Naruto",
        "seasons": [],
        "episodes": [],
        "languages": ["fr"],
        "codec": "avc",
        "dubbed": True,
        "group": "JySzE",
        "complete": True,
        "region": "R2J"
    }),
    ("Naruto HD [1080p] (001-220) [Complete Series + Movies]", {
        "title": "Naruto",
        "seasons": [],
        "episodes": list(range(1, 221)),
        "languages": [],
        "resolution": "1080p",
        "quality": "HDTV",
        "complete": True,
    }),
    ("[JySzE] Naruto [v3] [R2J] [VFR] [Dual Audio] [Complete] [Extras] [x264]", {   # check to see if it handles `[v3]`
        "title": "Naruto",
        "seasons": [],
        "episodes": [],
        "languages": ["fr"],
        "codec": "avc",
        "dubbed": True,
        "group": "JySzE",
        "complete": True,
        "region": "R2J"
    }),
    ("NARUTO CARTOON NETWORK-TOONAMI BROADCAST (2005-2009) [TVRip] [Episodes 001-209 Movies 1 & 3 & OVA)", {
        "title": "NARUTO",
        "seasons": [],
        "episodes": list(range(1, 210)),
        "languages": [],
        "quality": "TVRip",
        "complete": True,
        "extras": ["OVA"],
        "network": "Cartoon Network",
    }),
    ("NARUTO CARTOON NETWORK-TOONAMI BROADCAST (2005-2009) [TVRip] [Episodes 001-209 Movies 1 & 3 & OVA)", {
        "title": "NARUTO",
        "seasons": [],
        "episodes": list(range(1, 210)),
        "languages": [],
        "quality": "TVRip",
        "complete": True,
        "extras": ["OVA"],
        "network": "Cartoon Network",
    }),
    ("Naruto Complete [Ep 01 - 220][English][480p]", {  # was incorrectly parsing episodes before
        "title": "Naruto",
        "seasons": [],
        "episodes": list(range(1, 221)),
        "languages": ["en"],
        "complete": True,
        "resolution": "480p",
    }),
    ("[DBD-Raws][火影忍者/Naruto/NARUTO -ナルト-][166-192TV][BOX7][美版/USA.Ver][1080P][BDRip][HEVC-10bit][FLAC][MKV]", {
        "title": "Naruto",
        "seasons": [],
        "episodes": list(range(166, 193)),
        "languages": ["ja", "zh"],
        "quality": "BDRip",
        "audio": ["FLAC"],
        "resolution": "1080p",
        "codec": "hevc",
        "bit_depth": "10bit",
        "container": "mkv",
        "group": "DBD-Raws",
    }),
    ("Naruto Collection [DB 1080p][ Dual Audio ][ English & Arabic Sub ]", {
        "title": "Naruto",
        "seasons": [],
        "episodes": [],
        "languages": ["en", "ar"],
        "resolution": "1080p",
        "subbed": True,
        "dubbed": True,
        "complete": True,
    })
])
def test_random_releases_parse(parser, release_name, expected_output):
    assert parser.parse(release_name) == expected_output

@pytest.mark.parametrize("release_name, expected", [
    ("Агентство / The Agency / Сезон: 1 / Серии: 1-10 из 10 [2024 HEVC HDR10 Dolby Vision WEB-DL 2160p 4k] MVO (HDRezka Studio) + DVO (Viruse Project) + Original + Sub (Eng)", {
        "title": "The Agency",
        "seasons": [1],
        "episodes": list(range(1, 11)),
        "languages": ["en", "ru"],
        "quality": "WEB-DL",
        "resolution": "2160p",
        "bit_depth": "10bit",
        "codec": "hevc",
        "hdr": ["DV", "HDR"],
        "subbed": True,
        "year": 2024,
    })
])
def test_debug_releases_parse(parser, release_name, expected):
    assert parser.parse(release_name) == expected
