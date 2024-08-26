import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_audio", [
    ("Nocturnal Animals 2016 VFF 1080p BluRay DTS HEVC-HD2", ["DTS Lossy"]),
    ("Gold 2016 1080p BluRay DTS-HD MA 5 1 x264-HDH", ["DTS Lossless"]),
    ("Rain Man 1988 REMASTERED 1080p BRRip x264 AAC-m2g", ["AAC"]),
    ("The Vet Life S02E01 Dunk-A-Doctor 1080p ANPL WEB-DL AAC2 0 H 264-RTN", ["AAC"]),
    ("Jimmy Kimmel 2017 05 03 720p HDTV DD5 1 MPEG2-CTL", ["Dolby Digital"]),
    ("A Dog's Purpose 2016 BDRip 720p X265 Ac3-GANJAMAN", ["AC3"]),
    ("Retroactive 1997 BluRay 1080p AC-3 HEVC-d3g", ["AC3"]),
    ("Tempete 2016-TrueFRENCH-TVrip-H264-mp3", ["MP3"]),
    ("Detroit.2017.BDRip.MD.GERMAN.x264-SPECTRE", None),
    ("The Blacklist S07E04 (1080p AMZN WEB-DL x265 HEVC 10bit EAC-3 5.1)[Bandi]", ["EAC3"]),
    ("Condor.S01E03.1080p.WEB-DL.x265.10bit.EAC3.6.0-Qman[UTR].mkv", ["EAC3"]),
    ("The 13 Ghosts of Scooby-Doo (1985) S01 (1080p AMZN Webrip x265 10bit EAC-3 2.0 - Frys) [TAoE]", ["EAC3"]),
    ("[Thund3r3mp3ror] Attack on Titan - 23.mp4", None),
    ("Buttobi!! CPU - 02 (DVDRip 720x480p x265 HEVC AC3x2 2.0x2)(Dual Audio)[sxales].mkv", ["AC3"]),
    ("[naiyas] Fate Stay Night - Unlimited Blade Works Movie [BD 1080P HEVC10 QAACx2 Dual Audio]", ["AAC"]),
    ("Sakura Wars the Movie (2001) (BDRip 1920x1036p x265 HEVC FLACx2, AC3 2.0+5.1x2)(Dual Audio)[sxales].mkv", ["FLAC", "AC3"]),
    ("Spider-Man.No.Way.Home.2021.2160p.BluRay.REMUX.HEVC.TrueHD.7.1.Atmos-FraMeSToR", ["Atmos", "TrueHD"]),
    ("Monk.S01.1080p.AMZN.WEBRip.DDP2.0.x264-AJP69[rartv]", ["Dolby Digital Plus"]),
    ("Monk.S01E01E02.1080p.WEB-DL.DD2.0.x264-AJP69.mkv", ["Dolby Digital"]),
    ("Outlaw Star - 23 (BDRip 1440x1080p x265 HEVC AC3, FLACx2 2.0x3)(Dual Audio)[sxales].mkv", ["FLAC", "AC3"]),
])
def test_audio_detection(parser, release_name, expected_audio):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    if expected_audio:
        assert result.get("audio") == expected_audio, f"Failed for {release_name}"
    else:
        assert "audio" not in result, f"Unexpected audio detection for {release_name}"

@pytest.mark.parametrize("release_name, expected_audio", [
    ("Macross ~ Do You Remember Love (1984) (BDRip 1920x1036p x265 HEVC DTS-HD MA, FLAC, AC3x2 5.1+2.0x3)(Dual Audio)[sxales].mkv", ["DTS Lossless", "FLAC", "AC3"]),
    ("Escaflowne (2000) (BDRip 1896x1048p x265 HEVC TrueHD, FLACx3, AC3 5.1x2+2.0x3)(Triple Audio)[sxales].mkv", ["TrueHD", "FLAC", "AC3"]),
    ("[SAD] Inuyasha - The Movie 4 - Fire on the Mystic Island [BD 1920x1036 HEVC10 FLAC2.0x2] [84E9A4A1].mkv", ["FLAC"]),
])
def test_audio_detection_without_episode(parser, release_name, expected_audio):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    if expected_audio:
        assert result.get("audio") == expected_audio, f"Failed for {release_name}"
    else:
        assert "audio" not in result, f"Unexpected audio detection for {release_name}"
    assert result.get("episodes") == [], f"Unexpected episode detection for {release_name}"

@pytest.mark.parametrize("release_name, expected_audio, expected_episode", [
    ("Outlaw Star - 23 (BDRip 1440x1080p x265 HEVC AC3, FLACx2 2.0x3)(Dual Audio)[sxales].mkv", ["FLAC", "AC3"], [23]),
    ("Buttobi!! CPU - 02 (DVDRip 720x480p x265 HEVC AC3x2 2.0x2)(Dual Audio)[sxales].mkv", ["AC3"], [2]),
])
def test_audio_detection_with_episode(parser, release_name, expected_audio, expected_episode):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    if expected_audio and expected_episode:
        assert result.get("audio") == expected_audio, f"Failed for {release_name}"
        assert result.get("episodes") == expected_episode, f"Failed for {release_name}"
    else:
        assert "audio" not in result, f"Unexpected audio detection for {release_name}"

@pytest.mark.parametrize("release_name, expected_audio, expected_title", [
    ("The Shawshank Redemption 1994.MULTi.1080p.Blu-ray.DTS-HDMA.5.1.HEVC-DDR[EtHD]", ["DTS Lossless"], "The Shawshank Redemption"),
    ("Oppenheimer.2023.BluRay.1080p.DTS-HD.MA.5.1.AVC.REMUX-FraMeSToR.mkv", ["DTS Lossless"], "Oppenheimer"),
    ("Guardians.of.the.Galaxy.Vol.3.2023.BluRay.1080p.DTS-HD.MA.7.1.x264-MTeam[TGx]", ["DTS Lossless"], "Guardians of the Galaxy Vol 3"),
    ("Oppenheimer.2023.2160p.MA.WEB-DL.DUAL.DTS.HD.MA.5.1+DD+5.1.DV-HDR.H.265-TheBiscuitMan.mkv", ["DTS Lossless", "Dolby Digital Plus"], "Oppenheimer"),
    ("The.Equalizer.3.2023.BluRay.1080p.DTS-HD.MA.5.1.x264-MTeam", ["DTS Lossless"], "The Equalizer 3"),
    ("Point.Break.1991.2160p.Blu-ray.Remux.DV.HDR.HEVC.DTS-HD.MA.5.1-CiNEPHiLES.mkv", ["DTS Lossless"], "Point Break"),
    ("The.Mechanic.2011.2160p.UHD.Blu-ray.Remux.DV.HDR.HEVC.DTS-HD.MA.5.1-CiNEPHiLES.mkv", ["DTS Lossless"], "The Mechanic"),
    ("Face.Off.1997.UHD.BluRay.2160p.DTS-HD.MA.5.1.DV.HEVC.REMUX-FraMeSToR.mkv", ["DTS Lossless"], "Face Off"),
    ("Killers of the Flower Moon 2023 2160p UHD Blu-ray Remux HEVC DV DTS-HD MA 5.1-HDT.mkv", ["DTS Lossless"], "Killers of the Flower Moon"),
    ("Ghostbusters.Frozen.Empire.2024.1080p.BluRay.ENG.LATINO.HINDI.ITA.DTS-HD.Master.5.1.H264-BEN.THE.MEN", ["DTS Lossless"], "Ghostbusters Frozen Empire"),
    ("How.To.Train.Your.Dragon.2.2014.1080p.BluRay.ENG.LATINO.DTS-HD.Master.H264-BEN.THE.MEN", ["DTS Lossless"], "How To Train Your Dragon 2"),
    ("【高清影视之家发布 www.HDBTHD.com】奥本海默[IMAX满屏版][简繁英字幕].Oppenheimer.2023.IMAX.2160p.BluRay.x265.10bit.DTS-HD.MA.5.1-CTRLHD", ["DTS Lossless"], "高清影视之家发布"),
    ("Ocean's.Thirteen.2007.UHD.BluRay.2160p.DTS-HD.MA.5.1.DV.HEVC.HYBRID.REMUX-FraMeSToR.mkv", ["DTS Lossless"], "Ocean's Thirteen"),
    ("Sleepy.Hollow.1999.BluRay.1080p.2Audio.DTS-HD.HR.5.1.x265.10bit-ALT", ["DTS Lossy"], "Sleepy Hollow"),
    ("The Flash 2023 WEBRip 1080p DTS DD+ 5.1 Atmos x264-MgB", ["DTS Lossy", "Atmos", "Dolby Digital Plus"], "The Flash"),
    ("Indiana Jones and the Last Crusade 1989 BluRay 1080p DTS AC3 x264-MgB", ["DTS Lossy", "AC3"], "Indiana Jones and the Last Crusade"),
    ("2012.London.Olympics.BBC.Bluray.Set.1080p.DTS-HD", ["DTS Lossy"], "London Olympics BBC"),
    ("www.1TamilMV.phd - Oppenheimer (2023) English BluRay - 1080p - x264 - (DTS 5.1) - 7.3GB - ESub.mkv", ["DTS Lossy"], "Oppenheimer"),
    ("【高清影视之家发布 www.HDBTHD.com】年会不能停！[60帧率版本][国语音轨+中文字幕].Johnny.Keep.Walking.2023.60FPS.2160p.WEB-DL.H265.10bit.DTS.5.1-GPTHD", ["DTS Lossy"], "高清影视之家发布"),
    ("Big.Stan.2007.1080p.BluRay.Remux.DTS-HD.HR.5.1", ["DTS Lossy"], "Big Stan"),
    ("Ditched.2022.1080p.Bluray.DTS-HD.HR.5.1.X264-EVO[TGx]", ["DTS Lossy"], "Ditched"),
    ("Basic.Instinct.1992.Unrated.Directors.Cut.Bluray.1080p.DTS-HD-HR-6.1.x264-Grym@BTNET", ["DTS Lossy"], "Basic Instinct"),
])
def test_dts_separation(parser, release_name, expected_audio, expected_title):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    if expected_audio:
        assert result.get("audio") == expected_audio, f"Failed for {release_name}"
    else:
        assert "audio" not in result, f"Unexpected audio detection for {release_name}"
    if expected_title:
        assert result.get("title") == expected_title, f"Failed for {release_name}"
    else:
        assert "title" not in result, f"Unexpected title detection for {release_name}"

@pytest.mark.parametrize("release_name, expected_audio", [
    ("Madame Web (2024) 1080p HINDI ENGLISH 10bit AMZN WEBRip DDP5 1 x265 HEVC - PSA Shadow", ["Dolby Digital Plus"]),
    ("[www.1TamilMV.pics]_The.Great.Indian.Suicide.2023.Tamil.TRUE.WEB-DL.4K.SDR.HEVC.(DD+5.1.384Kbps.&.AAC).3.2GB.ESub.mkv", ["TrueHD", "Dolby Digital Plus", "AAC"]),
])
def test_ddp_separation(parser, release_name, expected_audio):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    if expected_audio:
        assert result.get("audio") == expected_audio, f"Failed for {release_name}"
    else:
        assert "audio" not in result, f"Unexpected audio detection for {release_name}"