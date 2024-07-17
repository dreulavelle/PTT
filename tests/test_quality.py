import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_quality", [
    ("Nocturnal Animals 2016 VFF 1080p BluRay DTS HEVC-HD2", "BluRay"),
    ("doctor_who_2005.8x12.death_in_heaven.720p_hdtv_x264-fov", "HDTV"),
    ("Rebecca.1940.720p.HDTVRip.HDCLUB", "HDTV"),
    ("Gossip Girl - 1ª Temporada. (SAT-Rip)", "SATRip"),
    ("A Stable Life S01E01 DVDRip x264-Ltu", "DVDRip"),
    ("The Vet Life S02E01 Dunk-A-Doctor 1080p ANPL WEB-DL AAC2 0 H 264-RTN", "WEB-DL"),
    ("Brown Nation S01E05 1080p WEBRip x264-JAWN", "WEBRip"),
    ("Star Wars The Last Jedi 2017 TeleSync AAC x264-MiniMe", "TeleSync"),
    ("The.Shape.of.Water.2017.DVDScr.XVID.AC3.HQ.Hive-CM8", "SCR"),
    ("Cloudy With A Chance Of Meatballs 2 2013 720p PPVRip x264 AAC-FooKaS", "PPVRip"),
    ("The.OA.1x08.L.Io.Invisibile.ITA.WEBMux.x264-UBi.mkv", "WEBMux"),
    ("[UsifRenegade] Cardcaptor Sakura [BD][Remastered][1080p][HEVC_10Bit][Dual] + Movies", "BDRip"),
    ("[UsifRenegade] Cardcaptor Sakura - 54 [BD-RM][1080p][x265_10Bit][Dual_AAC].mkv", "BDRip"),
    ("Elvis & Nixon (MicroHD-1080p)", "HDRip"),
    ("Bohemian Rhapsody 2018.2160p.UHDrip.x265.HDR.DD+.5.1-DTOne", "UHDRip"),
    ("Blade.Runner.2049.2017.4K.UltraHD.BluRay.2160p.x264.TrueHD.Atmos", "BluRay"),
    ("Terminator.Dark.Fate.2019.2160p.UHD.BluRay.X265.10bit.HDR.TrueHD", "BluRay"),
    ("When We Were Boys 2013 BD Rip x264 titohmr", "BDRip"),
    ("Key.and.Peele.s03e09.720p.web.dl.mrlss.sujaidr (pimprg)", "WEB-DL"),
    ("Godzilla 2014 HDTS HC XVID AC3 ACAB", "TeleSync"),
    ("Harry Potter And The Half Blood Prince 2009 telesync aac -- king", "TeleSync"),
    ("Capitao.America.2.TS.BrunoG", "TeleSync"),
    ("Star Trek TS-Screener Spanish Alta-Calidad 2da Version 2009 - Me", "TeleSync"),
    ("Solo: A Star Wars Story (2018) English 720p TC x264 900MBTEAM TR", "TeleCine"),
    ("Alita Battle Angel 2019 720p HDTC-1XBET", "TeleCine"),
    ("My.Super.Ex.Girlfriend.FRENCH.TELECINE.XViD-VCDFRV", "TeleCine"),
    ("You're Next (2013) cam XVID", "CAM"),
    ("Shes the one_2013(camrip)__TOPSIDER [email protected]", "CAM"),
    ("Blair Witch 2016 HDCAM UnKnOwN", "CAM"),
    ("Thor : Love and Thunder (2022) Hindi HQCAM x264 AAC - QRips.mkv", "CAM"),
    ("Avatar The Way of Water (2022) 1080p HQ S-Print Dual Audio [Hindi   English] x264 AAC HC-Esub - CineVood.mkv",
     "CAM"),
    (
    "Avatar The Way of Water (2022) 1080p S Print Dual Audio [Hindi   English] x264 AAC HC-Esub - CineVood.mkv", "CAM"),
    ("Good Deeds 2012 SCR XViD-KiNGDOM", "SCR"),
    ("Genova DVD-Screener Spanish 2008", "SCR"),
    ("El Albergue Rojo BR-Screener Spanish 2007", "SCR"),
    ("The.Mysteries.of.Pittsburgh.LIMITED.SCREENER.XviD-COALiTiON [NOR", "SCR"),
    ("El.curioso.caso.de.benjamin.button-BRScreener-[EspaDivx.com].rar", "SCR"),
    ("Thor- Love and Thunder (2022) Original Hindi Dubbed 1080p HQ PreDVD Rip x264 AAC [1.7 GB]- CineVood.mkv", "SCR"),
    ("Black Panther Wakanda Forever 2022 Hindi 1080p PDVDRip x264 AAC CineVood.mkv", "SCR"),
    ("Vampire in Vegas (2009) NL Subs DVDR DivXNL-Team", "DVD"),
    ("Звонок из прошлого / Kol / The Call (2020) WEB-DLRip | ViruseProject", "WEB-DL"),
    ("La nube (2020) [BluRay Rip][AC3 5.1 Castellano][www.maxitorrent.com]", "BRRip"),
    ("Joker.2019.2160p.BluRay.REMUX.HEVC.DTS-HD.MA.TrueHD.7.1.Atmos-FGT", "BluRay REMUX"),
    ("Warcraft 2016 1080p Blu-ray Remux AVC TrueHD Atmos-KRaLiMaRKo", "BluRay REMUX"),
    ("Joker.2019.UHD.BluRay.2160p.TrueHD.Atmos.7.1.HEVC.REMUX-JAT", "BluRay REMUX"),
    ("Spider-Man No Way Home.2022.REMUX.1080p.Bluray.DTS-HD.MA.5.1.AVC-EVO[TGx]", "BluRay REMUX"),
    ("Son of God 2014 HDR BDRemux 1080p.mkv", "BluRay REMUX"),
    ("Peter Rabbit 2 [4K UHDremux][2160p][HDR10][DTS-HD 5.1 Castellano-TrueHD 7.1-Ingles+Subs][ES-EN]", "BluRay REMUX"),
    ("Snatch cerdos y diamantes [4KUHDremux 2160p][Castellano AC3 5.1-Ingles TrueHD 7.1+Subs]", "BluRay REMUX"),
    ("Троя / Troy [2004 HDDVDRip-AVC] Dub + Original + Sub]", "DVDRip"),
    ("Структура момента (Расим Исмайлов) [1980, Драма, VHSRip]", "DVDRip"),
    ("Мужчины без женщин (Альгимантас Видугирис) [1981, Драма, VHS]", "DVD"),
    ("Преферанс по пятницам (Игорь Шешуков) [1984, Детектив, DVB]", "HDTV"),
    ("Соперницы (Алексей Дмитриев) [1929, драма, WEB-DLRip]", "WEB-DL"),
    ("Dragon Blade (2015) HDTSRip Exclusive", "TeleSync"),
    ("Criminal (2016) Hindi Dubbed HDTCRip", "TeleCine"),
    ("Avatar La Voie de l'eau.FRENCH.CAMHD.H264.AAC", "CAM")
])
def test_source_detection(parser, release_name, expected_quality):
    result = parser.parse(release_name)
    assert result.get("quality") == expected_quality, f"Source detection failed for {release_name}"
