import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_date", [
    ("Stephen Colbert 2019 10 25 Eddie Murphy 480p x264-mSD [eztv]", "2019-10-25"),
    ("Jimmy.Fallon.2020.02.14.Steve.Buscemi.WEB.x264-XLF[TGx]", "2020-02-14"),
    ("The Young And The Restless - S43 E10986 - 2016-08-12", "2016-08-12"),
    ("Indias Best Dramebaaz 2 Ep 19 (13 Feb 2016) HDTV x264-AquoTube", "2016-02-13"),
    ("07 2015 YR/YR 07-06-15.mp4", "2015-07-06"),
    ("SIX.S01E05.400p.229mb.hdtv.x264-][ Collateral ][ 16-Feb-2017 mp4", "2017-02-16"),
    ("WWE Smackdown - 11/21/17 - 21st November 2017 - Full Show", "2017-11-21"),
    ("WWE RAW 9th Dec 2019 WEBRip h264-TJ [TJET]", "2019-12-09"),
    ("EastEnders_20200116_19302000.mp4", "2020-01-16"),
    ("AEW DARK 4th December 2020 WEBRip h264-TJ", "2020-12-04"),
    ("WWE NXT 30th Sept 2020 WEBRip h264-TJ", "2020-09-30"),
    ("WWE Main Event 6th August 2020 WEBRip h264-TJ", "2020-08-06"),
    ("wwf.raw.is.war.18.09.00.avi", "2000-09-18"),
    # Negative cases
    ("11 22 63 - Temporada 1 [HDTV][Cap.103][Español Castellano]", None),
    ("September 30 1955 1977 1080p BluRay", None),
    ("11-11-11.2011.1080p.BluRay.x264.DTS-FGT", None),
])
def test_date_detection(parser, release_name, expected_date):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_date:
        assert "date" in result, f"Date key missing in result for {release_name}"
        assert result["date"] == expected_date, f"Incorrect date detected for {release_name}"
    else:
        assert "date" not in result, f"Incorrectly detected date for {release_name}"
