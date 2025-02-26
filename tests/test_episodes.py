import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p

@pytest.mark.parametrize("release_name, expected_episode", [
    ("(Hi10)_Re_Zero_Shin_Henshuu-ban_-_02v2_(720p)_(DDY)_(72006E34).mkv", [2]),
    ("004 - Male Unbonding - [DVD].avi", [4]),
    ("02 The Invitation.mp4", [2]),
    ("09 Movie - Dragon Ball Z - Bojack Unbound", []),
    ("2-06. Девичья сила.mkv", [6]),
    ("3-Nen D-Gumi Glass no Kamen - 13 [480p]", [13]),
    ("4-13 Cursed (HD)", [13]),
    ("4-13 Cursed (HD).m4v", [13]),
    ("22-7 (Season 1) (1080p)(HEVC x265 10bit)(Eng-Subs)-Judas[TGx] ⭐", []),
    ("24 - S01E04 - x264 - dilpill.mkv", [4]),
    ("24 - S01xE03.mp4", [3]),
    ("24.Legacy.S01E05.720p.HEVC.x265-MeGusta", [5]),
    ("30 M0N3D4S ESP T01XE08.mkv", [8]),
    ("102 - The Invitation.avi", [102]),
    ("321 - Family Guy Viewer Mail #1.avi", [321]),
    ("512 - Airport '07.avi", [512]),
    ("523 23.mp4", [523]),
    ("611-612 - Desperate Measures, Means & Ends.mp4", [611, 612]),
    ("All of Us Are Dead . 2022 . S01 EP #1.2.mkv", [2]),
    ("Anubis saison 01 episode 38 tvrip FR", [38]),
    ("Archer.S02.1080p.BluRay.DTSMA.AVC.Remux", []),
    ("BBC Indian Ocean with Simon Reeve 5of6 Sri Lanka to Bangladesh.avi", [5]),
    ("black-ish.S05E02.1080p..x265.10bit.EAC3.6.0-Qman[UTR].mkv", [2]),
    ("Bleach 10º Temporada - 215 ao 220 - [DB-BR]", list(range(215, 221))),
    ("Blue Bloods - Temporada 11 [HDTV 720p][Cap.1103][AC3 5.1 Castellano][www.PCTmix.com].mkv", [1103]),
    ("BoJack Horseman [06x01-08 of 16] (2019-2020) WEB-DLRip 720p", [1, 2, 3, 4, 5, 6, 7, 8]),
    ("breaking.bad.s01e01.720p.bluray.x264-reward", [1]),
    ("Breaking Bad S02 03.mkv", [3]),
    ("Breaking Bad S03e01-13 (1080p Ita Eng Spa h265 SubS) 2ndREPACK byMe7alh", list(range(1, 14))),
    ("Cestovatelé_S02E04_11_27.mkv", [4]),
    ("Chernobyl.S01E01.1.23.45.mkv", [1]),
    ("Chernobyl E02 1 23 45.mp4", [2]),
    ("clny.3x11m720p.es[www.planetatorrent.com].mkv", [11]),
    ("DARKER THAN BLACK - S00E00.mkv", [0]),
    ("Das Boot Miniseries Original Uncut-Reevel Cd2 Of 3.avi", [2]),
    ("Desperate.Housewives.S0615.400p.WEB-DL.Rus.Eng.avi", [15]),
    ("Desperate Housewives - Episode 1.22 - Goodbye for now.avi", [22]),
    ("Desperate_housewives_S03E02Le malheur aime la compagnie.mkv", [2]),
    ("Discovery. Парни с Юкона / Yokon Men [06х01-08] (2017) HDTVRip от GeneralFilm | P1", [1, 2, 3, 4, 5, 6, 7, 8]),
    ("Doctor.Who.2005.8x11.Dark.Water.720p.HDTV.x264-FoV", [11]),
    ("Doctor.Who.2005.8x11.Dark.Water.720p.HDTV.x264-FoV.mkv", [11]),
    ("Dragon Ball Super S01 E23 French 1080p HDTV H264-Kesni", [23]),
    ("Dragon Ball Super S05E53 - Ep.129.mkv", [53]),
    ("Dragon Ball Z Movie - 09 - Bojack Unbound - 1080p", []),
    ("Dragon Ball Z Movie - 09 - Bojack Unbound - 1080p BluRay x264 DTS 5.1 -DDR", []), # Correct. This should not match, its a movie.
    ("Dragon Ball [5.134] Preliminary Peril.mp4", [134]),
    ("DShaun.Micallefs.MAD.AS.HELL.S10E03.576p.x642-YADNUM.mkv", [3]),
    ("E5.mkv", [5]),
    ("El Chema Temporada 1 Capitulo 25", [25]),
    ("Food Wars! Shokugeki No Souma S4 - 11 (1080p)(HEVC x265 10bit)", [11]),
    ("Friends - [7x23-24] - The One with Monica and Chandler's Wedding + Audio Commentary.mkv", [23, 24]),
    ("Friends - [8x18] - The One In Massapequa.mkv", [18]),
    ("Friends.S07E20.The.One.With.Rachel's.Big.Kiss.720p.BluRay.2CH.x265.HEVC-PSA.mkv", [20]),
    ("Game.of.Thrones.S01.e01-02.2160p.UHD.BluRay.x265-Morpheus", list(range(1, 3))),
    ("Hogan's Heroes - 516 - Get Fit or Go Flight - 1-09-70.divx", [516]),
    ("House MD All Seasons (1-8) 720p Ultra-Compressed", []),
    ("Iron-Fist-2017-01_13-F.avi", [13]),
    ("Joker.2019.PROPER.mHD.10Bits.1080p.BluRay.DD5.1.x265-TMd.mkv", []),
    ("Juego de Tronos - Temp.2 [ALTA DEFINICION 720p][Cap.209][Spanish].mkv", [209]),
    ("Kyoukai no Rinne (TV) 3rd Season - 23 [1080p]", [23]),
    ("Le Monde Incroyable de Gumball - Saison 5 Ep 14 - L'extérieur", [14]),
    ("Lgds.of.Tmrow-02_17.F.avi", [17]),
    ("Lost.[Perdidos].6x05.HDTV.XviD.[www.DivxTotaL.com]", [5]),
    ("MARATHON EPISODES/Orphan Black S3 Eps.05-08.mp4", [5, 6, 7, 8]),
    ("Marvel's.Agents.of.S.H.I.E.L.D.S02E01-03.Shadows.1080p.WEB-DL.DD5.1", [1, 2, 3]),
    ("Mash S10E01b Thats Show Biz Part 2 1080p H.264 (moviesbyrizzo upload).mp4", [1]),
    ("Mazinger-Z-Cap-52.avi", [52]),
    ("Mob.Psycho.100.II.E10.720p.WEB.x264-URANiME.mkv", [10]),
    ("Mob Psycho 100 - 09 [1080p].mkv", [9]),
    ("MosGaz.(08.seriya).2012.WEB-DLRip(AVC).ExKinoRay.mkv", [8]),
    ("My Little Pony - A Amizade é Mágica - T02E22.mp4", [22]),
    ("My Little Pony FiM - 6.01 - No Second Prances.mkv", [1]),
    ("Naruto Shippuden - 107 - Strange Bedfellows", [107]),
    ("Naruto Shippuden - 107 - Strange Bedfellows.mkv", [107]),
    ("Naruto Shippuden Ep 107 - Strange Bedfellows.mkv", [107]),
    ("Naruto Shippuuden - 006-007.mkv", [6, 7]),
    ("NCIS Season 11 01.mp4", [1]),
    ("office_03_19.avi", [19]),
    ("Orange Is The New Black Season 5 Episodes 1-10 INCOMPLETE (LEAKED)", list(range(1, 11))),
    ("Otchayannie.domochozyaiki.(8.sez.21.ser.iz.23).2012.XviD.HDTVRip.avi", [21]),
    ("Ozk.02.09.avi", [9]),
    ("Ozk.02.10.F.avi", [10]),
    ("Pokemon Black & White E10 - E17 [CW] AVI", [10, 11, 12, 13, 14, 15, 16, 17]),
    ("Pokémon.S01E01-E04.SWEDISH.VHSRip.XviD-aka", [1, 2, 3, 4]),
    ("Prehistoric park.3iz6.Supercroc.DVDRip.Xvid.avi", [3]),
    ("Pwer-04_05.avi", [5]),
    ("S01 - E03 - Fifty-Fifty.mkv", [3]),
    ("S03E13_91.avi", [13]),
    ("Smallville (1x02 Metamorphosis).avi", [2]),
    ("Spergrl-2016-02_04.avi", [4]),
    ("Stargate Universe S01E01-E02-E03.mp4", [1, 2, 3]),
    ("Stargate Universe S01E01E02E03.mp4", [1, 2, 3]),
    ("Supernatural - S03E01 - 720p BluRay x264-Belex - Dual Audio + Legenda.mkv", [1]),
    ("SupNat-11_06.avi", [6]),
    ("Tajny.sledstvija.(2.sezon.12.serija.iz.12).2002.XviD.DVDRip.avi", [12]),
    ("Tajny.sledstviya-20.01.serya.WEB-DL.(1080p).by.lunkin.mkv", [1]),
    ("The.Man.In.The.High.Castle1x01.HDTV.XviD[www.DivxTotaL.com].avi", [1]),
    ("The.Witcher.S01.07.2019.Dub.AVC.ExKinoRay.mkv", [7]),
    ("The.Witcher.S01.07.mp4", [7]),
    ("The Amazing World of Gumball - 103 - The End - The Dress (720p.x264.ac3-5.1) [449].mkv", [103]),
    ("The Amazing World of Gumball - 103, 104 - The Third - The Debt.mkv", [103, 104]),
    ("The Amazing World of Gumball - 107a - The Mystery (720p.x264.ac3-5.1) [449].mkv", [107]),
    ("The Amazing World of Gumball - 107b - The Mystery (720p.x264.ac3-5.1) [449].mkv", [107]),
    ("The Avengers (EMH) - S01 E15 - 459 (1080p - BluRay)", [15]),
    ("The Avengers (EMH) - S01 E15 - 459 (1080p - BluRay).mp4", [15]),
    ("The Ed Show 10-19-12.mp4", []),
    ("The Office S07E25+E26 Search Committee.mp4", [25, 26]),
    ("The Simpsons E1-200 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole", list(range(1, 201))),
    ("The Simpsons S01E01 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole", [1]),
    ("The Simpsons S01E01-E02 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole", [1, 2]),
    ("The Simpsons S01E01-E02-E03-E04-E05 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole", [1, 2, 3, 4, 5]),
    ("The Simpsons S01E01E02 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole", [1, 2]),
    ("The Simpsons S01E01E02E03E04E05 1080p BluRay x265 HEVC 10bit AAC 5.1 Tigole", [1, 2, 3, 4, 5]),
    ("The Simpsons S28E21 720p HDTV x264-AVS", [21]),
    ("The Twilight Zone 1985 S01E22c The Library.mp4", [22]),
    ("The Twilight Zone 1985 S01E23a Shadow Play.mp4", [23]),
    ("Tokyo Ghoul Root A - 07 [S2-07] [Eng Sub] 480p [email protected]", [7]),
    ("Top Gear - 3x05 - 2003.11.23.avi", [5]),
    ("Vikings.s02.09.AVC.tahiy.mkv", [9]),
    ("Vikings.Season.05.Ep(01-10).720p.WebRip.2Ch.x265.PSA", list(range(1, 11))),
    ("Vikings.Season.05.Ep(01-10).720p.WebRip.2Ch.x265.PSA", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ("Watch Gary And His Demons Episode 10 - 0.00.07-0.11.02.mp4", [10]),
    ("Witches Of Salem - 2Of4 - Road To Hell - Gr.mkv", [2]),
    ("Witches Of Salem - 2Of4 - Road To Hell - Great Mysteries Of The World", [2]),
    ("wwe.nxt.uk.11.26.mkv", [26]),
    ("wwf.raw.is.war.18.09.00.avi", []),
    ("Yu-Gi-Oh! ZEXAL Temporada 1 Episodio 009 Dual Latino e Inglés [B3B4970E].mkv", [9]),
    ("Yu-Gi-Oh 3x089 - Awakening of Evil (Part 4).avi", [89]),
    ("Zvezdnie.Voiny.Voina.Klonov.3.sezon.22.seria.iz.22.XviD.HDRip.avi", [22]),
    ("[5.01] Weight Loss.avi", [1]),
    ("[92 Impatient Eilas & Miyafuji] Strike Witches - Road to Berlin - 01 [1080p][BCDFF6A2].mkv", [1]),
    ("[224] Darling in the FranXX - 14 [BDRip.1080p.x265.FLAC].mkv", [14]),
    ("[224] Shingeki no Kyojin - S03 - Part 1 - 13 [BDRip.1080p.x265.FLAC]", [13]),
    ("[224] Shingeki no Kyojin - S03 - Part 1 -  13 [BDRip.1080p.x265.FLAC].mkv", [13]),
    ("[a-s]_fairy_tail_-_003_-_infiltrate_the_everlue_mansion__rs2_[1080p_bd-rip][4CB16872].mkv", [3]),
    ("[ACX]El_Cazador_de_la_Bruja_-_19_-_A_Man_Who_Protects_[SSJ_Saiyan_Elite]_[9E199846].mkv", [19]),
    ("[animeawake] Naruto Shippuden - 072 - The Quietly Approaching Threat_2.mkv", [72]),
    ("[animeawake] Naruto Shippuden - 120 - Kakashi Chronicles. Boys' Life on the Battlefield. Part 2.mkv", [120]),
    ("[animeawake] Naruto Shippuden - 124 - Art_2.mkv", [124]),
    ("[AnimeRG] Naruto Shippuden - 107 [720p] [x265] [pseudo].mkv", [107]),
    ("[BenjiD] Quan Zhi Gao Shou (The King’s Avatar) / Full-Time Master S01 (01 - 12) [1080p x265] [Soft sub] V2", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    ("[CBM]_Medaka_Box_-_11_-_This_Is_the_End!!_[720p]_[436E0E90]", [11]),
    ("[CBM]_Medaka_Box_-_11_-_This_Is_the_End!!_[720p]_[436E0E90].mkv", [11]),
    ("[Eng Sub] Rebirth Ep #36 [8CF3ADFA].mkv", [36]),
    ("[Erai-raws] 3D Kanojo - Real Girl 2nd Season - 01 ~ 12 [720p]", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    ("[Erai-raws] 22-7 - 11 .mkv", [11]),
    ("[Erai-raws] Carole and Tuesday - 01 ~ 12 [1080p][Multiple Subtitle]", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    ("[Erai-raws] Granblue Fantasy The Animation Season 2 - 10 [1080p][Multiple Subtitle].mkv", [10]),
    ("[Erai-raws] Shingeki no Kyojin Season 3 - 11 [1080p][Multiple Subtitle].mkv", [11]),
    ("[Exiled-Destiny]_Tokyo_Underground_Ep02v2_(41858470).mkv", [2]),
    ("[F-D] Fairy.Tail.-.004v2.-. [480P][Dual-Audio].mkv", [4]),
    ("[F-D] Fairy Tail Season 1 - 6 + Extras [480P][Dual-Audio]", []),
    ("[F-D] Fairy Tail Season 1 -6 + Extras [480P][Dual-Audio]", []),
    ("[FFA] Koi to Producer: EVOL×LOVE - 01 - 12 [1080p][HEVC][AAC]", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    ("[Final8]Suisei no Gargantia - 05 (BD 10-bit 1920x1080 x264 FLAC)[E0B15ACF].mkv", [5]),
    ("[GM-Team][国漫][绝代双骄][Legendary Twins][2022][08][HEVC][GB][4K].mp4", [8]),
    ("[Golumpa] Star Blazers 2202 - 22 (Uchuu Senkan Yamato 2022) [FuniDub 1080p x264 AAC] [A24B89C8].mkv", [22]),
    ("[HorribleSubs] White Album 2 - 06 [1080p].mkv", [6]),
    ("[HR] Boku no Hero Academia 87 (S4-24) [1080p HEVC Multi-Subs] HR-GZ", [24]),
    ("[KH] Sword Art Online II - 14.5 - Debriefing.mkv", [14]),
    ("[KTKJ]_[BLEACH]_[DVDRIP]_[116]_[x264_640x480_aac].mkv", [116]),
    ("[OMDA] Bleach - 002 (480p x264 AAC) [rich_jc].mkv", [2]),
    ("[SSA] Detective Conan - 1001 [720p].mkv", [1001]),
    ("[SubsPlease] Digimon Adventure (2020) - 35 (720p) [4E7BA28A].mkv", [35]),
    ("[TBox] Dragon Ball Z Full 1-291(Subbed Jap Vers)", list(range(1, 292))),
    ("Викинги / Vikings / Сезон: 5 / Серии: 1 [2017, WEB-DL 1080p] MVO", [1]),
    ("Викинги / Vikings / Сезон: 5 / Серии: 1 из 20 [2017, WEB-DL 1080p] MVO", [1]),
    ("Доктор Хаус 03-20.mkv", [20]),
    ("Интерны. Сезон №9. Серия №180.avi", [180]),
    ("Комиссар Рекс 11-13.avi", [13]),
    ("Леди Баг и Супер-Кот – Сезон 3, Эпизод 21 – Кукловод 2 [1080p].mkv", [21]),
    ("Меч (05 сер.) - webrip1080p.mkv", [5]),
    ("Мистер Робот / Mr. Robot / Сезон: 2 / Серии: 1-5 (12) [2016, США, WEBRip 1080p] MVO", [1, 2, 3, 4, 5]),
    ("Проклятие острова ОУК_ 5-й сезон 09-я серия_ Прорыв Дэна.avi", [9]),
    ("Разрушители легенд. MythBusters. Сезон 15. Эпизод 09. Скрытая угроза (2015).avi", [9]),
    ("Серия 11.mkv", [11]),
    ("Anatomia De Grey - Temporada 19 [HDTV][Cap.1905][Castellano][www.AtomoHD.nu].avi", [1905]),
    ("[SubsPlease] Fairy Tail - 100 Years Quest - 05 (1080p) [1107F3A9].mkv", [5]),
    ("Mad.Max.Fury.Road.2015.1080p.BluRay.DDP5.1.x265.10bit-GalaxyRG265[TGx]", []),
    ("Vikkatakavi 01E06.mkv", [6]),
    ("[Deadfish] Hakkenden_Touhou Hakken Ibun S2 [720][AAC]", [])
])
def test_episode_parser(release_name, expected_episode, parser):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    assert result["episodes"] == expected_episode, f"Failed for {release_name}"
