# characters.py
# File ini bertugas membangun Binary Decision Tree untuk game Akinator
# Setiap LEAF NODE = 1 karakter yang bisa ditebak oleh Akinator
# Setiap INTERNAL NODE = pertanyaan Ya/Tidak yang mengarahkan ke karakter


from tree import Node, DecisionTree


def build_character_tree():
    """
    Membangun dan mengembalikan Binary Decision Tree berisi 65 karakter.

    Cara membaca tree ini:
    - node.yes  → cabang yang diambil jika user menjawab "Ya"
    - node.no   → cabang yang diambil jika user menjawab "Tidak"
    - Leaf node → node tanpa pertanyaan, hanya berisi nama karakter (tebakan akhir)
    """

    # ══════════════════════════════════════════════════════════════════
    # BAGIAN 1 — LEAF NODES (DAUN POHON)
    # Ini adalah node paling bawah / ujung dari tree.
    # Tidak punya cabang yes/no, langsung berisi nama karakter.
    # ══════════════════════════════════════════════════════════════════

    # ── Resident Evil ──────────────────────────────────────────────────
    daun_leon          = Node(character="Leon S. Kennedy")
    daun_chris         = Node(character="Chris Redfield")
    daun_jill          = Node(character="Jill Valentine")
    daun_ada           = Node(character="Ada Wong")
    daun_wesker        = Node(character="Albert Wesker")

    # ── Honkai: Star Rail ──────────────────────────────────────────────
    daun_acheron       = Node(character="Acheron")
    daun_kafka         = Node(character="Kafka")
    daun_dan_heng      = Node(character="Dan Heng")
    daun_march         = Node(character="March 7th")
    daun_jing_yuan     = Node(character="Jing Yuan")

    # ── Red Dead Redemption ────────────────────────────────────────────
    daun_arthur        = Node(character="Arthur Morgan")
    daun_john_marston  = Node(character="John Marston")
    daun_dutch         = Node(character="Dutch van der Linde")
    daun_sadie         = Node(character="Sadie Adler")
    daun_micah         = Node(character="Micah Bell")

    # ── Uma Musume: Pretty Derby ────────────────────────────────────────
    daun_agnes         = Node(character="Agnes Tachyon")
    daun_special_week  = Node(character="Special Week")
    daun_suzuka        = Node(character="Silence Suzuka")
    daun_tokai         = Node(character="Tokai Teio")
    daun_gold_ship     = Node(character="Gold Ship")

    # ── Crash Bandicoot ────────────────────────────────────────────────
    daun_crash         = Node(character="Crash Bandicoot")
    daun_coco          = Node(character="Coco Bandicoot")
    daun_neo_cortex    = Node(character="Dr. Neo Cortex")
    daun_aku_aku       = Node(character="Aku Aku")
    daun_dingodile     = Node(character="Dingodile")

    # ── Devil May Cry ──────────────────────────────────────────────────
    daun_vergil        = Node(character="Vergil")
    daun_dante         = Node(character="Dante")
    daun_nero          = Node(character="Nero")
    daun_trish         = Node(character="Trish")
    daun_lady          = Node(character="Lady")

    # ── Assassin's Creed ───────────────────────────────────────────────
    daun_ezio          = Node(character="Ezio Auditore")
    daun_altair        = Node(character="Altaïr Ibn-La'Ahad")
    daun_desmond       = Node(character="Desmond Miles")
    daun_edward        = Node(character="Edward Kenway")
    daun_connor        = Node(character="Connor Kenway")

    # ── NieR: Automata ─────────────────────────────────────────────────
    daun_2b            = Node(character="2B")
    daun_9s            = Node(character="9S")
    daun_a2            = Node(character="A2")
    daun_pascal        = Node(character="Pascal")
    daun_emil          = Node(character="Emil")

    # ── Tekken ─────────────────────────────────────────────────────────
    daun_kazuya        = Node(character="Kazuya Mishima")
    daun_jin           = Node(character="Jin Kazama")
    daun_heihachi      = Node(character="Heihachi Mishima")
    daun_nina          = Node(character="Nina Williams")
    daun_yoshimitsu    = Node(character="Yoshimitsu")

    # ── Tomb Raider ────────────────────────────────────────────────────
    daun_lara          = Node(character="Lara Croft")
    daun_winston       = Node(character="Winston Smith")
    daun_jonah         = Node(character="Jonah Maiava")
    daun_natla         = Node(character="Jacqueline Natla")
    daun_amanda        = Node(character="Amanda Evert")

    # ── Call of Duty: Modern Warfare ───────────────────────────────────
    daun_price         = Node(character="John Price")
    daun_ghost         = Node(character="Ghost")
    daun_soap          = Node(character="John \"Soap\" MacTavish")
    daun_gaz           = Node(character="Kyle \"Gaz\" Garrick")
    daun_makarov       = Node(character="Vladimir Makarov")

    # ── Mortal Kombat ──────────────────────────────────────────────────
    daun_scorpion      = Node(character="Scorpion")
    daun_sub_zero      = Node(character="Sub-Zero")
    daun_liu_kang      = Node(character="Liu Kang")
    daun_johnny_cage   = Node(character="Johnny Cage")
    daun_baraka        = Node(character="Baraka")

    # ── God of War ─────────────────────────────────────────────────────
    daun_kratos        = Node(character="Kratos")
    daun_atreus        = Node(character="Atreus")
    daun_mimir         = Node(character="Mimir")
    daun_freya         = Node(character="Freya")
    daun_baldur        = Node(character="Baldur")


    # ══════════════════════════════════════════════════════════════════
    # BAGIAN 2 — INTERNAL NODES (PERTANYAAN)
    # Dibangun dari bawah ke atas, per franchise.
    # Setiap node internal punya:
    #   .yes → cabang jika user jawab "Ya"
    #   .no  → cabang jika user jawab "Tidak"
    # ══════════════════════════════════════════════════════════════════


    # ─────────────────────────────────────────────────────────────────
    # CABANG: MORTAL KOMBAT (5 karakter)
    # Alur: ninja? → biru/es? → sub_zero / scorpion
    #              → biksu api? → liu_kang
    #                           → gigi tarkatan? → baraka / johnny_cage
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Sub-Zero vs Scorpion
    mk_tanya_warna_biru = Node(question="Apakah kostum atau auranya identik dengan warna biru / es?")
    mk_tanya_warna_biru.yes = daun_sub_zero    # Ya  → Sub-Zero (ninja biru/es)
    mk_tanya_warna_biru.no  = daun_scorpion    # Tidak → Scorpion (ninja kuning/api)

    # Pertanyaan untuk membedakan Baraka vs Johnny Cage (bukan ninja)
    mk_tanya_tarkatan = Node(question="Apakah dia memiliki gigi panjang menjijikkan / pisau yang keluar dari tangannya (ras Tarkatan)?")
    mk_tanya_tarkatan.yes = daun_baraka        # Ya  → Baraka (ras Tarkatan)
    mk_tanya_tarkatan.no  = daun_johnny_cage   # Tidak → Johnny Cage (aktor/petarung)

    # Pertanyaan untuk membedakan Liu Kang vs sisanya
    mk_tanya_biksu_api = Node(question="Apakah dia seorang petarung bergelar Earthrealm Champion dengan elemen api?")
    mk_tanya_biksu_api.yes = daun_liu_kang     # Ya  → Liu Kang (biksu api)
    mk_tanya_biksu_api.no  = mk_tanya_tarkatan # Tidak → lanjut tanya Baraka vs Johnny

    # ROOT cabang Mortal Kombat: pertanyaan pemisah pertama
    mk_root = Node(question="Apakah dia seorang ninja atau memakai penutup wajah ala ninja?")
    mk_root.yes = mk_tanya_warna_biru          # Ya  → ninja → tanya warna
    mk_root.no  = mk_tanya_biksu_api           # Tidak → bukan ninja → tanya api/tarkatan


    # ─────────────────────────────────────────────────────────────────
    # CABANG: TEKKEN (5 karakter)
    # Alur: perempuan? → nina
    #                  → pedang robot? → yoshimitsu
    #                                  → kakek botak? → heihachi
    #                                                 → bisa devil? → kazuya / jin
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Kazuya vs Jin
    tekken_tanya_kazuya_vs_jin = Node(question="Apakah dia bisa berubah menjadi Devil dan sangat membenci ayahnya (Heihachi)?")
    tekken_tanya_kazuya_vs_jin.yes = daun_kazuya   # Ya  → Kazuya (Devil Gene, benci Heihachi)
    tekken_tanya_kazuya_vs_jin.no  = daun_jin       # Tidak → Jin Kazama

    # Pertanyaan untuk membedakan Heihachi vs Kazuya/Jin
    tekken_tanya_heihachi = Node(question="Apakah dia kakek tua ahli bela diri dengan potongan rambut botak di tengah?")
    tekken_tanya_heihachi.yes = daun_heihachi           # Ya  → Heihachi
    tekken_tanya_heihachi.no  = tekken_tanya_kazuya_vs_jin  # Tidak → tanya Kazuya vs Jin

    # Pertanyaan untuk membedakan Yoshimitsu vs Mishima keluarga
    tekken_tanya_yoshimitsu = Node(question="Apakah dia menggunakan pedang dan memakai armor canggih seperti robot atau alien?")
    tekken_tanya_yoshimitsu.yes = daun_yoshimitsu   # Ya  → Yoshimitsu
    tekken_tanya_yoshimitsu.no  = tekken_tanya_heihachi  # Tidak → tanya Heihachi dst.

    # ROOT cabang Tekken: perempuan atau bukan?
    tekken_root = Node(question="Apakah tokoh ini adalah seorang perempuan pembunuh bayaran?")
    tekken_root.yes = daun_nina                # Ya  → Nina Williams
    tekken_root.no  = tekken_tanya_yoshimitsu  # Tidak → lanjut tanya Yoshimitsu dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: RESIDENT EVIL (5 karakter)
    # Alur: perempuan? → gaun merah? → ada_wong / jill
    #                 → kacamata hitam villain? → wesker
    #                                           → poni belah tengah? → leon / chris
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Ada Wong vs Jill Valentine (sama-sama perempuan)
    re_tanya_ada_vs_jill = Node(question="Apakah dia identik dengan gaun merah dan bekerja sebagai agen rahasia misterius?")
    re_tanya_ada_vs_jill.yes = daun_ada        # Ya  → Ada Wong (gaun merah, agen)
    re_tanya_ada_vs_jill.no  = daun_jill       # Tidak → Jill Valentine (STARS/BSAA)

    # Pertanyaan untuk membedakan Leon vs Chris (sama-sama laki-laki hero)
    re_tanya_leon_vs_chris = Node(question="Apakah rambutnya berponi belah tengah yang khas (gaya rambut Leon)?")
    re_tanya_leon_vs_chris.yes = daun_leon     # Ya  → Leon S. Kennedy
    re_tanya_leon_vs_chris.no  = daun_chris    # Tidak → Chris Redfield

    # Pertanyaan untuk membedakan Wesker (villain) vs Leon/Chris (hero)
    re_tanya_wesker = Node(question="Apakah dia memakai kacamata hitam dan merupakan antagonis/villain utama?")
    re_tanya_wesker.yes = daun_wesker           # Ya  → Albert Wesker
    re_tanya_wesker.no  = re_tanya_leon_vs_chris  # Tidak → tanya Leon vs Chris

    # ROOT cabang Resident Evil: perempuan atau laki-laki?
    re_root = Node(question="Apakah tokoh ini adalah karakter perempuan?")
    re_root.yes = re_tanya_ada_vs_jill  # Ya  → perempuan → tanya Ada vs Jill
    re_root.no  = re_tanya_wesker       # Tidak → laki-laki → tanya Wesker dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: CALL OF DUTY (5 karakter)
    # Alur: villain rusia? → makarov
    #                      → topeng tengkorak? → ghost
    #                                          → dipanggil Soap? → soap
    #                                                            → topi boonie kumis? → price / gaz
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Price vs Gaz (keduanya hero tanpa ciri khas unik)
    cod_tanya_price_vs_gaz = Node(question="Apakah dia kapten yang selalu memakai topi boonie dan berkumis tebal?")
    cod_tanya_price_vs_gaz.yes = daun_price    # Ya  → Captain John Price
    cod_tanya_price_vs_gaz.no  = daun_gaz      # Tidak → Kyle "Gaz" Garrick

    # Pertanyaan untuk membedakan Soap vs Price/Gaz
    cod_tanya_soap = Node(question="Apakah dia dipanggil 'Soap' dan dikenal dengan gaya rambut cepak atau mohawk?")
    cod_tanya_soap.yes = daun_soap             # Ya  → John "Soap" MacTavish
    cod_tanya_soap.no  = cod_tanya_price_vs_gaz  # Tidak → tanya Price vs Gaz

    # Pertanyaan untuk membedakan Ghost (topeng tengkorak) vs yang lain
    cod_tanya_ghost = Node(question="Apakah dia selalu memakai topeng bermotif tengkorak dan sangat misterius?")
    cod_tanya_ghost.yes = daun_ghost           # Ya  → Ghost (Simon "Ghost" Riley)
    cod_tanya_ghost.no  = cod_tanya_soap       # Tidak → tanya Soap dst.

    # ROOT cabang CoD: villain atau hero?
    cod_root = Node(question="Apakah dia merupakan pimpinan teroris berbahaya asal Rusia (Antagonis utama)?")
    cod_root.yes = daun_makarov    # Ya  → Vladimir Makarov
    cod_root.no  = cod_tanya_ghost # Tidak → lanjut tanya Ghost dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: UMA MUSUME: PRETTY DERBY (5 karakter)
    # Alur: ilmuwan nyentrik? → agnes
    #                        → rambut putih onar? → gold_ship
    #                                             → rambut coklat poni putih? → special_week
    #                                                                         → rambut orange? → suzuka / tokai
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Silence Suzuka vs Tokai Teio
    uma_tanya_suzuka_vs_tokai = Node(question="Apakah rambutnya dominan warna orange terang dengan poni?")
    uma_tanya_suzuka_vs_tokai.yes = daun_suzuka    # Ya  → Silence Suzuka (rambut orange)
    uma_tanya_suzuka_vs_tokai.no  = daun_tokai     # Tidak → Tokai Teio

    # Pertanyaan untuk membedakan Special Week vs Suzuka/Tokai
    uma_tanya_special_week = Node(question="Apakah dia karakter utama berambut coklat dengan sejumput rambut putih unik di dahi?")
    uma_tanya_special_week.yes = daun_special_week       # Ya  → Special Week
    uma_tanya_special_week.no  = uma_tanya_suzuka_vs_tokai  # Tidak → tanya Suzuka vs Tokai

    # Pertanyaan untuk membedakan Gold Ship vs yang lain
    uma_tanya_gold_ship = Node(question="Apakah rambutnya putih/silver dan dijuluki si pembuat onar (Gold Ship)?")
    uma_tanya_gold_ship.yes = daun_gold_ship       # Ya  → Gold Ship
    uma_tanya_gold_ship.no  = uma_tanya_special_week  # Tidak → tanya Special Week dst.

    # ROOT cabang Uma Musume: ilmuwan atau kuda idol biasa?
    uma_root = Node(question="Apakah dia ilmuwan jenius/nyentrik yang sering membawa tabung reaksi?")
    uma_root.yes = daun_agnes          # Ya  → Agnes Tachyon
    uma_root.no  = uma_tanya_gold_ship # Tidak → lanjut tanya Gold Ship dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: HONKAI: STAR RAIL (5 karakter)
    # Alur: laki-laki? → memimpin Luofu + petir? → jing_yuan / dan_heng
    #                 → pedang kilat ungu? → acheron
    #                                      → dual SMG jaket kulit? → kafka / march
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Jing Yuan vs Dan Heng (sama-sama laki-laki)
    hsr_tanya_jing_vs_dan = Node(question="Apakah dia pemimpin pasukan Luofu yang memiliki elemen Lightning (Petir)?")
    hsr_tanya_jing_vs_dan.yes = daun_jing_yuan  # Ya  → Jing Yuan
    hsr_tanya_jing_vs_dan.no  = daun_dan_heng   # Tidak → Dan Heng

    # Pertanyaan untuk membedakan Kafka vs March 7th (sama-sama perempuan bukan Acheron)
    hsr_tanya_kafka_vs_march = Node(question="Apakah dia menggunakan senjata api ganda (Dual SMG) dan berjaket kulit?")
    hsr_tanya_kafka_vs_march.yes = daun_kafka   # Ya  → Kafka
    hsr_tanya_kafka_vs_march.no  = daun_march   # Tidak → March 7th

    # Pertanyaan untuk membedakan Acheron vs Kafka/March (sama-sama perempuan)
    hsr_tanya_acheron = Node(question="Apakah dia membawa pedang panjang dengan elemen kilat ungu gelap?")
    hsr_tanya_acheron.yes = daun_acheron             # Ya  → Acheron
    hsr_tanya_acheron.no  = hsr_tanya_kafka_vs_march # Tidak → tanya Kafka vs March

    # ROOT cabang Honkai Star Rail: laki-laki atau perempuan?
    hsr_root = Node(question="Apakah tokoh ini adalah laki-laki?")
    hsr_root.yes = hsr_tanya_jing_vs_dan  # Ya  → laki-laki → tanya Jing vs Dan
    hsr_root.no  = hsr_tanya_acheron      # Tidak → perempuan → tanya Acheron dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: GOD OF WAR (5 karakter)
    # Alur: kepala terpenggal/bijaksana? → mimir
    #                                   → kepala botak tato merah? → kratos
    #                                                              → anak laki panah? → atreus
    #                                                                                → dewi sihir? → freya / baldur
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Freya vs Baldur
    gow_tanya_freya_vs_baldur = Node(question="Apakah dia Dewi perempuan yang menguasai sihir Vanir?")
    gow_tanya_freya_vs_baldur.yes = daun_freya   # Ya  → Freya
    gow_tanya_freya_vs_baldur.no  = daun_baldur  # Tidak → Baldur

    # Pertanyaan untuk membedakan Atreus vs Freya/Baldur
    gow_tanya_atreus = Node(question="Apakah dia anak kecil/remaja laki-laki yang membawa busur panah?")
    gow_tanya_atreus.yes = daun_atreus               # Ya  → Atreus
    gow_tanya_atreus.no  = gow_tanya_freya_vs_baldur # Tidak → tanya Freya vs Baldur

    # Pertanyaan untuk membedakan Kratos vs yang lain
    gow_tanya_kratos = Node(question="Apakah dia dewa perang berkepala botak dengan tato merah tebal di sekujur tubuhnya?")
    gow_tanya_kratos.yes = daun_kratos       # Ya  → Kratos
    gow_tanya_kratos.no  = gow_tanya_atreus  # Tidak → tanya Atreus dst.

    # ROOT cabang God of War: kepala terpenggal bijaksana atau bukan?
    gow_root = Node(question="Apakah dia berupa kepala terpenggal yang bijaksana dan selalu menemani perjalanan?")
    gow_root.yes = daun_mimir       # Ya  → Mimir
    gow_root.no  = gow_tanya_kratos # Tidak → tanya Kratos dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: NIER: AUTOMATA (5 karakter)
    # Alur: wujud mesin aneh? → tengkorak bulat? → emil / pascal
    #                        → android laki? → 9s
    #                                        → blindfold? → 2b / a2
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Emil vs Pascal (sama-sama "mesin aneh")
    nier_tanya_emil_vs_pascal = Node(question="Apakah dia berbentuk kepala tengkorak bulat besar yang sering menyeringai?")
    nier_tanya_emil_vs_pascal.yes = daun_emil   # Ya  → Emil
    nier_tanya_emil_vs_pascal.no  = daun_pascal # Tidak → Pascal

    # Pertanyaan untuk membedakan 2B vs A2 (sama-sama android perempuan)
    nier_tanya_2b_vs_a2 = Node(question="Apakah dia android perempuan berambut putih pendek yang memakai blindfold (penutup mata)?")
    nier_tanya_2b_vs_a2.yes = daun_2b   # Ya  → 2B (rambut pendek, blindfold)
    nier_tanya_2b_vs_a2.no  = daun_a2   # Tidak → A2 (rambut lebih panjang)

    # Pertanyaan untuk membedakan 9S vs android perempuan
    nier_tanya_9s = Node(question="Apakah dia android laki-laki yang memakai celana pendek dan berperan sebagai Scanner?")
    nier_tanya_9s.yes = daun_9s              # Ya  → 9S
    nier_tanya_9s.no  = nier_tanya_2b_vs_a2 # Tidak → tanya 2B vs A2

    # ROOT cabang NieR: Automata: mesin aneh atau android humanoid?
    nier_root = Node(question="Apakah wujud tubuhnya adalah mesin usang/aneh (bukan bentuk menyerupai manusia)?")
    nier_root.yes = nier_tanya_emil_vs_pascal  # Ya  → mesin aneh → tanya Emil vs Pascal
    nier_root.no  = nier_tanya_9s              # Tidak → android humanoid → tanya 9S dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: DEVIL MAY CRY (5 karakter)
    # Alur: perempuan? → bazooka Kalina Ann? → lady / trish
    #                 → mantel biru + katana? → vergil
    #                                        → mantel merah? → dante / nero
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Lady vs Trish (sama-sama perempuan DMC)
    dmc_tanya_lady_vs_trish = Node(question="Apakah dia membawa senjata berat/bazooka besar bernama Kalina Ann?")
    dmc_tanya_lady_vs_trish.yes = daun_lady   # Ya  → Lady
    dmc_tanya_lady_vs_trish.no  = daun_trish  # Tidak → Trish

    # Pertanyaan untuk membedakan Dante vs Nero (laki-laki bukan Vergil)
    dmc_tanya_dante_vs_nero = Node(question="Apakah dia memakai mantel merah panjang dan bersenjata pedang besar (Rebellion/Sparda)?")
    dmc_tanya_dante_vs_nero.yes = daun_dante  # Ya  → Dante
    dmc_tanya_dante_vs_nero.no  = daun_nero   # Tidak → Nero

    # Pertanyaan untuk membedakan Vergil vs Dante/Nero
    dmc_tanya_vergil = Node(question="Apakah dia memakai mantel biru dan bersenjata katana bernama Yamato?")
    dmc_tanya_vergil.yes = daun_vergil             # Ya  → Vergil
    dmc_tanya_vergil.no  = dmc_tanya_dante_vs_nero # Tidak → tanya Dante vs Nero

    # ROOT cabang Devil May Cry: perempuan atau laki-laki?
    dmc_root = Node(question="Apakah tokoh ini adalah perempuan?")
    dmc_root.yes = dmc_tanya_lady_vs_trish  # Ya  → perempuan → tanya Lady vs Trish
    dmc_root.no  = dmc_tanya_vergil         # Tidak → laki-laki → tanya Vergil dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: RED DEAD REDEMPTION (5 karakter)
    # Alur: perempuan bounty hunter? → sadie
    #                               → pemimpin geng "I have a plan!"? → dutch
    #                                                                 → pengkhianat antagonis? → micah
    #                                                                                         → TBC? → arthur / john
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Arthur vs John Marston
    rdr_tanya_arthur_vs_john = Node(question="Apakah dia protagonis utama game kedua yang menderita penyakit TBC?")
    rdr_tanya_arthur_vs_john.yes = daun_arthur       # Ya  → Arthur Morgan
    rdr_tanya_arthur_vs_john.no  = daun_john_marston # Tidak → John Marston

    # Pertanyaan untuk membedakan Micah vs Arthur/John
    rdr_tanya_micah = Node(question="Apakah dia pengkhianat menyebalkan yang menjadi antagonis utama di game kedua?")
    rdr_tanya_micah.yes = daun_micah                 # Ya  → Micah Bell
    rdr_tanya_micah.no  = rdr_tanya_arthur_vs_john   # Tidak → tanya Arthur vs John

    # Pertanyaan untuk membedakan Dutch vs Micah/Arthur/John
    rdr_tanya_dutch = Node(question="Apakah dia pemimpin geng yang kharismatik dan selalu bilang 'I have a plan!'?")
    rdr_tanya_dutch.yes = daun_dutch      # Ya  → Dutch van der Linde
    rdr_tanya_dutch.no  = rdr_tanya_micah # Tidak → tanya Micah dst.

    # ROOT cabang RDR: perempuan atau laki-laki?
    rdr_root = Node(question="Apakah dia perempuan pejuang (bounty hunter) berambut pirang yang tangguh?")
    rdr_root.yes = daun_sadie     # Ya  → Sadie Adler
    rdr_root.no  = rdr_tanya_dutch # Tidak → lanjut tanya Dutch dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: ASSASSIN'S CREED (5 karakter)
    # Alur: era modern/Animus? → desmond
    #                         → bajak laut Karibia? → edward
    #                                               → penduduk asli Amerika? → connor
    #                                                                        → Renaissance Italia? → ezio / altair
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Ezio vs Altair (keduanya Assassin klasik)
    ac_tanya_ezio_vs_altair = Node(question="Apakah dia Assassin legendaris dari zaman Renaissance Italia?")
    ac_tanya_ezio_vs_altair.yes = daun_ezio    # Ya  → Ezio Auditore
    ac_tanya_ezio_vs_altair.no  = daun_altair  # Tidak → Altaïr (era Perang Salib)

    # Pertanyaan untuk membedakan Connor vs Ezio/Altair
    ac_tanya_connor = Node(question="Apakah dia merupakan ras penduduk asli Amerika (Native American / Mohawk)?")
    ac_tanya_connor.yes = daun_connor             # Ya  → Connor Kenway
    ac_tanya_connor.no  = ac_tanya_ezio_vs_altair # Tidak → tanya Ezio vs Altair

    # Pertanyaan untuk membedakan Edward vs Connor/Ezio/Altair
    ac_tanya_edward = Node(question="Apakah dia seorang Kapten Bajak Laut dari wilayah Karibia?")
    ac_tanya_edward.yes = daun_edward     # Ya  → Edward Kenway
    ac_tanya_edward.no  = ac_tanya_connor # Tidak → tanya Connor dst.

    # ROOT cabang Assassin's Creed: era modern atau era bersejarah?
    ac_root = Node(question="Apakah dia hidup di era modern sebagai subjek tes mesin Animus?")
    ac_root.yes = daun_desmond    # Ya  → Desmond Miles
    ac_root.no  = ac_tanya_edward # Tidak → karakter sejarah → tanya Edward dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: CRASH BANDICOOT (5 karakter)
    # Alur: manusia jahat (huruf N)? → neo_cortex
    #                               → topeng kayu terbang? → aku_aku
    #                                                      → mutan dingo+buaya? → dingodile
    #                                                                           → bandicoot perempuan? → coco / crash
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Coco vs Crash (keduanya bandicoot)
    crash_tanya_coco_vs_crash = Node(question="Apakah dia bandicoot perempuan berambut pirang yang suka membawa laptop?")
    crash_tanya_coco_vs_crash.yes = daun_coco   # Ya  → Coco Bandicoot
    crash_tanya_coco_vs_crash.no  = daun_crash  # Tidak → Crash Bandicoot

    # Pertanyaan untuk membedakan Dingodile vs Coco/Crash
    crash_tanya_dingodile = Node(question="Apakah dia mutan perpaduan Dingo dan Buaya yang membawa penyembur api besar?")
    crash_tanya_dingodile.yes = daun_dingodile          # Ya  → Dingodile
    crash_tanya_dingodile.no  = crash_tanya_coco_vs_crash  # Tidak → tanya Coco vs Crash

    # Pertanyaan untuk membedakan Aku Aku vs yang lain
    crash_tanya_aku_aku = Node(question="Apakah wujudnya hanyalah sebuah topeng kayu terbang ajaib berwarna-warni?")
    crash_tanya_aku_aku.yes = daun_aku_aku        # Ya  → Aku Aku
    crash_tanya_aku_aku.no  = crash_tanya_dingodile  # Tidak → tanya Dingodile dst.

    # ROOT cabang Crash: ilmuwan manusia jahat atau bukan?
    crash_root = Node(question="Apakah dia ilmuwan manusia jahat dengan huruf 'N' besar di dahinya?")
    crash_root.yes = daun_neo_cortex    # Ya  → Dr. Neo Cortex
    crash_root.no  = crash_tanya_aku_aku # Tidak → lanjut tanya Aku Aku dst.


    # ─────────────────────────────────────────────────────────────────
    # CABANG: TOMB RAIDER (5 karakter)
    # Alur: protagonis wanita penjelajah? → lara
    #                                    → antagonis Atlantis? → natla
    #                                                          → musuh dari entitas mistis? → amanda
    #                                                                                       → pelayan tua? → winston / jonah
    # ─────────────────────────────────────────────────────────────────

    # Pertanyaan untuk membedakan Winston vs Jonah
    tr_tanya_winston_vs_jonah = Node(question="Apakah dia pelayan tua (butler) keluarga Croft yang sering dikurung di kulkas?")
    tr_tanya_winston_vs_jonah.yes = daun_winston  # Ya  → Winston Smith
    tr_tanya_winston_vs_jonah.no  = daun_jonah    # Tidak → Jonah Maiava

    # Pertanyaan untuk membedakan Amanda vs Winston/Jonah
    tr_tanya_amanda = Node(question="Apakah dia teman masa lalu Lara yang kembali sebagai musuh dengan menggunakan entitas mistis?")
    tr_tanya_amanda.yes = daun_amanda                # Ya  → Amanda Evert
    tr_tanya_amanda.no  = tr_tanya_winston_vs_jonah  # Tidak → tanya Winston vs Jonah

    # Pertanyaan untuk membedakan Natla vs Amanda/Winston/Jonah
    tr_tanya_natla = Node(question="Apakah dia antagonis abadi dan penguasa ras purba dari Atlantis?")
    tr_tanya_natla.yes = daun_natla     # Ya  → Jacqueline Natla
    tr_tanya_natla.no  = tr_tanya_amanda  # Tidak → tanya Amanda dst.

    # ROOT cabang Tomb Raider: protagonis utama atau karakter pendukung?
    tr_root = Node(question="Apakah dia protagonis utamanya (wanita penjelajah makam yang ikonik)?")
    tr_root.yes = daun_lara      # Ya  → Lara Croft
    tr_root.no  = tr_tanya_natla # Tidak → lanjut tanya Natla dst.


    # ══════════════════════════════════════════════════════════════════
    # BAGIAN 3 — ROUTING UTAMA / ROOT NODE
    # Ini adalah pertanyaan-pertanyaan paling awal yang menentukan
    # user akan diarahkan ke franchise mana (cabang mana di tree).
    # Dibangun dari level terdalam ke level teratas.
    # ══════════════════════════════════════════════════════════════════

    # ── Level 3: Pemisah dalam kategori Fighting, Shooter, dll ────────

    # Pemisah dalam kategori Fighting: MK vs Tekken
    routing_fighting_mk_vs_tekken = Node(question="Apakah franchise gamenya sangat brutal, sadis, dan identik dengan gerakan 'Fatality'?")
    routing_fighting_mk_vs_tekken.yes = mk_root      # Ya  → Mortal Kombat
    routing_fighting_mk_vs_tekken.no  = tekken_root  # Tidak → Tekken

    # Pemisah dalam kategori Shooter: RE vs CoD
    routing_shooter_re_vs_cod = Node(question="Apakah game shooter ini bertema horor kelangsungan hidup (survival horror / membasmi zombie)?")
    routing_shooter_re_vs_cod.yes = re_root   # Ya  → Resident Evil
    routing_shooter_re_vs_cod.no  = cod_root  # Tidak → Call of Duty

    # Pemisah dalam kategori Anime/Gacha: Uma Musume vs Honkai
    routing_gacha_uma_vs_hsr = Node(question="Apakah inti dari game tersebut berfokus pada balapan gadis kuda idol?")
    routing_gacha_uma_vs_hsr.yes = uma_root  # Ya  → Uma Musume: Pretty Derby
    routing_gacha_uma_vs_hsr.no  = hsr_root  # Tidak → Honkai: Star Rail

    # Pemisah dalam kategori Hack & Slash: NieR vs DMC
    routing_hackslash_nier_vs_dmc = Node(question="Apakah karakter/semesta di gamenya difokuskan pada Android dan Mesin buatan manusia?")
    routing_hackslash_nier_vs_dmc.yes = nier_root  # Ya  → NieR: Automata
    routing_hackslash_nier_vs_dmc.no  = dmc_root   # Tidak → Devil May Cry

    # Pemisah dalam kategori Hack & Slash: GoW vs NieR/DMC
    routing_hackslash_gow_vs_sisanya = Node(question="Apakah gamenya berlatar belakang mitologi Dewa-dewa kuno (Yunani / Nordik)?")
    routing_hackslash_gow_vs_sisanya.yes = gow_root                 # Ya  → God of War
    routing_hackslash_gow_vs_sisanya.no  = routing_hackslash_nier_vs_dmc  # Tidak → NieR atau DMC

    # Pemisah dalam kategori History/Open World: RDR vs AC
    routing_history_rdr_vs_ac = Node(question="Apakah gamenya memiliki tema Wild West / Koboi Amerika?")
    routing_history_rdr_vs_ac.yes = rdr_root  # Ya  → Red Dead Redemption
    routing_history_rdr_vs_ac.no  = ac_root   # Tidak → Assassin's Creed

    # Pemisah antara Crash Bandicoot vs Tomb Raider (keduanya bukan kategori besar di atas)
    routing_platformer_crash_vs_tr = Node(question="Apakah karakternya merupakan hewan antropomorfik / tokoh platformer klasik era PS1?")
    routing_platformer_crash_vs_tr.yes = crash_root  # Ya  → Crash Bandicoot
    routing_platformer_crash_vs_tr.no  = tr_root     # Tidak → Tomb Raider

    # ── Level 2: Pemisah Kategori Besar ───────────────────────────────

    # Apakah dari game sejarah / open world? → RDR atau AC; jika tidak → Crash atau TR
    routing_history_vs_platformer = Node(question="Apakah game tersebut mengambil inspirasi kuat dari sejarah dunia nyata (zaman kuno / era koboi)?")
    routing_history_vs_platformer.yes = routing_history_rdr_vs_ac       # Ya  → ke cabang sejarah
    routing_history_vs_platformer.no  = routing_platformer_crash_vs_tr  # Tidak → ke cabang platformer/TR

    # Apakah dari game Hack & Slash? → GoW/NieR/DMC; jika tidak → sejarah atau platformer
    routing_hackslash_vs_sisanya = Node(question="Apakah karakter ini berasal dari game aksi 'Hack and Slash' yang menggunakan kombo jarak dekat?")
    routing_hackslash_vs_sisanya.yes = routing_hackslash_gow_vs_sisanya  # Ya  → GoW, NieR, atau DMC
    routing_hackslash_vs_sisanya.no  = routing_history_vs_platformer     # Tidak → sejarah atau platformer

    # Apakah dari game Anime/Gacha? → Uma atau HSR; jika tidak → Hack & Slash dst.
    routing_gacha_vs_sisanya = Node(question="Apakah karakter ini memiliki grafis ala Anime dan berasal dari game Gacha buatan Asia?")
    routing_gacha_vs_sisanya.yes = routing_gacha_uma_vs_hsr    # Ya  → Uma atau HSR
    routing_gacha_vs_sisanya.no  = routing_hackslash_vs_sisanya  # Tidak → Hack & Slash dst.

    # Apakah dari game Shooter? → RE atau CoD; jika tidak → Gacha atau lainnya
    routing_shooter_vs_sisanya = Node(question="Apakah karakter ini dominan bertarung menggunakan senjata api militer (Shooter FPS/TPS)?")
    routing_shooter_vs_sisanya.yes = routing_shooter_re_vs_cod  # Ya  → RE atau CoD
    routing_shooter_vs_sisanya.no  = routing_gacha_vs_sisanya   # Tidak → Gacha atau lainnya

    # ── Level 1: ROOT NODE — pertanyaan PERTAMA yang ditampilkan ke user ──
    root = Node(question="Apakah karakter ini berasal dari game pertarungan 1 lawan 1 (Fighting Game Arena)?")
    root.yes = routing_fighting_mk_vs_tekken  # Ya  → Fighting → MK atau Tekken
    root.no  = routing_shooter_vs_sisanya     # Tidak → bukan fighting → lanjut tanya


    # ══════════════════════════════════════════════════════════════════
    # BAGIAN 4 — BUILD DAN RETURN TREE
    # Setelah semua node terhubung, masukkan root ke dalam DecisionTree
    # lalu kembalikan objek tree agar bisa digunakan di game.py
    # ══════════════════════════════════════════════════════════════════
    tree = DecisionTree()
    tree.build(root)  # Set root node sebagai titik awal traversal
    return tree       # Kembalikan tree yang sudah jadi


# ══════════════════════════════════════════════════════════════════════
# DAFTAR KARAKTER — diletakkan di luar fungsi
# Bisa digunakan untuk keperluan lain (misalnya menampilkan daftar)
# ══════════════════════════════════════════════════════════════════════
CHARACTER_LIST = [
    # Resident Evil
    "Leon S. Kennedy", "Chris Redfield", "Jill Valentine", "Ada Wong", "Albert Wesker",
    # Honkai: Star Rail
    "Acheron", "Kafka", "Dan Heng", "March 7th", "Jing Yuan",
    # Red Dead Redemption
    "Arthur Morgan", "John Marston", "Dutch van der Linde", "Sadie Adler", "Micah Bell",
    # Uma Musume: Pretty Derby
    "Agnes Tachyon", "Special Week", "Silence Suzuka", "Tokai Teio", "Gold Ship",
    # Crash Bandicoot
    "Crash Bandicoot", "Coco Bandicoot", "Dr. Neo Cortex", "Aku Aku", "Dingodile",
    # Devil May Cry
    "Vergil", "Dante", "Nero", "Trish", "Lady",
    # Assassin's Creed
    "Ezio Auditore", "Altaïr Ibn-La'Ahad", "Desmond Miles", "Edward Kenway", "Connor Kenway",
    # NieR: Automata
    "2B", "9S", "A2", "Pascal", "Emil",
    # Tekken
    "Kazuya Mishima", "Jin Kazama", "Heihachi Mishima", "Nina Williams", "Yoshimitsu",
    # Tomb Raider
    "Lara Croft", "Winston Smith", "Jonah Maiava", "Jacqueline Natla", "Amanda Evert",
    # Call of Duty: Modern Warfare
    "John Price", "Ghost", "John \"Soap\" MacTavish", "Kyle \"Gaz\" Garrick", "Vladimir Makarov",
    # Mortal Kombat
    "Scorpion", "Sub-Zero", "Liu Kang", "Johnny Cage", "Baraka",
    # God of War
    "Kratos", "Atreus", "Mimir", "Freya", "Baldur",
]