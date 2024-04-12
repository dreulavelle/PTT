import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_resolution", [
    ("Annabelle.2014.1080p.PROPER.HC.WEBRip.x264.AAC.2.0-RARBG", "1080p"),
    ("doctor_who_2005.8x12.death_in_heaven.720p_hdtv_x264-fov", "720p"),
    ("UFC 187 PPV 720P HDTV X264-KYR", "720p"),
    ("The Smurfs 2 2013 COMPLETE FULL BLURAY UHD (4K) - IPT EXCLUSIVE", "4k"),
    ("Joker.2019.2160p.4K.BluRay.x265.10bit.HDR.AAC5.1", "4k"),
    ("[Beatrice-Raws] Evangelion 3.333 You Can (Not) Redo [BDRip 3840x1632 HEVC TrueHD]", "4k"),
    ("[Erai-raws] Evangelion 3.0 You Can (Not) Redo - Movie [1920x960][Multiple Subtitle].mkv", "1080p"),
    ("[JacobSwaggedUp] Kizumonogatari I: Tekketsu-hen (BD 1280x544) [MP4 Movie]", "720p"),
    ("UFC 187 PPV 720i HDTV X264-KYR", "720p"),
    ("IT Chapter Two.2019.7200p.AMZN WEB-DL.H264.[Eng Hin Tam Tel]DDP 5.1.MSubs.D0T.Telly", "720p"),
    ("Dumbo (1941) BRRip XvidHD 10800p-NPW", "1080p"),
    ("BluesBrothers2M1080.www.newpct.com.mkv", "1080p"),
    ("BenHurParte2BD1080.www.newpct.com.mkv", "1080p"),
    ("1993720p_101_WWW.NEWPCT1.COM.mkvv", "720p"),
])
def test_resolution_detection(parser, release_name, expected_resolution):
    result = parser.parse(release_name)
    assert result.get(
        "resolution") == expected_resolution, f"Expected resolution to be {expected_resolution} for {release_name}"
