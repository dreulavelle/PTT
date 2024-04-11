import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_hdr", [
    ("The.Mandalorian.S01E06.4K.HDR.2160p 4.42GB", ["HDR"]),
    ("Spider-Man - Complete Movie Collection (2002-2022) 1080p.HEVC.HDR10.1920x800.x265. DTS-HD", ["HDR"]),
    ("Bullet.Train.2022.2160p.AMZN.WEB-DL.x265.10bit.HDR10Plus.DDP5.1-SMURF", ["HDR10+"]),
    ("Belle (2021) 2160p 10bit 4KLight DOLBY VISION BluRay DDP 7.1 x265-QTZ", ["DV"]),
    ("Андор / Andor [01x01-03 из 12] (2022) WEB-DL-HEVC 2160p | 4K | Dolby Vision TV | NewComers, HDRezka Studio",
     ["DV"]),
    ("АBullet.Train.2022.2160p.WEB-DL.DDP5.1.DV.MKV.x265-NOGRP", ["DV"]),
    ("Bullet.Train.2022.2160p.WEB-DL.DoVi.DD5.1.HEVC-EVO[TGx]", ["DV"]),
    ("Спайдерхед / Spiderhead (2022) WEB-DL-HEVC 2160p | 4K | HDR | Dolby Vision Profile 8 | P | NewComers, Jaskier",
     ["DV", "HDR"]),
    ("House.of.the.Dragon.S01E07.2160p.10bit.HDR.DV.WEBRip.6CH.x265.HEVC-PSA", ["DV", "HDR"]),
    ("Флешбэк / Memory (2022) WEB-DL-HEVC 2160p | 4K | HDR | HDR10+ | Dolby Vision Profile 8 | Pazl Voice",
     ["DV", "HDR10+", "HDR"]),
])
def test_hdr_detection(parser, release_name, expected_hdr):
    result = parser.parse(release_name)
    assert "hdr" in result, f"HDR key missing in result for {release_name}"
    assert set(result["hdr"]) == set(expected_hdr), f"Incorrect HDR tags detected for {release_name}"
