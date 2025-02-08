import pytest

from PTT.handlers import add_defaults
from PTT.parse import Parser


@pytest.fixture
def parser():
    p = Parser()
    add_defaults(p)
    return p


@pytest.mark.parametrize("release_name, expected_date, expected_year", [
    # ("Stephen Colbert 2019 10 25 Eddie Murphy 480p x264-mSD [eztv]", "2019-10-25", "2019"),
    # ("Jimmy.Fallon.2020.02.14.Steve.Buscemi.WEB.x264-XLF[TGx]", "2020-02-14", "2020"),
    # ("The Young And The Restless - S43 E10986 - 2016-08-12", "2016-08-12", "2016"),
    # ("Indias Best Dramebaaz 2 Ep 19 (13 Feb 2016) HDTV x264-AquoTube", "2016-02-13", "2016"),
    # ("07 2015 YR/YR 07-06-15.mp4", "2015-07-06", "2015"),
    # ("SIX.S01E05.400p.229mb.hdtv.x264-][ Collateral ][ 16-Feb-2017 mp4", "2017-02-16", "2017"),
    # ("WWE Smackdown - 11/21/17 - 21st November 2017 - Full Show", "2017-11-21", "2017"),
    # ("WWE RAW 9th Dec 2019 WEBRip h264-TJ [TJET]", "2019-12-09", "2019"),
    # ("EastEnders_20200116_19302000.mp4", "2020-01-16", "2020"),
    # ("AEW DARK 4th December 2020 WEBRip h264-TJ", "2020-12-04", "2020"),
    # ("WWE NXT 30th Sept 2020 WEBRip h264-TJ", "2020-09-30", "2020"),
    # ("WWE Main Event 6th August 2020 WEBRip h264-TJ", "2020-08-06", "2020"),
    # ("wwf.raw.is.war.18.09.00.avi", "2000-09-18", "2000"),
    ("Arsenal - Newcastle United 07.01.2025.mkv", "2025-01-07", "2025"),
    # ("Arsenal - Newcastle United 2025.01.07.mkv", "2025-01-07", "2025"),
    # Negative cases
    # ("11 22 63 - Temporada 1 [HDTV][Cap.103][Español Castellano]", None, None),
])
def test_date_detection(parser, release_name, expected_date, expected_year):
    result = parser.parse(release_name)
    assert isinstance(result, dict), f"Parser did not return a dict for {release_name}"
    if expected_date:
        assert "date" in result, f"Date key missing in result for {release_name}"
        assert result["date"] == expected_date, f"Incorrect date detected for {release_name}"
        assert result["year"] == expected_year, f"Incorrect year detected for {release_name}"
    else:
        assert "date" not in result, f"Incorrectly detected date for {release_name}"
        assert "year" not in result, f"Incorrectly detected year for {release_name}"
