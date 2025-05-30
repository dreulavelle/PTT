import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_episode_code", [
    # Should Match
    ("[CBM]_Medaka_Box_-_11_-_This_Is_the_End!!_[720p]_[436E0E90].mkv", "436E0E90"),
    ("[Final8]Suisei no Gargantia - 05 (BD 10-bit 1920x1080 x264 FLAC)[E0B15ACF].mkv", "E0B15ACF"),
    ("[Golumpa] Fairy Tail - 214 [FuniDub 720p x264 AAC] [5E46AC39].mkv", "5E46AC39"),
    ("[ACX]El_Cazador_de_la_Bruja_-_19_-_A_Man_Who_Protects_[SSJ_Saiyan_Elite]_[9E199846].mkv", "9E199846"),
    ("Gankutsuou.-.The.Count.Of.Monte.Cristo[2005].-.04.-.[720p.BD.HEVC.x265].[FLAC].[Jd].[DHD].[b6e6e648].mkv", "B6E6E648"),
    ("[D0ugyB0y] Nanatsu no Taizai Fundo no Shinpan - 01 (1080p WEB NF x264 AAC[9CC04E06]).mkv", "9CC04E06"),
    ("[ACX]El_Cazador_de_la_Bruja_-_19_-_A_Man_Who_Protects_[SSJ_Saiyan_Elite]_[9E199846].mkv", "9E199846"),
    ("(Hi10)_Re_Zero_Shin_Henshuu-ban_-_02v2_(720p)_(DDY)_(72006E34).mkv", "72006E34"),

    # Should Not Match
    ("[Erai-raws] Evangelion 3.0 You Can (Not) Redo - Movie [1920x960][Multiple Subtitle].mkv", None),
    ("BLACK PANTHER - Wakanda Forever (2022) 10bit.m1080p.BRRip.H265.MKV.AC3-5.1 DUBPL-ENG-NapisyPL [StarLord]", None),
    ("Lost.[Perdidos].6x05.HDTV.XviD.[www.DivxTotaL.com].avi", None),
    ("[Exiled-Destiny]_Tokyo_Underground_Ep02v2_(41858470).mkv", "41858470"),
])
def test_episode_code_detection(parser, release_name, expected_episode_code):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_episode_code:
        assert "episode_code" in result, f"Episode code key missing in result for {release_name}"
        assert result["episode_code"] == expected_episode_code, f"Incorrect episode code detected for {release_name}"
    else:
        assert "episode_code" not in result, f"Incorrectly detected episode code for {release_name}"
