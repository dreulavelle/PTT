import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_group", [
    ("Nocturnal Animals 2016 VFF 1080p BluRay DTS HEVC-HD2", "HD2"),
    ("Gold 2016 1080p BluRay DTS-HD MA 5 1 x264-HDH", "HDH"),
    ("Hercules (2014) 1080p BrRip H264 - YIFY", "YIFY"),
    ("The.Expanse.S05E02.720p.WEB.x264-Worldmkv.mkv", "Worldmkv"),
    ("The.Expanse.S05E02.PROPER.720p.WEB.h264-KOGi[rartv]", "KOGi"),
    ("The.Expanse.S05E02.1080p.AMZN.WEB.DDP5.1.x264-NTb[eztv.re].mp4", "NTb"),
    ("Western - L'homme qui n'a pas d'étoile-1955.Multi.DVD9", None),
    ("Power (2014) - S02E03.mp4", None),
    ("Power (2014) - S02E03", None),
    ("3-Nen D-Gumi Glass no Kamen - 13", None),
    ("3-Nen D-Gumi Glass no Kamen - Ep13", None),
    ("[AnimeRG] One Punch Man - 09 [720p].mkv", "AnimeRG"),
    ("[Mazui]_Hyouka_-_03_[DF5E813A].mkv", "Mazui"),
    ("[H3] Hunter x Hunter - 38 [1280x720] [x264]", "H3"),
    ("[KNK E MMS Fansubs] Nisekoi - 20 Final [PT-BR].mkv", "KNK E MMS Fansubs"),
    ("[ToonsHub] JUJUTSU KAISEN - S02E01 (Japanese 2160p x264 AAC) [Multi-Subs].mkv", "ToonsHub"),
    ("[HD-ELITE.NET] -  The.Art.Of.The.Steal.2014.DVDRip.XviD.Dual.Aud", None), # Should not be detected as group, site instead
    ("[Russ]Lords.Of.London.2014.XviD.H264.AC3-BladeBDP", "BladeBDP"),
    ("Jujutsu Kaisen S02E01 2160p WEB H.265 AAC -Tsundere-Raws (B-Global).mkv", "B-Global"),
    ("[DVD-RIP] Kaavalan (2011) Sruthi XVID [700Mb] [TCHellRaiser]", None),
    ("the-x-files-502.mkv", None),
    ("[ Torrent9.cz ] The.InBetween.S01E10.FiNAL.HDTV.XviD-EXTREME.avi", "EXTREME"),
])
def test_group_detection(parser, release_name, expected_group):
    result = parser.parse(release_name)
    if expected_group:
        assert result.get("group") == expected_group, f"Incorrect group detected for {release_name}"
    else:
        assert "group" not in result, f"Incorrectly detected group for {release_name}, with group {result['group']}"
