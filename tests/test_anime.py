# import pytest

# from PTT import parse_title


# @pytest.mark.parametrize("release_name, expected_anime", [
#     ("Sword.Art.Online.Alternative.S01.v2.1080p.Blu-Ray.10-Bit.Dual-Audio.LPCM.x265-iAHD", True),
#     ("[SubsPlease] Tearmoon Teikoku Monogatari - 01 (1080p) [15ADAE00].mkv", True),
#     ("[SubsPlease] Fairy Tail - 100 Years Quest - 05 (1080p) [1107F3A9].mkv", True),
#     ("[Erai-raws] Tearmoon Teikoku Monogatari - 01 [1080p][Multiple Subtitle] [ENG][POR-BR][SPA-LA][SPA][ARA][FRE][GER][ITA][RUS]", True),
#     ("Hunter x Hunter (2011) - 01 [1080p][Multiple Subtitle] [ENG][POR-BR][SPA-LA][SPA][ARA][FRE][GER][ITA][RUS]", True),
#     ("Naruto Shippuden (001-500) [Complete Series + Movies] (Dual Audio)", True),
#     ("[Erai-raws] Sword Art Online Alternative - Gun Gale Online - 10 [720p][Multiple Subtitle].mkv", True),
#     ("One.Piece.S01E1116.Lets.Go.Get.It!.Buggys.Big.Declaration.2160p.B-Global.WEB-DL.JPN.AAC2.0.H.264.MSubs-ToonsHub.mkv", True),
#     ("[Erai-raws] 2-5 Jigen no Ririsa - 08 [480p][Multiple Subtitle][972D0669].mkv", True),
#     ("[Exiled-Destiny]_Tokyo_Underground_Ep02v2_(41858470).mkv", True)
# ])
# def test_random_anime_parse(release_name, expected_anime):
#     result = parse_title(release_name)
#     if expected_anime:
#         assert result["anime"] is True
#     else:
#         assert result["anime"] is False
