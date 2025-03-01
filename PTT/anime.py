import regex

from PTT.parse import Parser
from PTT.transformers import boolean


def anime_handler(parser: Parser):
    """Anime handlers."""
    # Episode Code
    parser.add_handler("anime", regex.compile(r"\b\[([A-F0-9]{8})\]\b", regex.IGNORECASE), boolean, {"remove": True})

    # Anime type check
    parser.add_handler("anime", regex.compile(r"\[Yameii\]|-Yameii\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Legion\]|-Legion\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[sam\]|-sam\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(LostYears)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Spark\]|-Spark\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(HorribleRips)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(HorribleSubs)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(SubsPlease)\b", regex.IGNORECASE), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[EMBER\]|-EMBER\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Judas\]|-Judas"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Tsundere\]|-Tsundere(?!-)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(BlueLobster)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Erai-raws)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[GHOST\]|-GHOST\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(?:Ani(?:me|s)|[Аа]ниме)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Aergia\]|-Aergia(?!-raws)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Arg0)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(LYS1TH3A)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(OZR)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(SCY)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[smol\]|-smol\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Vanilla\]|-Vanilla\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Vodes\]|(?<!Not)-Vodes\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(ZeroBuild)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(0x539)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Alt\]|-Alt\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[ARC\]|-ARC\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Arid\]|-Arid\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(aro)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Baws)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(BKC)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Brrrrrrr)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Chotab)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Crow\]|-Crow\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(CUNNY)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(CsS)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(D-Z0N3)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Dae)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Datte13)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Drag\]|-Drag\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(FLFL)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(hydes)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(iKaos)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(JySzE)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Lulu\]|-Lulu\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Matsya)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(MC)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Metal\]|-Metal\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(MTBB)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Not-Vodes\]|-Not-Vodes\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Noyr)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(NSDAB)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Okay-Subs)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(pog42)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(pyroneko)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(RAI)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Reza)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Shimatta)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Smoke\]|-Smoke\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Spirale)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Thighs\]|-Thighs\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(UDF)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Yuki\]|-Yuki\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(torenter69)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Golumpa)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(KamiFS)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[AC\]|-AC$"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(ASC)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(AssMix)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Ayashii\]|-Ayashii\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(CBT)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(CTR)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(CyC)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Dekinai\]|-Dekinai\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[EXP\]|-EXP\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Galator)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(GSK[._-]kun)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Holomux)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(IK)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(AnimeKaizoku)\b|\[Kaizoku\]|-Kaizoku\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Kametsu)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(KH)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(kuchikirukia)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(LazyRemux)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(MK)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Mysteria\]|-Mysteria\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Netaro)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Pn8)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Pookie)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Quetzal)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Rasetsu)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Senjou\]|-Senjou\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(ShowY)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(WBDP)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(WSE)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Yoghurt)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[YURI\]|-YURI\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(ZOIO)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(ANThELIa)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(AP)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(BluDragon)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(D4C)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Dragon-Releases)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(E[.-]N[.-]D)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(KAWAiREMUX)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(MKVULTRA)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Raizel)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(REVO)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(SRLS)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(TTGA)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(ZR)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Afro\]|-Afro\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Akai\]|-Akai\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Almighty\]|-Almighty\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[ANE\]|-ANE$"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Asenshi)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(BlurayDesuYo)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Bunny-Apocalypse)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[CH\]|-CH\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(EJF)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Exiled-Destiny|E-D)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(FFF)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Final8)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(GS)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Harunatsu\]|-Harunatsu\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Impatience\]|-Impatience\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Inka-Subs)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Judgment\]|-Judgment\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Kantai\]|-Kantai\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(LCE)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Licca)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Nii-sama\]|-Nii-sama\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(niizk)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Nishi-Taku)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(OnDeed)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(orz)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(PAS)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(peachflavored)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Saizen)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(SCP-2223)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(SHiN-gx)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(SmugCat)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Soldado\]|-Soldado\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Sushi\]|-Sushi\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Vivid\]|-Vivid\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Watashi\]|-Watashi\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Yabai\]|-Yabai\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Zurako)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(A-L)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(ANiHLS)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(CBM)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(DHD)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(DragsterPS)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(HAiKU)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Hark0N)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(iAHD)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(inid4c)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(MCR)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[NPC\]|-NPC\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(RedBlade)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(RH)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(SEV)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[STRiFE\]|-STRiFE\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(TENEIGHTY)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(WaLMaRT)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(AkihitoSubs)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Arukoru)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[EDGE\]|-EDGE\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[naiyas\]|-naiyas\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Nep[ ._-]Blanc)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Prof\]|-Prof\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Shirσ)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[YURASUKA\]|-YURASUKA\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(GST)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(KAN3D2M)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(KS|KiyoshiStar)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Lia\]|-Lia\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(NanDesuKa)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(URANIME)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(VARYG)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[ZigZag\]|-ZigZag\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(9volt)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(GJM)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Kaleido)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(SobsPlease)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Asenshi)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Chihiro\]|-Chihiro\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Commie)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(DameDesuYo)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[Doki\]|-Doki\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Asuka[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Beatrice[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Daddy[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Fumi[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Iriza[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Kawaiika[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\[km\]|-km\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Koi[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Lilith[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"LowPower[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Moozzi2)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Nanako[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"NC[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"neko[ ._-]?(raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"New[ ._-]?(raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Ohys[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Pandoratv[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(Raws-Maji)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"\b(ReinForce)\b"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Scryous[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Seicher[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
    parser.add_handler("anime", regex.compile(r"Shiniori[ ._-]?(Raws)"), boolean, {"remove": False, "skipIfAlreadyFound": True})
