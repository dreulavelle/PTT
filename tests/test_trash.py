import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p

@pytest.mark.parametrize("release_name, expected_trash", [
    ("(Hi10)_Re_Zero_Shin_Henshuu-ban_-_02v2_(720p)_(DDY)_(72006E34).mkv", False),
    ("Anatomia De Grey - Temporada 19 [HDTV][Cap.1905][Castellano][www.AtomoHD.nu].avi", False),
    ("[SubsPlease] Fairy Tail - 100 Years Quest - 05 (1080p) [1107F3A9].mkv", False),
    ("Body.Cam.S08E07.1080p.WEB.h264-EDITH[EZTVx.to].mkv", False),
    ("Body Cam (2020) [1080p] [WEBRip] [5.1] [YTS] [YIFY]", False),
    ("Avengers Infinity War 2018 NEW PROPER 720p HD-CAM X264 HQ-CPG", True),
    ("Venom: Let There Be Carnage (2021) English 720p CAMRip [NO LOGO]", True),
    ("Oppenheimer (2023) NEW ENG 1080p HQ-CAM x264 AAC - HushRips", True),
    ("Hatyapuri 2022 1080p CAMRp Bengali AAC H264 [2GB] - HDWebMovies", True),
    ("Avengers: Infinity War (2018) 720p HQ New CAMRip Line Audios [Tamil + Telugu + Hindi + Eng] x264 1.2GB [Team TR]", True),
    ("Brave.2012.R5.DVDRip.XViD.LiNE-UNiQUE", True),
    ("Guardians of the Galaxy (CamRip / 2014)", True),
    ("Guardians of the Galaxy (2014) 1080p BluRay 5.1 DTS-HD MA 7.1 [YTS] [YIFY]", False),
])
def test_trash_parser(release_name, expected_trash, parser):
    result = parser.parse(release_name)
    assert isinstance(result, dict)
    assert result.get("trash", False) == expected_trash, f"Failed for {release_name}"
