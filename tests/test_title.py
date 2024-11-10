import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize(
    "release_name, expected_title",
    [
        ("La famille bélier", "La famille bélier"),
        ("La.famille.bélier", "La famille bélier"),
        ("Mr. Nobody", "Mr. Nobody"),
        ("doctor_who_2005.8x12.death_in_heaven.720p_hdtv_x264-fov", "doctor who"),
        ("[GM-Team][国漫][太乙仙魔录 灵飞纪 第3季][Magical Legend of Rise to immortality Ⅲ][01-26][AVC][GB][1080P]", "Magical Legend of Rise to immortality Ⅲ"),
        ("【喵萌奶茶屋】★01月新番★[Rebirth][01][720p][简体][招募翻译]", "Rebirth"),
        ("【喵萌奶茶屋】★01月新番★[別對映像研出手！/映像研には手を出すな！/Eizouken ni wa Te wo Dasu na!][01][1080p][繁體]", "Eizouken ni wa Te wo Dasu na!"),
        ("【喵萌奶茶屋】★01月新番★[別對映像研出手！/Eizouken ni wa Te wo Dasu na!/映像研には手を出すな！][01][1080p][繁體]", "Eizouken ni wa Te wo Dasu na!"),
        ("[Seed-Raws] 劇場版 ペンギン・ハイウェイ Penguin Highway The Movie (BD 1280x720 AVC AACx4 [5.1+2.0+2.0+2.0]).mp4", "Penguin Highway The Movie"),
        ("[SweetSub][Mutafukaz / MFKZ][Movie][BDRip][1080P][AVC 8bit][简体内嵌]", "Mutafukaz / MFKZ"),
        ("[Erai-raws] Kingdom 3rd Season - 02 [1080p].mkv", "Kingdom"),
        ("Голубая волна / Blue Crush (2002) DVDRip", "Blue Crush"),
        ("Жихарка (2007) DVDRip", "Жихарка"),
        ("3 Миссия невыполнима 3 2006г. BDRip 1080p.mkv", "3 Миссия невыполнима 3"),
        ("1. Детские игры. 1988. 1080p. HEVC. 10bit..mkv", "1. Детские игры"),
        ("01. 100 девчонок и одна в лифте 2000 WEBRip 1080p.mkv", "01. 100 девчонок и одна в лифте"),
        ("08.Планета.обезьян.Революция.2014.BDRip-HEVC.1080p.mkv", "08 Планета обезьян Революция"),
        ("Американские животные / American Animals (Барт Лэйтон / Bart Layton) [2018, Великобритания, США, драма, криминал, BDRip] MVO (СВ Студия)", "American Animals"),
        ("Греческая смоковница / Griechische Feigen / The Fruit Is Ripe (Зиги Ротемунд / Sigi Rothemund (as Siggi Götz)) [1976, Германия (ФРГ), эротика, комедия, приключения, DVDRip] 2 VO", "Griechische Feigen / The Fruit Is Ripe"),
        ("Греческая смоковница / The fruit is ripe / Griechische Feigen (Siggi Götz) [1976, Германия, Эротическая комедия, DVDRip]", "The fruit is ripe / Griechische Feigen"),
        ("Бастер / Buster (Дэвид Грин / David Green) [1988, Великобритания, Комедия, мелодрама, драма, приключения, криминал, биография, DVDRip]", "Buster"),
        ("(2000) Le follie dell'imperatore - The Emperor's New Groove (DvdRip Ita Eng AC3 5.1).avi", "Le follie dell'imperatore - The Emperor's New Groove"),
        ("[NC-Raws] 间谍过家家 / SPY×FAMILY - 04 (B-Global 1920x1080 HEVC AAC MKV)", "SPY×FAMILY"),
        ("GTO (Great Teacher Onizuka) (Ep. 1-43) Sub 480p lakshay", "GTO (Great Teacher Onizuka)"),
        ("Книгоноши / Кнiганошы (1987) TVRip от AND03AND | BLR", "Кнiганошы"),
        ("Yurusarezaru_mono2.srt", "Yurusarezaru mono2"),
        ("www.1TamilMV.world - Ayalaan (2024) Tamil PreDVD - 1080p - x264 - HQ Clean Aud - 2.5GB.mkv", "Ayalaan"),
        ("www.Torrenting.com   -    Anatomy Of A Fall (2023)", "Anatomy Of A Fall"),
        ("[www.arabp2p.net]_-_تركي مترجم ومدبلج Last.Call.for.Istanbul.2023.1080p.NF.WEB-DL.DDP5.1.H.264.MKV.torrent", "Last Call for Istanbul"),
        ("www,1TamilMV.phd - The Great Indian Suicide (2023) Tamil TRUE WEB-DL - 4K SDR - HEVC - (DD+5.1 - 384Kbps & AAC) - 3.2GB - ESub.mkv", "The Great Indian Suicide"),
        ("ww.Tamilblasters.sbs - 8 Bit Christmas (2021) HQ HDRip - x264 - Telugu (Fan Dub) - 400MB].mkv", "8 Bit Christmas"),
        ("www.1TamilMV.pics - 777 Charlie (2022) Tamil HDRip - 720p - x264 - HQ Clean Aud - 1.4GB.mkv", "777 Charlie"),
        ("Despicable.Me.4.2024.D.TELESYNC_14OOMB.avi", "Despicable Me 4"),
        ("UFC.247.PPV.Jones.vs.Reyes.HDTV.x264-PUNCH[TGx]", "UFC 247 Jones vs Reyes"),
        ("[www.1TamilMV.pics]_The.Great.Indian.Suicide.2023.Tamil.TRUE.WEB-DL.4K.SDR.HEVC.(DD+5.1.384Kbps.&.AAC).3.2GB.ESub.mkv", "The Great Indian Suicide"),
        ("Game of Thrones - S02E07 - A Man Without Honor [2160p] [HDR] [5.1, 7.1, 5.1] [ger, eng, eng] [Vio].mkv", "Game of Thrones"),
        ("Pawn.Stars.S09E13.1080p.HEVC.x265-MeGusta", "Pawn Stars"),
        ("Pawn Stars -- 4x13 -- Broadsiding Lincoln.mkv", "Pawn Stars"),
        ("Pawn Stars S04E19 720p WEB H264-BeechyBoy mp4", "Pawn Stars"),
        ("Jurassic.World.Dominion.CUSTOM.EXTENDED.2022.2160p.MULTi.VF2.UHD.Blu-ray.REMUX.HDR.DoVi.HEVC.DTS-X.DTS-HDHRA.7.1-MOONLY.mkv", "Jurassic World Dominion"),
        ("www.Torrenting.com   -    14.Peaks.Nothing.Is.Impossible.2021.1080p.WEB.h264-RUMOUR", "14 Peaks Nothing Is Impossible"),
        ("Too Many Cooks _ Adult Swim.mp4", "Too Many Cooks"),
        ("О мышах и людях (Of Mice and Men) 1992 BDRip 1080p.mkv", "Of Mice and Men"),
        ("Wonder Woman 1984 (2020) [UHDRemux 2160p DoVi P8 Es-DTSHD AC3 En-AC3].mkv", "Wonder Woman 1984"),
        ("www.TamilBlasters.cam - Titanic (1997)[1080p BDRip - Org Auds - [Tamil + Telugu + Hindi + Eng] - x264 - DD5.1 (448 Kbps) - 4.7GB - ESubs].mkv", "Titanic"),
        ("S.W.A.T.2017.S08E01.720p.HDTV.x264-SYNCOPY[TGx]", "S W A T"),
        ("Grimm.INTEGRAL.MULTI.COMPLETE.BLURAY-BMTH", "Grimm"),
        ("Friends.1994.INTEGRALE.MULTI.1080p.WEB-DL.H265-FTMVHD", "Friends"),
        ("STEVE.martin.a.documentary.in.2.pieces.S01.COMPLETE.1080p.WEB.H264-SuccessfulCrab[TGx]", "STEVE martin a documentary in 2 pieces"),
        ("The Lockerbie Bombing (2013) Documentary HDTVRIP", "The Lockerbie Bombing"),
    ],
)
def test_title_detection(parser, release_name, expected_title):
    result = parser.parse(release_name)
    assert result["title"] == expected_title, f"Title detection failed for {release_name}"
