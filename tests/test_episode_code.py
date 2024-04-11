import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_episode_code", [
    ("[Golumpa] Fairy Tail - 214 [FuniDub 720p x264 AAC] [5E46AC39].mkv", "5E46AC39"),
    ("[Exiled-Destiny]_Tokyo_Underground_Ep02v2_(41858470).mkv", "41858470"),
    ("[ACX]El_Cazador_de_la_Bruja_-_19_-_A_Man_Who_Protects_[SSJ_Saiyan_Elite]_[9E199846].mkv", "9E199846"),
    ("[CBM]_Medaka_Box_-_11_-_This_Is_the_End!!_[720p]_[436E0E90]", "436E0E90"),
    ("Gankutsuou.-.The.Count.Of.Monte.Cristo[2005].-.04.-.[720p.BD.HEVC.x265].[FLAC].[Jd].[DHD].[b6e6e648].mkv",
     "b6e6e648"),
    ("[D0ugyB0y] Nanatsu no Taizai Fundo no Shinpan - 01 (1080p WEB NF x264 AAC[9CC04E06]).mkv", "9CC04E06"),
    # Negative test case: no episode code should be detected
    ("Lost.[Perdidos].6x05.HDTV.XviD.[www.DivxTotaL.com].avi", None),
])
def test_episode_code_detection(parser, release_name, expected_episode_code):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_episode_code:
        assert "episodeCode" in result, f"Episode code key missing in result for {release_name}"
        assert result["episodeCode"] == expected_episode_code, f"Incorrect episode code detected for {release_name}"
    else:
        assert "episodeCode" not in result, f"Incorrectly detected episode code for {release_name}"
