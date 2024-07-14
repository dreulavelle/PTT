import pytest

import PTT


@pytest.mark.parametrize("release_name, expected_site", [
    ("The.Expanse.S05E02.1080p.AMZN.WEB.DDP5.1.x264-NTb[eztv.re].mp4", "eztv.re"),
    ("www.1TamilBlasters.lat - Thuritham (2023) [Tamil - 2K QHD AVC UNTOUCHED - x264 - AAC - 3.4GB - ESub].mkv", "www.1TamilBlasters.lat"),
    ("www.1TamilMV.world - Raja Vikramarka (2024) Tamil HQ HDRip - 400MB - x264 - AAC - ESub.mkv", "www.1TamilMV.world"),
    ("Anatomia De Grey - Temporada 19 [HDTV][Cap.1905][Castellano][www.AtomoHD.nu].avi", "www.AtomoHD.nu"),
    ("[HD-ELITE.NET] -  The.Art.Of.The.Steal.2014.DVDRip.XviD.Dual.Aud", "HD-ELITE.NET"),
])
def test_group_detection(release_name, expected_site):
    result = PTT.parse_title(release_name)
    if expected_site:
        assert result.get("site") == expected_site, f"Incorrect site detected for {release_name}"
    else:
        assert "site" not in result, f"Incorrectly detected site for {release_name}"
