# characters.py
# File ini bertugas membangun Binary Decision Tree untuk game Akinator
# Setiap LEAF NODE = 1 karakter yang bisa ditebak oleh Akinator
# Setiap INTERNAL NODE = pertanyaan Ya/Tidak yang mengarahkan ke karakter

import random
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
    # BAGIAN 2 — INTERNAL NODES (PERTANYAAN SUB-KATEGORI)
    # Ini adalah node pertanyaan untuk menebak karakter di dalam satu franchise
    # ══════════════════════════════════════════════════════════════════
    
    #mortal kombat
    mk_tanya_warna_biru = Node(question="Apakah kostum atau auranya identik dengan warna biru / es?")
    mk_tanya_warna_biru.yes = daun_sub_zero
    mk_tanya_warna_biru.no = daun_scorpion

    mk_tanya_tarkatan = Node(question="Apakah dia memiliki gigi panjang menjijikkan / pisau yang keluar dari tangannya (ras Tarkatan)?")
    mk_tanya_tarkatan.yes = daun_baraka
    mk_tanya_tarkatan.no = daun_johnny_cage

    mk_tanya_biksu_api = Node(question="Apakah dia seorang petarung bergelar Earthrealm Champion dengan elemen api?")
    mk_tanya_biksu_api.yes = daun_liu_kang
    mk_tanya_biksu_api.no = mk_tanya_tarkatan

    mk_root = Node(question="Apakah dia seorang ninja atau memakai penutup wajah ala ninja?")
    mk_root.yes = mk_tanya_warna_biru
    mk_root.no = mk_tanya_biksu_api

    #tekken
    tekken_tanya_kazuya_vs_jin = Node(question="Apakah dia bisa berubah menjadi Devil dan sangat membenci ayahnya (Heihachi)?")
    tekken_tanya_kazuya_vs_jin.yes = daun_kazuya
    tekken_tanya_kazuya_vs_jin.no = daun_jin

    tekken_tanya_heihachi = Node(question="Apakah dia kakek tua ahli bela diri dengan potongan rambut botak di tengah?")
    tekken_tanya_heihachi.yes = daun_heihachi
    tekken_tanya_heihachi.no = tekken_tanya_kazuya_vs_jin

    tekken_tanya_yoshimitsu = Node(question="Apakah dia menggunakan pedang dan memakai armor canggih seperti robot atau alien?")
    tekken_tanya_yoshimitsu.yes = daun_yoshimitsu
    tekken_tanya_yoshimitsu.no = tekken_tanya_heihachi

    tekken_root = Node(question="Apakah tokoh ini adalah seorang perempuan pembunuh bayaran?")
    tekken_root.yes = daun_nina
    tekken_root.no = tekken_tanya_yoshimitsu

    #resident evil
    re_tanya_ada_vs_jill = Node(question="Apakah dia identik dengan gaun merah dan bekerja sebagai agen rahasia misterius?")
    re_tanya_ada_vs_jill.yes = daun_ada
    re_tanya_ada_vs_jill.no = daun_jill

    re_tanya_leon_vs_chris = Node(question="Apakah rambutnya berponi belah tengah yang khas (gaya rambut Leon)?")
    re_tanya_leon_vs_chris.yes = daun_leon
    re_tanya_leon_vs_chris.no = daun_chris

    re_tanya_wesker = Node(question="Apakah dia memakai kacamata hitam dan merupakan antagonis/villain utama?")
    re_tanya_wesker.yes = daun_wesker
    re_tanya_wesker.no = re_tanya_leon_vs_chris

    re_root = Node(question="Apakah tokoh ini adalah karakter perempuan?")
    re_root.yes = re_tanya_ada_vs_jill
    re_root.no = re_tanya_wesker

    #call of dutty
    cod_tanya_price_vs_gaz = Node(question="Apakah dia kapten yang selalu memakai topi boonie dan berkumis tebal?")
    cod_tanya_price_vs_gaz.yes = daun_price
    cod_tanya_price_vs_gaz.no = daun_gaz

    cod_tanya_soap = Node(question="Apakah dia dipanggil 'Soap' dan dikenal dengan gaya rambut cepak atau mohawk?")
    cod_tanya_soap.yes = daun_soap
    cod_tanya_soap.no = cod_tanya_price_vs_gaz

    cod_tanya_ghost = Node(question="Apakah dia selalu memakai topeng bermotif tengkorak dan sangat misterius?")
    cod_tanya_ghost.yes = daun_ghost
    cod_tanya_ghost.no = cod_tanya_soap

    cod_root = Node(question="Apakah dia merupakan pimpinan teroris berbahaya asal Rusia (Antagonis utama)?")
    cod_root.yes = daun_makarov
    cod_root.no = cod_tanya_ghost

    #umamusume
    uma_tanya_suzuka_vs_tokai = Node(question="Apakah rambutnya dominan warna orange terang dengan poni?")
    uma_tanya_suzuka_vs_tokai.yes = daun_suzuka
    uma_tanya_suzuka_vs_tokai.no = daun_tokai

    uma_tanya_special_week = Node(question="Apakah dia karakter utama berambut coklat dengan sejumput rambut putih unik di dahi?")
    uma_tanya_special_week.yes = daun_special_week
    uma_tanya_special_week.no = uma_tanya_suzuka_vs_tokai

    uma_tanya_gold_ship = Node(question="Apakah rambutnya putih/silver dan dijuluki si pembuat onar (Gold Ship)?")
    uma_tanya_gold_ship.yes = daun_gold_ship
    uma_tanya_gold_ship.no = uma_tanya_special_week

    uma_root = Node(question="Apakah dia ilmuwan jenius/nyentrik yang sering membawa tabung reaksi?")
    uma_root.yes = daun_agnes
    uma_root.no = uma_tanya_gold_ship

    #honkai star rail
    hsr_tanya_jing_vs_dan = Node(question="Apakah dia pemimpin pasukan Luofu yang memiliki elemen Lightning (Petir)?")
    hsr_tanya_jing_vs_dan.yes = daun_jing_yuan
    hsr_tanya_jing_vs_dan.no = daun_dan_heng

    hsr_tanya_kafka_vs_march = Node(question="Apakah dia menggunakan senjata api ganda (Dual SMG) dan berjaket kulit?")
    hsr_tanya_kafka_vs_march.yes = daun_kafka
    hsr_tanya_kafka_vs_march.no = daun_march

    hsr_tanya_acheron = Node(question="Apakah dia membawa pedang panjang dengan elemen kilat ungu gelap?")
    hsr_tanya_acheron.yes = daun_acheron
    hsr_tanya_acheron.no = hsr_tanya_kafka_vs_march

    hsr_root = Node(question="Apakah tokoh ini adalah laki-laki?")
    hsr_root.yes = hsr_tanya_jing_vs_dan
    hsr_root.no = hsr_tanya_acheron

    #god of war
    gow_tanya_freya_vs_baldur = Node(question="Apakah dia Dewi perempuan yang menguasai sihir Vanir?")
    gow_tanya_freya_vs_baldur.yes = daun_freya
    gow_tanya_freya_vs_baldur.no = daun_baldur

    gow_tanya_atreus = Node(question="Apakah dia anak kecil/remaja laki-laki yang membawa busur panah?")
    gow_tanya_atreus.yes = daun_atreus
    gow_tanya_atreus.no = gow_tanya_freya_vs_baldur

    gow_tanya_kratos = Node(question="Apakah dia dewa perang berkepala botak dengan tato merah tebal di sekujur tubuhnya?")
    gow_tanya_kratos.yes = daun_kratos
    gow_tanya_kratos.no = gow_tanya_atreus

    gow_root = Node(question="Apakah dia berupa kepala terpenggal yang bijaksana dan selalu menemani perjalanan?")
    gow_root.yes = daun_mimir
    gow_root.no = gow_tanya_kratos

    #nier automata
    nier_tanya_emil_vs_pascal = Node(question="Apakah dia berbentuk kepala tengkorak bulat besar yang sering menyeringai?")
    nier_tanya_emil_vs_pascal.yes = daun_emil
    nier_tanya_emil_vs_pascal.no = daun_pascal

    nier_tanya_2b_vs_a2 = Node(question="Apakah dia android perempuan berambut putih pendek yang memakai blindfold (penutup mata)?")
    nier_tanya_2b_vs_a2.yes = daun_2b
    nier_tanya_2b_vs_a2.no = daun_a2

    nier_tanya_9s = Node(question="Apakah dia android laki-laki yang memakai celana pendek dan berperan sebagai Scanner?")
    nier_tanya_9s.yes = daun_9s
    nier_tanya_9s.no = nier_tanya_2b_vs_a2

    nier_root = Node(question="Apakah wujud tubuhnya adalah mesin usang/aneh (bukan bentuk menyerupai manusia)?")
    nier_root.yes = nier_tanya_emil_vs_pascal
    nier_root.no = nier_tanya_9s

    #devil may cry
    dmc_tanya_lady_vs_trish = Node(question="Apakah dia membawa senjata berat/bazooka besar bernama Kalina Ann?")
    dmc_tanya_lady_vs_trish.yes = daun_lady
    dmc_tanya_lady_vs_trish.no = daun_trish

    dmc_tanya_dante_vs_nero = Node(question="Apakah dia memakai mantel merah panjang dan bersenjata pedang besar (Rebellion/Sparda)?")
    dmc_tanya_dante_vs_nero.yes = daun_dante
    dmc_tanya_dante_vs_nero.no = daun_nero

    dmc_tanya_vergil = Node(question="Apakah dia memakai mantel biru dan bersenjata katana bernama Yamato?")
    dmc_tanya_vergil.yes = daun_vergil
    dmc_tanya_vergil.no = dmc_tanya_dante_vs_nero

    dmc_root = Node(question="Apakah tokoh ini adalah perempuan?")
    dmc_root.yes = dmc_tanya_lady_vs_trish
    dmc_root.no = dmc_tanya_vergil

    #red dead redemption
    rdr_tanya_arthur_vs_john = Node(question="Apakah dia protagonis utama game kedua yang menderita penyakit TBC?")
    rdr_tanya_arthur_vs_john.yes = daun_arthur
    rdr_tanya_arthur_vs_john.no = daun_john_marston

    rdr_tanya_micah = Node(question="Apakah dia pengkhianat menyebalkan yang menjadi antagonis utama di game kedua?")
    rdr_tanya_micah.yes = daun_micah
    rdr_tanya_micah.no = rdr_tanya_arthur_vs_john

    rdr_tanya_dutch = Node(question="Apakah dia pemimpin geng yang kharismatik dan selalu bilang 'I have a plan!'?")
    rdr_tanya_dutch.yes = daun_dutch
    rdr_tanya_dutch.no = rdr_tanya_micah

    rdr_root = Node(question="Apakah dia perempuan pejuang (bounty hunter) berambut pirang yang tangguh?")
    rdr_root.yes = daun_sadie
    rdr_root.no = rdr_tanya_dutch

    #assasin creed
    ac_tanya_ezio_vs_altair = Node(question="Apakah dia Assassin legendaris dari zaman Renaissance Italia?")
    ac_tanya_ezio_vs_altair.yes = daun_ezio
    ac_tanya_ezio_vs_altair.no = daun_altair

    ac_tanya_connor = Node(question="Apakah dia merupakan ras penduduk asli Amerika (Native American / Mohawk)?")
    ac_tanya_connor.yes = daun_connor
    ac_tanya_connor.no = ac_tanya_ezio_vs_altair

    ac_tanya_edward = Node(question="Apakah dia seorang Kapten Bajak Laut dari wilayah Karibia?")
    ac_tanya_edward.yes = daun_edward
    ac_tanya_edward.no = ac_tanya_connor

    ac_root = Node(question="Apakah dia hidup di era modern sebagai subjek tes mesin Animus?")
    ac_root.yes = daun_desmond
    ac_root.no = ac_tanya_edward

    #crash
    crash_tanya_coco_vs_crash = Node(question="Apakah dia bandicoot perempuan berambut pirang yang suka membawa laptop?")
    crash_tanya_coco_vs_crash.yes = daun_coco
    crash_tanya_coco_vs_crash.no = daun_crash

    crash_tanya_dingodile = Node(question="Apakah dia mutan perpaduan Dingo dan Buaya yang membawa penyembur api besar?")
    crash_tanya_dingodile.yes = daun_dingodile
    crash_tanya_dingodile.no = crash_tanya_coco_vs_crash

    crash_tanya_aku_aku = Node(question="Apakah wujudnya hanyalah sebuah topeng kayu terbang ajaib berwarna-warni?")
    crash_tanya_aku_aku.yes = daun_aku_aku
    crash_tanya_aku_aku.no = crash_tanya_dingodile

    crash_root = Node(question="Apakah dia ilmuwan manusia jahat dengan huruf 'N' besar di dahinya?")
    crash_root.yes = daun_neo_cortex
    crash_root.no = crash_tanya_aku_aku

    #tomb raider
    tr_tanya_winston_vs_jonah = Node(question="Apakah dia pelayan tua (butler) keluarga Croft yang sering dikurung di kulkas?")
    tr_tanya_winston_vs_jonah.yes = daun_winston
    tr_tanya_winston_vs_jonah.no = daun_jonah

    tr_tanya_amanda = Node(question="Apakah dia teman masa lalu Lara yang kembali sebagai musuh dengan menggunakan entitas mistis?")
    tr_tanya_amanda.yes = daun_amanda
    tr_tanya_amanda.no = tr_tanya_winston_vs_jonah

    tr_tanya_natla = Node(question="Apakah dia antagonis abadi dan penguasa ras purba dari Atlantis?")
    tr_tanya_natla.yes = daun_natla
    tr_tanya_natla.no = tr_tanya_amanda

    tr_root = Node(question="Apakah dia protagonis utamanya (wanita penjelajah makam yang ikonik)?")
    tr_root.yes = daun_lara
    tr_root.no = tr_tanya_natla

    # ══════════════════════════════════════════════════════════════════
    # BAGIAN 3 — ROUTING UTAMA (LEVEL 1)
    # Ini adalah pertanyaan pertama yang ditanyakan ke user, diacak saat mulai
    # ══════════════════════════════════════════════════════════════════

    routing_fighting_mk_vs_tekken = Node(question="Apakah franchise gamenya sangat brutal, sadis, dan identik dengan gerakan 'Fatality'?")
    routing_fighting_mk_vs_tekken.yes = mk_root
    routing_fighting_mk_vs_tekken.no = tekken_root

    routing_shooter_re_vs_cod = Node(question="Apakah game shooter ini bertema horor kelangsungan hidup (survival horror / membasmi zombie)?")
    routing_shooter_re_vs_cod.yes = re_root
    routing_shooter_re_vs_cod.no = cod_root

    routing_gacha_uma_vs_hsr = Node(question="Apakah inti dari game tersebut berfokus pada balapan gadis kuda idol?")
    routing_gacha_uma_vs_hsr.yes = uma_root
    routing_gacha_uma_vs_hsr.no = hsr_root

    routing_hackslash_nier_vs_dmc = Node(question="Apakah karakter/semesta di gamenya difokuskan pada Android dan Mesin buatan manusia?")
    routing_hackslash_nier_vs_dmc.yes = nier_root
    routing_hackslash_nier_vs_dmc.no = dmc_root

    routing_hackslash_gow_vs_sisanya = Node(question="Apakah gamenya berlatar belakang mitologi Dewa-dewa kuno (Yunani / Nordik)?")
    routing_hackslash_gow_vs_sisanya.yes = gow_root
    routing_hackslash_gow_vs_sisanya.no = routing_hackslash_nier_vs_dmc

    routing_history_rdr_vs_ac = Node(question="Apakah gamenya memiliki tema Wild West / Koboi Amerika?")
    routing_history_rdr_vs_ac.yes = rdr_root
    routing_history_rdr_vs_ac.no = ac_root

    # Node fallback terakhir (Platformer)
    routing_platformer_crash_vs_tr = Node(question="Apakah karakternya merupakan hewan antropomorfik / tokoh platformer klasik era PS1?")
    routing_platformer_crash_vs_tr.yes = crash_root
    routing_platformer_crash_vs_tr.no = tr_root

    # Mengacak urutan 5 pertanyaan level 1
    categories = [
        {
            "q": "Apakah karakter ini berasal dari game pertarungan 1 lawan 1 (Fighting Game Arena)?",
            "y": routing_fighting_mk_vs_tekken
        },
        {
            "q": "Apakah karakter ini dominan bertarung menggunakan senjata api militer (Shooter FPS/TPS)?",
            "y": routing_shooter_re_vs_cod
        },
        {
            "q": "Apakah karakter ini memiliki grafis ala Anime dan berasal dari game Gacha buatan Asia?",
            "y": routing_gacha_uma_vs_hsr
        },
        {
            "q": "Apakah karakter ini berasal dari game aksi 'Hack and Slash' yang menggunakan kombo jarak dekat?",
            "y": routing_hackslash_gow_vs_sisanya
        },
        {
            "q": "Apakah game tersebut mengambil inspirasi kuat dari sejarah dunia nyata (zaman kuno / era koboi)?",
            "y": routing_history_rdr_vs_ac
        }
    ]

    random.shuffle(categories)

    # Membangun rantai pertanyaan utama berdasarkan urutan yang sudah diacak
    root = Node(question=categories[0]["q"])
    root.yes = categories[0]["y"]

    current_node = root
    for i in range(1, len(categories)):
        next_node = Node(question=categories[i]["q"])
        next_node.yes = categories[i]["y"]
        current_node.no = next_node
        current_node = next_node

    # Menempelkan cabang terakhir ke Platformer (Crash vs TR)
    current_node.no = routing_platformer_crash_vs_tr

    tree = DecisionTree()
    tree.build(root)
    return tree

# ══════════════════════════════════════════════════════════════════
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

art = {
    "Leon S. Kennedy": """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣶⡄⠀⠀⠀⠀⢰⡿⣿⣿⣿⣿⣟⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠀⠀⠀⠀⠀⣏⣖⠻⣋⠵⣯⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀⠀⠀⠀⢺⢧⣱⣤⣧⣿⣿⡿⣟⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣿⣟⣯⠀⠀⠀⠀⠀⠘⠊⡅⣿⡦⣙⣾⣕⣻⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣘⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⣰⢌⣹⣷⣿⣿⠿⡿⢿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⣿⣅⠀⠀⣀⣤⣾⣿⣷⢲⢿⠿⣜⣫⣵⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣿⢋⣶⡽⣻⣿⣷⣿⣿⣿⣿⣿⣿⣎⣟⣾⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⠻⡷⣿⣳⣳⢯⣿⠿⣿⣿⣿⣿⣿⣿⣷⣾⣻⢿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣽⡻⢬⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣽⣻⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⢾⣯⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠐⣾⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⢯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠿⣿⣿⣿⣿⣿⠏⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⣿⣿⣿⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⠇⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "2B": """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠡⠩⡙⢮⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣬⡌⡐⡐⠌⠇⢅⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⢺⢝⠢⢢⠡⡑⢔⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⢤⣁⣆⣕⣕⠃⠊⠂⢀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣦⡭⣗⢯⣫⣿⢯⡷⣤⣦⡀⠰⣜⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⣿⣿⢯⢿⣻⣿⣻⣵⣩⣳⣆⠸⡚⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣸⢾⠋⠉⠻⣟⣟⡿⣿⣿⣿⢋⠐⡍⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢐⢬⣦⣄⣆⣧⣾⢿⠀⢠⣀⢪⢳⣻⣳⢿⣿⣪⣜⣶⣅⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠠⢭⠚⢽⣟⠿⠗⠋⠸⠟⠟⢷⡿⣿⣺⣿⣟⢾⠿⢖⠒⠀⠀⠀⠀⠀
⢍⢮⢶⢖⡌⠆⠳⠙⡍⠺⠿⡿⡽⡝⠍⢕⢽⢟⣿⣿⣻⣷⡀⡀⡀⠀⠀⠀⠀⠀
⠀⠁⠁⠋⠁⢠⣠⡦⢅⡄⡦⡲⣸⠨⡨⣰⣸⣽⢿⣯⣿⣿⣿⣾⣝⢷⣷⣄⠀⠀
⠀⠀⠀⣠⣾⣿⠟⠊⡁⠸⣨⣪⣳⢝⣞⣞⣗⣿⣟⣯⣿⣷⣟⣯⣿⡿⣾⣻⡇⠀
⠀⠀⣼⢿⠽⠊⢐⢰⣴⣿⣻⣽⣾⣟⣯⣿⣻⣟⣿⣿⡽⣟⣿⣯⢿⢿⣻⣿⣧⡀
⠀⠀⠁⠀⠀⠀⠨⡪⡻⢾⣯⣿⣯⣿⣯⣫⣪⠃⠀⢯⡻⣻⣿⣿⣿⡽⣫⣳⣻⡏
⠀⠀⠀⠀⠀⠀⠀⠈⠪⠪⠂⣺⡽⣺⡻⣿⠇⠀⠀⠸⡽⣽⣿⣿⣽⣿⢪⢾⠙⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣻⢜⡾⡝⠀⠀⠀⠀⢿⢿⢿⢿⣝⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣼⣟⣿⡟⠀⠀⠀⠀⠀⢸⣿⣫⣿⣗⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣑⣿⣽⡟⠀⠀⠀⠀⠀⠀⠐⣿⣗⣿⡗⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⣼⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠽⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡐⣔⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⡑⣿⢿⡃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡐⣾⣿⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⠠⣸⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣿⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢽⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣾⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣽⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣽⡧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢐⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣽⣟⣿⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢐⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡗⢸⣟⣇⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⢿⣺⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠋⠉⠀⠀⠀
    """,
    "Chris Redfield": """
    ⠀⠀⠠⣥⣾⠀⡁⠠⠈⠄⠀⠡⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⣻⣿⣿⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣸⣿⣿⡇⠀⠀⣀⣦⣾⣶⣧⣦⣐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⢀⠸⣧⣿⣿⣇⠠⠐⣼⣿⣯⣿⢷⣟⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⡁⣆⣧⣿⣜⢯⡿⣯⠀⠁⣿⣿⣿⣿⡿⣿⣿⡿⢀⠀⠀⠀⠀⠀⠠⣀⠄⠀
⠀⠀⣾⣿⣿⣿⣿⣿⣿⡽⠀⠀⢹⣇⣦⣱⣬⢝⡿⡇⢀⠀⠀⠀⠀⢌⣾⡿⠃⠀
⠀⠀⠸⣿⣿⣿⣿⣿⡟⣡⣶⡶⣼⣿⣁⡯⣱⣾⣿⣧⣦⡔⢀⠀⠈⢼⣿⠁⡈⠀
⠀⠀⠀⢽⣿⣿⡿⢛⠟⣿⡽⣿⣿⣿⣿⣿⣿⣿⡿⢏⣻⢿⣷⣾⣤⣾⣿⠀⡀⠀
⠀⠀⠈⣾⣿⣿⡿⣌⠪⣍⣿⢻⣿⣿⣿⣿⣿⡿⡽⣋⡔⢢⠈⡙⣿⣿⣿⡄⠀⠀
⠀⠠⢹⣿⣿⣿⣿⣎⡱⠰⡌⠿⣯⡟⢫⠙⡘⠷⣍⢳⣞⣧⣶⣾⣿⣿⠇⠀⠀⠀
⠄⡁⣿⣿⣿⣿⣿⣷⣝⣣⢜⣡⢘⡰⢁⢎⡐⣡⡙⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀
⠂⠄⣿⣿⣿⣿⣿⣿⣟⣾⣭⣿⣯⣶⣯⣾⣽⣧⣿⣶⣿⣿⣿⡿⣽⡇⠈⠐⠀⠀
⠁⠂⡘⠛⢋⠋⡉⠀⠌⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢀⠀⠀⠀⠀
⡀⠂⠐⠈⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀
⠐⠀⠂⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⡿⣿⠏⠠⠈⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣿⠿⣷⠸⣧⢣⣸⠆⡡⢈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣿⣭⣭⣿⣟⠐⣏⠳⣿⢾⡄⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠠⣹⣿⣿⣿⣿⣿⣯⢠⣽⣿⣺⣷⣷⣿⣿⠄⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡟⠿⡗⠺⣜⠿⠿⢛⠉⢯⣿⣿⣿⡟⠡⢈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⣥⣿⣮⣕⣯⡷⡜⣘⡼⢌⡙⢊⠙⢻⡿⠀⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⣦⠿⣴⣹⣟⣧⡚⡍⢢⡱⢢⠔⠠⢌⠢⣝⠠⢀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⢰⣿⣷⣸⣦⣽⣿⣷⣼⣡⢊⠤⣈⠐⡈⢦⣙⣄⠂⠌⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⣏⡒⡄⡁⠢⢄⡙⢻⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⢻⣿⣿⣿⠛⣿⣿⣿⣿⠟⣹⣻⣔⡁⢂⠰⣈⢳⠈⡐⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣞⢻⣿⣿⣿⣿⣿⣿⣿⠂⢧⢡⡃⡔⠠⢆⡡⣘⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣶⣿⣷⣮⣍⣛⢻⣻⣿⠏⡀⢯⣷⣿⣶⢿⣦⣶⣾⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢳⣮⣿⣿⣿⣿⣿⣿⣿⡦⠐⠠⠙⣿⡟⡉⠫⢿⣿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣿⣿⣿⣿⢻⣿⣿⣯⠁⠂⠀⠂⣿⣧⢡⡎⢽⣿⡿⡏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⠻⡄⠀⠀⠀⢻⣿⣧⣟⣿⣿⣿⣿⡆⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣯⣿⢂⡗⠀⠀⠀⠘⢿⣿⣿⣿⣿⣿⣿⣯⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠁⣾⣏⡼⣿⣻⣧⡞⠠⠀⠀⢈⠘⢿⣿⣿⣿⣿⠏⡡⢇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠂⡧⢜⣼⣿⣷⣿⡇⠀⠀⠀⠀⠈⠘⣿⣿⠻⡅⠻⡘⢯⠄⠀⠀
⠀⠀⠀⠀⠀⢈⠰⣙⠯⣿⣿⣿⣿⠁⢂⠀⠀⠀⠀⢈⢻⣷⠷⠹⠃⠌⣙⠃⠀⠀
⠀⠀⠀⠀⠀⠠⠘⡝⣮⠱⣿⡿⡽⢀⠂⠀⠀⠀⠀⠀⠂⢻⣇⠱⢈⠰⢨⢹⠀⠀
⠀⠀⠀⠀⠀⡁⣧⡜⡠⢛⡾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠨⣷⣍⠢⣄⠷⣸⠀⠌
⠀⠀⠀⣀⢢⡼⢓⣾⣷⣿⣟⣿⡇⢈⠀⠀⠀⠀⠀⠀⠀⢀⠻⣟⠿⠿⢟⡰⡁⠀
⢡⣆⣁⢊⣃⣰⢯⣿⣿⣿⣿⣿⣏⠀⠂⠀⠀⠀⠀⠀⠀⠀⠘⣯⡐⢨⠤⣱⣳⠀
⠙⠿⣿⣿⣿⣿⠿⠋⠄⡈⠙⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠟⠻⠟⣿⠄
⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣏⢧⣼⡏⠀
⠄⠀⠀⠐⠀⠄⠁⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡘⣧⣷⣺⡞⢧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣕⣠⣄⣉⣾⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⣿⣿⣿⣿⡿⠗
    """,
    "Jill Valentine": """
    ⠀⠀⠀⠀⠀⢠⣈⣶⣻⣾⣷⣦⡈⠀⠁⠀⠈⠄⠁⠠⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢐⣾⣷⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⣖⢧⢯⡽⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢨⣹⡷⣿⣿⡾⣳⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⣿⡟⣯⣷⣯⡷⣭⢿⣿⣿⣿⠚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠑⠻⢿⣿⣷⣻⣞⣿⣿⡿⠟⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡁⣸⣿⣾⣷⡿⡎⠍⠠⠈⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣰⣖⡳⣶⣶⡿⣟⡿⣯⢿⣅⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢼⣿⣜⡳⣭⢿⣿⣭⢻⣜⡻⣞⡿⣶⣷⣿⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢾⣿⣾⡱⢧⣻⣿⣷⣋⡞⢷⡹⣞⡽⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣿⣷⣟⢧⡓⢿⣻⣽⣻⡷⣿⣌⡳⣽⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠙⣿⣿⣿⣧⢻⡱⢏⣿⣷⣿⣿⣿⣶⣿⣿⣻⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢹⣿⣿⣿⣷⣹⡙⣞⣿⣿⣿⣿⣿⣿⣾⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣿⣿⣿⣿⣷⡝⣮⠽⣿⣿⣿⣿⣿⣿⣟⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣮⣟⡽⢿⣿⡿⣿⣿⣾⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣭⢻⣿⣏⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣗⡻⣿⣼⣿⣿⣿⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣳⢻⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⡹⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣆⣄⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⣿⣿⣿⣿⣦⡀
⢀⣀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠛⠉⠁⠈⠃⠌⠻⣿⡷
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡁⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⠁⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠉⠈⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⡏⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⢸⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⣸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢈⣿⣿⣿⣿⡟⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢲⣿⣿⣿⣿⣿⠆⣹⣿⣿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣿⣿⣿⣿⣿⠀⣾⣿⣿⣿⡿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⣿⣿⣿⣿⣇⠀⣿⣿⣿⣿⣯⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠰⣿⣿⣿⣿⣷⢨⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⠘⠿⢿⠿⢿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣿⣵⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣿⠿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Ada Wong": """
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣤⣤⣄⣠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⡽⢻⣟⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⣿⣿⢣⣜⣩⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣯⢥⣃⠞⡳⣽⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡷⢫⣝⣳⣽⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣀⣴⣴⣷⣾⣿⣿⣶⣿⣿⣷⣿⣿⣿⣧⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⣄⣴⣴⣾⣶⣷⣾⣿⣿⣟⣿⣿⣿⣾⣿⣞⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣰⣤⣖⣻⣿⣿⣿⣿⣿⣿⣿⡿⢿⠿⠟⠛⠛⠛⠿⢿⣿⣿⣯⣿⣿⣿⡿⣯⣿⣾⢿⣻⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣄⣿⣿⣿⣿⣿⣞⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣟⣿⣻⣷⣿⣿⣿⣳⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⢿⡿⠿⠿⠟⠛⠉⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣿⣿⣿⣿⣟⣿⣿⣾⣿⢿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣟⣿⣾⣟⣿⣾⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣯⣿⣿⣻⣽⣾⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣻⣽⣿⡿⣿⣿⣏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣟⣿⣿⢯⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣻⣯⣿⣿⣟⣯⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣽⣿⣯⣿⣿⣿⣻⣽⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⢿⣟⣿⣿⣿⣿⢿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣻⢿⡿⣯⣷⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣽⡿⣿⣿⣿⣻⣽⣿⣿⣿⣿⢿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣟⣷⣿⣿⣳⣿⣿⣿⣿⣿⣽⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⡹⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡾⣷⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣹⣿⡿⢹⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣟⣿⣽⣿⠃⠸⣿⣿⣿⣿⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣿⣿⣷⣿⡟⠀⠀⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⣿⣿⣾⣿⠅⠀⢨⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣾⡿⠀⠀⣾⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⣿⠇⠀⢠⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⠃⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⣿⠇⠀⠀⠀⠸⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡏⠀⠀⠀⠀⠘⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⡟⠀⠀⠀⠀⠀⢸⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡿⠀⠀⠀⠀⠀⢀⣻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⠇⠀⠀⠀⠀⢀⣾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢸⡟⢿⣿⣿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠸⠇⠈⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣟⣿⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Albert Wesker": """
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠠⣡⣎⣤⣥⣈⠄⡁⠄⠈⠄⠀⠡⠈⠀⠁⠈⠀⠌⠀⠁⠈⠀⠈⠀⠁⠀⠁⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⣯⣭⢹⡆⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠸⣿⢿⣿⣧⢙⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⢹⣿⣿⣷⣮⡆⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢄⣷⣿⣿⣿⣿⣟⠤⣁⠂⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⠀⠀⠠⢠⣓⡮⢽⣿⣿⣿⣿⢯⣿⣦⣱⢬⢐⡠⣁⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⣿⡆⠀⢀⢰⣿⣿⣿⣿⡿⣾⣿⣿⣾⣿⣿⣷⣧⣟⣴⣯⢖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⢀⠀⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣏⢤⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡀⢘⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣛⣽⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠙⠉⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣿⣿⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠷⠟⠡⢀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⡄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⡞⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠸⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⡜⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⠃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠮⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣽⣿⡷⡀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣼⣿⣷⢎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢺⣿⣿⡼⡄⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⣿⣿⣧⣇⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⢓⣿⣿⣿⠦⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡫⢿⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡙⣿⣿⣏⢾⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢿⡏⢹⣿⣿⣿⡏⠙⡉⠛⠛⠁⢿⣿⡏⣼⣻⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢺⣿⣿⣶⠋⠉⠉⠄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Acheron": """
⣿⣿⣉⣿⣛⣿⣌⡛⠟⡿⠻⢿⣟⢿⡻⣟⡛⣭⣿⡛⣿⣿⡿⣿⢿⣟⠩⣿⣿⢿⣻⣿⣿⣿⡿⣽⣿⡿⣿⣿⣿⣿⡿⡿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣙⠽⡠⠙⣿⣿⣿⡿⣟⡿⣿⢿⣻⢿⡿⡿⢿⢏⣿⣿⣭⣿⣟⠿⣟⡿⣿⢿⡿⣿⣿⢿⡿⣿⡏⢻⣻⣟⣿⣻⢿⣛⡿⣟⣿⣛⠿
⣿⠇⣼⣿⣿⣿⣿⣿⣿⣷⢯⣬⣉⢮⣑⡶⣿⣙⣧⣽⣿⣿⣵⡷⣾⡼⣧⣟⣻⡞⣟⣿⣿⡗⣼⣧⣧⡝⡼⣍⡷⣯⣟⣹⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣟⣯⣿⣟⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢽⣇⡌⠴⣿⡿⣿⣽⣻⡽⣾⢯⣷⣻⡝⣫⣾⣟⣿⣿⣻⣽⣷⣙⡻⡽⢯⡟⣷⢯⡿⣽⣳⢣⣟⡷⣺⠳⣏⣟⡾⣽⣳⡞⣭⡟
⣿⣿⡜⣾⢯⣿⡿⣿⣟⣿⡿⣽⣿⣟⣿⢆⢣⣿⣿⣿⣿⣿⢮⣽⡽⢿⣮⠎⣷⡿⣿⣻⠍⣼⣿⣿⡿⣿⣷⢯⣿⠷⣍⣾⣿⣿⣿⢿⣽⣷⣿⣿⣿⣻⣿⣿⣿⣿⣿⣯⣿⣿⣻⣷⣻⡾⣽⣿⣿⣿⣿⣿⣿⣭⣍⡽⠞⡠⡟⣯⢷⢫⣗⣿⣽⣯⣗⢣⣾⣛⣷⢿⣳⣟⣿⣽⢯⣟⡿⣿⢧⢻⣯⣟⡿⡽⣩⡶⣝⡞⣥⢿⡸⣞⣽⡳⣗⣻⢶⡝
⣿⣿⣿⠸⣟⡾⡽⣿⣻⣿⣿⣿⣻⡿⣍⣎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣴⣘⠦⣃⠾⣽⢯⡎⡹⣭⢟⡿⣭⢫⣿⣿⣿⣿⣻⣯⣿⣿⢿⣽⣷⡿⣽⡷⣿⣻⡿⣿⣷⣿⣻⣽⢿⣹⢿⣾⣷⣿⣻⣿⢿⣿⣶⣿⣿⢿⠿⢿⡿⣿⣿⣻⣬⣷⣮⣙⢯⣿⡿⣿⣿⣯⢿⣽⣻⣿⣽⡿⡏⢾⣳⣯⣳⣟⣷⢫⡝⡾⣝⣯⡇⣿⢶⣽⢫⡞⣧⣛
⣿⣷⢋⣼⣿⣿⣿⣷⣿⣷⣿⣻⡷⣭⣿⣿⢿⣿⣿⣿⣿⣿⡯⣿⣿⣿⣿⣷⣳⢯⠓⣬⠙⣬⠉⡍⢩⢉⡭⢒⠤⣻⣿⣿⣳⣟⣿⣻⣟⣾⣿⣻⢾⣟⣯⣿⣻⢷⣿⣻⣽⣷⣿⢯⡿⢽⣾⡿⣾⣟⣿⣻⣿⣿⣿⣿⣿⣿⣧⣎⢻⣧⢻⣽⣻⣾⡽⣿⢸⣷⣿⡿⣷⣿⣿⢾⣟⡷⣿⣽⡡⢟⡷⣯⢷⣻⣞⢷⣻⣽⢳⣎⢷⢯⣛⡾⣝⢾⡱⢌
⣿⢉⣶⣿⡷⣿⣿⣿⡿⣷⡿⣏⣳⣹⣿⣿⣏⣿⣟⣻⢿⡿⣿⣽⣿⣿⣟⣿⣿⠃⣾⡽⣮⡼⠐⢬⢥⣚⣬⢝⡮⣿⣿⣿⢷⣯⢻⣿⣽⢿⣞⡿⣯⣟⣷⢯⣟⡿⣾⣽⣳⣿⣻⣧⢟⣷⡜⢿⣟⣾⣯⣟⡿⣾⣿⣿⣿⣿⣿⣿⣷⣿⣏⢾⣳⣿⣻⣽⡧⣻⣟⣿⣻⣷⡿⣿⢯⣿⢷⣯⡗⣩⢿⡽⣯⢷⣯⢿⡽⣞⡷⣎⣚⣌⡲⢱⣉⣦⡙⡬
⡎⣼⣿⣿⣿⣿⣿⣿⣿⣻⣝⣾⣿⣟⣻⣿⣿⣿⣿⣿⣮⣽⣙⠻⢿⡼⣹⠾⡁⣾⣳⡿⣝⡳⣟⣯⢯⣹⣷⡟⣼⣿⣿⣯⣟⣾⢭⡻⣾⣽⢫⣿⣯⢿⣾⣻⣽⣻⢷⣻⡝⣞⢧⢿⣿⢯⣿⣆⠹⣿⣞⣯⣿⣽⣻⢿⣮⢙⡻⣿⣿⣿⣿⣯⣷⢻⣿⣻⡖⣿⣿⣟⡿⣽⣻⣟⣯⣟⠿⣊⣵⣦⣉⡞⣹⣟⡾⣯⣟⣯⡽⣭⡿⣽⣻⡭⢿⡴⣋⠳
⣿⠸⣿⡿⣿⣿⣿⣿⣿⣿⣞⡽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣳⢯⣟⣦⣖⡙⠦⣹⣿⣿⢷⣾⣻⣽⣾⣿⡿⢧⣹⣿⣿⣿⢾⣟⣿⣎⢷⡟⣯⡳⡭⢷⣛⠷⣻⠷⣫⢞⡵⣻⣮⣟⡾⣯⢿⣞⣿⣧⡈⢿⣟⣾⡽⣿⡿⣿⣷⡱⢎⣷⢏⠿⣿⣿⣏⡾⣿⣇⣿⣟⡿⣿⣟⡷⡟⢎⣼⣷⣿⣿⣟⣿⣿⣶⡌⢿⣳⡽⢶⣹⢳⢿⣽⣳⣟⣧⢻⣍⠳
⡿⡇⣿⢿⣿⣿⣿⢿⣿⡟⡞⣴⣿⣿⣿⣿⣿⣿⠿⣿⣷⣯⢻⡾⣽⣻⠃⣵⣦⣌⣽⡾⣷⢿⣿⣯⢷⣛⣼⣿⣿⣿⣯⢿⡾⣯⣯⠏⡐⢸⡿⣕⣛⣯⡞⣥⠻⣥⢻⣼⢧⣻⡾⣽⣻⣻⢾⣽⣻⣷⡀⢹⣿⡽⣷⣿⣿⣿⣿⣮⠽⣷⣍⢺⡽⣿⣿⣳⡽⣿⢾⣻⣽⢞⡻⢡⣿⣿⢯⣿⢾⣟⣷⣯⢿⣿⢦⡹⣼⡖⣯⣛⡟⣞⣷⡻⣜⢧⢎⢿
⣥⠒⣭⣿⣟⣿⣻⢯⣞⣱⣿⣿⣿⣿⣿⣿⣿⣿⡹⢶⣙⢿⣯⣟⣷⢃⣾⣿⣫⣿⣿⡿⣿⣾⣥⣛⢧⣾⣿⣿⣿⣿⣯⢿⣽⣳⠏⡑⠒⠥⣿⡿⣽⣵⣻⣞⡷⣯⢿⡽⣯⢷⣻⢷⡽⣇⢿⣞⣷⣻⣷⡀⢹⣿⣷⣻⣿⣿⣿⣿⣿⣝⢿⢿⡿⣵⣻⣿⣽⣯⣟⡷⢍⣶⣿⣿⣿⣿⣿⣿⢿⣿⣿⣾⡿⣯⢿⡝⣧⣛⡆⢇⡻⡝⣞⢷⡹⢎⡞⣸
⣿⣑⠮⣻⡽⣳⢏⣶⣿⣿⣿⣿⣿⡿⣿⣿⣿⢳⡝⣧⢫⢜⣿⣾⢡⣾⣿⣿⣿⡿⣿⣿⣿⣷⣯⢏⣾⣽⣏⣾⣿⣿⣯⣟⣾⡽⠳⣿⣷⣧⣌⣿⡳⣞⡷⢯⣽⡳⣟⠾⣵⡻⣎⣿⣽⣻⢸⣏⣾⣽⣿⣷⡈⡽⣷⣟⣿⣿⣿⣿⣞⡿⣯⣻⣟⡷⣯⣿⣟⣾⢭⢲⡿⣯⣿⣿⣿⣾⣿⢿⣿⣻⣿⢾⣿⡽⣷⣿⣷⣿⡾⢌⡳⡝⡞⣬⠳⡎⡴⣡
⣿⣿⣦⢡⢛⣴⡿⣏⣿⣿⣿⣿⢿⣽⣟⣾⣿⣿⣜⡧⢟⡾⣿⢣⡾⣿⣿⣾⣷⣿⣿⣷⣿⡿⣞⢾⣿⣿⣎⣿⣿⣿⣿⣞⣷⣇⢣⢱⠣⣘⠏⠛⢿⣼⡹⣟⡶⣻⢭⣟⣳⡽⣝⣮⢷⣿⠂⣿⣾⣽⡿⣾⣧⢱⢫⡿⣞⣿⣿⣯⣿⡼⣻⣿⣿⣼⡹⣏⠿⣘⣦⣿⣽⣷⣯⣽⣙⠾⡽⢫⠟⡧⢏⣛⠼⣻⡝⡻⢯⠿⣹⢌⣳⣙⣜⢢⡓⣬⠵⡥
⣿⢿⣙⣶⡿⣏⢷⣽⣟⠿⣻⣽⣿⣾⣿⣷⢫⣿⣯⣽⣷⣿⢣⣿⣿⡹⣏⢿⣿⣽⣿⣾⣟⣿⡭⣿⣿⣷⣏⢿⣿⣿⣿⣾⡽⣹⣦⢣⠇⠠⢈⠐⠠⠙⢷⣻⣌⠳⣯⡽⣷⡿⣽⣞⣻⡻⡅⣿⣯⢿⣽⣻⢉⢇⡛⣯⡽⣷⣻⣿⣽⣗⢧⣻⣽⣇⢷⣬⣷⣿⣿⣿⡿⣟⢣⠏⡍⢓⠊⠥⡉⠔⡡⣌⢢⠡⢌⠩⣉⠛⠵⣚⠴⣩⢎⢧⡹⣌⢳⡙
⣙⣾⡟⣧⢿⣽⡿⢻⣎⢷⣳⣿⣯⣿⡷⣏⡏⣿⣿⡿⣯⢧⣿⢯⣟⣿⣻⣷⣏⡿⣿⣾⢿⣳⣏⣿⣿⣟⣮⡞⣿⣿⣿⢻⣧⢱⡹⣿⣞⡄⠂⠌⣀⠃⠄⡙⢾⣧⡈⠛⠷⣮⡙⠾⣷⣷⠱⣿⢯⡿⣽⣻⣀⠚⡵⣏⠻⢽⣿⣽⠿⡻⠟⢷⣯⢿⣮⢺⡝⢯⠙⢂⣡⣀⣦⣴⣼⣶⣿⢿⣿⣿⣟⡿⣻⣿⣿⡿⣽⣳⣶⣤⣘⠢⢎⠦⡱⢌⠦⡱
⣿⢳⣽⣽⡟⣧⣻⣳⣾⢿⣿⢫⣿⣽⣟⠦⣽⣿⣿⣟⣯⣿⣿⡻⡚⠭⢡⢉⡛⢾⣽⣻⣿⣿⣾⣿⣿⣿⣷⣿⡹⣿⣿⢺⣯⢶⡱⣭⢻⣿⣦⣆⣈⠢⠐⡀⢂⠙⠷⣌⡐⠠⢉⠂⠄⢨⢧⣿⠯⠽⠳⠿⠿⠿⠷⠧⠝⠒⡉⠄⢂⢐⣼⣿⣿⣯⢿⣧⡩⣦⢿⣿⣿⣿⣿⣷⣿⣞⡽⣿⢿⣽⣾⡷⣿⣻⣿⣿⣿⣽⣷⣿⢯⣟⢮⡣⡑⢎⡲⣕
⣭⢿⣾⣿⣹⢶⣿⣻⣽⣿⣿⣏⠷⢮⣍⣾⣿⣿⣿⣻⣿⡿⢁⠆⡱⢈⢆⣢⣙⠢⠕⣯⣷⣿⣿⣷⣿⡿⣷⣯⣷⣛⣿⣯⣟⣧⡻⣜⡿⣶⣹⠰⣄⠂⠡⢐⡠⣈⠐⠠⢉⠂⠄⣈⠔⣇⠾⢻⡇⠰⢁⠂⡐⢀⠂⣐⣈⣐⣠⢬⢶⣿⣿⣿⣻⢿⣿⣿⣷⡈⢿⣺⢿⣿⣿⣿⣿⣿⠟⣽⣯⣿⣿⣷⣻⣿⣿⣿⢿⡾⣷⡛⡟⣎⣧⣷⣟⢯⡟⣯
⢾⣻⣿⣿⡾⣯⢿⣿⣿⢿⣿⡿⣟⣡⣿⣿⣿⣟⣭⣿⠻⣔⠣⢜⣠⣿⡿⢿⣻⢷⣽⡜⣯⢿⣻⡿⣷⣿⣟⣮⣷⣿⢮⢿⣿⣿⣳⢯⣟⣳⢼⠳⢬⡙⢦⡀⠐⠠⢈⠐⠠⣈⡖⡭⢍⡒⡆⣼⢈⠐⣠⣶⣽⢿⡿⣟⠿⠿⣷⣭⣾⢳⡭⣿⣿⣿⣮⣟⠿⣿⣄⡙⣯⠟⡿⡟⡿⢿⡹⢶⢯⣝⡳⣋⠿⣹⢞⣱⣮⣵⡶⣿⣻⣏⣟⡶⣽⢾⣽⣾
⢯⣿⣟⢯⣿⣿⣧⣛⡾⣯⣛⡷⣡⣿⣿⣿⠿⣼⣣⢏⣟⡲⣩⣾⡟⣧⢟⣧⣛⢮⣛⣿⣜⢯⢿⣿⣿⣛⣼⣟⣿⣿⣟⠾⣿⣿⣹⢿⣾⣗⢺⡛⣦⣽⢪⣟⡤⣁⢢⢼⡩⡟⡣⢜⢢⠱⣽⠃⢆⠠⣷⣻⠼⢫⡕⢮⡙⢧⢎⡽⣿⣿⣞⡵⣯⣟⣿⣿⣿⣷⣭⣓⡤⢳⣕⠩⡝⣣⠽⡭⢮⡹⣭⡙⢯⡝⢯⠻⣜⢧⡻⣵⢳⢮⣳⣻⡽⣿⢿⣽
⣿⣻⣼⣋⠿⣿⣽⣷⣙⣏⣙⡒⣿⣿⣿⢯⢿⣱⡭⣞⣼⣽⣿⡳⣯⠽⣞⠶⣭⡳⣝⢮⢿⡏⢾⢣⣞⣾⡿⣿⣿⣿⣿⣏⢿⣿⣯⢿⡽⣻⡷⣝⡶⣯⢻⠜⡢⢍⡃⢎⡱⣼⠁⢎⠦⢹⣇⠘⠤⡘⣿⡃⢎⡱⢌⡓⠬⣀⠌⠠⠹⣿⣭⡟⣷⢯⣟⣾⢿⣿⣿⣿⣿⣷⣮⣽⣒⣣⡼⣈⣇⠳⢬⡙⢧⡛⢧⡛⡞⣎⠷⣩⢟⡾⣱⢯⢛⡵⣛⡶
⣿⣿⣿⣿⣿⣜⢿⣿⣿⡽⣿⡽⣿⣿⣿⣫⢟⣮⢳⣝⡼⣿⣿⠷⣭⣟⣞⠯⠷⠽⠮⠿⡊⢌⢢⡝⣾⢿⣿⣿⡿⣿⢾⡿⣞⢿⣿⢯⠳⣽⡝⣾⣝⣣⡁⣎⣵⣬⣜⢢⠱⡏⡴⢮⣐⢹⣾⡌⢂⠡⢏⡙⢦⠱⣊⠄⠡⢀⠑⢄⠡⢈⠛⢿⣧⣞⡽⣾⣟⣾⣯⡿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣶⣿⣶⣿⣼⣾⣷⣿⣿⣾⣶⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣇⢻⣿⣿⣽⢣⣟⣮⡷⣫⣞⡽⣫⠭⡁⠒⠠⢁⠁⢂⠐⡴⢚⠆⢸⡜⡑⢋⠜⢣⠻⣜⡵⢻⣬⣫⠽⣮⣛⠿⢟⡷⡜⠴⢫⠝⣿⠱⢛⠛⡛⣿⠾⣷⣛⠶⣥⢥⣆⡈⠜⡐⢂⠑⠨⢓⠕⡄⠈⠄⠱⣀⠉⢆⠹⣿⡟⣯⣿⣻⣾⢿⣿⣻⡿⣿⣿⣿⣾⣿⣾⣿⣽⣾⡿⠿⢟⡛⣛⣯⣽⣷⣟⢿⣿⣿⣿⣿⡿⣟
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⡟⣮⡳⣗⢮⣳⢳⡎⡖⢧⠂⠤⢁⠂⠄⡈⠄⡻⡌⡟⢀⠂⡆⠐⠠⢈⠉⠻⠷⠘⠣⣜⢧⣛⡶⣭⣚⠭⡖⢯⠻⣭⣛⠶⣮⡀⢣⢸⣯⣟⠶⡿⢿⣟⠳⡻⢿⣶⣽⠀⠌⡐⢈⠢⡈⢅⠈⡐⢠⡙⣄⢃⢿⣿⣻⡷⣿⡽⣿⣟⣿⣿⢿⣽⡿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣾⣧⢯⣝⢯⡿⣮⡻⣭⣽⣴⣷⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠯⣜⣱⡽⣞⢧⣏⢷⡹⢎⡇⡘⢀⠂⠌⡐⢀⠂⣳⠁⡐⢀⠂⠄⠡⠐⠠⢈⠐⡈⠤⡁⠌⠒⠽⡻⣿⣾⣷⣿⣿⣿⣿⣷⣿⣵⡿⣄⢺⣿⢿⣿⣿⣿⡽⣿⣦⣕⠲⢵⡈⠐⡀⢂⠐⡈⠄⡑⢄⠂⡜⠤⡃⢎⠻⣳⢽⣳⡿⣯⣟⣿⣾⣿⢿⣿⣿⣽⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⡽⣚⡵⣛⡿⢿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⡡⣟⣮⠷⣎⢷⡹⣇⠢⡁⠂⠌⡐⢀⠂⠄⡃⠐⡀⢆⡈⠄⠡⢈⠐⡀⢂⠐⠠⠘⡈⢓⠢⠤⣵⣩⠷⣾⣖⣳⣎⢿⣿⣻⢿⣿⠿⣟⡤⢛⠻⣿⣝⣿⣿⣻⣿⣦⣝⡄⠐⡀⢂⠐⠠⠐⡈⠦⡈⢧⡙⠴⣁⢻⣿⣼⣿⢯⣿⢾⡷⣿⣿⣻⣾⢿⣟⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣳⣅⢫⣓⠚⡬⢏
⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢧⡳⣬⠳⣿⡹⣎⢷⣹⠠⣁⠊⡐⢀⠂⠌⢰⢩⢓⢦⣈⠳⣌⠐⡀⢂⠐⠠⢌⡄⡡⠐⠚⠶⣷⣿⣿⡿⡡⢎⠭⡙⣾⣽⣯⣳⣌⣳⣭⣧⠙⠦⡉⠿⣭⠻⣍⢯⡹⡜⡸⢄⠐⠠⠈⠄⠡⠐⠠⠑⢤⡙⢦⡑⡺⣿⢿⣾⡿⣯⣿⢿⣽⣾⢿⣽⡿⣿⣯⣿⢿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⣌⢿⡱⣎
⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣎⢷⡹⡖⣏⠶⣙⠎⡷⣍⢖⠠⢃⠔⠠⠈⠄⡇⢸⢭⠲⣍⠶⣌⠳⡀⠂⠌⡐⠠⠙⠵⣋⢗⡲⡔⢦⡔⣲⠹⣌⠧⣹⣿⡿⠿⢿⣿⣿⣿⣿⣇⢡⠀⡁⠢⣍⣈⠄⡁⠡⠁⠌⡠⠁⠌⠠⠁⠌⡐⠈⠄⡩⢆⡱⢒⣹⡵⣞⡽⢿⣯⣿⣟⣾⡿⣯⣿⢿⣽⡿⣿⣻⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⢶⡹⣎
⣿⣞⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡏⣾⡱⢏⣜⡣⡝⡎⢼⣦⠙⢦⡁⢎⠠⢁⡸⢳⡜⣎⠷⣬⠳⣍⡻⡜⣮⣔⣠⢥⡚⢶⡩⢎⡵⣙⢦⣙⢦⡛⣬⢓⠿⣛⡵⣩⠒⣽⣿⡿⢿⣋⣄⠲⣔⢳⠲⣬⢹⡑⢏⡹⢌⡱⣉⢎⡱⢈⠐⠠⢁⠂⡘⡌⢮⡣⠔⣻⣟⠾⣧⣯⣝⣻⢿⣽⡿⣯⣿⣟⣿⡿⣟⣿⣿⣽⣿⣿⣿⣿⣿⣾⣷⣫⣏⠿⣷⣫
⣟⡿⢎⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⡶⣹⢋⣶⣱⣽⣼⢾⣯⡑⢢⠘⣄⣃⢆⡹⣓⢾⢬⠳⣜⠻⣜⠳⣝⠶⣩⡝⣫⣛⣭⣷⣻⣾⣟⣮⣽⡶⣽⢮⣏⣷⣭⡽⢷⣯⣽⣿⡸⡱⢎⡜⡳⣌⢧⡛⡴⢣⡝⡲⢆⣌⠠⢁⠂⡐⢀⠂⡐⢀⠂⠰⣉⠶⣙⠮⣔⢫⣟⠶⣭⢏⣟⣻⠾⣿⣟⣷⣿⣻⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣻⢷
⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣵⡿⣯⣟⡾⣽⠻⣎⢼⣡⢟⡶⣩⣮⣷⢟⣣⢎⠷⣌⣳⣼⣿⢻⣟⢿⡝⣯⢳⣾⣻⣽⣮⣝⡿⢿⣿⢯⢃⢾⡟⣮⡷⣿⣿⣿⡟⣳⣟⣾⣚⡷⣚⠶⣛⠶⡳⢞⣱⠻⠴⣏⢖⡢⢔⡀⢂⠐⠠⢈⠰⡩⠖⣍⡚⣄⢃⣯⣟⣧⢿⣎⢷⣻⢷⣞⣮⢳⣏⣯⢷⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣳⣯⣿⢫⣗⢮⡳⣝⡎⡷⣿⣟⣧⠞⡜⣎⣳⣾⢿⢟⣾⣟⢮⣿⢾⣱⣿⣻⣿⣿⣿⣿⣿⣿⣶⢦⡚⣮⣾⣟⡱⣿⢿⣻⣿⣿⣿⣿⣿⡷⣩⠞⡥⣏⢵⣋⠮⣝⠳⡜⢦⣱⢎⡜⣄⠓⡀⠢⠘⣥⢛⡴⡹⣘⠄⢺⣽⢧⣟⣯⣟⣷⣯⣞⡽⣟⡾⣼⢫⣽⢻⢾⡝⣿⣻⢿⣿⣿⣿⣿⣿⣿⣿⣿
    """,
    "Kafka": """
⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠀⠄⠠⢀⠐⠠⠠⢀⠐⠠⠀⠂⡀⠄⠠⠀⠄⢀⠠⠀⠀⠀⠀⠀⠀⡀⠀⡀⠠⠐⠐⡐⡐⠔⡐⢅⠣⡣⢱⣳⣗⣟⡎⡪⣎⢯⡺⡽⣝⣯⣟⣿⣻⢟⣝
⠀⢠⢡⢔⠎⠁⠀⠀⠀⠠⠐⠀⠁⢀⠀⠄⠂⠐⡀⠄⡁⢂⠐⡀⢂⢀⣁⣀⢄⡂⡐⠀⠄⠀⠄⠈⠀⠀⠈⠀⠀⢀⠀⠄⠂⢁⠐⠠⠡⠈⣄⣕⡬⣽⢾⣽⣗⠥⡊⡆⡳⢭⡫⡞⡞⡮⣺⢮⡿⣽
⢸⠱⠑⠃⠀⠀⢀⠀⠁⢀⠀⠂⠁⠀⠀⠄⠂⠁⠄⠂⡠⢆⣖⡼⣜⣞⡾⣽⢽⡽⡽⣽⣺⣖⣦⣄⡂⠀⠀⠀⡀⠀⢀⠠⠈⠀⠄⠡⠐⢸⣶⣮⢯⠯⣏⣗⠳⣕⣕⡇⡑⢕⢜⢜⢎⡯⡯⡯⣟⣿
⠀⠠⠐⠀⠂⠀⡀⠀⠐⠀⡀⡀⡀⠄⠂⠐⠈⣐⢴⣝⡾⣻⢮⢯⢷⢷⣻⡳⡯⣯⡻⣞⣾⣺⡳⡯⣟⣦⣀⠀⠀⠀⠀⠀⡀⠁⠠⠁⠄⢽⢯⢿⣻⢿⢽⡿⡯⣗⢧⠃⡌⢆⢣⢣⢳⡹⣺⢽⡻⣾
⠀⠀⠠⠐⠀⠁⢀⠐⡈⡰⠐⠀⠐⠈⢀⢅⡧⣷⣻⣞⣯⢯⡯⡿⡽⣯⢾⢽⣻⢮⡯⣗⣗⡷⣻⣽⣻⣺⣳⢧⡀⠀⠀⠂⠀⡈⢀⡆⡞⡭⣪⣲⣞⣟⣿⣻⢽⢽⢕⠌⡐⡑⡌⢎⠎⡞⡎⣗⡯⣷
⠀⠀⠀⠀⠠⠐⡁⠔⠈⠀⠀⢀⠁⡄⣧⢯⡻⣽⢾⣳⡽⣽⣺⢯⣯⡯⡿⣽⡺⡽⣫⡗⣗⣝⢗⡵⣻⡺⣽⣻⡺⡄⠀⠀⢀⠀⣲⣧⣯⢾⣷⣻⣞⣯⣿⢯⣻⢵⠇⠂⢌⣢⢬⠖⡓⡪⣚⢜⣞⣗
⠱⠲⠰⠡⠡⠁⠠⠀⡀⠀⠀⢀⣮⢞⣯⢾⣻⣻⣟⣷⢯⡷⣯⢿⡯⣿⣝⢮⢯⢯⢮⢻⡜⡮⡳⣝⡮⣺⢵⢯⢿⢽⠀⠠⠀⠀⣷⡿⣾⡿⣷⢿⣾⢿⣽⢯⡾⡵⡡⣵⡻⢊⠢⡱⢱⢱⢕⣝⢮⢞
⠀⠠⠐⠀⠐⠀⠂⠠⠀⠄⣴⣻⣺⡽⣯⢿⢽⢞⡷⣝⢽⣽⣫⢯⢟⡽⣞⢭⡳⡻⣜⢵⡫⣫⢝⢮⢞⢷⣝⣞⡽⣯⠂⠀⠀⠈⠉⠋⣷⣿⣿⢿⣟⣿⣯⢗⣯⡺⡝⡞⠈⠄⠕⡘⢌⠎⢎⢎⣪⣭
⠀⠠⠐⠈⢀⠈⡀⠂⣤⣟⣾⣺⣗⡯⡯⣟⡽⣫⢞⢎⢯⡺⣮⢯⢷⡻⡕⣗⢝⣝⢮⢳⡹⣪⢏⢷⢝⡗⣗⡷⣽⣻⡅⠀⡀⠂⠀⠠⣿⢷⣟⣿⣯⢿⡾⣽⠮⡎⠏⢀⢨⣔⢶⡺⣖⣯⢯⣋⠡⠠
⠀⠂⠀⠄⠠⠀⠠⣞⣷⢷⣻⣞⡮⡯⡯⣗⢯⡪⡳⣹⢱⢝⢎⢗⡳⡝⡎⡮⡳⡕⣝⢎⡞⣎⢯⣫⡳⣝⢞⣞⡷⣳⢽⣺⢼⢤⠀⢸⣽⢿⣯⣷⣟⣿⢯⣞⢭⡋⣰⢮⣗⢯⢯⢯⣻⡺⠽⠽⠷⠶
⠀⠂⠐⠀⠐⠈⡼⢋⢾⡽⡷⡯⣞⣯⢫⢞⡵⡫⣎⢞⣜⢜⢵⢕⡧⡱⣣⡳⣝⢮⢮⡳⣝⢮⡻⣜⢾⣮⡳⣳⢽⣻⣳⢷⡽⣹⢵⢼⡿⣝⣗⡽⣪⣿⡳⣏⢾⡸⣕⢗⣕⠯⠓⠉⢀⠠⠈⡀⠂⠐
⠐⠀⡀⠁⡈⠀⠅⣸⡯⡯⢹⣝⢷⢽⣪⣞⣞⣝⡎⡷⡕⣏⣗⢽⠈⠀⠱⡳⣝⢮⡳⡕⡧⣳⢝⣗⢽⡞⣟⣮⣗⢷⣝⡯⡯⣗⣝⣽⣿⣻⣽⡯⣫⣷⣻⢕⡗⣝⡮⠗⠁⠐⠀⢁⢀⠠⠐⠀⡈⠄
⠀⠁⢀⠠⠀⠂⡀⡇⡿⡇⠀⡷⡽⡝⣮⣂⡑⠳⡽⡅⢫⢮⢘⢎⢦⢶⢤⣸⣓⣗⢵⢝⢮⡳⡽⣞⣽⡺⣵⡳⣯⢿⣺⢽⡽⣺⣲⣽⣳⢯⣷⢿⣽⢷⢽⢕⡯⠓⠁⠀⠀⠂⠁⢀⠆⠀⡀⠂⡀⠄
⠈⠀⡀⠀⡀⠂⠀⠀⢹⠅⠀⠘⣗⢽⡸⠲⡈⠈⠈⠢⠈⠓⠅⠁⠀⡣⡙⣪⠺⡺⣪⡳⡽⣝⣽⣳⣳⣫⣗⣯⣯⡯⢯⡪⡏⣗⢼⣟⡾⣟⣯⡷⣿⢯⡟⣜⠀⠀⠀⠀⡀⣄⣖⠏⠀⠠⠀⡢⣠⠐
⠀⠄⠀⠀⠀⠀⠀⠁⠀⠃⠀⡼⣹⣣⢯⠀⠀⠠⠈⠀⠀⠠⠀⠀⠠⠠⠋⠀⢰⡫⣞⢞⡽⣳⢽⣺⡵⣗⣟⣾⠓⠁⢵⡹⡪⣵⡿⣗⣿⡽⡾⡽⣟⣷⣫⡺⡤⡤⣔⢖⠯⠚⠀⠀⠌⢀⠣⣷⣯⠂
⠀⠄⠂⠀⢀⠈⠀⠈⠀⠀⢸⢽⢳⣳⢹⠂⠀⠁⠄⠀⠐⠀⠀⠐⠀⠀⢀⣰⠝⠎⢳⠽⡽⣹⡽⣮⡻⡮⡷⡥⡲⡤⣸⢪⢊⣖⢟⢟⣿⡿⣝⢞⡿⡾⣜⠎⠉⠘⠈⠁⠀⠀⠂⠁⢐⠀⣸⢽⡾⢱
⠀⠀⠀⠀⠀⠀⠀⠄⢐⢈⠀⢏⡐⠹⣎⣮⣂⠀⠂⡀⢄⢀⠐⠀⠀⠈⠀⠀⠀⡀⡆⡻⡪⣗⢏⡳⡯⣯⢯⣟⡽⣳⢵⣫⢝⣮⡫⡷⣕⠫⣫⣑⣽⣟⢼⠁⠀⠀⠀⠀⠀⠂⢀⠁⠄⠂⢼⣗⢇⡯
⠀⠀⢀⠐⠈⠀⡀⡢⠁⠀⠠⠀⢉⠙⠘⢸⢮⢧⡀⠀⢀⠀⠀⡀⠂⠁⡀⠔⢅⠕⠌⢌⢯⢎⢯⡆⢽⢺⣝⣗⣟⡮⣿⡾⡷⡵⡝⢪⡢⡽⡮⡳⣽⢮⣫⠀⠀⠀⠀⠀⠀⠀⠠⠐⠀⠂⣟⡇⡮⡯
⠀⠀⡀⠀⢄⢪⢐⠀⠀⠀⠀⠄⠅⠀⠀⠈⣯⣗⢧⣂⢀⣀⢤⣤⣦⣃⠪⡘⢔⠡⡃⢅⠣⣯⢳⢽⢘⣼⣗⣗⣧⣿⢻⣪⢯⣷⣕⢧⢻⣺⣺⢵⣯⡳⡅⠀⠀⠀⠀⠀⠀⠄⠀⠄⠁⠂⡿⣸⡺⡝
⢀⠀⡄⢎⠎⠊⠀⠀⡀⠄⠕⠁⠀⠀⠀⠂⢳⡳⣻⢽⢽⣺⡽⣾⢗⢢⣿⣌⣢⠕⢌⢢⠡⢹⡕⡯⡯⣾⡺⣾⣟⣮⣷⣽⡿⣽⢾⢕⢯⣺⣺⡝⢕⠽⡅⠀⠀⠀⠀⠀⠀⠀⠠⠐⠈⠀⡽⡵⡫⣨
⡱⣕⢵⢱⢱⠡⠃⡁⡀⡁⡀⡀⠀⠀⠁⠀⣝⢮⢯⢯⢯⣷⣻⡟⣕⢱⢹⡾⣯⣣⠱⠠⡡⢱⣫⡫⣯⢗⢯⢳⢕⢯⣻⣷⢿⢯⡳⡽⣸⣺⢵⢑⠅⡕⡅⠕⡄⠀⠀⠀⠀⠀⡀⠄⠂⡼⣝⣽⣳⣞
⢫⠺⠘⠁⠀⠀⠀⠁⠁⠁⠁⠉⠊⠶⢄⡮⣳⣝⠷⣽⣻⣺⣗⡧⣱⢸⢸⢹⢘⠌⢇⢃⠢⣝⢮⣺⢕⡯⣎⢧⢯⣻⣽⡿⡯⡳⡝⣼⢣⣟⢇⢅⠪⢂⠪⡈⠆⠀⠀⠀⠀⠀⠀⣀⢮⢯⠊⢸⣺⣷
⠒⠁⠁⠀⠀⠀⠀⠀⠀⠐⢈⢀⡤⣔⣗⠽⣱⠕⢠⣗⣿⣺⡳⡯⢣⢇⡏⡢⢃⠅⡕⣢⢹⣪⢯⣺⢵⣝⢮⣯⢿⢽⢛⢝⣝⣝⢎⡷⡯⣺⠠⠕⡩⢨⠑⠀⡣⡳⡲⣔⢤⢬⢔⠗⡙⡄⣮⢷⣟⣾
⣐⣒⣒⠢⠀⠄⢂⡡⠲⣙⣯⡻⠚⠁⢡⠼⠊⣹⢽⣺⣳⢽⣞⠌⢌⡞⢄⠣⡡⣪⡰⣯⡷⣽⣝⢞⣷⢽⣻⡾⠉⡈⠆⡃⢗⣗⡯⣷⣻⡜⡁⡂⡆⠅⡀⠀⣺⣱⠙⠊⠉⠁⡄⣪⣲⢯⡿⣽⡳⡹
⢗⣗⢵⢫⠅⠠⠊⠀⡴⡫⠊⠀⠀⢐⠍⣠⢾⢽⡯⣯⡟⣜⣮⢮⡷⡮⡲⣝⢽⣜⣺⣿⣻⢿⣾⣻⣽⢿⠝⡀⠁⡠⠊⠪⣘⢘⠽⡳⢗⠁⠀⢂⠢⢁⠂⢈⠌⠺⣮⢲⣑⡽⣼⢗⣯⡯⣿⢽⡪⣫
⠀⠀⠉⠓⠀⠀⠀⠠⡯⠁⠀⠄⠁⠀⠙⢯⢿⣫⣿⣳⠿⠾⡽⡝⣞⡮⣯⢾⣻⢾⢼⣷⢿⣻⣯⣿⢾⠋⢀⠀⡜⠨⡊⢌⢐⠢⡑⡕⡁⠀⠀⠀⡨⡠⡡⢰⠈⠢⣈⠳⣖⢝⠳⣟⣷⣻⢯⡷⣵⣻
⠀⠀⠀⠀⠀⡀⠄⠀⠃⠀⢀⠠⠀⠂⢀⣼⣯⢷⣻⢞⢘⡼⡳⢋⡵⢛⢹⢛⠝⠫⠛⠿⢟⣿⡷⡏⡣⡰⣴⢬⣴⡵⠾⠴⠴⢌⡆⢅⠢⢒⢐⢑⠅⡂⡊⢆⠄⠀⠊⡆⠈⢻⢷⣔⢣⣯⣻⢝⣯⡿
⣦⢄⡀⠠⠀⠀⠀⢀⠐⠈⠀⠀⢀⣴⣟⡷⣯⣟⡿⡐⣕⠏⠠⡸⡐⠐⠨⠐⠈⡀⠀⠀⠀⠀⠁⠸⡈⡢⠚⠉⡀⠀⢀⢀⠄⣂⡂⡅⠌⡂⡂⢎⢐⠌⡂⡑⢀⠀⢀⠇⡐⠀⠉⠺⣧⢳⣻⣗⡯⣗
⣯⢯⡯⣳⡲⣔⢌⣀⠀⠠⠐⠈⢾⡯⣾⣫⢷⣫⡇⡂⡏⢔⠑⡐⠀⡀⠨⠀⠐⠀⠀⠁⠀⠠⠐⠁⠈⢊⠢⢲⢦⣵⣲⣞⣯⡟⡐⡙⢌⠢⡊⡢⢁⠂⢂⠊⠀⠠⡊⠀⠀⠩⠐⠐⠌⣳⡵⣳⢿⢵
⣾⣫⡯⡷⣝⡮⣳⢕⢽⡱⡢⡄⡄⠀⠉⠺⡯⣯⡇⡂⡪⠐⠀⠀⡀⠄⠀⠠⠁⠀⠄⠂⠁⠐⠀⡀⠄⠀⠨⢑⠍⡗⣞⣳⢷⣳⣌⠔⡁⡊⡐⢄⠄⡄⠂⠀⢔⠑⢌⠀⠐⠈⠀⠐⢀⠀⠻⣯⢯⢯
⢄⢈⢻⢽⣳⣫⢞⡽⣸⢪⡣⣫⢪⢕⠬⡰⡝⣯⣷⠨⡐⡀⠁⢂⠀⠂⠐⠀⠂⠀⡀⠔⠈⠀⢀⠀⢀⠠⠀⠂⠕⡔⢌⢺⢽⣞⣞⡿⣮⣬⣌⠢⡑⢌⠄⢕⠅⢕⠡⠨⠀⠀⠂⠀⠄⢂⠀⢻⣯⣯
⢸⢰⢀⠹⣞⢾⣝⣞⢮⡣⣣⢣⢣⢣⠣⣝⡾⡽⣞⣷⣌⠢⡈⡐⠠⢊⡐⠌⠀⡂⠂⠀⠄⠈⠀⡀⢀⠀⠠⠈⡌⡢⠢⢵⢹⠸⢷⣻⣽⣾⢾⣧⡅⢕⠨⢂⢑⢅⠪⠨⢂⠁⠀⠂⢀⠐⡨⠨⣿⣾
⢰⢑⠕⣅⠩⢳⣳⢵⡳⣝⢮⠣⡣⡣⡣⡳⡯⡿⣽⣺⡾⣻⣶⣮⣔⣔⣌⡪⡱⡰⡐⢅⠠⠈⡀⠠⠀⡀⢂⢌⢆⡪⣪⢣⢧⢹⡸⣪⣳⣟⣿⢾⣷⡡⢊⠔⡡⢂⢅⠣⡁⡂⡈⠀⠄⠀⡂⠅⣿⢿
⢪⢪⢊⡲⠀⠌⠺⠵⡫⠮⠃⠀⠌⠪⢪⣻⣻⣻⢯⣗⡿⣽⣺⣳⣷⣣⢗⡯⡿⣽⣫⢷⣳⡵⣦⠦⣕⢔⣥⣣⢇⢗⡲⢵⢜⡜⠁⢫⢯⢯⣟⢿⣻⢷⣁⠪⡐⡡⢂⠕⡨⢂⠢⠡⡀⢁⠠⠡⣻⣿
⣜⢮⢺⠊⡐⢈⠄⠡⠀⡂⠨⠀⠅⡈⣞⣯⣿⡾⣿⣺⣽⣳⠏⢂⠈⡿⣗⣯⣟⡾⡽⢯⡳⡝⣞⢽⠚⠽⣝⣯⣿⢯⣿⣻⣧⢯⡳⣫⢯⣻⣺⢽⣞⡯⣗⣧⣆⣪⠐⢅⠢⡡⡑⡑⢌⠔⡨⣊⣾⣟
    """,
    "Dan Heng":"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠐⢄⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢀⣠⡴⣶⢿⣟⡿⣶⣼⢿⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⢀⢤⣚⣿⣝⣯⢗⣵⡻⣺⢗⡿⣽⡻⣯⢿⣆⠃⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠤⢌⣽⢿⢮⡯⡾⣝⢮⣫⡳⣫⢟⣵⣫⢯⢷⣝⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠤⣰⣽⣻⣟⢷⣻⢽⣮⡳⣵⣫⢳⢯⣎⢷⡝⣮⢷⣻⡞⡷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣱⣿⣿⡻⣾⢯⣟⢷⡽⣞⣯⢞⡯⣷⡺⣗⣽⣳⢯⡯⣿⣖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠐⣽⢹⣯⢿⡯⣿⡽⣟⡾⣯⢷⣻⣟⣵⢿⣽⢮⣟⣷⣻⢯⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢩⠾⣙⣯⣟⣿⣽⣻⣟⡽⣟⣷⢯⡾⡷⣿⣝⣿⢾⡿⣻⡚⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢖⠳⢿⣞⡿⡮⣟⣞⠁⣿⢯⣟⣿⡛⢹⡾⣻⣷⢿⣯⠁⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⢊⠻⣟⡎⠻⠚⠒⠉⣷⣫⢏⡟⣦⠭⢭⢹⢯⣏⠛⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣳⣜⡡⠀⠀⡀⠀⠇⠸⣧⠣⠈⠈⢡⣳⠺⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣍⣿⠠⠐⠀⠄⠠⠀⠰⠀⠀⠀⡠⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢰⣅⡁⢱⠄⠐⠠⠀⡁⢀⢁⣼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⢿⡷⣿⣢⡐⠀⢄⣴⣏⣑⣂⡂⠴⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠔⡄⣠⡾⢳⡿⣯⢿⣽⡧⣿⣿⣿⡇⣿⣿⡽⡿⣷⡁⠀⠁⢹⢎⡖⢄⠐⡆⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢄⡂⢡⢑⢎⢮⠱⣎⡅⡛⢿⣯⢾⣷⣹⣯⣻⡟⣿⣟⡿⣷⡔⣿⡔⠀⡱⢜⣝⣲⠆⡼⣗⢢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠄⠒⡈⠠⢂⠩⣲⠕⡱⡕⡳⢜⣏⠳⣦⣙⢿⣳⣮⠷⣻⣟⡻⣽⣟⡷⡵⢗⣿⡼⡓⢤⢪⣲⢫⢙⠥⡫⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⢐⢆⢍⢎⢌⡊⠔⠃⠁⢫⡚⢮⢪⠳⡼⡩⣫⣽⣇⠽⣾⢿⣽⢹⡿⡼⣝⣟⣿⠘⢷⣻⡌⠓⢳⡕⣼⢎⢣⢫⢪⡒⡤⣠⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣜⠵⡨⢂⡵⠁⢃⠀⠂⠄⡈⡾⡱⣍⢗⠵⢎⠜⣯⢞⡆⠺⣷⣻⣎⡿⣽⢽⣮⡻⣶⢜⢷⣻⡀⢸⢌⡇⠐⠓⣳⢵⠻⡜⢵⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡪⣮⢕⢩⠊⢀⠀⡀⠎⠐⠄⢀⠸⡗⡵⣩⡫⣺⢅⢻⣝⣿⡑⢿⣪⣯⡻⣞⢷⢫⡾⣳⣟⣵⡝⠧⠲⢇⠞⢶⢺⠃⠸⡩⡽⣧⠵⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠠⣲⢃⢗⡠⠚⠀⢂⠅⢐⠀⠸⠀⡐⠀⠀⢟⢮⡪⡺⡢⡗⣅⡿⣞⡇⢼⡷⣝⣾⣝⢯⡷⣝⠷⣽⢮⣻⣤⣇⣋⢗⣸⠙⠎⠀⡗⢜⠕⡿⣆⡄⠀⠀⠀⠀
⠀⠀⢀⢴⢊⠆⡕⡜⡐⠠⡈⡀⠢⡀⢅⠈⡔⠀⠌⡀⢸⡧⡹⡜⡵⣹⡢⢜⡿⡇⣸⢟⣞⢾⢮⣻⣞⣽⡻⣺⣕⣻⢮⡿⣨⢝⢸⠀⠘⡈⢏⢽⠾⢮⡪⣵⠀⠀⠀⠀
⠀⡠⣲⠜⣃⡺⡨⣈⡛⠔⠔⢄⠢⠐⡐⠠⣇⠁⡰⡁⠀⣯⢚⢮⡺⢼⡷⣅⠽⡧⢺⣯⢯⣻⡳⣽⢮⡾⣝⡷⣽⡺⡷⣮⡏⢭⡇⡆⠀⣰⠀⢅⣬⣾⣿⣫⡳⡄⠀⠀
⣞⡫⢒⢓⠊⡑⢈⠊⠠⡈⣂⠔⠤⡡⠒⠔⣗⠠⡣⠠⠀⣯⢳⡝⣮⢻⣞⢿⣍⢏⣽⢷⣫⡷⣻⣳⡻⣞⣽⢞⡷⣽⣻⣞⣿⠘⣞⢣⠐⠠⢶⣿⢿⡽⣿⣿⠷⣟⡄⠀
⢼⡡⠣⡡⡑⡌⢤⢃⢣⠱⣈⡪⡢⡕⣝⢪⢆⢏⠜⠀⠂⣿⡪⣞⡵⣻⣝⡯⣿⢸⢺⡯⣾⣝⢷⣽⣝⣷⢽⣝⣟⢾⢷⣽⡏⢀⠘⣟⡄⡑⠌⣿⣳⡿⠊⡀⠢⢈⠻⠆
    """,
    "March 7th": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢄⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢄⢎⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⢔⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠔⡢⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢊⠜⢄⠫⣀⠀⠀⠀⠀⠀⠀⢀⠔⡡⡹⣀⣀⡀⠀⠀⠀⠀⠀⠀⢀⠄⠂⠀⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⠱⡀⡣⢊⠜⢄⠅⠀⠀⠀⡠⢠⠑⢌⠒⠔⡢⠰⡩⡱⣂⠀⠀⠀⠀⠁⠀⢀⠐⡀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⡐⢕⠌⡪⢐⠅⡕⡑⢌⠂⠀⠠⡈⠢⠂⡁⠊⠈⠄⠡⠑⢌⠢⡌⠀⠀⠀⠀⠀⠀⠀⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⢷⣢⠀⠀⠀⠠⡈⡪⠢⡈⠢⡑⢌⠢⡑⠄⠀⠐⠠⠈⠐⠀⠀⠈⠀⠂⠀⡑⠨⠂⠀⠀⠀⠀⠀⠀⣀⠤⠒⠁⠀⡀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⢾⠄⠀⠠⠐⡡⢈⠔⢈⠂⢕⠨⢂⠁⡠⠈⠠⠁⠐⠀⡤⠑⠈⠐⠄⠠⠀⠈⠀⠀⠀⠀⠀⡐⠅⢌⠒⡈⢂⠑⡌⡪⢦⢍⠯⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⡁⠪⡀⠂⠔⡀⠑⠄⢊⠀⠂⢐⠈⠀⠄⠤⡉⢆⠐⠄⣠⠈⡂⠀⢅⠀⢀⢀⠐⠀⠔⡈⢄⠂⢌⠠⠊⢄⠑⡐⠡⡊⡄⢤⢂⠲⡰⢢⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⡄⠡⡈⠨⠂⠌⡈⠂⠔⠁⠊⠀⠀⠀⠀⠂⠣⠌⡢⡀⢄⠎⠀⠡⠄⢊⠀⠄⠈⠀⠀⠀⠀⠀⠢⠈⢂⠔⠠⢊⢌⢌⠢⡑⡡⡩⠊⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠨⠀⣻⣀⠂⡁⠊⠀⢈⠐⠈⠀⠀⠀⠀⠀⠀⢀⠎⠈⠄⢐⢀⡆⡈⣧⡠⢰⣃⠀⠀⠀⠀⠀⠀⠄⡐⢁⠢⠐⡁⡢⠡⡂⢕⠠⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠄⠳⣬⡀⠀⠀⠠⠁⠂⡀⠀⠀⠠⢔⢖⡱⡥⣊⡔⣑⠜⡸⡰⢱⡈⠀⠉⠀⠀⠠⠐⠁⠌⡐⠠⢁⠔⢈⠔⠈⠂⠀⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠄⠌⡐⠐⠈⠳⡲⢧⣀⠀⠀⠀⠂⠀⢊⠈⠊⡼⢲⢼⣪⠣⡥⢊⠈⠀⠀⠀⠀⢀⠈⡐⠈⢄⠈⠔⠀⡃⠀⠔⠐⠀⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠐⡈⠄⠁⠀⠀⠀⠈⠣⢝⢗⠿⠷⢆⣘⠡⠄⠾⡸⡴⢢⣏⠮⣝⡫⡶⡀⡠⠀⠂⠐⠀⠈⠀⠀⠀⠠⢈⠀⠠⠁⠈⠠⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠀⠀⡈⠀⠂⠄⠁⠀⠀⢀⠰⡶⢩⠫⣣⡈⢣⡘⠀⢠⣟⢗⢯⡪⠪⠱⠠⠁⣄⠆⣀⠀⠀⠀⠀⠀⡀⡀⠌⠀⠀⠄⠐⠁⡁⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢬⠀⠀⠂⠁⠌⠈⡀⠠⠂⠁⢀⠘⣇⠈⡐⣽⢐⡕⡑⠕⣯⠳⢃⠁⡐⠀⠀⠨⠂⢸⣙⢳⡦⠀⠁⢁⠄⢐⠀⠀⠄⠀⠀⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠠⡢⠀⢀⠁⠀⠀⠁⠠⡁⡘⠅⢊⠀⠘⣢⢋⢎⠪⡈⢻⢲⣄⡣⢢⡡⡘⠀⠀⠀⠄⢢⠈⠀⠈⠁⠀⠠⠐⠀⠠⡈⢀⠄⢌⠄⡰⢀⠆⠤⡠⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠰⡂⠄⠀⠀⠀⠀⠀⠊⢠⡈⠢⠀⠉⠱⣨⢃⡀⠐⠔⠄⡕⢌⠻⣶⡠⠱⡑⠠⠀⢈⣂⠀⠀⠀⠀⡀⠐⠄⢊⠐⡐⠔⡈⢂⠜⡠⡡⣊⢊⢆⢪⠂⠀⠀⠀⠀
⠀⠀⠀⠑⠌⡐⠀⠀⠀⠀⢀⢠⠁⠨⠀⠀⠑⡱⠁⠁⡪⠢⡀⢱⢘⢌⡪⠂⡙⡳⣬⡈⡒⢔⢏⢷⢤⠾⡄⢊⢀⡁⡂⢁⠈⠔⠐⢔⠀⢔⠢⡢⣑⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠡⠐⡀⠀⠀⠀⡊⠀⡀⠰⠁⠐⣰⠃⠈⠊⠀⢰⢕⠬⡢⠃⠁⠀⠐⡀⠰⣁⠪⡀⠡⠑⠓⠉⠠⠁⠀⠀⠐⠀⠡⢁⠑⠄⡁⠂⠕⠈⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢈⡀⠀⠀⢆⠠⡀⠨⠀⠀⠁⠀⠀⠀⠠⠀⠊⠑⠉⢹⡱⡲⡌⣆⠸⠀⠀⠑⢌⠄⣀⢀⠁⠀⠀⠀⠀⠀⠀⠀⠄⢘⠠⠑⡈⢐⠁⠢⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠢⡀⠁⠡⡀⠀⠀⠀⠄⢁⠐⡁⠌⠀⠠⢈⠈⠊⠊⠷⣄⠀⠀⠀⠘⣆⢦⡁⠐⠄⠄⠄⡀⣀⢀⠒⠠⡁⠂⠌⠠⡁⡱⢠⠑⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢈⠆⠐⠀⢂⠈⠀⢊⠄⢈⠄⠀⠀⠀⢀⠬⡐⡁⡐⡀⠕⠀⠀⠀⡼⢕⣗⠈⡠⢈⠐⠄⢄⠐⡈⠀⡔⡡⡊⢔⠔⡌⡢⢣⠪⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠪⡁⠢⢀⠐⠀⠂⠌⠀⡂⠀⠔⡀⠡⡀⢈⠌⠠⡈⠂⠁⠄⡀⠀⠘⣿⡃⠠⡈⠀⠡⢂⢑⠄⡌⢢⢘⢌⢎⢪⢊⠮⡨⡓⠄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠩⡈⠢⠡⠂⡌⠈⠀⢁⢀⡂⠡⢀⠊⠀⠀⠌⢀⠐⠄⡀⠈⠀⠀⠊⢌⢡⢑⢌⢆⠊⠂⠑⠈⠂⠓⠁⠁⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠈⠐⠢⠂⡊⠂⠅⠈⠄⡀⠢⠂⠀⠀⠀⠢⠠⡈⡐⢀⢂⠀⠀⠀⠀⠀⠃⠪⡌⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠄⠊⠐⠑⠐⠀⠁⠀⠀⠀⠀⠀⠐⢌⠔⡡⢑⠌⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢂⠕⡌⡪⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Jing Yuan": """
⡔⣄⠠⠂⡐⢠⠈⢝⢝⡿⣻⢿⣟⢟⣯⣻⣻⣟⢿⠄⣪⠶⡻⠻⠿⢿⡿⣟⣿⠅⢀⢢⣾⢟⡟⠝⠥⠀⠄⠄⡰⠫⢻⢝⡯⡫⠂⠀⢀⣔⣝⢿⣻⡿⣿⣿⡻⡫⠂⡠⢚⠙⡡⢂⠢⢂⠆⣘⣠⣟⣽⠱⣿⢿⣿⡻⡫⣟⣽⢫
⣿⢼⣕⢧⡳⣕⢎⡄⢊⠪⡙⡑⠪⡫⡪⠳⢝⢞⢯⡀⢊⣐⡴⣂⡄⠈⠛⡽⠁⡐⢀⣿⠑⠋⠄⠀⠈⠂⢌⠀⠊⠀⠠⠣⠙⠈⠀⢀⠶⡵⣯⣟⣷⡻⣷⢝⢇⢈⠠⢂⠄⠣⣈⣦⣋⣡⣶⡽⠝⢻⡾⡕⣯⡿⣾⢕⠸⣗⣽⢥
⣿⢷⣻⣽⢯⣯⣻⢎⡧⣲⢔⣜⣔⢔⣄⡣⡢⡈⢣⠓⢡⠄⠔⠔⠄⢅⠊⠦⡈⠄⠏⠓⠐⠆⢀⠅⠑⠀⡂⢐⠈⠀⡂⠀⠁⢀⠰⠑⢏⣟⢾⡵⡟⠝⠏⠪⡐⢄⠑⢅⡸⣮⠿⡽⢮⠳⣋⢔⢔⠄⣉⣄⢭⣿⣫⣷⢯⣻⡵⣗
⣿⣻⣽⣯⢿⣞⢷⣝⢯⢾⣝⡮⡾⣵⣣⣟⣵⠃⡁⠂⠁⢀⠀⠂⡀⠀⠀⡀⠱⣦⠂⡪⠐⠔⠀⠠⠀⠡⠀⠅⡐⠀⡀⠀⠀⢊⠀⡢⢀⠈⠃⠋⠊⢌⠊⠚⠠⠁⠤⡀⠉⡚⠙⢊⠒⣍⠂⠵⠑⢞⡕⢑⠟⢳⡻⠳⢯⠳⡫⡋
⡿⡯⡷⣻⡻⡳⣯⡺⣯⡳⣯⡻⣞⣵⢷⣯⢃⠔⠈⠀⠁⣀⠌⠠⠀⠂⠀⠄⠠⡈⢬⠘⠅⠐⠄⠑⠀⡂⠈⠠⠀⠢⠀⠂⢀⠢⢑⠄⡅⠱⢀⢊⠒⠄⠑⢈⠆⠣⡀⠎⣠⠑⠎⠌⠠⠐⠢⠈⡇⠘⠀⡺⠀⢫⣪⡷⣷⣻⣽⡺
⢉⢎⢔⠡⡝⡽⣪⢟⣼⣫⣞⢽⡾⣯⣻⢅⡬⠀⢅⠁⠨⢀⠀⠠⡑⢌⠀⠢⣀⠈⢔⠩⡊⡄⠡⠐⢀⠀⠑⡈⠀⠄⢈⠀⢡⠊⠢⢌⠌⡨⡡⡡⠉⡈⠂⡐⠅⢂⠊⢂⠅⡩⠐⠁⠢⠈⢌⠐⢬⡺⣳⢿⢾⣶⣾⢶⣿⣳⣟⣿
⢪⡗⡽⡢⣌⢘⢜⢯⡺⣶⣝⣯⢻⣝⡥⡿⢡⠢⡨⢡⠈⢆⠠⣈⠎⠒⠓⠢⢨⡣⠑⢉⢘⢄⡐⡡⢀⠑⠠⡀⢁⠄⠢⡑⢀⠁⠃⡂⢔⠰⡂⠠⠪⡀⠱⡀⡪⢠⠁⠄⠠⠄⢈⢀⢂⢊⠆⠑⠄⠹⠕⢟⢻⣞⡷⣟⣷⢯⣿⣽
⠨⡪⡫⡺⣔⢥⡢⡳⣎⠲⡍⠊⠁⡠⣀⢄⢣⢧⠐⣅⢓⠌⠒⠐⠢⠀⡠⡃⢠⠃⢣⡱⣣⠁⡈⠄⠀⡁⠂⠄⠡⡘⠐⠠⠀⠢⠨⢐⠌⡢⠐⡅⢢⢡⠘⢄⠕⠠⡡⠈⣠⠒⡔⢢⠑⡁⡔⡢⡪⡒⢖⠔⡄⠹⡽⣯⣻⣟⣾⣻
⠰⡦⣚⡝⡊⢖⠜⢦⡪⡒⢜⢌⡡⢀⣁⢡⠅⡣⢱⠐⡃⠀⠀⠠⠀⠀⡸⢄⡝⢌⢶⠠⡡⠁⡀⠠⠀⡐⠈⠌⠂⢠⠈⢆⠨⡑⠅⢨⠊⢠⠑⡌⢂⠅⠠⣑⠈⢂⡄⢞⠄⠳⠈⠔⡊⡜⡜⡜⡜⡜⣕⢕⡙⡦⡈⠻⣞⣷⢽⣿
⡺⣕⢯⡺⣝⢮⣫⢳⢎⢏⡌⢢⠐⢄⠐⢀⠔⡱⢈⠦⡡⣑⡢⣀⣤⣪⡸⡰⠁⠞⡳⣁⠠⢀⣀⣂⠀⡈⠀⠂⢌⢂⠑⠤⡀⠪⠐⠐⢕⠠⠢⡢⡡⠃⡘⡀⡀⠁⢸⡄⠔⠒⡘⡉⡈⠪⠜⡜⡪⢎⢮⢪⡕⣕⢍⠂⣹⣞⢷⣝
⡪⣳⢵⡫⣞⡗⣽⡹⡣⢣⠘⠔⠐⠶⡢⡳⡱⡁⣪⠁⡰⣩⢷⡼⡤⠐⢄⢔⣭⣞⣫⡾⣟⢯⣫⠝⠓⠒⠌⡈⠢⠠⢃⡊⢔⠄⡝⡀⢕⢰⡭⣭⢣⡆⠌⢔⠈⢆⠐⡌⣑⢔⠢⠤⣈⠲⢤⣈⢊⠁⡣⢳⢜⢆⠕⠁⡾⣝⡷⣻
⣪⢗⡵⣯⣎⡫⡪⡓⢅⢅⣨⠂⠭⣸⡄⡩⢀⢔⣥⡳⣞⣽⢥⣶⠡⡊⢖⣼⢯⣯⣫⣳⣝⣯⠇⠀⠀⠄⠀⠠⢀⢮⣑⢓⢎⣚⣬⢽⣭⣻⣽⢯⣗⡻⣶⣦⡑⡈⣢⢜⡄⠲⣩⢑⡅⡢⡑⢌⡣⡳⡠⡁⢣⠪⡀⢡⡫⢪⠻⡜
⡷⣝⡽⡮⡾⡽⡎⣿⡺⡗⠡⣊⢖⢓⡼⡢⢴⢱⡷⡫⡺⣜⡷⣳⢸⠘⠂⠀⠑⠲⣵⢟⣾⡕⠰⡀⠎⡐⢀⢂⣗⢷⢩⣎⢯⣷⣻⢿⣶⣝⢾⣯⢿⠝⡖⠭⡉⡝⢔⢆⡙⢦⡱⡱⣍⢎⡺⡢⡪⡪⢢⠕⢄⠑⢠⢆⡕⣱⢝⣎
⡽⣮⢻⡺⣝⢾⢝⡵⣏⠦⠷⢜⡧⠋⣢⢇⡿⣫⣝⢖⠧⡊⣆⢝⣺⠆⡄⠀⠀⠀⢹⡯⣷⡏⢌⠐⢌⠰⡀⠸⣽⢿⡮⢿⣝⢷⣟⡿⢎⢕⠫⡓⡻⠈⢐⠅⠄⡪⡣⡣⢜⠢⡣⢳⢌⢮⡪⡪⡪⢪⠃⠘⢤⠁⣴⢻⢮⣫⠛⠊
⣟⢮⣫⢝⣭⡫⡳⣶⣨⣱⡕⢫⢅⣾⡵⡳⡵⣫⣪⣑⠳⣨⣗⢾⡡⡻⢝⣆⠠⠀⡰⣿⢞⣿⣄⡣⢂⠢⡈⢂⠻⣽⣟⣷⡻⠷⡭⡓⢡⢌⠪⢀⡄⢪⡑⡕⠄⢈⢀⠑⢕⢁⢜⢆⠗⡱⡜⢜⢌⡣⣓⣕⢒⡡⠨⢅⡑⠁⠀⠀
⡧⡳⣑⢋⠒⠝⠕⠕⡃⠚⠘⡛⡺⢗⣿⡺⣦⢏⢮⣮⡵⣟⠜⢷⣭⡫⣎⢿⡄⠨⠢⣿⣻⠓⡕⢨⢒⢕⠬⣄⢅⡈⣑⣟⣏⠫⢂⠡⡆⠕⣠⢏⢞⠄⡣⡪⡪⣊⢕⠭⡢⡣⠳⢝⢍⢎⣪⢶⡳⣝⢵⣕⢯⣞⢟⡶⣆⡀⠀⠀
⡳⡱⣡⢋⢎⠪⡘⡔⣼⣫⣿⣫⢻⠃⠱⣿⣝⢇⣎⡷⡋⠀⠀⠀⠈⢻⡵⣽⡇⡘⢌⣿⠃⢜⡴⣡⢎⣳⢳⣍⢯⣛⡝⡭⢋⣛⣙⠚⠴⢪⡣⣫⢎⢧⢔⢬⣐⢅⡱⡵⡵⣜⣝⢮⢮⢾⣕⢯⡺⠎⠃⠁⠀⢀⠠⠀⠈⠀⡑⣃
⢜⠮⣢⢧⣵⢝⠮⣔⣽⢾⣾⢈⠟⠀⢀⡿⣺⢯⡝⡾⠀⠈⠀⢁⠐⡀⣙⢷⣫⣼⢶⡽⣻⡻⣞⢽⢍⢗⡕⣣⠳⣡⠊⢎⡱⢕⡜⡪⡑⠦⢲⢄⣉⠒⠣⠳⡡⠗⠙⠚⠉⠈⠉⠑⠛⠺⢎⠟⠀⠀⠀⠠⡈⠄⢢⡨⣎⢝⢮⣮
⢞⢏⣓⢭⠲⡑⠇⠜⠫⠳⢏⠨⢣⠁⢰⡯⡷⣫⢮⠇⢀⢐⣤⡵⣞⣾⡻⣯⢷⢯⣳⢿⢵⡫⡮⢣⡑⢗⢔⠦⡫⢊⠬⢣⢓⢕⢭⢪⡍⡛⡴⡣⣝⢙⠕⠂⠀⠀⠀⠀⢀⢄⢂⣦⣨⡂⢎⢀⠀⢄⡀⢐⢄⠷⡣⢳⡘⣕⠽⣎
⡜⢥⢣⢊⢎⢌⢊⢐⠁⠄⡀⠁⠊⡂⢸⡷⣟⣞⣻⢶⣯⢿⡷⣻⣟⢾⠽⠷⢟⢽⢓⢏⠚⠕⠝⠥⠪⢎⢎⡳⣅⣋⣩⢵⡣⣫⢚⢆⢾⡸⡪⡲⣔⣍⡃⠀⠀⡀⠠⡈⢢⡡⢍⢎⠻⡁⢧⢨⢕⠕⡜⣥⢃⡳⡱⢧⠽⣘⢓⢎
⢪⡣⡱⡱⢌⢆⢅⠢⠁⠂⠄⡈⠠⣸⣟⠞⢋⢋⢋⡩⣉⢍⣜⢒⡕⣛⢛⣟⣮⢣⠣⣩⣉⢓⢒⠖⠴⠤⣄⠨⡐⢩⠬⣎⡺⡱⡥⡻⠔⠑⠉⠊⡈⠊⠊⠂⠴⢤⢢⢬⠢⡫⢪⢆⢗⠱⣅⢳⣘⢎⢎⠥⡩⣊⢎⠲⠕⡩⣊⢗
⢆⠷⡵⣮⢖⡔⢅⢃⠙⠠⠥⡴⣞⠷⠛⡡⠈⢢⢡⠊⢼⣯⢗⣯⢟⣿⣻⣽⢎⠧⡑⢆⠢⡱⡡⡑⢕⠱⡨⠣⡪⣂⢳⢘⢜⠳⠈⠀⠀⠀⠔⡀⢂⢄⡢⣆⢖⢦⠲⠒⠗⢑⢃⣃⢥⡰⡣⣎⢆⠓⣑⢡⣈⢄⠡⡑⣑⠜⡬⡪
⡝⣪⠸⡷⢯⡐⢕⠌⡊⢢⠠⡠⢀⢄⣅⠔⠥⡅⢕⢹⡻⣞⣽⢞⣿⡵⣿⠎⡎⡢⡑⢅⠣⠢⡘⢌⢊⠪⡘⢌⠢⢅⠕⢥⠋⠀⠀⠀⠀⠑⠄⣬⢖⡭⢪⡲⡱⡲⣍⢏⣫⢋⡥⡕⢧⡊⡷⣸⡪⣫⢎⣕⡪⡱⡫⣜⠤⡋⡒⠕
    """,
    "Agnes Tachyon": """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣄⡀⠀⠀⣀⡀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣶⣌⢠⣘⣧⢦⣀⢤⡴⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢀⡷⡑⣔⣯⣓⣝⢵⢾⣜⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣤⣻⢝⢮⠷⣱⡝⡵⡗⡷⡵⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠔⣯⡻⡮⣗⢽⡑⠓⣸⢝⠖⢽⣞⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣏⢯⡷⣝⢮⡕⠀⡡⡀⢄⣿⠎⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⢩⣟⢺⣳⣛⠦⣄⣦⣮⡗⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡉⠞⠓⠪⡏⢾⡾⣽⡪⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⢐⠀⡂⢠⠀⠀⠀⠀⠎⢶⡀⠆⣀⠈⢙⢶⢽⣈⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠁⢡⠀⠄⢱⠁⡂⠀⠀⠀⠒⠥⣏⠔⠉⠀⠀⡆⡐⢪⠵⢀⠂⠀⡀⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠘⠃⠀⡀⠨⡐⢁⠈⠄⠐⠄⠐⡐⠀⡭⡢⠂⠄⢸⠨⡲⢰⠜⡜⠄⢢⢹⡱⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠶⠀⠀⠂⠀⠢⢀⠡⠀⠡⠑⠌⠔⠘⡵⢉⢧⠐⠀⡏⢜⡪⢺⡇⣙⢔⢅⠮⣘⢅⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡾⡃⠀⠀⢀⠁⠐⠩⣀⠂⠈⠄⠘⢄⠳⡜⢃⠦⠊⣇⠀⢗⠕⡕⣝⢇⠮⡸⡢⢣⠪⡪⣂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⢕⣝⡪⡓⢶⠶⡶⠷⠄⠈⠂⡁⠢⢠⡡⠎⠁⡐⢄⠡⢓⠆⡸⡱⣜⣯⣳⠹⣌⠇⡜⣑⢕⢬⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠘⠃⠉⠀⢀⣀⣤⣄⡚⡒⠱⠀⠂⡰⡀⠁⠀⢸⢡⢎⡲⣝⣾⡽⢸⡪⡒⢌⢆⢱⠁⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢀⠤⣐⢲⡪⣻⡳⣛⡬⢢⡛⣠⠀⠑⠔⠈⠀⠈⡀⠰⢧⢪⡳⢯⡾⣽⣃⠓⠡⠃⠊⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⡰⣔⢕⢷⣜⢵⢝⠞⣩⡠⢂⠟⣥⡚⣫⢔⠇⠐⣁⡈⠀⡂⢀⠄⣺⢃⠵⣴⡫⣾⢯⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣒⠢⢤⡣⣏⢞⡭⡳⠜⣈⢔⠱⠐⠄⠈⢘⠨⡞⡌⡵⡽⢋⡴⡠⡦⠈⠶⡴⣫⢕⠒⠘⣮⣻⡵⣳⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡳⡕⠙⣄⠔⠊⠀⠄⠀⠀⠈⠠⢀⠠⠆⠾⠺⣤⠟⣢⠾⠂⣠⠻⡜⣄⡣⠳⡌⠪⣪⢟⡮⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠄⡰⠈⠊⢀⠀⡁⢈⠀⡀⠡⢴⠔⠕⢁⠀⠐⢘⣁⠿⠊⢷⣨⣕⣝⡴⣮⣼⣵⡾⣷⣧⡻⣞⢾⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⠤⡄⠆⠋⢀⠈⡐⠀⡐⠠⢀⢂⠬⠋⠎⢀⠂⢀⠁⠄⡀⡀⢁⢴⣿⣥⣝⣊⣺⢯⡿⣽⣞⢷⣝⢷⡝⣮⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⠒⠀⠀⠄⢁⠠⠀⠌⣠⠢⠊⠀⡰⠈⠄⠂⠠⠀⠄⠠⠸⣦⣏⢲⢳⡷⣝⢮⡯⣻⡙⡳⣯⣟⣽⣫⢿⡞⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠄⠡⡘⠔⠁⠀⡠⠋⢀⠅⡐⢁⢂⢁⠊⢠⣾⢯⡻⡧⡩⣿⣺⡳⣯⣻⢕⢭⡪⣝⣮⣟⣽⣻⢽⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⠀⠀⠠⠜⢀⠊⢄⠢⠨⡀⠢⠰⠆⢿⣟⢎⢿⡙⡆⠘⣷⢻⡮⣿⠢⣣⣾⡺⣗⣯⡾⣽⡳⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠰⡉⡐⠄⡑⠠⢊⠐⡐⠠⠂⠀⠈⢯⡏⢮⣳⣱⠀⣹⣟⢾⢷⣞⢟⣮⡻⣞⢗⡫⡵⣝⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠤⡈⠢⠁⠌⡠⠁⠀⠀⠀⠀⠹⡕⢮⡳⡄⣺⡵⣟⡗⣽⣫⠎⠋⢀⢭⠚⡮⣺⢮⡂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠌⢀⠑⠐⠀⠀⠀⠀⠀⠀⣀⣈⣧⢻⣝⣾⡝⣾⢇⠃⠁⠀⠀⠣⠘⠀⠈⠳⣫⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠁⠀⠀⠀⢠⠴⠞⣏⢳⢜⣗⠷⣽⣞⣽⣻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⡱⡫⣪⠪⠻⣺⢷⣳⡽⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢏⡺⡨⠃⢡⠀⢀⡟⠈⢯⣟⣽⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢮⠅⠀⠀⠙⠈⠀⠀⠈⢿⢮⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣽⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⢿⠄⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢌⠢⡣⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠓⢔⠱⠀⠔⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠚⠑⠚⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Special Week": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡖⢄⣀⢤⠔⠤⣤⣀⢶⡻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢜⢧⢻⡌⠁⠀⠀⠳⢝⣝⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡷⣓⠀⡀⠃⠀⡘⣗⢗⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣽⢅⣠⡄⠀⠐⣤⠌⣯⡻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢉⣾⡇⠉⠀⠠⠀⢁⠁⣿⡝⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠼⠞⣿⣀⠀⠉⠑⢀⠼⣯⡻⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⣄⠍⡈⢣⢨⡕⢥⣐⠡⢁⠂⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⢓⠰⢈⠆⣝⢖⡥⠏⡪⠃⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠄⠙⠀⠀⢢⡫⡞⠐⠱⠘⠔⠀⠀⠈⠂⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠀⠀⠀⣁⣔⣉⣻⠈⠀⠀⠀⠀⡂⢄⢐⠔⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⢪⡗⡵⣭⣀⡂⠀⠨⠀⠀⠉⠐⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣅⢶⢏⡺⠆⣽⢹⡗⡖⠖⠀⠀⠀⠈⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⡱⠯⠱⣝⣝⢎⡗⡽⣩⠇⠀⠀⠀⠀⠀⠐⢈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠂⠀⠉⠊⠉⠀⠀⠱⡃⠀⠀⠀⠀⠀⠀⠀⠀⠅⠀⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢆⢖⠦⡂⠀⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⢅⠔⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢪⡒⠭⣪⢷⢭⠀⢁⠄⠀⠀⢀⠀⠀⠀⠆⠂⠀⠀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠁⢈⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢎⠚⠦⣫⢫⡲⡢⡤⡲⡩⢦⡠⣔⢄⡶⢤⢢⠀⡈⢄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠪⡡⠛⢎⢞⢜⣎⢳⢕⡵⡵⣹⠪⣗⠵⣢⢠⣈⢶⡳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠢⢝⠆⡕⢵⠪⠲⣐⠦⣣⢜⢝⢬⡣⡧⡹⢣⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⡀⢈⠀⠀⢀⣿⣧⠈⠚⢦⡅⠕⠈⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠴⡳⠈⠀⠀⠀⠀⠀⢐⣷⢻⣆⠀⠀⠀⢤⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠀⢐⣯⣟⢾⡀⠀⠀⠐⢎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⢮⡟⠇⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠂⠀⠀⠀⠀⠀⠈⡷⠝⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⢈⠃⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⢀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣤⠂⢀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣆⠀⠳⠢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⢂⠨⡄⠜⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⡶⣥⠊⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠖⠁⠠⡊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣣⢗⡽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠠⠊⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣫⡺⣪⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⢺⢕⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠉⠙⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Silence Suzuka": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢜⡅⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⡅⢸⡍⡨⠤⡠⡀⣖⠝⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡰⠃⡝⡜⠤⡨⡎⢔⠨⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡪⡓⢌⢎⢆⠓⡜⢌⠢⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⡱⡡⠍⠋⡁⠀⠡⠓⡌⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡳⡺⣈⠇⠀⢀⠐⠀⡸⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡽⡪⡪⠦⢅⠄⣠⢞⢝⡕⢷⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠏⠈⠊⠳⡲⣍⢎⠳⡙⠘⢳⢄⠑⠦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡫⡀⠀⠀⠈⢔⢊⣔⢷⣭⣢⡀⠫⢲⡀⣟⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡢⢧⢝⡀⠀⡀⣔⡠⠑⣻⣮⠚⣷⡻⣀⢄⣗⣙⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣔⢏⡞⣕⢝⢦⠺⡨⠶⠴⠀⠳⠝⡃⢈⢿⠔⡳⢬⠺⡵⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢪⢎⡾⣱⡫⠎⠀⢹⡘⡵⡀⢠⠀⠢⠠⢌⢇⢳⢑⢯⢺⣕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡳⣝⢮⡺⠲⠍⠀⠀⠀⣎⢒⡷⡴⣤⢞⢷⣂⠕⡵⣫⡓⡷⣜⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡽⡪⢧⡀⠀⢀⣀⡀⠀⠸⣯⢞⢷⠵⡫⢫⠃⣸⡳⢕⡟⠜⠚⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠃⢀⡴⣹⢣⠯⠪⣀⡀⢱⡩⠣⠣⡀⠐⠄⠓⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣔⢝⠮⠃⠀⠀⠒⠤⠨⣘⢢⣡⡦⡱⠀⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⢬⢯⠁⠀⠀⠠⠀⢀⠀⠀⢡⢗⣝⢧⢑⠊⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⡕⣳⡃⠀⠀⡐⠀⠄⠀⠀⠂⢸⡣⣟⢾⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢗⢭⡪⡇⠀⡔⠤⣈⢀⠂⢠⠀⢀⠻⣪⠇⠀⠀⡀⣁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢕⢵⡹⡆⠸⡨⣑⠂⠜⢌⢌⡔⡰⣀⣊⣐⢁⢎⢌⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢜⡕⡵⣹⢣⠔⢧⡨⣈⢃⠒⠔⠠⠌⠤⠤⠄⠥⠂⠂⣊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣝⢎⢷⡂⠀⠈⠨⠙⣣⢟⡶⡲⣖⢶⢲⠒⠋⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡇⢎⡳⡝⣮⡂⠀⠀⠀⢼⡳⣝⢮⢯⣫⡛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⡘⣕⠽⣜⢽⣄⠀⠀⣸⢳⡝⣮⢳⢵⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠪⣎⠾⣌⠳⣤⣫⡳⣝⡼⣳⠯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢝⢮⢳⢳⣜⡳⢫⣞⢵⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡷⣣⡳⡍⢸⣎⢷⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢟⣮⡓⠉⢱⡳⣝⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣗⠵⠀⠀⢸⣝⢮⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢼⠃⠀⠀⢸⢮⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡝⠇⠀⠀⠀⣞⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡹⠀⠀⠀⣠⢗⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣴⢆⠀⠠⣏⣾⡹⣧⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⠀⠐⠍⠑⠀⢳⢼⣝⢮⣳⢝⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠦⠀⠀⡀⠀⠈⠃⠈⠳⢝⢷⢵⡝⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Tokai Teio": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⡀⠀⠀⠀⠀⢤⣖⣐⣞⢿⡧⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣟⠷⣒⡿⠀⠘⣭⢷⡹⡯⣾⢝⣭⢯⡳⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠖⠚⣼⢫⡾⣃⠀⠘⢎⢖⡵⣩⢏⢾⡝⡽⡶⣍⢷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣓⢖⡏⢱⠍⢦⢈⠱⠎⢞⢎⣴⢽⢵⡛⠺⣣⢝⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡹⡜⢁⣁⠙⠢⠅⣶⡶⢨⡏⣳⢝⡄⠫⡄⠈⠳⡵⡫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣮⢧⠙⠋⠀⠀⠀⠀⠠⠠⣿⠸⠁⠀⠀⠈⠀⢸⡹⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠛⣧⠀⠁⠔⠅⠊⠀⡰⠯⠃⠀⠀⠀⠀⠀⢸⣳⡻⣻⡭⣽⣢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡞⠧⡔⡍⢢⢤⠁⢌⣸⢱⢀⡀⢀⡀⠀⠀⠀⠈⠑⠋⠁⠀⠁⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⣀⠀⠷⡓⡄⠸⡓⠖⠭⠛⠃⠚⠀⢿⡳⡶⣤⣀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢄⠀⠈⠲⡷⣄⡪⡙⠀⢔⠪⡀⡀⠀⡠⠄⣿⡹⡞⠕⠉⠑⠄⠀⠀⢰⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣦⣆⡀⣼⣴⡿⡼⢆⢥⠏⠰⢄⢑⡐⠴⡹⠀⠞⠉⠀⡀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠞⣟⡿⣻⠞⠃⡻⡪⡆⠱⡱⠴⢤⠑⢧⡟⠀⠀⣌⢍⢺⡿⣻⣧⡀⠀⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢹⢮⡠⠁⠁⢱⠸⠠⡚⣅⠀⠀⡷⣲⡅⣿⢮⢷⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⢖⠑⡀⠀⠀⠙⠉⢓⡼⡀⠀⠈⠚⠑⠛⠓⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢇⣏⠃⠀⡀⠠⣀⠚⣡⡫⠺⠕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠣⡻⠔⠋⠙⠀⠁⢀⠀⠀⠀⡀⠀⠂⡁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠊⠀⢀⠑⢄⢈⣔⢀⣤⢄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠁⠀⠀⡢⠀⣤⣈⣤⢜⡭⣗⢾⡇⠙⠾⣵⣯⣮⡹⣛⠶⢶⡤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⢴⢻⣄⣄⠶⣲⡴⣪⡣⢿⠕⠡⡈⡈⢁⢐⣍⠰⠠⠸⢦⣫⣝⢝⣝⢞⡽⣳⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠷⠪⠓⠟⠴⡕⢝⠗⠝⠁⠀⠀⡐⢁⠐⠠⠁⠄⠀⠀⠀⠀⠀⠈⠊⠷⢝⣎⢷⡹⣎⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠠⠀⠃⡀⠀⠀⠀⠠⠁⠌⠂⠁⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠙⣮⡝⣮⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠄⠠⡀⠀⠀⠀⠀⠈⡀⠄⠐⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⢯⣽⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⠠⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢈⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠘⠸⣾⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠌⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠄⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣟⠂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⠀⠂⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠠⠀⠄⣠⡀⠀⠀⠀⠀⠀⢐⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠟⠀⢀⠀⡂⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⠊⡠⠀⠠⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⠁⠐⢀⠀⡅⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠀⡠⠁⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⡦⣤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠞⣹⠣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡱⡈⢛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠖⠁⠔⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠄⢀⠈⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠈⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⠠⠀⢁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠀⠐⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠁⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠲⠚⠒⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠀⢠⠄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Gold Ship": """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⡨⣛⢞⡖⡱⣄⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠣⠘⠳⠾⢔⣩⣔⡝⠀⢀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⠛⡀⢁⠄⠀⠀⠀⠈⠄⠰⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⠋⠰⠀⠢⢁⠊⠀⢌⠀⠄⡑⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡅⠁⡈⠐⠠⠁⠐⢁⢐⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢢⡃⠈⠋⠋⠀⠀⠠⣅⣀⢨⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠐⠄⠀⠀⠀⠼⡱⣃⠀⠂⠠⠀⠁⢀⠀⢨⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠁⠔⠈⠀⢀⠊⡔⢍⠦⡀⠀⠐⠀⡀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡁⠀⠀⠀⡤⡋⡜⡪⣂⣌⠠⡈⣶⣜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⡠⡊⠖⠌⠎⢈⢹⣯⣷⠖⠳⢟⢷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠂⢀⠈⠢⡕⠉⠀⡀⠀⢢⣞⢕⢛⡲⢧⡤⡾⡹⢦⡄⣄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⡤⠤⠠⠤⠔⡵⣄⠀⡀⢐⣿⣘⢗⡆⢽⣪⣞⡽⣞⢷⡽⣸⣇⠝⢠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡨⡉⠋⠛⠙⢉⣥⠘⡦⢪⢰⢯⣫⣯⣻⢸⢷⡽⣞⣽⢯⡞⡼⠊⠠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⡐⣍⠪⡄⠀⠀⠌⢀⠺⡔⡕⡕⣵⠶⣟⢮⣷⠮⣟⣟⡻⣛⢞⣻⡍⡀⠀⣀⣄⢀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⡊⣆⢣⠪⡊⠦⡄⣅⢎⢎⠳⡸⢌⢎⢮⢠⡟⣜⢪⢇⢗⠼⡹⣍⠮⢰⡣⣙⠈⠀⠈⢉⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠌⢦⠑⢔⠕⡱⣉⢎⠲⠈⡔⣅⢫⠪⡪⣒⢕⡑⢷⡜⣕⢕⢨⡕⡳⢜⢮⡘⡦⢃⠀⠈⠠⠄⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⡙⠆⢑⢅⠫⡢⡊⠂⠀⡨⠲⡌⣎⢱⡑⣎⢪⢪⢒⢯⡪⣕⢅⣍⢞⡱⡣⣆⢻⡄⠀⣈⠪⡢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠐⠌⡎⠀⠅⡪⡱⠌⠀⠀⠀⢎⢕⢜⢄⠧⢪⠢⡣⡣⢘⡵⡱⢎⢆⢧⢫⢮⣞⢾⢫⣯⡀⠣⡂⠱⡡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠅⢈⠐⡕⡌⠀⠀⠀⠀⢗⠰⡑⡬⢐⢧⡯⣮⣪⢞⢜⡕⢫⣖⣫⡷⡳⡝⡵⡂⢮⡳⣀⢈⠄⢪⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡀⠀⠀⠀⠀⢣⠘⡬⠂⡼⣻⡞⢶⡵⣥⢮⡴⡇⣹⣗⢻⢞⠽⡷⠷⠞⣾⣻⢆⢂⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠋⢢⢱⡿⣝⣯⡻⣞⢕⢾⠠⡣⣫⢳⡝⣵⡙⣧⢱⢱⡪⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣯⡽⡼⡮⣻⢝⢎⠷⢸⡁⡷⣱⢳⡪⣞⣜⠸⡄⡷⡹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢝⡮⣪⢳⢝⣝⢰⠅⡯⣪⢳⢕⡮⣪⡃⢧⢸⡳⣽⣃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠼⢯⢺⡜⣕⢯⡪⡮⢰⡃⢞⣕⢏⠞⠼⠕⣝⠸⢐⠗⠮⡫⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⡡⠂⠎⢌⠱⡉⢚⠠⠁⠁⠀⠀⢅⠑⠔⠠⡐⠄⢪⢂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⢇⢥⣀⡀⡈⢂⠂⠀⠀⠀⠀⡀⠈⠈⠀⠀⠀⡪⡢⣑⢍⠢⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⠊⡀⠙⠱⠝⠽⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⣕⠜⢔⠥⣃⢊⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⢀⠂⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠉⢢⠱⡅⡕⡡⢫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠄⠀⠀⠀⢕⠸⡜⢔⠡⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⡀⠀⠀⠀⢆⢝⡸⡂⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢄⠠⢀⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⡄⠀⠀⠀⢊⠦⠁⠠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⢀⠀⠢⡁⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠡⠈⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠠⠀⡀⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠐⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⢈⠂⢀⠄⡱⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠈⠠⠈⡀⠠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠆⢠⣇⡨⢂⡄⢐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣖⠀⠐⣐⠄⣱⡄⠱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣬⣟⣷⡽⡏⡠⡢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠢⣿⣳⡾⣤⢺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⣻⣮⣟⡽⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⡷⣳⡿⡽⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣟⣮⢵⣫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣽⡈⠿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⡱⠇⢸⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣟⡺⠱⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡳⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡫⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠃⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⡀⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⡀⡐⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠐⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Crash Bandicoot": """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⣼⠀⠀⠀⡅⡜⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠀⠈⠀⠀⠈⠀⠀⠀⢀⠀⠁⠀⠀⠁⠀⠈⠀⢀⠈⠀⠀⠈⠀⠀⠈⠀⢰⣿⡆⢀⠄⣧⡇⠀⠀⢠⣟⠀⠀⠐⠀⠈⠀⠀⠀⠀⡀⠈⠀⠀⠁⠀⠀⠁⠀⡀⠁
⠀⠠⠀⠀⠄⠀⠁⠀⡀⠈⠀⠀⠀⠀⠈⠀⠀⠈⠀⢀⠀⠀⠀⠁⠀⠀⠁⠀⢀⣿⣿⡇⢸⣧⣿⠇⠀⢀⣟⣾⠀⠀⠀⠀⠀⠄⠈⠀⠀⠀⠀⠄⠀⠂⠀⠁⠀⡀⠀⠀
⠐⠀⠀⠠⠀⠀⠠⠀⠀⠀⠀⠀⠂⠀⠐⠀⠀⠐⠀⠀⠀⠀⡀⠐⠀⠀⠂⠀⣼⣏⢿⣿⣸⡳⡯⣣⠤⠾⠝⣿⠀⠀⣴⣾⠖⠀⠀⠀⠀⠂⠀⠀⠀⢀⠀⠄⠀⠀⠀⠀
⠀⠀⠀⡀⠀⠀⡀⠀⢀⠀⠁⠀⡀⠀⠠⠀⠁⠀⠀⠀⠄⠀⠀⠀⠀⠀⠄⠀⣿⢾⡳⡵⣫⢞⠉⠴⣷⢖⢤⡻⣒⢟⠛⠉⠀⠀⠀⠈⠀⠀⠀⠂⠀⠀⠀⠀⠀⠠⠀⠈
⠀⠐⠀⠀⢀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⢀⠀⠁⠀⠀⠀⠄⠈⠀⠀⠀⠀⡿⡵⣫⡻⡜⣏⡳⣮⡲⡯⣮⣳⡽⠉⠀⠀⠀⠀⠀⠠⠀⠈⠀⠀⠀⠐⠀⠈⠀⠀⠀⠀
⠐⠀⠀⠀⣀⠀⠐⠀⠈⠀⠀⠀⠀⡀⠈⠀⠀⠀⠀⡀⠈⠀⠀⠀⢀⠀⠁⢰⡫⣞⡕⣝⡺⣝⡽⣾⡽⣿⠞⠃⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⢀⠀⠁⠀⠀⠀⡀⠀⠈⠀
⡀⠀⠈⠀⠀⠳⣦⣀⠀⠠⠀⠠⠀⠀⠀⡀⠀⠠⠀⠀⠀⡀⠀⢄⣀⣄⢤⡫⣺⢵⢹⣿⣿⣷⣾⣾⣿⢏⡾⣤⣀⠀⠀⠀⠄⠀⠠⠀⠈⠀⠀⠀⢀⠀⠁⠀⠀⡴⠀⠀
⠀⠤⠤⣤⣠⣄⣹⡝⣿⣦⣄⠀⠀⠀⠀⠀⡀⣠⡤⡶⢶⣚⢏⡯⣲⢕⣗⢽⣕⢇⣽⣿⣿⣿⣿⣿⢏⣾⡵⣧⣫⢗⢷⢦⣤⡀⠀⠀⠀⡀⠐⠀⠀⠀⢀⡤⡿⢁⡠⠂
⠀⠀⠀⠀⠁⣙⣮⣻⣾⣿⣟⣷⣠⢴⣓⢯⣫⢳⡝⣮⢳⣝⢮⢷⣽⣳⣽⢷⡽⣠⡛⠻⠻⠿⠿⡏⠉⠉⠈⠁⠉⠉⠙⠚⠲⠯⡻⣖⣤⣀⣤⣶⣾⣿⣟⢮⣛⢮⠄⠀
⢀⠤⠴⠚⠛⠋⠊⠁⠈⡼⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣿⡺⣦⣙⢦⡦⡶⡕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠻⣿⣟⠿⠿⠕⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠜⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢵⢇⢞⢕⡝⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣯⡳⡕⣝⠪⡮⠀⠀⠀⠀⠀⠁⠀⠀⠠⠀⠀⢀⠀⠀⢀⠀⠀⠀⠀⠈⠡⠀⠀⠀⠀⠀⠄
⠀⠄⠀⠂⠀⠀⠂⠀⠠⠀⠀⠠⠀⠀⠐⠀⠀⠂⠀⠈⠀⠀⠈⠀⠀⠀⢸⣎⢞⢜⣬⢓⠅⠀⠀⠀⠀⠐⠀⠈⠀⠀⠀⠄⠀⠀⠠⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀
⡀⠀⠀⡀⠐⠀⢀⠀⢀⠀⠀⢀⠀⠐⠀⠀⠀⡀⠀⠂⠀⠐⠀⠀⠈⠀⢸⣎⢧⣹⣿⠧⠀⠀⠀⠀⠁⠀⠀⠀⡀⠀⠂⠀⠀⠐⠀⠀⠀⡀⠀⠂⠀⠐⠀⠀⠁⠀⡀⠀
⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠈⠀⠀⠀⡀⠀⢀⠀⠈⠀⠀⣾⣪⢇⢮⢱⡃⠀⠀⡀⠀⠂⠀⠁⠀⠀⠀⡀⠀⠀⠄⠀⠠⠀⠀⠀⡀⠀⠀⠄⠀⠄⠀⠀⠀
⠐⠀⠀⠀⢀⠀⠂⠀⠐⠀⠀⠀⠠⠀⠐⠀⠀⠠⠀⠀⠀⠀⠀⠠⠀⠀⣷⣿⡾⣷⣷⡇⠀⠀⠀⠀⠀⠀⠄⠀⠐⠀⠀⠀⠄⠀⠀⠄⠀⠠⠀⠀⠀⢀⠀⠀⠀⠀⠐⠀
⠀⠀⠀⡀⠀⠀⠀⠀⠀⠄⠀⠁⠀⠀⠀⠀⠐⠀⠀⠐⠀⠈⠀⠀⠀⢨⣿⡿⣿⢿⣿⣧⠀⠀⠀⠀⠁⠀⠀⠀⢀⠀⠀⡀⠀⠀⡀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠁⠀⡀⠀
⠈⠀⠀⠀⢀⠀⠁⠀⠄⠀⠀⡀⠀⠐⠀⠁⠀⠀⠀⡀⠀⠀⠄⠀⠀⣺⣿⢿⡟⠀⢻⣿⣷⡀⠀⠁⠀⠀⠐⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠁⠀⡀⠀⠀⠄⠈⠀⠀⠀⠀
⠐⠀⠀⠁⠀⠀⠀⠀⠀⠀⡀⠀⠀⡀⠀⠀⡀⠈⠀⠀⠀⢀⠀⠠⢠⣿⡿⣿⠁⠀⠀⠻⣿⣷⡄⠀⠀⠈⠀⠀⠐⠀⠀⠁⠀⠀⠀⢀⠀⠂⠀⠀⠀⢀⠀⠀⢀⠀⠂⠀
⢀⠀⠀⠄⠀⠀⡀⠁⠀⡀⠀⠀⡀⠀⠀⡀⠀⠀⡀⠀⠄⠀⠀⠀⣸⣯⢿⠃⠀⠀⠀⠀⠹⣿⣿⡄⠈⠀⠀⠀⠠⠀⠀⠄⠀⠈⠀⠀⠀⠀⡀⠀⠂⠀⠀⢀⠀⠀⠀⠀
⠀⠀⠀⡀⠠⠀⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢠⣟⢾⡏⠀⠀⠀⠀⠀⠀⠹⣿⣻⣄⠀⠀⠁⠀⠀⠀⠀⠀⠐⠀⠀⠐⠀⠀⠀⠀⠀⠄⠀⠀⠀⠀⠁
⠀⠠⠀⠀⠀⠀⠀⡀⠈⠀⠀⠀⠀⡀⠈⠀⠀⠈⠀⢀⠀⠁⠀⣾⢝⣷⠁⠀⠀⠀⢀⠀⠀⠀⠸⣿⣻⣧⡀⠀⠐⠀⠀⠁⠀⠠⠀⠂⠀⠀⢀⠀⠁⠀⠀⠀⢀⠈⠀⠀
⠂⠀⠀⡀⠀⠠⠀⠀⠀⡀⠈⠀⠀⠀⠀⠀⠁⠀⡀⠀⠀⠀⣼⢻⢮⡇⠀⠀⠀⠀⠀⠀⡀⠀⠀⠹⣷⢷⣳⡄⠀⠀⠀⠂⠀⠀⠀⠀⠀⠠⠀⠀⢀⠀⠐⠀⠀⠀⢀⠀
⠀⠀⠀⠀⠀⠀⡀⠠⠀⠀⠀⢀⠀⠂⠀⠀⠂⠀⠀⠀⠀⠈⣯⣁⡉⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠙⣿⣑⣉⠀⠀⠂⠀⠀⡈⠀⠀⠂⠀⠀⠀⠀⠀⠀⡀⠐⠀⠀⠀
⠀⠁⠀⠁⠀⡀⠀⠀⠀⠀⠄⠀⠀⢀⠀⠁⠀⠀⠠⠀⠁⢰⣿⣯⣷⣄⡀⢀⠀⠁⠀⡀⠐⠀⠀⠀⠀⣿⣿⣿⣦⣴⣶⣧⣿⣿⣶⡄⠀⠐⠀⠀⠁⠀⡀⠀⠀⠀⠀⡀
⠀⠄⠀⠄⠀⠀⠀⠀⠐⠀⠀⠀⠄⠀⠀⠀⠀⠠⠀⠀⢀⣾⣿⣿⣽⣿⣿⡄⠀⠀⠀⠀⠀⠀⠐⠀⠀⡟⡟⢿⠻⠿⠿⡿⠿⠿⠿⠿⢆⠀⠀⠀⠂⠀⠀⠀⠀⠐⠀⠀
⠀⠀⠀⠀⠀⢀⠀⠁⠀⢀⠀⠂⠀⠀⢀⠀⠁⠀⠀⠀⠸⠭⠭⠭⡩⠍⠕⠂⠀⠀⠐⠀⠀⠂⠀⠀⠀⠀⠉⠈⠁⠉⠈⠉⠉⠉⠁⠉⠀⠀⠀⠂⠀⠀⠂⠀⠁⠀⢀⠀
⠈⠀⠀⠁⠀⠀⠀⠀⠄⠀⠀⠀⠀⠄⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠀⠠⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠠⠀⠀⠠⠀⠀⠀
    """,
    "Vergil": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⡈⠄⠠⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣱⠱⢄⢅⢢⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢔⠇⡠⠀⡈⢂⡃⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣇⠙⢙⠈⡫⡍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡝⢾⣂⣑⢲⣑⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡠⣤⢞⢵⢫⢗⢕⣮⣥⣇⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⢟⣿⡣⡷⣝⢝⣧⢳⡡⡹⣓⢞⣿⣼⢹⠽⣧⠤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⡯⣞⢟⡯⣞⢷⡵⢧⢳⢹⢸⡵⣼⡿⡼⡗⣿⣇⢆⢹⢗⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣟⣞⢞⣿⣕⢿⣜⢷⣻⣕⡽⡪⡾⣕⣿⣿⡕⣿⣿⢸⠌⣟⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣮⢳⢯⢾⣽⣗⣽⣫⣷⣚⢧⢧⣟⣖⡿⣽⣷⣿⣿⡏⡧⣳⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⡷⣹⢯⡷⣳⣟⣮⢷⢯⣮⢯⢾⢧⣻⡿⣯⣿⣿⣽⣯⡇⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣗⢿⢵⣻⣺⣹⣷⢯⣻⣇⢷⡞⣳⢿⣼⣿⣞⣿⣿⡾⣷⡫⣿⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡿⣝⡷⣫⡷⡧⣻⣽⡿⣵⡟⣲⣯⡻⣓⣿⣷⣽⣿⣻⡾⣿⣹⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣟⡵⣟⣽⣏⡗⢸⣷⢿⡾⣮⣏⡾⣽⢷⣿⣷⢿⣿⣯⢿⣿⢮⣿⣾⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢾⣝⣾⣮⢧⠃⢨⣿⢷⡻⣪⣾⣝⡾⣾⣿⣾⢿⣟⣷⣟⣿⣗⢿⡷⣟⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣟⡷⣝⣾⡳⢯⠀⢨⣿⣻⡽⣏⣾⡵⢷⣿⣷⣿⡿⣿⡿⣯⡿⣿⢼⡿⣽⣭⣓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣯⡻⣞⣓⣿⡑⠀⢸⣿⡽⣫⣾⣫⡟⣾⣿⡷⣯⣿⣿⢿⣿⣽⣿⣏⣿⡻⣾⣕⠥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣯⢟⣽⠯⣗⠅⢠⣿⣯⣟⢽⡷⣯⢻⣿⣿⢿⣟⡿⣿⣿⡿⡷⣻⣿⣞⣿⡽⣯⣟⣂⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣯⣻⣽⢟⡯⠀⣼⣿⢾⣵⣿⣻⣝⣿⢟⣿⢿⣿⡿⣿⢿⡾⡿⣵⢺⣷⡹⣿⣳⣿⣿⡮⠳⢂⠀⡀⢀⢀⡀⣀⣴⡶⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢾⣧⣿⣾⠃⢰⣿⣟⢷⣟⣾⡽⣼⡷⣻⡯⣿⣽⣻⣻⣯⣟⡿⣵⣭⣻⡟⣿⠿⣷⣿⢷⣟⣞⣽⠭⠯⠯⠾⠼⠼⠟⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣻⢷⡷⣾⠇⣸⣯⣯⢿⣯⡾⣽⢷⢿⢯⣟⡿⣾⣻⡷⣿⢾⣿⣳⡧⡺⣿⡓⢞⣾⢿⡿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣟⣿⣻⣳⣴⣿⣯⣻⣟⣾⣳⣟⣿⣻⣯⣿⣽⣿⣽⣟⣿⣫⣷⣿⣽⡿⣸⣧⠀⠀⠘⠮⡀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⣵⣵⣯⡍⣾⣯⣾⡿⣽⣳⣯⣿⣽⡷⣿⣾⣷⣿⣽⣿⣽⣿⣯⣿⢾⣷⣵⢿⡄⠀⠀⠀⠈⠣⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⣷⢿⡾⣷⣽⢷⣟⡿⣵⣿⣞⣷⣟⣿⣿⣽⣷⣿⢿⣯⣿⣻⣾⢿⣿⣾⣫⢿⣧⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⣿⢰⣷⣸⣿⡿⣽⡿⣾⢿⣽⣯⣿⣾⡟⢸⣿⣿⣿⣽⣯⣿⣻⣷⣿⢿⣶⣿⡀⠀⠀⠀⠀⠀⠁⠘⠆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡃⣏⣾⣿⣿⡽⣽⣟⣿⣻⣿⣽⣟⣿⡾⡏⢸⣿⣯⣿⣾⣿⢷⣿⢷⣿⣿⣻⣿⡇⠀⠀⠀⠀⠀⠀⠈⠀⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⢿⣷⡿⣽⣿⣽⣯⣿⢷⣿⢿⣯⣿⠇⢸⣿⣿⢿⣯⣿⢿⣿⢿⣷⣿⣽⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣟⣾⡿⣿⢾⣷⣿⣿⢿⣟⣾⣿⠀⢸⣿⣿⡿⣿⣻⣿⢿⣿⣷⡿⣷⢿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠐⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠗⣼⣿⡿⣿⢿⣿⣾⢿⣿⣯⣿⡟⠀⢸⣿⣿⢿⣿⡿⣿⣻⣯⣿⣿⣟⡿⣿⣇⠀⠀⠀⠀⠀⠀⠀⢘⠀⠀⠀⠘⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡇⢠⣿⣿⡿⣿⣿⣷⣿⣿⡿⣾⣿⡇⠀⢸⣿⣿⣿⢿⣿⣿⣿⣟⣿⣾⣿⣿⣻⣿⠀⠀⠀⠀⠀⠀⠀⢸⠄⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣟⣿⠀⣾⣿⣿⣿⣿⣾⣿⣾⡿⣽⣿⣿⠃⠀⢸⣿⣷⣿⣿⣿⣷⣿⢿⣯⣿⣯⣿⣯⣿⡄⠀⠀⠀⠀⠀⠀⢸⡆⠀⠀⠀⣯
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡇⢸⣿⣿⣷⣿⣾⣿⣾⣿⣽⣿⣿⣿⠀⠀⢸⣿⣿⣯⣿⣾⣿⣻⣿⡿⣿⣽⣷⣯⣿⡆⠀⠀⠀⠀⠀⠀⢨⡇⠀⠀⠀⠁
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣟⣿⠀⣿⣿⣿⣾⣿⣯⣿⣻⡷⣿⣽⣷⡏⠀⠀⢸⣿⣿⣽⣿⣟⣿⡿⣿⣿⣿⣿⣯⣿⣽⡇⠀⠀⠀⠀⠀⠀⠰⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣯⣿⣿⡟⢸⣿⣿⣿⣷⣿⣿⣽⣿⢿⣿⣿⢿⡇⠀⠀⢸⣿⣿⣻⣯⣿⣿⣿⣿⣿⣷⣿⣿⣽⣻⡇⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣟⣿⣯⣿⠇⣼⣿⣿⢾⣿⣿⣻⣿⡿⣿⣿⣻⣿⠁⠀⠀⣼⣿⣿⢿⣿⣻⣿⣾⣿⣾⣟⣿⣷⣿⣺⡇⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣯⣿⣟⣿⣿⠀⣿⣽⡿⣿⣷⣿⣯⣿⣽⣿⡿⣿⣿⠀⠀⠀⣿⣿⣿⣿⡿⣿⣻⣿⣾⣟⣿⣯⣿⣟⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣯⣿⢿⣿⣿⢰⣿⣿⣿⣿⣾⣿⣽⡿⣾⣿⣿⣿⡏⠀⠀⢠⣿⣿⣾⣿⢿⣿⣿⣿⣻⣿⣻⣟⣿⣿⣵⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⣿⣿⣾⣷⣿⣿⡿⣷⣼⣿⣿⣷⣿⢿⣯⣿⣿⣿⡿⣷⣿⠇⠀⠀⢸⣿⣿⣯⣿⣿⣿⣷⣿⣿⣿⣿⢿⣿⣿⣽⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⣴⣿⣿⡿⣷⢿⣾⣷⡿⣿⣷⣿⣿⣽⣷⣿⣿⣿⢿⣿⣾⣿⣿⣿⠀⠀⠀⣾⣿⣯⣿⣿⣷⣿⣯⣿⣟⣿⣿⢿⣿⣾⡿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣾⣿⣿⣟⣿⣻⣟⣷⢿⣻⠟⢻⣽⣿⣟⣿⣿⣟⠟⠛⠙⠚⠛⠚⠏⠀⠀⢀⣿⣿⣯⣿⣾⣯⣿⣿⣽⣿⣿⣿⣿⣿⢿⣿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣰⣿⢿⣿⣽⢿⣽⣯⢿⠝⠋⠀⠀⢸⣿⣿⢿⣿⢿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠻⢽⣿⢿⣾⣿⣷⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠔⠁⠀⠀⠀⠀⠈⠈⠈⠁⠀⠀⠀⠀⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣟⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⡿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣿⣿⣿⣷⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣯⣿⣿⡭⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣟⣳⢾⣿⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣾⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⢯⡫⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣽⣯⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⢿⡝⢧⣻⠿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⢻⣿⣿⣻⣿⣽⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣷⡿⣮⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Dante": """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣠⣄⣤⣠⠠⡤⡀⡀⢄⢠⣀⣀⢀⡀⡀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣀⣠⣤⣤⣶⢶⣾⢿⡿⣿⢻⣗⢽⡽⣓⡗⣷⣹⣥⠧⡘⢔⢄⠕⢧⣍⣍⣺⡻⣋⣽⣳⣱⡢⣄⣾⣏⣢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠒⠒⠋⠋⠉⠉⠁⠹⢷⣷⣽⣝⣞⣮⣳⣕⣯⣾⣾⣮⣾⣵⣷⣈⠵⠥⢏⣲⢝⣬⣻⣧⣛⣿⢷⣽⣏⣿⣿⡶⣿⠄⠞⣟⡛⢷⡶⣴⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠙⠛⠻⠋⡿⠫⢿⠫⢿⠿⣾⣩⣆⠒⡄⢻⣾⣿⣿⣿⣿⣿⣿⣾⣏⢿⣯⣟⡰⢧⡰⣯⣦⣽⡉⠚⠚⠽⢫⡧⣢⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣯⣟⣥⡨⣓⣿⡮⢻⣿⢻⣿⡻⣿⢡⣿⣿⣿⣽⢽⡇⡟⡾⡟⣤⣤⣤⣄⣀⣤⣕⡻⣒⠤⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣈⣽⣿⣿⡻⣌⣮⣿⢴⣻⣷⣿⣻⣿⣵⣿⣾⣿⣿⣿⣷⣿⡗⠑⠈⠀⠀⠀⠈⠉⠛⠽⣿⡯⠷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣟⣿⣿⣽⡇⣼⣻⡯⣷⣾⣋⠺⡟⢿⣯⣿⢾⣯⡿⠝⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣵⣿⣷⡿⣧⣟⡷⣟⣾⠭⣻⣟⢿⣟⣿⠝⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣯⣿⢧⣿⣺⡷⣟⣿⣽⣻⡽⣿⡸⢮⡾⣿⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣰⣾⣿⣿⣿⡯⣿⣿⣽⣟⣯⣿⢾⣯⣟⣯⣞⢵⣿⢩⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⣿⣯⣿⣯⣿⠟⢻⡿⣷⣿⣯⡷⣿⣻⣞⣯⣿⣯⡳⣟⡽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⡒⠹⡟⠁⠀⠀⣿⣿⣾⡷⣟⣿⣞⢷⣝⣿⣮⡻⣟⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢯⣖⢵⡄⠀⠀⣽⣿⣽⢿⣿⣺⣯⣟⢾⣽⣷⡫⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⣿⣶⡄⣿⣯⣟⣿⢷⣝⣷⡽⣳⡽⣷⣝⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣽⣟⣿⡺⣷⣛⢿⡽⣿⡮⣾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣯⣿⡿⣷⢿⣾⣽⣻⢯⢯⡾⡿⡷⣿⡳⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡧⣿⣿⣿⢿⣝⣾⢽⣯⣻⣝⢽⡝⣝⢿⣽⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣯⣿⣿⣯⡿⣽⢯⣿⣶⢷⣹⣺⣽⣘⢯⣻⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣷⣿⣿⣟⣟⣟⣿⣿⣿⣿⣿⡿⣾⣮⣳⣝⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⢿⣟⡾⣷⣽⣿⣿⣿⣿⣿⡷⣕⢯⣞⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⢿⣿⡿⣿⣯⣿⡳⣿⢿⣿⣿⣿⣿⣻⣯⣳⡧⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿⣽⣿⣿⣟⢷⣟⣿⣻⡏⣿⣿⣿⣿⣿⣻⡺⣞⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿⣿⣿⣿⣿⣟⣿⣞⣿⢇⣿⣿⣿⣿⣿⣿⣯⠷⡿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⣿⣿⣻⣿⣿⢷⡿⣽⡇⣿⣿⣿⡿⣿⣯⣿⣻⡺⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣻⣿⣻⡿⣿⣿⣿⣟⣿⠨⣿⣿⣿⣿⣿⣿⣿⣽⡿⣽⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠾⠿⠋⠉⢻⣿⣾⢿⣿⡴⠿⠿⠿⠯⠟⢙⣿⣿⣻⡾⣽⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⢸⣿⣿⣟⣷⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣻⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣾⣻⡿⠀⠀⠀⠀⠀⠀⣾⣿⣿⣳⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣷⡻⣿⠀⠀⠀⠀⠀⠀⢸⣿⣿⣻⢾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣟⣿⠀⠀⠀⠀⠀⠀⠈⣿⣿⡿⣷⣧⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⡷⣯⢿⡁⠀⠀⠀⠀⠀⠀⢺⣿⣿⣯⣾⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡿⣾⣻⠇⠀⠀⠀⠀⠀⠀⠀⣿⣿⣾⡲⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣝⣿⠀⠀⠀⠀⠀⠀⠀⠀⢙⣿⣿⣻⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣝⢿⣿⢿⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡫⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣾⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⠿⢿⣷⣽⡳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠙⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Nero": """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⡀⠀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⢶⣦⢄⠀⡀⢻⣧⠄⠀⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣻⣻⣞⠧⡣⢀⠘⣿⢶⢰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⢳⣝⣮⣑⣠⣂⢠⠍⢟⡷⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⣻⢮⣻⡀⢡⣿⣷⣠⢿⣽⣿⣽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣾⣿⣼⣟⣗⣭⡾⣯⣿⣗⣒⡘⢿⡷⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢻⣿⣿⣿⣷⣻⣟⣯⣿⣿⣿⣿⣟⣿⣝⡿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣫⣿⣿⣿⣿⣾⣿⡳⣟⣿⣯⣿⢿⣿⣯⣻⡂⠂⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣿⣾⣿⣷⣿⣿⣿⣽⣫⡿⣷⣿⣿⣿⣿⣯⣏⠢⣼⣄⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣻⣿⣿⣾⣿⣷⢿⣿⣿⣾⢿⣿⣿⣿⣿⣛⢻⣿⢿⣿⣿⡿⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣟⣿⣿⢿⣿⣽⣿⣟⣿⣿⣿⡿⡇⠀⠉⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⡻⣿⣿⣿⣻⣿⣿⣿⣿⣻⣿⣿⢿⣿⣿⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣷⡿⢯⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⢵⣿⣯⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣷⠿⠃⢰⣿⣿⣿⣯⣿⣾⣟⣾⣿⣿⣗⢿⣽⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⣿⡻⠁⣰⣿⣿⣿⣷⣿⣟⣾⢯⣟⢽⣿⣿⣗⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣞⠁⣰⢿⣿⣿⢻⣯⣟⠽⣟⠻⣷⢵⣽⢿⣿⣷⣟⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡛⢹⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣯⣥⣽⣽⣿⣿⣿⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢟⠭⢉⣾⣿⣿⣿⣿⣟⣯⣿⣿⣿⣟⣿⣿⣻⣿⡻⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣽⣿⣯⣿⣿⣿⣻⢷⣯⢿⣿⣿⣿⣷⣿⢿⣽⣻⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⠇⣿⣿⣿⣿⣟⢷⡽⣿⡯⠘⣿⣿⣿⣯⡷⣻⡿⠛⠀⠀⠈⠛⠛⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡀⢺⣿⠈⣿⣿⡻⣞⣯⡧⠀⢿⣿⣿⣾⣟⣿⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠟⠛⠁⢸⡿⠀⢿⣿⡿⣳⣟⡇⠀⢸⣿⣿⣿⣽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠏⠀⠀⠀⠀⠀⠀⣼⣿⣿⣝⣾⡟⠀⠈⣿⣿⣿⡾⣽⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣮⢿⠯⠀⠀⢿⣿⣿⣿⣽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡾⣿⡇⠀⠀⣿⣿⣿⢷⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣧⠀⠀⣿⣿⡿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⢾⣿⠀⠨⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⣿⡄⠀⣿⣿⣿⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⣿⠀⢠⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⢿⠀⢸⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡿⡄⠸⣷⢿⣯⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣝⡇⠀⢹⠻⣼⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣽⣮⣗⠀⠈⠿⠿⠋⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⠷⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Kazuya Mishima": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣽⣿⣻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣻⢯⡿⣟⣿⣻⡷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣳⠟⢟⢿⣻⢻⢾⢝⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⡞⡨⡐⡍⣖⣝⣝⢵⠥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠅⣛⣮⣞⣮⣞⢗⠨⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⢮⡪⠄⡷⣽⠝⡈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⣰⢼⢌⠢⢽⢵⡯⡧⡝⣖⡤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢢⢃⣓⢽⢝⢮⢪⠮⠷⡿⡽⡡⡻⡺⠽⢄⠠⠢⣄⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⡂⢕⢜⣕⢧⡳⣝⢮⢳⢡⢙⠸⡐⡨⡣⣓⣞⣼⡰⡐⡁⠂⠍⢕⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠑⣌⢞⣜⣮⣳⣳⢕⣗⢵⡱⡰⢐⠠⡘⢜⡮⣞⡾⣽⢐⠀⠂⠉⢄⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡨⡸⡸⣪⢟⣾⣺⣾⣽⢽⡮⣳⢕⡽⣸⡰⡌⡮⣯⢗⡯⣗⣇⢆⠈⠀⡵⣄⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢎⢮⣺⣽⣯⣷⢿⣷⣿⢯⣯⣗⣯⢯⣺⣪⢯⢿⣽⢯⡯⣷⣳⡳⣱⢰⣟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⢜⠸⣕⡟⣞⢺⣺⣻⢿⡾⡿⡿⣾⣻⣽⢷⢟⣟⣯⢿⣝⢯⢷⢷⠿⠑⢿⣽⢮⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⢜⢔⢡⢧⢇⢪⢱⣻⢾⣯⣟⣯⣟⢮⢮⣓⡗⣗⢗⣟⡗⡵⣫⠁⢕⡽⡀⣹⣯⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡘⡷⣳⡵⣝⢕⣵⣻⡝⣿⢷⣻⢾⣝⡷⣻⡪⡾⡽⡽⣞⡯⣞⣟⡆⢹⢽⢐⢽⡾⣯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡸⢸⣳⢽⣺⣽⡺⡪⠀⠙⡿⠣⢽⣺⡽⡽⡽⣝⠽⡝⣗⠯⣳⡫⣙⣞⡎⣸⢯⣿⢷⣻⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⢗⡯⣟⡿⠜⠈⠀⠀⠀⠈⡈⡢⣳⣟⣽⢝⣎⢇⢇⣷⣫⣞⣮⣺⣳⠅⢸⢽⡾⣟⣯⡫⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⢎⢮⢯⣗⡏⠀⠀⠀⠀⠀⢠⢠⡳⣻⣞⣗⡟⡮⣳⣻⣗⢷⣳⣗⣟⣮⣢⡀⢫⣟⣯⡷⣗⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢢⢱⣯⢷⡯⡯⠀⠀⠀⠀⠀⢐⠥⠷⣚⢮⣳⣩⣯⢧⣳⣹⢽⣵⡻⡾⡾⡇⡃⠈⢞⣗⡯⣗⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠵⣹⡺⣽⡳⡙⠀⠀⠀⠀⠀⠠⠝⡿⣾⢾⢾⡾⣺⢼⣺⣾⢯⣗⣿⡽⡿⡝⠄⠀⠈⠪⣟⣗⢗⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠨⣺⣺⣽⡝⠄⠀⠀⠀⠀⢠⠀⠂⡐⠕⡩⠩⡵⣻⣟⡿⣟⣟⢿⣾⣹⢢⠢⡀⠀⠀⠀⢑⣗⣽⢽⣗⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⢜⢞⡷⣏⠀⠀⠀⠀⠀⢼⠀⠂⢌⢂⠢⢅⣝⢗⢕⢽⢸⢜⣗⣿⢾⣸⢕⢅⠂⠀⠀⠀⡯⣺⢯⣷⡃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣜⣼⣿⣳⡀⠀⠀⠀⡰⠉⠀⢌⢌⠢⢣⣱⢇⢇⢇⢗⣕⣯⡾⣻⣗⣯⡻⡜⡀⠀⠀⠀⢘⣷⡱⣿⣝⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠜⢼⣾⣳⡃⠀⠀⢈⠀⠀⠅⡂⢆⠥⣣⣿⢵⢝⢼⢵⡿⡾⣵⢟⣗⣗⢯⢇⡣⠀⠀⠀⠰⡳⢟⡽⣯⢧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠴⡫⣟⢿⣞⣦⣄⡡⢀⠂⢈⠪⡢⡕⡼⣾⣻⣽⡽⣟⣿⣻⡵⣟⢿⣺⣝⢗⠥⡁⠀⠀⠣⡫⡳⠽⠯⠛⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣳⢪⣳⣿⣳⣯⣿⢄⢔⢇⢨⡲⡭⡯⣿⣳⣿⠀⢿⣟⡯⣟⡽⣝⡿⣮⣏⢇⢌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠴⡉⣿⣽⣟⣮⠏⠃⡁⡆⣇⡯⣞⣯⢿⣳⡇⠀⢸⣯⢿⢽⣻⡽⡯⡿⣾⣇⢇⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⣯⡷⣯⠇⠀⠅⡧⣻⣪⣯⢷⣟⣿⢯⡃⠀⠈⣾⢿⡽⣞⣯⡿⣯⢷⣻⣵⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⣎⡆⢱⣕⢯⢾⣞⣯⣷⣿⡻⠀⠀⠀⠘⡽⣽⣻⣺⡯⣿⢯⣷⢷⡕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⢐⣕⠇⣎⢮⢯⣳⣟⣾⢿⣽⠇⠀⠀⠀⠀⠘⣵⢷⢗⣿⡽⣿⣽⣯⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢁⠼⡜⠠⣳⣫⢯⢷⣻⣽⡿⡝⠀⠀⠀⠀⠀⠀⠪⡻⣽⣞⣯⣷⣿⡾⣟⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠈⢁⠠⣚⢞⡮⣟⡿⣽⢷⡻⠁⠀⠀⠀⠀⠀⠀⠁⠨⡪⣞⢿⡷⣿⢿⣟⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⢕⢮⢯⣯⢿⣽⣿⢽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠡⠪⡫⡯⣿⣽⡿⣟⡆⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⢵⢝⣵⣟⣿⣻⣞⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⢑⠹⢝⣗⣯⣿⠫⣣⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡀⢜⣯⣻⣺⣷⣿⡽⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡍⣓⢭⣻⣽⢢⣽⢿⠐⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠄⣳⣻⢮⣷⣿⡽⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢩⢸⢹⣽⢾⣔⢜⠻⣏⢆⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠌⡸⣺⡯⣯⣷⡿⣯⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢌⡗⡟⣮⡿⡽⣷⣯⡖⠅⡱⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡡⡃⣏⡷⣟⡷⣟⣿⡽⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⣗⢽⢱⢯⡿⣿⡾⣿⠅⡎⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢐⢰⢱⢕⡿⣯⣟⡿⡷⣟⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⡳⣫⢿⢽⣳⢿⣻⡜⡮⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢂⢕⢵⢽⢽⣷⣻⣟⣿⣻⡕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⣏⣏⣯⣟⣾⢿⣿⡚⠯⡃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠐⢈⢀⢪⢪⢯⣻⢾⣽⣯⡷⣟⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢚⢮⣳⡽⣞⣯⣷⢯⠣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡢⢽⡽⣯⣿⢿⣾⣻⡝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠈⡳⣳⢻⡽⣽⣺⢧⣏⠠⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢁⠂⠀⡪⡳⣿⣻⣽⡿⣾⣗⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠊⠂⠣⣯⣷⣟⢯⢳⢻⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠀⢢⢱⣹⣿⣽⢷⣿⣻⢞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠮⡎⡎⡳⡸⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠀⢐⢜⣞⡾⣷⢿⣻⣽⢯⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢁⣮⣲⣳⡷⣿⣟⣿⠽⠟⠿⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢍⢜⢸⠪⣟⣿⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢢⢣⢃⢇⠷⠏⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Jin Kazama": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⣶⢵⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⣰⣾⣽⣿⣻⣽⡷⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡽⣟⣿⢽⣯⢿⣯⡷⣿⢅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣾⣟⡿⣽⡿⣯⣟⡷⣟⣯⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣻⣽⢳⣿⣟⣿⣿⡽⣿⣽⢷⣣⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣳⠸⡳⡙⣯⣷⢿⣾⢿⣻⡽⣏⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⠁⠈⠊⠪⣟⣗⢽⢽⡳⣝⣴⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣀⡤⡢⢄⠀⠀⠀⠀⠀⠘⢳⢽⢽⢽⢽⣞⣯⢳⡳⢭⢢⢂⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⢱⢜⣽⢽⣲⡔⡆⠀⠀⠀⠀⠀⠫⠯⡻⢽⢳⠱⢑⢍⠧⣣⣃⢂⠁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢕⢼⡹⣞⣿⢯⣟⣾⢬⠄⠀⠀⠀⠀⠁⠀⢂⢅⢎⢔⢔⢨⠠⠙⠪⣆⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣐⣷⢯⡯⡯⣟⣟⡟⠁⠀⠀⠀⠀⠀⠠⠨⡲⡱⡱⣝⢵⣳⣝⢎⠄⠈⢅⠂⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠐⣸⡺⣯⡻⣽⣳⢯⣷⠀⠀⠀⠀⠀⠠⠡⣱⢵⣝⢞⡮⣟⣾⣺⢵⢱⠁⣗⢦⠐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡴⡏⣗⣽⢽⡾⡯⣞⣯⢆⠀⢀⢠⢸⣜⣯⢿⣺⣯⢿⢽⡾⣽⣽⣺⢮⡢⠙⡕⠈⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⡽⡺⣝⣾⣻⡽⣞⡻⡮⣢⡳⣝⢮⣺⡽⣟⡾⣝⡧⡫⣞⣷⢿⡽⡮⣂⠪⢐⡽⣆⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡜⡷⡳⣽⢽⣳⢯⡪⡧⣟⡵⣗⣗⣯⢷⣫⣗⢇⡷⣿⣻⡯⣿⢵⣕⢎⢐⣯⡷⡅⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡱⣼⢿⣺⢿⣻⣽⣽⣺⡳⣻⣳⣟⡾⣽⣺⣺⣵⣿⣯⡷⣿⢽⣻⡺⣇⣯⡷⣿⢽⠄⢀⠄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⣗⣯⣿⣽⡷⣟⡮⣯⡢⣷⣫⢯⢧⢷⣻⡷⣿⣞⣿⡽⣯⡷⣯⢲⣟⣿⣽⣽⠗⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠫⢾⣟⣯⣷⣿⣻⣳⢯⣟⡵⠫⡫⡝⣝⢷⣻⣽⡾⣷⣟⣯⢯⠗⣿⣽⣯⡿⡇⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣯⠳⡫⠛⢾⡋⠀⠀⠨⡺⣌⢮⢯⣗⣯⣟⣗⣟⣾⡫⡃⣿⡿⠻⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢆⠀⠀⠀⠁⠀⢠⡎⠜⡜⡜⡼⣞⣗⢷⢽⣞⣾⣳⢴⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⡰⣳⣿⡿⣾⣳⣗⣷⣯⣿⣿⣽⣾⣻⡽⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠜⡧⣿⣟⣷⡷⣷⣷⢿⣾⣿⣻⣯⣷⣟⣯⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⡘⣮⢿⣽⢽⣻⣻⣽⡿⣟⣯⣿⣻⣽⣷⣗⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠎⠃⡠⡳⣽⢽⣳⡿⡯⣿⢾⣿⣻⣟⡾⣿⢿⣿⣿⣺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠖⠍⠁⢀⣮⢪⣟⡾⣝⣗⢽⢝⣷⡿⣾⣯⣷⣿⣿⡿⣿⣻⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠾⠋⠀⠀⣐⢾⡪⣟⣮⣟⢮⢺⢝⣿⣳⡿⣟⣿⣽⣾⢯⢯⣗⡯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢜⢬⣣⢿⣽⢾⣿⡯⡪⡳⣱⣳⡿⣟⣯⣿⣾⢿⣵⢳⡹⡑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢎⣾⡸⡾⣽⣟⣿⣿⣗⢇⢕⡵⣯⢿⣻⣟⣿⣾⢿⡯⣷⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢩⠢⣖⢽⣽⣿⣽⣿⣿⣿⢰⢣⢻⣺⢿⣽⣯⣿⢿⣯⢿⢵⡫⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢜⡆⣿⣮⣻⣻⣻⣿⣿⣿⣯⢧⢱⢹⣞⡿⣞⣷⣟⣿⣿⣻⣯⢞⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⣸⢮⣛⡿⣯⣿⣽⣿⣿⣿⣿⢇⢇⢯⣞⣯⢿⡷⣿⣽⣾⣿⣻⡵⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣗⡽⣻⣻⣻⢿⣻⣽⣿⣿⠯⠋⢸⢸⢜⡾⣽⡯⣿⣽⡾⣿⣞⣿⣽⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡮⣟⣾⢿⣿⣿⣿⣿⣿⡳⡁⠀⢐⢱⢱⢯⡷⣟⣿⣺⣯⣷⣿⣻⣮⡊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⢿⣞⣿⣟⣿⣯⣿⢾⣳⡄⠀⠀⡣⡫⡯⡿⣽⢷⡿⣽⣯⢿⣻⣮⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢕⢿⣿⣻⣿⡿⣿⣾⡿⣟⡬⠀⠀⢪⢣⢟⣯⢿⣽⣟⣿⢾⡿⣯⣗⡖⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣗⢿⣻⣯⣿⣿⣷⣿⢯⡺⠀⠀⠨⣪⢯⡿⣽⢷⣻⣽⡿⣟⣿⢾⡷⣕⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣺⢯⣟⣿⣿⣻⣾⣟⣯⠣⠀⠀⠀⠵⣟⣿⣽⣟⡿⣷⢿⣟⣿⣻⡽⡯⣇⢇⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡳⡯⣟⣯⣿⢿⣞⣿⣎⠇⠀⠀⠀⠈⡫⣿⣽⣾⣿⣽⢿⣽⣯⣷⣿⣽⣮⡳⡕⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢧⡿⣽⣿⢿⣿⣻⣗⡇⠁⠀⠀⠀⠀⠈⠺⡽⣾⣻⣽⣿⣷⣿⢾⡷⣿⣞⣿⢮⡪⡂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢱⢹⣽⣯⣿⣟⡯⣷⢱⠀⠀⠀⠀⠀⠀⠀⠘⢽⢯⡯⣷⢿⣾⡿⣿⢿⣾⣻⣯⢷⡍⡂⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠠⣢⣫⡿⣵⣻⣷⡽⣮⡷⣟⣯⣗⠅⠀⠀⠀⠀⠀⠀⠀⠈⢫⣟⣯⡿⣷⣿⢿⣿⣽⢿⣺⡿⡽⡮⡂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠰⠒⠼⢾⣿⢿⣿⣷⣿⣿⣻⣻⠝⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡪⡿⣽⣟⣾⣿⢷⡿⣿⣯⣿⡽⣽⡨⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢞⣿⣻⣷⣟⣿⢿⣿⢾⣷⡿⣷⡳⡈⠄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⣯⢿⣻⣿⣯⡿⣯⣿⣻⡿⣯⡳⣕⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢕⢯⡷⣿⣽⣿⣿⣾⢷⣻⢯⢿⣸⡄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⠿⣽⣞⣷⢿⡾⣿⣟⣯⣿⣽⡪⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⡿⣳⣿⣺⣯⣿⣷⣿⣿⣽⣾⣫⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠩⣻⣯⣿⣻⣷⣿⣾⣯⣿⣽⣾⢯⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣐⣜⢞⣯⡿⣿⣻⣟⣿⣿⢿⠁⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢺⢞⣮⢿⣞⣿⣽⣿⣻⣿⠚⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠳⢍⡎⡮⡫⢞⠵⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Heihachi Mishima": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡡⡈⠢⠀⠀⠀⠀⠀⠀⠀⠀⡀⢌⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡨⠨⠀⠐⡌⡎⡪⡠⢐⢅⠢⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⡅⠅⢨⢢⡣⣣⢪⠨⡐⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡀⢄⡊⢔⢦⣣⢯⡺⣨⡜⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣐⢄⢌⢆⢇⣧⣺⡜⡬⡢⡂⡱⡑⡱⢝⡎⢎⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠜⡫⠓⡍⡧⢂⠣⡳⣕⣯⣗⡽⡸⡪⡢⣗⠵⡣⡍⢾⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠁⢄⠕⡜⡜⡵⡮⣝⢮⢷⡵⣏⣞⡮⣧⣳⢯⣣⢏⢽⣗⣝⢶⡪⡢⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡑⡌⣎⢮⡪⣯⡻⣪⢺⡽⣻⣺⣳⣹⢮⢯⡫⡗⡇⡳⢽⡪⣮⡳⣅⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⢎⢾⢜⣞⡾⣵⣫⡿⡽⣽⣽⣺⡺⣞⡯⣯⢮⢪⡣⡱⣹⢮⢺⣺⢽⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣫⢯⢿⢷⣟⣗⣯⡷⡯⣟⣷⢵⣻⡽⣯⢯⡯⡧⣣⢏⢾⢜⡵⣳⡳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⠈⡐⡭⣝⢽⣻⣿⣯⣿⢽⣿⡯⣯⡷⣿⣻⣯⣿⡽⣾⣽⣫⢗⡽⡵⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠄⢀⢎⢎⢮⣳⢽⣾⣷⡿⣟⣯⣿⣷⣿⣻⣿⣽⣾⣿⢷⢯⢾⣽⢯⣟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⣎⡢⣗⡯⣟⣞⣝⣯⣷⣿⢿⣻⣷⣿⣽⣿⣯⣿⡿⣾⣿⣻⣯⣿⣻⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⡠⡢⠀⠀⠀⢄⢅⠢⡩⡳⡿⣯⢞⢯⣯⣿⣾⣿⣽⣾⣿⣽⣯⣿⣟⣿⣿⣳⣟⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠐⣜⠮⡃⡃⣇⠌⣪⠠⡑⡔⡕⣝⡼⡜⣎⢧⡃⠰⣗⣿⣗⡯⡯⡷⡷⣟⢷⣟⣽⢷⣿⣺⣽⡿⣿⡳⣕⢄⠀⠀⠀⠀⡀⡀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⢆⣕⡮⡞⡒⣟⢗⢇⡧⡳⡽⣵⢯⢟⡞⠕⠀⠠⣹⢮⢿⣽⣻⢿⢾⣻⣟⣿⣟⣿⣟⣿⣯⣿⣿⢽⣮⡺⣝⢴⡰⣔⢽⡕⣸⢪⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢁⢕⡜⣮⡺⡸⡪⡓⢝⢽⢹⠺⠹⠑⠁⠀⠀⡠⣳⡿⣟⣷⣿⣿⣿⣽⣯⡿⣽⣯⢿⣻⣺⢮⣗⢿⠮⢻⡺⣝⣞⢮⣻⢝⢆⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠭⡣⠏⠞⠉⠈⠀⠀⠀⠀⠀⠀⠀⢀⢴⣹⡳⡯⣿⣽⣞⣷⢯⣷⣿⣿⣻⣾⢯⣗⣿⣿⣾⡽⣻⣆⡀⠀⠈⠈⠊⠋⠊⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⢾⡭⣎⡼⣹⡳⣯⡻⣮⣿⣯⣿⣾⣷⣻⣗⢯⡿⣯⣿⣻⣺⣪⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢏⢎⢗⢽⣹⢯⣿⣮⣳⣝⣷⣻⣾⡳⣟⣿⣞⣯⡳⣻⣽⣻⢿⣗⢯⣳⢽⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡢⢢⣣⢯⢷⣻⣻⡷⣿⣿⣾⣮⣷⢯⣟⡯⣿⣿⢷⣏⢗⢗⢕⣟⣽⣝⢾⡽⣵⡳⣔⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡢⣪⢺⣱⣳⣻⡽⣯⣿⣻⣟⣿⢿⣿⣿⣷⣵⢿⣿⣿⣿⣿⣧⡯⣿⣟⣿⢮⡻⣽⣷⢿⣜⣕⠦⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⡰⡸⢸⢸⢳⡳⣳⢗⣿⣻⣽⣻⣯⣿⢿⢿⡾⣯⣿⣯⣷⣿⣷⣿⣾⣿⣿⣽⣻⡧⣻⣽⣾⣯⣿⣮⣯⡢⣕⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢐⢕⣜⢬⢪⢯⢯⣻⣽⢿⣽⡿⣾⣿⣽⣿⡿⣿⠟⠉⠀⠀⠉⠉⠛⠟⢿⣟⣿⡿⣷⣿⡽⣟⣿⣟⣿⣯⣿⡯⣗⢗⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣂⢯⢧⣗⣟⣯⢷⣯⣿⣽⢿⣯⣿⢿⢾⣿⠻⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⢾⣿⣿⣻⣿⣻⣽⣷⣻⣾⣝⠆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣘⣜⡷⣽⢽⣾⣵⣻⣺⣽⣿⣻⣞⣟⠯⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣣⢷⣿⣿⣿⣟⣿⣿⣿⣷⠏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢷⣻⣻⣿⡿⣷⣿⣞⣿⣿⡞⡑⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⣗⢯⣯⣟⣷⢿⣻⣟⣷⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢣⡳⣽⣻⣾⡿⣟⣿⢿⣟⣷⠽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠪⠺⣝⢷⡻⣝⢿⣝⡟⠂⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢪⢪⣞⣞⣯⣿⣻⣿⣽⣿⣟⢽⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⣝⢖⡵⣝⠞⠑⠑⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢜⢜⢮⣻⣾⣟⣯⣿⣾⢾⣯⣟⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡣⣗⢗⣝⡎⡇⡆⢄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡝⡼⣯⢿⣞⣿⣻⣽⣿⣯⣷⢯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠝⠮⠗⠗⠝⠮⣫⢮⡪⣪⣐⢄⠄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⡣⣹⣽⡳⣟⣿⢿⣟⣷⡿⣾⠪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠌⡎⡾⣺⡳⣯⣿⣻⡽⣻⢪⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢨⢣⢿⢭⣳⡳⣯⡳⠑⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡂⡫⡪⡪⣞⢽⢳⡫⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⢱⢸⢸⡸⡜⣎⡷⣕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠠⠨⡐⠨⠊⡆⡧⣻⠪⠗⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⢪⠨⡐⡐⡍⢰⢸⣚⡎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢅⠎⡌⡰⠜⡠⡣⣗⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠘⠂⠵⢵⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Sub-Zero": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣖⣦⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣟⣯⣿⢿⣿⣯⢟⢶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣾⣳⡯⣟⣟⡿⣿⡯⣻⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣻⢮⣻⠻⣗⢿⣼⣿⢽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡯⣗⠝⡕⡙⣽⡯⡿⡡⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣺⣿⡯⣯⣗⢾⣪⣞⢮⠏⣮⣴⣤⣦⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣿⣿⣗⣽⣟⣷⣯⣿⣵⣿⣿⣿⣿⣿⣿⣿⣿⣾⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⢾⢽⢿⣯⣿⢾⣿⡿⣿⣿⢿⣿⢷⣿⣷⣿⣿⣿⣻⣿⡝⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣶⣟⡿⣽⣫⢯⡻⣿⡾⣿⢷⣿⣿⢿⣻⣟⣿⣯⡷⣿⣷⣿⣿⣯⣷⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⣷⡯⣟⣾⣺⢝⡮⡻⣟⣿⢯⣷⡿⣿⡯⣿⣞⣷⣿⢿⣻⣿⢾⡿⣿⣇⠅⣿⣶⡇⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣜⣯⢿⡯⣻⣪⢾⢵⢯⢫⢝⡿⣿⢾⣿⣻⣟⣷⢿⣻⣾⣿⣿⣿⣟⡿⣿⣿⣵⣿⣿⣜⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⢎⢎⢗⣟⢷⢝⢝⣕⡽⣝⢕⢝⣽⡿⡷⣿⣽⣾⣿⡿⣿⣿⣽⣾⣷⡹⡽⡾⣿⢿⣽⣿⡪⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣻⡵⡣⠯⣶⡩⣳⢫⢪⢪⣢⢯⢏⣞⢿⣻⣽⣾⢿⣾⣿⣿⣿⣽⣿⣿⠇⢽⣽⣟⣿⣷⣳⣽⣔⢴⡐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⣽⡊⡐⡱⣽⣿⡮⣳⣳⡋⣎⣖⢗⢏⣿⣟⣷⡿⣿⣿⡿⣽⡿⣿⣿⣿⡅⠀⠘⠹⡺⣻⡿⣟⣿⣟⣽⡺⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠠⠐⠀⢠⣙⢖⢽⡲⣽⣯⡿⠁⠘⢘⠽⡧⣧⢗⣯⣗⣿⣯⣿⣿⢯⣻⣽⢿⣷⣽⣻⣧⠀⠀⠀⠈⠝⠸⡹⣪⡿⣷⣳⣝⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⡀⢠⣺⡺⣮⡢⡁⡟⣿⡟⠀⠀⠀⠀⠑⢵⡳⣽⣷⣻⣷⡿⣟⣯⣿⡿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠈⢸⣜⣞⡿⣽⣿⣟⣞⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠈⢊⠎⡫⣞⣾⡻⠀⠀⠀⠀⠀⠀⠈⣻⢽⡾⣯⣞⣽⣻⣾⡷⣿⣿⣿⣽⣿⣿⣿⣷⠀⠀⠀⠀⠈⠓⢹⢽⣞⣾⣻⣿⡺⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠀⠠⠀⠀⠄⠀⠀⠀⢀⠀⠀⡰⣸⣺⡚⠀⠀⠀⠀⠀⠀⠀⠀⢸⣻⣟⣯⣷⣻⡷⣟⣿⢿⣿⣽⣯⣿⣾⣿⣿⣧⠀⠀⠀⠀⠀⠀⠉⠙⢮⢯⣿⣯⡳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠄⠁⠀⠄⠇⠀⠀⠀⠀⢀⢢⣂⠦⠚⠊⠀⠀⠁⠀⠀⠀⠀⢀⣮⣯⡿⣾⢿⣻⢾⣿⣻⣟⣿⣿⣽⣿⣿⢿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠈⠿⣝⣾⣻⣟⣯⢤⡀⠠⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠂⠐⠈⠌⠐⡉⢔⢀⠀⡀⠐⡰⠐⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⣮⡿⣾⣻⣟⣯⡿⣯⣿⣽⣿⣽⣾⣿⣾⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠺⡑⢹⢽⣳⡵⡢⡀⠈⠀⠀⠀⠀⠀
⠀⠀⠀⡁⠐⠈⠄⠨⠀⠠⠀⡀⢌⠂⠁⢀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡯⣟⣯⣿⣿⣻⣿⣻⣯⣿⣾⣿⣯⣿⣾⣿⣽⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡈⢣⡀⠉⢮⢝⣦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠀⡈⠀⠁⠈⠀⠐⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⣼⢯⣟⣿⣿⣻⣿⣿⡾⣟⣿⣻⣽⣷⣿⣿⢿⣾⣿⢿⣯⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠠⠀⠀⡀⠂⢀⠈⢀⠣⠑⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠐⠈⠀⠀⠀⠂⠀⠀⠀⠀⢰⣿⣽⢿⣽⣿⣽⣟⡾⣿⣿⣯⣿⣿⣿⣿⢿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⡀⠀⠄⠀⠠⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⡿⣞⣿⣿⣻⣾⣳⣟⣯⣿⣷⣿⣿⣾⣿⣿⣿⣿⣻⣿⣟⣿⣟⣿⣿⣻⣿⣿⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠠⠈⠀⠀⠂⠁⠀⢀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⢿⣿⣿⣿⣿⣻⣾⢿⣿⣿⣿⣽⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⢿⣻⣿⣿⣿⣟⠀⠀⠀⠀⠀⠈⠀⠀⠈⠀⠠⠐⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡿⣟⣿⣿⣿⣿⣿⣽⣿⣿⣿⣟⣿⣿⡏⠀⠈⠻⢿⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣯⣿⣆⡀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⣷⣿⣿⣿⣿⣾⣿⣿⢟⣿⣿⣿⣿⣿⡏⠀⠀⠠⠀⢀⠘⠻⣿⣿⣿⣯⣷⣿⣿⣻⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠀⠀⠀
    """,
    "Scorpion": """
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⡻⢏⢻⣻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣹⣙⠙⢿⣿⣿⣿⣿⣿⠻⠫⡱⡽⣽⣞⣟⢽⣷⣄⠈⡙⠛⢛⡻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⢟⡙⡝⣙⠝⠿⠿⠿⠿⠻⣿⣄⠍⢟⠟⣻⢥⣻⣿⣽⡺⣿⢿⣯⡺⣽⣽⣔⣵⣳⢼⣯⡲⣂⢉⠙⠙⠙⠻⢿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⡉⢍⢩⡉⡍⡛⠿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣽⡿⡿⡿⣿⣱⣵⣧⣻⣺⣿⣯⡂⢟⣮⣗⣯⡿⣷⢯⣹⡿⣿⣝⡿⣾⣽⣿⢾⣿⣯⡳⡝⢐⡮⣮⡰⡀⡀⢻⡝⡿⣿⣿⣿⣿⡿⢋⢠⢼⣪⣾⣳⡵⡣⡣⠢⡊⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡛⢕⣾⣾⡾⣯⣿⣿⣿⣿⣿⠿⣿⢷⣽⣻⣯⣗⣿⣻⣿⣞⣿⣿⡿⣽⣟⣿⣿⣿⣿⣽⣯⡇⡀⣟⣷⣵⢱⢐⢜⣿⢨⢙⠿⠿⢩⢨⣿⣑⣽⣟⣾⡾⣽⢽⣪⡪⡢⡉⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣾⣾⠏⣷⣾⠿⣿⠿⣛⣛⡮⢟⣲⢽⡾⣿⣟⣵⣷⣯⣵⣿⣯⣯⣿⣿⣿⣷⣝⡯⣿⣿⣿⣖⣴⣿⣿⣾⢷⣵⣮⣿⢞⡗⡆⣷⣞⣿⣿⣺⣷⣿⣟⣿⣯⣯⡷⣟⡮⢺⣼⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣮⠝⢖⡫⣕⣫⣵⣳⣽⣻⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⡡⣯⣿⣿⣿⣿⣿⣿⣷⣿⣿⡯⣷⣻⢺⣻⣿⣿⣿⣿⣿⣟⣿⣽⡿⣙⢝⢞⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠟⣋⣬⣼⣮⣾⣷⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⢰⢵⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⢯⣺⣽⣻⣿⣿⣿⣿⣿⣿⣿⣿⢯⣾⣯⣷⢱⢼⣿⣿⣿⣿
⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢎⡦⣽⣿⡿⣯⢷⣿⣿⣿⣿⣿⡿⡯⡇⣿⣳⣿⣿⣿⣿⣿⡿⣿⣻⣟⣿⢽⣻⣞⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⠋⣖⣿⣿⢯⡟⣾⣟⣿⣿⣿⣿⣿⡿⣯⣇⢗⢵⣿⣿⣿⣟⡟⣿⣼⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⢝⣾⣯⣿⣿⣿⣿⣽⣿⣿⣿⣿⣿⣿⣟⣯⣟⡮⣺⣿⣟⡷⡟⣗⡗⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣟⣿⢷⠏⣽⡯⣿⣿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣽⣟⢾⡾⣯⣿⣯⢗⡽⡕⡿⣇⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣽⣷⣿⣿⣿⣿⣽⣿⣿⣿⣽⣾⣿⣿⣿⢃⢎⣾⡻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣺⣯⣿⣿⢷⡳⣯⢿⡣⣹⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿
⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣟⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢽⣳⢿⣽⣿⣿⣻⣿⣿⣿⣿⣿⣿⣟⣾⡿⣞⣯⣿⣟⡾⣽⣽⣿⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣯⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⢾⢰⣜⡼⣽⣻⣿⣿⣿⣿⣿⣿⣿⣷⣟⡷⣿⣿⢿⠯⣷⣿⣽⣿⣿⡷⢫⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣼⢮⣴⣱⣵⣿⣿⣯⣿⣽⣿⣿⣿⢿⣿⣿⣪⣿⣿⢵⣿⣇⢿⣿⣿⣿⣿⣽⣢⢌⣻⣿⣿⣿⣿⣿⣿⣿⣿⢿⣻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢫⣾⣯⣯⣿⣯⣿⣽⣾⣿⣿⣿⣯⣿⡽⣽⣽⡽⣿⣧⢽⣝⣛⣓⡻⠹⠾⢿⣿⣿⣽⣷⣖⢍⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⣿⣿⣿⣿⣿⣿⣿⡟⣞⣽⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⢿⣿⣿⣧⢳⣿⣷⣿⣽⣳⣵⡲⣬⡹⡙⠿⢷⣧⢏⠻⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⢾⣽⣻⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣿⣿⣧⣿⣿⣷⣿⣟⣷⣿⣗⣯⣯⣫⣲⡨⡻⡯⡉⡋⣛⡛⢟⢟⡻⢿⢿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣟⡿⢵⢯⣟⣿⣿⣿⣿⣿⣿⣿⣽⣿⣿⣾⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣾⣾⣿⣿⣟⣿⣯⣯⣯⣷⣷⣷⢶⣯⣾⣱⡧⢹⣿⣿⣿⡯⢯⣝⣟⢿
⣿⣿⣿⣿⡿⣟⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⡿⣟⢿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣜⢿⢮⣿⣷⣿⣿⣷⢽⣷⣽⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣻⣼⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡹⣵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    """,
    "Ezio Auditore": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠆⠅⢐⢐⢌⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⢇⡑⢄⢅⡪⡪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⣽⣟⣷⢿⣳⡹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡠⡸⢼⣿⡾⣏⢯⣿⢮⠢⡂⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠬⠘⣜⣰⣮⡪⡚⣿⣟⣟⢯⢓⣵⡑⡽⣮⡫⣖⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡌⢆⢴⢉⢫⡟⡭⣷⣄⢝⢚⠜⣠⣟⢭⢳⣫⣗⡯⣺⣽⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⢪⢜⣮⢪⢻⣶⣵⣫⡗⢸⢘⣗⣳⢭⢮⢾⣺⣺⣗⣿⢾⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠈⡪⣳⡕⡌⢝⣯⢿⡈⠢⣙⢹⣟⣿⣻⣟⢷⢽⡺⣽⣟⡾⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡁⡂⡪⣾⢹⡮⣆⣾⣻⣾⡿⣖⣳⢯⣯⣷⣫⣭⡮⡇⡃⢟⢯⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠡⠐⢔⢕⠇⠐⡯⣏⣿⡫⡞⡽⣷⡻⣫⣗⣿⣻⣿⣽⢪⢨⠐⢌⠹⣻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠂⢈⠠⢘⢰⠑⠀⠀⡷⡵⣽⣪⠪⠪⢸⢯⣻⣺⢾⢿⣿⣿⣕⢆⠕⢐⢐⣼⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠀⠄⠠⠐⢀⢠⢑⠌⠀⠀⢰⣟⡟⣡⢲⢪⣗⣜⡨⡙⣏⣿⣻⣿⣿⣿⣷⣜⣤⢽⣺⣪⣻⣻⣷⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣲⣳⣀⠂⢄⢂⠢⡢⠁⠀⠀⠀⣼⢿⣟⠿⡩⣯⣿⣌⠻⢟⣷⢿⣟⣿⣿⣿⣿⣿⣿⣻⣼⣝⡝⣗⣗⣿⣷⡀⠀⠀⠀⠀
⠀⠒⠖⣖⢮⡻⡺⣿⢿⡿⣶⠁⠁⠀⠀⠀⠀⠀⣻⢿⢾⣗⣭⣻⣞⣣⣕⡿⢾⢛⢫⣿⣿⣾⢿⣿⣿⣿⣿⣯⣾⣜⢔⢹⢘⠅⢤⠰⠄⠀
⠀⡠⡴⡟⣏⣾⡽⠋⠑⢿⠃⠀⠀⠀⠀⠀⢠⢺⡑⡼⡁⠣⣝⠑⡍⡇⢂⠊⡧⡂⡂⣗⣿⣾⢿⣻⣽⣿⣿⣿⣿⡿⠏⢍⢫⡲⡞⣄⠀⠀
⠉⣐⡴⠓⡻⠊⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⢃⣷⣕⡕⢌⢢⠧⡡⡊⡵⡀⡂⡏⡦⣚⢺⣟⣿⣻⣟⣯⣿⡿⣿⠏⠁⠀⠈⠰⡝⠮⢆⠌⠁
⠂⠀⠀⠐⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⢁⡞⡜⡔⡝⣮⢺⣑⣵⡵⣸⢱⡘⡪⡣⡪⡪⣫⣿⢿⣞⣯⣷⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠀⡸⢐⠱⡸⡨⢢⢫⣷⣿⣿⣾⢑⠔⡑⢕⢜⠜⡬⡿⣟⣯⣟⣷⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠏⠀⠀⡇⠷⣕⢥⠣⡱⡱⣿⣿⣻⣞⢔⠡⡸⢰⢑⢕⣵⣻⡿⣿⣽⢾⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡠⠲⠋⠁⠀⠀⢨⠂⠸⣽⣷⣝⢬⢹⣯⣿⣯⡗⠕⡅⡪⣪⣾⣿⡧⢻⣻⡯⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⠀⠀⠀⢀⡜⢀⢵⣿⢿⣿⣿⣮⣷⣿⣾⡇⣱⣼⣾⣿⢿⣿⣷⠱⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠐⣿⠁⠀⠀⠀⠀⢀⣤⠞⠀⢴⣿⣻⡿⣿⣾⡿⣾⣷⡿⣿⣟⣿⣽⣾⣿⢿⣾⣯⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠙⠪⢿⣿⣿⣿⣿⣻⣻⣽⣭⣯⣽⢿⡯⡻⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⢿⢿⢷⢿⡿⣽⣾⣳⢷⣟⡿⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣟⣿⣿⣻⡾⣯⣿⢷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣻⣾⣻⣽⣿⣽⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⡿⣽⡯⡷⣟⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣯⢿⣻⣿⠗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⣿⢽⡯⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⠀⠄⠀⠄⠠⠀⠄⠠⣿⣟⡽⡽⣝⣎⠠⢀⠂⠠⠠⠀⠄⠠⠀⠄⠠⠀⡀⢀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠀⠄⠐⢀⠁⡈⠄⡂⡐⡠⠡⡊⢌⢌⠬⡨⡪⡨⣿⢯⣟⢞⣷⡟⡔⢔⢅⢕⢡⢡⢡⠡⡡⢊⢐⢐⠠⢀⠂⠄⢀⠂⠐⠀⠠⠀⠀
⠂⠁⠀⠠⠐⠈⡀⠂⠌⡂⠪⡰⢘⢜⠸⡘⡜⢜⢜⢜⢼⣿⣫⣞⣳⣽⣧⢣⢣⢣⢱⢱⠱⡸⡨⡊⡢⡑⠔⠨⠐⠠⠁⠄⠀⠂⠁⠀⠀⠂
⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠁⠀⠂⠀⠁⠊⠈⠌⠂⢑⠱⢙⢛⣞⡺⣳⢿⠸⡘⠜⠌⢂⠃⠅⠂⠈⠀⠀⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠕⢿⣿⣷⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Kratos": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⡢⠡⢂⢕⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡪⡪⡐⢅⢂⠎⡐⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢇⣇⣇⡑⡜⣬⠬⣐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⣵⣙⢺⢑⠨⢓⢕⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⢾⣕⢷⣜⢮⣺⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⡴⣿⣻⣞⣗⣗⣿⣺⡓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⣄⠤⣄⣆⢦⣳⡪⣷⣟⣿⣽⣾⢵⣳⣳⢯⠂⢄⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣝⢾⢽⢞⡼⡱⣕⢝⢮⢿⣗⡿⣽⣟⣾⢝⢂⢅⠣⡣⡑⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣖⣗⣯⣗⣯⠽⣝⡯⣞⣞⢜⣕⢽⢽⢽⢝⠪⠂⡂⡢⡣⠣⠈⠌⠠⢁⢂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣱⢿⣽⣷⣯⣟⣮⣫⡷⣽⡺⣣⢇⢏⢎⢗⢬⣂⢆⢕⠬⠡⠁⠅⢅⢂⢕⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⣿⣻⣾⢷⣿⣟⣟⣿⣳⠷⡵⡵⣕⡜⡔⡕⣜⢸⢱⡫⢶⢥⡨⣲⢰⣹⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⢿⣿⣻⣟⣿⣷⣿⣻⣾⣻⢯⡷⣻⢾⢝⢷⣯⣖⣗⣧⣫⣗⡽⡽⡯⢇⠳⡱⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢜⢵⡫⢿⢽⡯⢷⢿⡽⡾⣽⣻⣞⡮⡮⠎⢯⡺⣝⢽⢾⡷⣟⣾⣼⡏⡆⣑⢐⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢣⢣⢇⢇⡯⠃⠨⣿⢽⣝⢗⢕⠕⢌⢆⢕⡐⢅⢣⢑⢍⣿⣻⣽⣯⢹⡎⡆⡆⡇⡂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣊⢢⢙⡷⡝⠈⠀⠈⢟⡷⣝⡮⣆⣇⣆⡢⡡⡪⡸⡐⣅⡪⣸⢾⣽⠏⠀⢿⣳⢏⢆⣢⢢⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⡀⠀⠀⠀⠀⢘⡷⡮⣪⢪⠪⠁⠀⠀⠀⢸⢽⣮⣟⣞⣎⡎⡏⡫⡪⡪⡪⢪⠪⡣⣻⣽⡴⡆⡽⣮⣟⢽⢸⢽⡅⠀⠀
⠀⠀⠀⠀⠀⢹⣯⣯⢧⣀⠀⠀⢽⢯⣫⢎⢯⡓⠀⠀⠀⠀⢼⢟⣷⢽⡿⣾⣻⣳⢷⡱⡫⣾⣟⢿⡽⣯⣷⣿⠀⠘⣗⡷⣍⡧⣫⡷⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠿⣻⣗⣷⣠⢿⣻⣎⡗⡏⠂⠀⣸⣿⢰⣿⣣⣏⢿⣟⣿⣻⣯⣿⢾⣻⣷⡼⣽⣫⢷⣻⣪⠇⠀⠈⢿⣺⣝⢮⢝⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠹⣯⣿⡽⡞⡞⡽⠂⠀⠀⠨⣿⡿⣽⣷⣻⣶⣕⡕⡯⡳⡫⡫⡻⢳⢫⢣⣪⣺⢾⡾⡅⠀⠀⠨⢗⣷⡫⡿⣅⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡯⣯⡳⡇⠀⠀⠀⠀⠹⣿⣽⢾⡿⣾⣶⣭⣗⡷⡵⣧⣳⡯⡽⣗⣟⢽⣣⣿⢵⣢⠀⠀⠘⣷⢵⢝⣕⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣯⡮⡖⡇⡀⠀⠀⠀⢀⣿⡯⣟⡿⡽⣺⣳⢷⣿⣻⡽⣼⢺⡪⣗⣗⢷⢵⢿⣽⣮⡁⠀⢀⡳⣹⢷⢽⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣺⢮⢳⢵⡥⠀⠀⠀⠀⣿⢿⣕⢿⣝⡮⣿⣿⢝⢵⢻⣜⢵⣝⢷⢽⣫⢯⣳⣻⡺⣣⠀⢈⣗⣽⢯⢷⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠾⣪⢯⡯⡿⠀⠀⠀⢠⣿⣻⣽⡳⣟⣯⢿⣾⢏⣗⡷⡽⡵⡯⣏⣯⡾⡯⣞⡵⣿⠓⠀⠐⠁⢚⡯⡏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢯⣟⢦⠀⠀⢼⢷⣻⣽⡯⣷⡯⣿⢯⡿⣵⢯⣯⣿⢽⣺⢾⢽⣿⣗⡯⡅⠀⠀⠀⢀⣯⡛⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡽⡧⡄⣸⣟⣿⡯⣟⡷⣟⣿⡿⣽⡯⣟⣾⣽⣟⣾⣽⢯⣿⡿⣞⡇⠀⠀⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣟⣞⣟⣿⣟⣯⡯⣟⣿⣳⣿⣯⢿⣽⡯⣷⣟⣾⣯⣻⣽⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠿⣞⣞⢿⣽⣿⡻⣿⡽⣷⣿⣟⣷⢿⣻⣽⣿⣿⣽⡿⣯⣷⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣿⣯⡷⣽⡺⣿⣯⣿⡽⣷⢿⢽⡏⢹⣿⣻⣽⣿⣻⣿⣽⣿⡃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⣯⣿⣞⢮⣫⢷⠀⢿⣻⣟⠝⠀⠀⢻⣿⡿⣟⣿⣽⢿⢾⡁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣻⢷⢿⡯⡾⣜⢦⠀⢙⡾⣵⢢⠀⠀⢹⣿⣿⣟⣿⣻⣟⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡦⣺⢷⣻⢯⢷⣿⣻⣎⢮⢵⢴⣟⣾⡳⠀⠀⠐⣿⣻⣽⡿⣷⢿⡯⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣝⣟⣯⢟⣿⢽⣯⠗⢣⣳⢹⡺⣺⠃⠀⠀⠀⢨⣿⣟⣿⢿⣟⣿⡯⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡷⡽⣞⡿⡽⡿⡿⣵⣻⡯⡿⣔⢽⠂⠀⠀⠀⢐⣿⣻⣟⣿⣟⣯⣧⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⡾⣽⢽⡽⣽⢯⡷⣫⡻⠉⠉⠁⠀⠀⠀⠀⠨⣿⣯⣿⡷⣟⣿⣗⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣞⣯⢯⡯⣟⣽⡺⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⣟⣯⣷⣿⡿⣟⡷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣳⡽⡯⣯⣿⡚⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣟⣿⣯⣿⡿⡗⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡽⣿⣽⣻⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣯⣿⢾⡿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣻⡿⣾⣯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣾⣿⣻⣟⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣻⣿⡾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣽⣯⣿⡃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢿⣳⣟⣷⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⣷⣟⡷⣯⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⣿⢾⣿⣯⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣾⡷⣿⡿⣿⣯⣿⣧⣆⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣯⣿⢾⣻⣷⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠟⡿⣿⣽⢾⣳⣿⣻⣧⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣿⣻⡿⣷⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠛⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠉⠋⠋⠉⠃⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Arthur Morgan": """
⢯⣳⡫⡯⣫⢾⢽⢝⡽⣝⡽⣝⡽⣝⢽⣹⢵⡫⣗⢯⣳⣫⢯⡳⣯⣫⣗⣯⣯⣾⢽⣝⣞⡽⣝⡵⡯⡯⣞⡽⣝⣞⢽⢝⡮⡯⣺⢽⣹⢝⡽⣝⢽⢕⡯⣳⢽⣹⢽⢵
⣳⡳⡽⡝⣽⣹⣕⣏⡫⣞⣞⡵⣫⣞⢽⣪⢗⣽⡺⡝⠎⣎⣿⣿⣿⣿⣿⣿⣿⣿⣻⢾⣺⣝⣗⢯⡯⣞⣗⡽⣺⡪⡯⣫⢾⢝⡷⣝⣮⣻⡺⡵⡯⣳⣫⢗⣟⢮⢯⣳
⡺⣺⢽⠌⣿⣿⣽⡇⡾⣕⣗⢽⣕⣗⢯⣞⡽⡮⡫⠀⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⡷⣳⢽⣽⣻⣽⣞⢾⢵⣫⢯⢯⣫⢯⢾⢵⡳⣵⣫⢯⢯⣳⢽⣝⣞⡽⣳⢽
⢮⡳⡽⡌⣿⣿⣽⡇⡯⣺⢮⣳⣳⡳⣽⡺⡮⡯⡇⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣽⡾⣯⢯⡳⣯⢷⣷⣻⢽⢵⣫⢗⡯⣞⡽⣵⣫⢯⣞⢮⢯⣳⢽⢵⣳⡳⣝⣗⢽
⣳⢽⢝⡔⣿⣿⣻⣇⢽⡳⣽⡺⣺⡺⣕⢯⡳⡽⡕⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⢯⡯⡯⣾⣻⣗⡿⡽⣕⡯⣳⢯⢞⡽⣺⣪⣗⣗⢯⢯⣞⢽⡳⣳⢝⣞⢮⣳
⢮⣳⣫⠆⣿⣿⣿⡇⣟⢮⡳⡽⣕⢯⢞⣗⢽⣝⠆⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣟⣟⣟⣮⣷⣯⡿⡽⡮⡯⣳⣫⢯⢯⣳⡳⣵⣳⡫⣗⣗⡽⣺⢵⣫⢞⡵⣳
⣗⢗⣗⢕⣿⣿⣻⡇⣞⡵⡯⣫⣞⢽⢵⣫⡳⣵⠉⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⣷⣯⡾⣽⣷⣳⡯⣿⡽⣝⢾⢵⣫⢷⢝⣞⢮⣗⡵⣫⢗⣗⢽⢵⣫⢞⡽⣺⢕
⢗⣽⡪⣸⣟⡗⣽⡇⣗⡝⣊⣣⡙⠙⠗⠷⡿⣾⣦⣷⣿⣿⣿⣿⣿⣿⡿⣟⡿⡽⣯⣻⢽⣻⣻⢿⣻⡿⣷⣿⣯⣯⣷⣷⣯⣿⣾⣿⣾⣟⢽⢵⣫⢯⣳⢽⢝⣞⡵⡯
⢯⣞⡵⢸⡷⣏⢾⣇⢺⢮⡪⡛⠿⣿⣿⣾⣶⣵⡽⣽⡿⡿⣿⣻⣟⡿⣿⢿⣿⡿⣿⣽⣿⣽⣾⣽⡷⣿⣯⣿⣿⣷⣿⣿⣿⣿⣿⣿⡫⣞⡽⣵⡳⣯⡺⣝⡽⣺⣪⢯
⣗⣗⣝⢸⣿⡳⣝⣧⢳⢽⡺⡵⣦⣀⠑⠝⡿⡻⡸⣻⠄⠘⢟⣟⣯⣿⣽⣟⡯⣟⣿⣟⣿⡯⣯⡫⡯⡺⣿⢿⣿⣿⣿⣿⡿⡿⡽⡮⡯⣳⢽⣺⡺⣕⡯⣞⢽⡺⣪⢗
⢵⣳⡳⢸⣯⢷⢱⣳⢱⢯⣫⢯⢞⡮⣟⢦⣣⢑⡁⡗⠈⡮⣫⢯⢯⢯⢟⡵⡫⡞⡽⡳⡳⡝⡪⠊⠌⡐⣽⡿⡪⣿⢿⢽⢽⢝⣽⡺⡽⡽⡵⣳⣫⢗⡽⣺⢵⡫⣗⡽
⢯⣞⢮⢘⣿⣝⢎⡾⡱⣻⣪⢯⣻⢺⢝⡵⣫⡳⣕⢽⠀⡹⣪⢮⡳⣝⢵⢽⠨⢂⢅⠋⠅⡂⢆⢪⢂⢢⡿⡯⢺⣝⣗⢯⣫⢯⡺⡮⣻⡺⡽⣕⣗⢯⣫⢞⣵⣻⡪⣯
⣗⣗⢗⠠⣿⢮⡣⣟⢜⡵⣳⢝⡮⣏⢯⢞⣗⢽⣪⠪⢁⠈⡾⣕⣝⡾⡧⣧⣣⣐⣌⢗⠅⢄⠱⡡⢑⣸⣭⣢⢟⡮⣺⢵⡳⣽⡺⡽⣕⢯⣫⣞⢮⢯⣞⡽⣺⣪⢾⣕
⣞⢮⢇⢐⣿⢯⢎⡷⣹⣺⢵⡻⣪⢗⡯⣳⡳⣽⡪⡗⠠⠀⠨⣺⢼⣾⣽⣷⡿⣾⣕⡥⣩⢐⠠⢪⢱⣫⣿⡳⣫⣞⢽⣕⢟⡮⣞⡽⣺⣝⣞⢮⢯⣳⡳⣝⣗⡽⣕⣗
⡮⡯⡃⢐⣿⢽⡱⣟⡽⡮⣳⢝⣗⡽⣝⢮⢯⣺⡺⣜⠌⢂⠁⡞⣿⢟⣿⢾⣺⢽⢮⢟⣷⣵⣕⡼⣝⣾⣵⢹⣕⢷⢝⡮⣳⢽⣪⢟⡞⣮⡺⡽⡵⣳⢽⢵⡳⡽⣺⣪
⡮⡯⡂⢹⣯⡯⣪⢿⣺⢽⡺⣝⣞⢮⡳⡯⣳⡳⣽⡺⡽⣄⠆⠕⣿⣳⢵⣯⣷⣵⢅⢌⠺⡽⡮⣿⢯⣻⡽⣇⢗⡽⡳⡽⡵⣫⣞⡵⣻⡪⣯⣫⢞⣗⢯⢗⡯⣻⡺⣪
⡮⣻⠂⢹⣷⣻⢪⣿⣹⣳⣫⢗⣗⢯⢯⣫⢷⢝⣞⢞⣽⣿⡌⣜⣹⣯⣿⡯⡷⡝⢍⢣⡱⣽⡷⡟⢨⣿⣿⣿⢱⡹⣹⣝⢾⢕⣗⡽⡮⡯⣞⢮⡻⡮⡯⡯⣺⢵⡫⣞
⣞⡵⡃⢸⣿⢮⢳⣻⢜⣞⡮⡯⣞⡽⡵⣳⣝⣗⠝⣬⣿⣿⣷⣞⢷⣝⣾⣿⢷⣟⣿⣾⣯⢟⠨⡠⣻⡿⣟⢟⢮⡪⡺⡯⣯⣿⣕⣺⢿⡫⡚⢽⢝⣵⡫⡯⣺⢵⡻⣪
⣞⢾⡁⣺⣿⣝⢎⣿⢹⣺⢝⣽⣪⢯⣫⡳⢕⡃⣡⣛⣿⣿⡈⣿⣿⣾⣿⣻⡿⣿⣿⢟⠊⣄⣶⣿⣻⣯⠟⣨⡗⣕⠵⡽⣿⣿⣦⣯⡟⢎⣶⢽⢵⡳⡽⣝⡮⣳⢽⢕
⣯⣳⢵⣿⣿⣞⢺⣿⢸⡯⡯⣺⢪⢳⣳⢓⣰⣿⣿⣿⣗⣻⣷⣌⠻⣿⣿⣾⣺⣝⢕⣕⣾⣿⣟⡯⣛⣴⣻⣿⣮⣞⡜⡼⡹⣦⣯⣟⢿⡮⡯⣏⢧⢫⢝⢞⢮⡳⡽⣕
⣞⢮⣻⣿⣿⣯⣻⣾⢽⡏⡌⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣦⡈⡛⣿⣿⣿⣿⣾⣿⣿⢛⣼⣿⣿⣿⡯⡹⣽⢿⣾⣋⣾⢾⣝⢲⣝⢽⡪⡪⣪⢪⢪⢺⢸⢹⡪
⡽⣝⣾⣿⣿⣿⣺⡯⡷⣿⢷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣿⣿⣿⣽⣿⢣⣿⣿⣿⣿⢿⣇⡿⣵⣿⢿⣪⣿⠷⣙⡿⣪⢗⢇⢇⢇⢿⣜⡕⣇⠧⡝
⢽⡺⣺⣿⣿⣗⢵⡿⣽⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⡝⡝⣿⣿⣿⣿⣿⣿⣳⢽⣾⣳⢸⣿⣿⣿⢏⠮⡯⣺⣿⣙⣾⣯⡟⢮⣞⢮⡳⡣⡣⣻⡬⣻⣗⢇⢗⣿⡪
⢯⢽⢝⣿⣿⡯⣯⡿⢿⠇⣺⣿⣿⣿⣿⣿⣿⣿⣿⡏⡎⡎⡎⡎⡝⡽⣿⡿⢿⣿⣿⣿⣾⣿⣿⡫⡪⡪⣺⣪⣿⣏⣯⣿⢮⡹⡷⣱⢣⢣⢣⢍⢿⣇⣿⡿⡸⡩⣿⡮
⣯⣺⢯⣿⣿⣟⢾⣻⣿⣽⣾⣿⣿⣿⣿⣿⣿⣿⣿⢎⢎⢎⢜⢌⢎⢮⣿⣷⣅⣻⣿⣿⣻⣿⡣⣇⢧⡯⣷⣿⣯⣾⣽⠷⣥⢻⡪⢧⢣⢣⢣⢣⣻⣷⣿⡳⡱⣵⡽⣏
⡷⣹⡿⢽⣗⡇⣯⣏⢧⣿⣿⣿⣿⡟⣽⣿⣿⣿⡝⡎⡎⡇⡇⡇⣇⣿⣿⡿⣿⣿⣿⣯⡿⡣⡳⣵⣟⣽⡯⣝⣽⢾⣯⣷⣝⢗⡝⣞⢜⢜⢼⡸⣺⣿⣿⣣⢗⣿⡏⡷
⣷⣿⣿⢍⡚⢮⣺⣷⣽⣾⣿⢿⢏⢎⣾⣿⣿⣿⡣⡣⡣⡣⡣⡣⣾⣿⢻⢸⢽⣿⣿⢪⣏⢮⣾⣟⡾⣿⢿⣯⣟⣧⡻⣻⡪⢧⢹⡸⡸⡸⡸⣪⣿⣿⣷⢯⡣⣿⢎⢇
⣽⣿⣿⢷⣽⢣⡿⣿⣿⣿⣯⢫⢎⢾⣿⣿⡿⡳⣱⢱⢱⢱⢱⣽⢫⢪⢎⡇⡯⣿⣷⣻⣵⢿⣳⣇⢏⣻⢿⣾⣿⡿⣝⡼⣎⢇⢇⢯⢪⢪⢪⣿⣿⣿⢝⣿⣸⡟⡜⣜
⣿⣿⣿⡷⣿⡱⣟⡳⡱⣹⣿⢜⢵⣿⣿⡿⣱⡹⡜⡜⡜⡜⡎⡎⡎⡎⡮⡪⣻⣺⣿⣟⣞⣿⢼⣔⣟⣿⣯⡙⣗⢵⣳⣟⢼⢸⣸⢕⡕⡕⣝⣿⣿⣿⣽⣷⣿⢕⢕⢕
⡶⡫⠩⠚⢳⢹⣻⣕⡧⣪⣿⡪⣾⣿⣿⣣⣿⡺⡸⡸⡸⡸⡸⡸⡸⡸⡕⣝⡮⣾⣻⣞⡷⣲⣶⣽⢿⣇⣛⡯⣳⢿⡿⡕⣇⣷⣟⢵⢱⢱⣹⣿⣿⣯⣿⣿⣿⡕⡕⡅
    """,
    "John Marston": """
⢿⡽⣽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢽⢝⡽⡽⣝⡽⡽⣝⡽⡽⣝⢽⢹⣹⡽⣝⡽⡽⣝⡽⡽⣝⡽⡽⣝⡽⡽⣝⡽⡽⣝⡽⡽⣝⡽⡽⣝⡽⣵
⢽⡽⣽⢽⣫⡯⣯⢯⢯⢯⢯⣗⡯⣯⢣⢹⡮⡯⡯⡯⡯⡯⡯⡯⣻⢮⢯⡻⡮⡯⣏⡎⡎⡞⣿⣿⣷⣽⢽⡺⡽⣝⡮⣯⡻⡮⡯⣻⢮⢯⡻⡮⡯⣻⢮⢯⡻⣮⣻⣺
⢽⣺⢽⡽⣞⡽⡾⡽⣽⣝⣗⣗⢯⢯⢪⢸⡯⡯⡯⡯⡯⡯⡯⡯⣳⣫⣳⣝⣝⣕⣟⣬⣼⣮⣿⣿⣽⣿⣷⣯⣿⣾⣽⣮⡯⡯⡯⣳⢯⣳⢯⢯⢯⣳⢯⣳⣻⣺⡺⣺
⣻⣺⢽⡽⣳⢯⣟⣽⣳⣳⣳⢽⢽⢽⢪⢸⡿⡽⡽⡽⡽⣝⢾⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣻⣻⣻⣿⢿⣿⣿⣿⣿⣿⣿⣿⣯⢯⢗⣟⡮⡯⣯⣳⣝⣗⣗⣗⢷⣝⢷
⣺⣺⡽⣽⢽⣳⣳⣳⣳⣳⡳⡯⡯⣟⡜⣸⡯⡯⡯⡯⡯⣞⣿⣿⣿⣿⣿⣿⣿⣟⣯⣿⡷⣏⣷⣿⣻⣟⣷⡿⣿⣿⣿⣿⣿⣿⢽⢽⢮⢯⢯⣞⣞⣞⢞⣞⢮⢷⢽⢽
⡮⣗⡯⣗⣿⣺⣺⣺⡺⡮⡯⡯⣻⡢⣯⢸⡯⡯⡯⡯⣻⢮⣻⣿⣿⣿⣿⣿⣟⣗⢯⢺⡹⣨⣺⢕⡳⡹⣕⣿⣿⣿⣿⣿⣿⣿⢯⢯⣳⢯⣳⣳⡳⣳⣻⡺⡽⡽⡽⣝
⣝⣗⡯⣗⣗⣗⣗⣗⢯⢯⢯⢯⣳⡣⡯⢺⡯⡯⡯⣯⣳⣻⡺⣿⣿⣿⣿⣿⣿⢌⠎⡑⠵⡳⡳⣽⣜⢵⣳⣻⣯⣿⣿⣿⣿⣟⡽⣵⣫⣗⣗⣗⢯⣗⢷⢽⢽⢽⣝⣞
⣳⡳⣯⣳⣳⣳⡳⡽⡽⣝⣗⢯⣚⡪⣟⢼⡿⡽⣝⣞⣞⣞⢾⢝⣿⣿⣿⣿⣟⡧⡱⡝⢬⢶⡽⣵⣻⡳⣗⣿⣫⣿⣿⣿⣿⣳⣻⣺⣺⡺⣺⣪⢷⢽⢽⢽⢽⢵⣳⡳
⣗⣟⣞⣞⣞⢮⢯⢯⣻⡺⣮⢱⣷⢋⡞⣼⢯⣻⣺⣺⣺⣪⢯⡻⣮⡻⡿⣿⣮⣿⣺⣿⣬⣶⣽⣾⣾⣿⢿⣿⣿⣿⣿⢿⢵⣳⡳⣵⣳⢽⣳⢽⢽⢽⢽⢵⢯⢗⣗⡯
⣗⣗⢗⣗⡽⡽⣝⣗⣗⢏⠮⣽⡻⡸⡣⡿⣼⣺⣺⡺⣺⣪⢯⡻⡮⡯⡯⣯⣻⣿⡿⣿⣿⣿⣿⣿⣿⡿⣿⢯⣿⣟⡽⣝⣗⣗⢯⣳⡳⡯⣞⡽⡽⡵⡯⡯⡯⣻⣪⢯
⣺⣪⢟⡮⣯⣻⣺⡺⡮⣣⣷⡮⡷⣿⣮⠪⣺⣺⣺⣺⡳⡽⡽⡽⣝⣽⣺⢵⣳⢿⡇⠘⠿⣞⢿⣺⡷⣟⢏⢏⣷⣿⣟⣞⣞⢮⣟⢮⢯⢯⡳⡯⡯⡯⡯⣫⢯⣳⢽⢽
⡺⡮⣯⣻⡺⣪⣲⣱⣘⢔⡙⣷⣿⣷⣳⣟⣞⢮⣞⣞⢾⢽⢽⣝⣞⣞⢮⣻⢸⣱⣀⡁⢥⢕⢽⢪⢺⡸⣽⣿⣿⣿⣟⡷⣝⢷⢽⢽⢝⣗⣯⡯⣯⢯⣫⢯⢯⢾⢽⢽
⣺⢽⣺⣺⡺⣿⢕⡝⡿⣧⢽⡲⣽⣿⡯⡧⣗⣟⢮⢾⢽⢽⢵⣳⡣⡳⢽⡾⣿⡿⣿⣿⣿⣴⡑⢜⡼⣾⣿⣿⣿⣿⣿⣿⣿⣯⣯⣯⣿⣽⣞⣯⣿⡳⡽⡽⡽⣝⡽⡽
⡯⣗⣗⢷⢽⡺⣇⣗⣽⣽⣿⣾⣷⡿⡯⣯⣳⢽⢽⠽⢽⣹⢱⢢⢫⢮⢣⢻⢻⡝⡜⢭⢙⢕⡕⣕⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣟⡾⡽⡽⡽⣝⡮⡯⡯
⡯⣗⡽⣝⣗⢿⣿⣿⣿⣿⣿⣿⡿⡽⣝⣞⡮⡏⠃⢙⢜⢺⢵⡱⡕⡬⡳⣝⢮⢳⣽⡬⡣⡣⡏⣞⢮⢪⢾⣿⣿⣿⣟⡿⣟⡿⣽⣽⣿⣿⣿⠡⢊⠫⡯⡯⣾⢽⢽⢝
⣯⢗⡯⡷⡽⣝⣿⣿⣿⣿⣿⣿⢽⣝⣞⡮⠃⠠⠈⡀⢮⢽⡹⢽⢵⢝⡬⡖⣫⢳⢭⢻⣪⡣⡗⣝⣯⢿⣻⣿⢻⡻⣝⢿⡷⡹⣼⣾⢾⣻⣿⠨⢐⠨⢹⣽⢽⡯⡯⡯
⣿⢽⡽⣽⢽⣳⢟⣿⣿⣿⣿⣿⡳⣗⣷⡁⠐⡀⠂⡘⣺⣇⢏⢎⢿⢿⣕⡯⢮⡝⡺⡵⣺⡹⣏⢾⣜⢜⠼⣼⣿⣿⣷⣷⣽⣹⣮⣾⣾⣿⡟⡎⡆⠅⡹⣾⢯⣿⢽⣝
⡽⣯⢯⢯⡯⣟⣾⢽⣺⣳⣫⠫⣻⣽⢾⠑⠐⠐⢕⢘⢼⣿⣽⣿⣿⣿⣿⣽⢯⣞⡽⡺⡵⣻⢼⡹⡽⡿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡘⡜⡐⢅⠪⣿⣽⣯⣿⡾
⣟⣟⡿⣯⡯⣷⡳⣹⢞⣞⢼⢌⢻⡾⠉⠄⠪⠈⠨⣊⢺⣿⣿⢟⡯⡻⣝⢵⢹⢺⣵⡯⣗⣏⣞⢽⢮⣝⢽⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⢕⢸⢸⠐⠔⣿⣾⣷⢿⣟
⣻⡽⣯⢷⣟⡷⡇⣗⢯⢮⡳⣑⡙⠀⠄⠂⠈⠌⡂⢜⢔⣿⣿⣽⡫⡎⣎⢮⡺⡕⡗⡽⣞⡵⣗⡽⡞⡷⣻⡼⣺⢻⣿⣿⣿⣿⣿⣿⣿⠪⡂⢎⢮⢊⠌⣿⡷⣿⣻⡿
⢯⡿⣽⣻⣞⣯⡇⡗⣯⡳⣝⢮⢢⠁⠔⡈⠄⡂⡌⢜⢜⢾⣿⢣⢫⢞⡫⡺⡜⡽⡸⡜⣎⢯⡷⣗⣟⣽⢞⣽⢯⣷⡷⢮⣯⣿⣿⣿⣟⢵⠘⡜⡎⠔⡈⢷⣿⣿⡿⣿
⢯⡿⣽⢾⡽⣞⠆⣯⡺⣝⣞⢽⡱⡡⠣⡪⡱⢣⡣⡣⡣⡻⣗⢍⢎⡆⡇⣗⢝⡜⣎⢞⡜⣜⡧⡫⣷⡿⣝⣷⣟⣽⣻⣿⣽⣿⣿⣿⡳⡕⡕⡜⡎⣎⢔⢕⠨⣿⡿⣿
⣫⣟⡽⣽⣫⢿⡅⡷⣝⣗⡵⣫⢞⢜⠬⣊⢜⡢⣣⢫⢳⢹⢕⢗⡳⣝⡮⣞⡜⣎⢎⣮⣾⡮⣷⣿⣮⣟⡯⣿⣾⣳⣟⣾⣻⣷⣿⢿⣣⢫⢎⡎⡂⡢⡡⡕⡨⢙⣿⣻
⣳⣗⣿⡺⡮⣗⣇⢽⣺⡺⣺⢵⡫⡧⡱⢑⢕⡕⣕⠵⣷⢿⡱⡱⣽⡞⣝⢮⣳⢱⢻⡹⣜⢜⣮⣯⣯⣿⣿⣾⣿⣿⣿⣾⢯⣿⢽⣟⣧⢳⡱⡑⢬⢪⠪⡪⢌⢢⢻⣿
⣿⡾⣷⣟⣯⣷⣫⡪⣞⣞⢷⣝⢮⣳⢅⢅⢣⢣⣷⢽⣯⡿⣎⢽⢕⣗⡵⡟⡎⣮⣣⣗⣵⣿⣻⣻⣿⣿⣿⣿⣿⣿⣾⢿⣿⣻⣽⣻⣯⣗⢕⢵⢱⢕⢕⠜⠨⡂⡙⣷
⣷⢿⣿⣽⢿⣽⣯⣷⢱⣫⢷⣝⣗⣽⣪⡮⣟⣽⣻⣻⡽⣿⢕⢯⣪⢲⣹⣾⣿⣿⡿⡟⣝⣵⡽⡱⣽⣹⣹⢝⡿⣿⣿⣿⣻⣿⣿⣺⢿⣾⣕⢧⢳⢕⣵⢼⣼⡲⣌⣾
⣽⣟⣷⣟⣿⢷⡿⣾⡷⣧⡷⣳⣳⣗⡷⣯⣟⣮⢷⢯⢿⣽⢪⡳⣜⡾⣫⢞⢏⢧⣳⣟⣧⣗⢝⣺⣾⣿⣻⢻⣿⣮⣮⣻⣻⣞⣿⣿⡽⣾⣗⣷⣻⢯⢯⣟⢞⡮⡳⣻
⣽⣯⣷⢿⣽⣟⣿⣽⢿⣻⢿⡯⣷⣳⡯⣷⣳⡯⣟⣯⢿⣺⢹⢵⢳⡹⣜⣮⣷⢷⡧⣳⢳⡱⣽⡪⡯⣻⣻⢿⢯⣿⣿⣿⣿⣿⣷⢿⣿⣻⣿⢷⡽⡽⣽⡺⣕⢯⡺⡹
⣿⣾⣻⣿⣽⣯⣷⣿⣟⣿⡽⣽⣳⢯⢿⢽⢾⣽⣻⣞⡿⡵⡟⡯⣳⣹⣱⣣⣳⠽⡼⣪⡾⣼⢮⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣯⣿⡿⣯⢯⣗⢯⣳⢳⢍⢗
⣿⣾⣿⣾⣿⣾⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣷⣿⣿⢱⢍⢟⢝⣝⣕⣧⣧⣯⣾⣟⢽⣾⣿⣟⢟⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣪⣟⢮⣳⡑⠔
    """,
    "9S": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⡁⢂⠐⠠⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡂⢐⠀⡂⢐⠈⡐⡐⢐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⢐⢐⢐⠐⡀⠂⠄⢌⠰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡢⣆⢅⣦⣷⣮⠌⡊⣮⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣪⣿⣿⣷⣻⠯⡞⣯⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠩⠩⠈⠄⠌⡐⣸⡇⡿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣁⣇⣥⡕⠶⣯⣯⣿⡟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠽⠢⣘⣼⣿⣽⡾⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⣴⡵⢃⣬⣾⢿⣿⢽⣳⡽⣾⣺⣲⣶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣷⠄⣥⣞⡿⡽⣯⣿⣾⣿⣯⣟⡮⣪⣿⢷⡝⡷⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢶⣾⢮⣗⣿⡻⣯⣟⣿⣽⣷⢿⣽⣗⣿⣻⣯⢮⣻⡄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⢾⣽⣾⡿⡻⣿⢺⣻⣾⡯⣟⡷⣿⣯⢟⣿⣽⡾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢵⣯⣿⢿⣟⡿⣽⡯⣿⡽⣾⡿⣟⣿⣽⣿⣷⡽⣞⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣽⣾⣟⣿⡿⡯⣾⣷⣷⣿⣿⣿⣿⣿⣷⡿⣿⣿⣧⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢯⢞⣾⣿⣿⣿⣵⡿⣾⣷⢿⣿⣽⣗⢿⣿⣽⣿⣻⣿⡆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣯⡯⣭⣿⣿⣷⣗⣭⣿⣻⣾⣿⣿⡟⠀⢸⣿⣾⣻⣾⢿⣧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣯⢇⣿⣿⣿⣿⣿⡿⣾⡿⣽⣽⣾⡇⠀⠈⣾⣾⡿⣽⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡷⣿⢸⣿⣿⣿⡿⣷⡻⣯⣾⣿⣿⣯⣇⠀⠠⣿⣷⣿⣿⡿⣟⠆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⢾⡳⡯⡇⢿⣿⣿⣯⣿⡯⡾⡯⣷⣟⣿⣻⣾⣆⢠⣟⣗⡿⣷⣻⡽⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢄⣨⡳⡽⣝⡅⣸⣻⣾⣿⣷⡿⡿⣿⢿⣽⣾⢿⢽⣞⢈⡛⣗⣿⡽⡮⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠌⣼⡷⡯⣯⣞⢂⣿⣿⣿⣷⣿⣿⢯⣿⣻⢯⣿⣯⢯⢖⣼⣯⣟⣿⡯⣿⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣈⢯⣿⣫⡷⠛⢸⣿⢿⣾⣿⣯⣿⣿⢗⣯⣿⣻⣞⣯⣏⣷⣿⣟⣾⣟⣵⡗⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢬⡶⣿⠝⠀⠀⠀⣸⣿⣟⣿⣿⣿⣽⣟⣯⡷⣿⣟⡿⣗⡧⣽⣿⣿⣿⡾⠓⠏⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡞⣾⡯⡳⠀⠀⠀⠀⢨⡻⣾⢻⣫⣯⣯⣿⣯⡿⣯⣗⣯⣿⣻⣷⣿⣷⣿⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⡿⢧⣟⢾⠀⠀⠀⠀⠀⢵⣽⣽⢝⣷⣻⡮⣷⣻⣟⣯⣟⣾⢽⣿⣻⣿⢿⡯⣷⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡯⠀⡟⢹⡈⠓⠀⠀⠀⠨⡱⣷⢽⣿⣽⣞⣯⣷⣻⣿⣟⣾⢿⣯⣺⣯⣿⣻⡽⣵⡂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠁⠀⠙⠀⠁⠀⠀⠀⠀⠀⢰⣻⣿⣿⣽⣯⣿⣳⣻⣿⣫⢾⣻⣟⣮⢿⢽⠓⠋⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢊⣶⣷⣯⢷⣻⢷⡷⣷⣯⣷⣿⣿⣿⣽⣿⣿⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢞⣟⣿⣻⣯⣯⣳⢿⣻⣿⣿⣻⣗⡿⡷⣻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢯⣿⡿⡿⣟⣿⡎⣿⣿⣿⣾⡿⣟⣝⣾⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣿⢯⣿⣻⢿⣻⣽⣣⢻⣿⣷⣯⣿⣿⡳⣷⣝⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢻⣟⣽⣾⣿⣻⢾⢽⡺⣿⡷⣿⢾⢗⣟⣗⡷⣅⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡿⡿⣟⢿⢗⡿⠹⠊⠯⠿⣽⣻⢽⡳⣯⡻⠺⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⡂⠢⠡⡑⠅⠀⠀⠀⠀⠣⠢⡑⢌⢌⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡂⠡⠁⠔⡁⠀⠀⠀⠀⠨⢁⠂⢂⠡⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠡⢁⠅⠄⠀⠀⠀⠀⠀⢂⠌⡐⠨⠀⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠡⠨⡐⠠⠡⠀⠀⠀⠀⠀⠀⠢⠨⠐⡁⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⠨⠠⢁⠊⠄⠀⠀⠀⠀⠀⠨⠠⢁⠂⡂⢂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣥⡪⣤⡬⡶⡀⠀⠀⠀⠀⢸⣲⡦⣶⣲⣼⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣻⡵⣗⡯⡇⠀⠀⠀⠀⠀⣷⣿⣺⣞⢿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣳⢧⣳⣫⠂⠀⠀⠀⠀⠀⣿⣺⢷⢽⢝⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⣓⣯⣻⢽⣺⣺⣼⢶⠀⠀⠀⣺⣽⣽⣵⣫⢯⢾⡒⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⢾⡿⣟⠇⠀⠀⠀⢸⣷⣿⡵⣝⣽⣟⠇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⢷⣯⣿⢿⢽⠀⠀⠀⠀⠀⣿⣾⣯⡷⣟⡾⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣫⣟⣯⢷⡯⠃⠀⠀⠀⠀⠀⢹⣛⣚⣯⢳⡍⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⡷⡿⣯⠉⠀⠀⠀⠀⠀⠀⠈⣿⣷⣻⢬⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣟⣟⣯⣟⠃⠀⠀⠀⠀⠀⠀⠸⣟⣾⣽⢽⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⣿⢿⣻⣽⡆⠀⠀⠀⠀⠀⠀⠠⣫⡿⣽⣣⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣶⣿⣻⣻⣽⣻⣝⣞⣇⠀⠀⠀⠀⠀⠀⣸⢯⢿⣷⡷⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠫⠯⠮⠮⠝⠊⠁⠉⠉⠁⠀⠀⠀⠀⠀⠀⡿⣿⢿⢾⡏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Liu Kang": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⡀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣽⣿⣟⣿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣻⡿⣟⣯⢿⢿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡬⡗⣯⡻⡮⡯⣏⢷⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡽⡨⡳⣻⠹⡻⡕⡽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣯⣆⢝⣖⢷⣫⢪⢿⡯⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⣿⣿⡪⣮⣟⣮⣿⣊⢫⠁⠀⡠⣴⣞⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠏⠿⢙⠁⣗⢽⡳⣳⢻⡜⡔⢔⣿⣯⢷⡋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠁⠈⢄⢊⢔⠱⡩⡊⢎⢊⠊⢼⣟⣾⣷⡳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣌⠀⡀⠅⡂⠂⡂⢕⠰⡘⡌⣔⠌⡿⣿⣿⣾⣻⡭⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡐⡕⢀⢆⢪⢢⣣⣣⣗⣯⡂⣿⣻⣽⣿⡞⣿⠥⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡡⣪⡪⡰⡱⣕⣗⣷⣳⣿⣻⣧⡟⣿⣿⡿⡯⡯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠘⡕⡕⢯⢯⡯⣷⢿⣽⢾⢿⣾⣻⣗⣗⣿⡻⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣮⡪⣸⢸⢸⢜⡾⡽⣽⣞⣟⣿⣺⣗⡿⡊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢜⣯⣷⡷⢸⡘⡼⡽⡽⡯⣗⣟⣞⣷⣻⣞⠍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⣝⣾⣻⣿⢪⢮⡺⣽⢽⣝⡷⡽⣺⣺⢾⢝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣕⡝⣟⡿⢪⣳⢜⣗⣟⡮⣗⢽⢵⡫⣯⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣵⣟⣾⡆⢷⣳⣳⣷⣷⣯⢷⢯⢗⣯⢯⡿⡅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠉⠑⠁⣹⣿⢿⣿⣿⣯⢟⣟⡿⣽⣽⢾⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣾⣿⣿⣿⣿⣿⣿⢿⣷⣻⣟⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⢿⣿⣿⣿⣿⣿⣿⢿⣯⢿⡯⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣻⣷⣿⣿⡽⣟⣟⣯⣟⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⢿⣾⣟⣯⢟⡮⣯⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⣾⣿⢿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⡿⣷⡿⣿⡿⣿⢽⡾⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡟⠿⠙⠈⣷⣿⡯⣟⣗⣟⡯⣿⣽⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⠈⠀⠀⠀⠀⠀⡿⣷⣿⣿⣞⡮⡯⣷⢿⡿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢻⣿⣾⡿⣾⣟⣿⣻⣯⣿⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣷⣿⣿⣽⣾⢿⣾⣿⣷⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣟⣿⣻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣯⣿⣽⣿⣿⣿⣿⢽⢵⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⢿⣝⣗⣷⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢹⣿⣿⣟⣯⣿⢪⣞⣷⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣿⣿⣯⣿⣿⡿⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢻⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⢿⣟⣟⣯⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣷⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⢿⣿⢿⣻⣽⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⡿⣯⡿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠿⠿⠿⠿⠿⠛⠉⠉⠉⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣷⣿⣽⣯⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⢿⣾⣿⣷⣿⡿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠾⠿⠿⠿⠟⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Johnny Cage": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢀⡄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⣿⣯⡿⣯⡯⡷⣄⠀⠀⠀⠀⠀⠀⠀⠀⢰⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠨⣷⡿⣿⢾⣿⣿⢿⣿⡷⡆⠀⠀⠀⠀⠀⠀⠀⢸⣳⢿⣐⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⡿⠩⢰⢱⣻⢾⡇⠄⢻⣯⠀⠀⠀⠀⠀⠀⣊⡧⣪⢿⣹⢕⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⣯⡱⣨⣺⣺⢿⣽⡢⡹⣯⡃⠀⠀⠀⠀⠀⠲⣳⢧⢷⢿⣟⣮⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⡺⡽⡟⡝⣿⣿⠽⠈⢳⡅⠀⠀⠀⠀⠀⠀⠀⡙⣽⣫⢗⡷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢃⢇⠯⠧⣧⡼⣿⡥⢑⢠⠂⠀⠀⠀⠀⠀⠀⢀⠫⣒⢽⢽⢽⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⡹⡱⣳⡯⣳⢏⡢⡀⠀⠀⠀⠀⠀⠀⠀⡀⡪⡪⡯⣫⣗⡇⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣮⢪⢝⣧⣕⡵⣓⠀⠀⠀⠀⠀⢀⠄⠄⡂⢮⣺⢽⣳⣳⠣⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡊⡻⣻⣿⢿⣻⡢⡁⡌⢤⠠⠨⡂⠌⠨⡪⣕⣗⣟⣗⣯⢇⠅⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡊⡪⣺⢺⠫⡩⢊⠅⡜⠌⡊⢌⢢⢱⣱⣹⢯⡿⣞⣯⣷⢵⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠪⡚⠨⡐⠔⢌⠢⢑⠠⡑⢬⢲⣷⣷⣿⣽⣿⣟⣿⣻⣽⡗⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠠⡐⡁⡂⠕⡈⡔⡨⡸⢐⢑⠄⢕⢜⢼⣽⡿⣾⣿⣯⣷⣿⣿⣻⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠠⡃⢕⢰⢐⢌⢆⠣⡑⢌⠢⡱⠐⡅⣇⡯⣟⣾⣿⢿⣷⢿⣻⣯⡿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⢐⢍⢎⠆⠕⠔⢜⢂⠃⠅⡢⡱⡨⡪⡮⣗⣿⡿⣟⣿⣻⠽⣻⡫⡣⠪⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢡⢱⠱⠨⠨⠨⡸⡨⠢⡡⢡⠨⡢⢪⢮⢯⣿⣽⣿⣻⡽⡸⢈⠮⡊⡢⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣑⢸⠨⡨⠨⡪⡪⡘⢌⠪⡪⡪⡜⡜⡾⢽⢷⣿⣽⣟⣎⢆⢡⠨⡂⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠱⣑⢜⣜⡎⡃⠅⡢⢁⢂⢂⢪⢘⢜⢽⢽⡷⣿⣟⡮⠪⡐⢕⠔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⡑⢕⢏⠎⢔⢐⠅⡎⠔⡐⠜⡜⡌⡎⣏⢯⡿⣟⣿⡪⡱⠨⡂⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢅⢂⢳⣳⡑⡕⡂⠅⡊⡌⢄⢣⢣⡳⣝⡼⣝⡿⣿⣯⡳⡡⠊⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⠆⣗⣿⣧⡃⡢⡑⢜⢌⠢⡣⡱⣝⢾⣽⢷⣫⢿⡾⣕⠢⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠢⡹⣪⣷⡿⡘⡔⠌⡈⡂⠅⡂⢕⢕⣟⣿⣿⣽⣳⡻⡽⡌⠄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⡨⣹⡽⡫⠫⠀⠨⢂⢐⠨⢐⠨⡪⡳⢽⣻⣾⢿⣺⠪⢗⠬⡠⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢐⠠⡣⣟⡜⡎⡂⠅⠨⠐⡐⢨⢂⠪⡐⡪⢍⡕⣕⢷⣲⢯⣳⡛⡎⡊⠌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⢌⠪⡘⡜⠜⠨⠂⣆⢇⡓⡔⡬⣪⣣⢳⣳⡽⣟⡾⣯⣟⣞⡮⡳⡱⡈⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡪⡪⣿⣲⣔⡁⠊⠠⡳⡕⡌⡲⣱⡪⣺⢜⣷⣻⣻⣽⢷⣻⣾⣻⣽⣲⡢⣂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠬⣺⡻⡺⣎⠏⠀⠰⢱⣣⡷⣽⣮⣾⣽⡷⣿⣾⣟⣿⣿⣽⣾⡿⣷⢯⣟⠽⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡁⡕⡟⢼⠱⠊⠀⠀⣸⣟⣟⢿⣻⣞⡿⣾⢿⣿⣟⣿⡿⣯⣿⣟⣿⢯⣟⣞⡞⡮⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢔⢝⢎⠗⠁⠀⠀⠀⢼⣺⣺⣻⡽⣞⡿⣽⢿⣷⢿⣟⡿⡽⣞⣗⣯⣟⣞⡮⣳⢬⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢜⡪⡀⠀⠀⠀⠀⢀⡯⣞⢞⣞⣟⣯⢿⣻⣿⣻⢿⢽⡽⣽⣳⣻⣺⣳⡳⡯⡯⣇⢻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢌⢪⣻⠄⠀⠀⠀⠀⢸⣞⢗⣟⣾⣺⣞⣿⣺⣯⣿⣻⡯⣯⢗⣗⣗⡷⣯⢯⡯⡯⡾⡝⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢨⢠⢳⢿⠁⠀⠀⠀⠀⣺⢮⣻⢾⢾⢷⣿⣽⣿⣽⣯⣷⣻⡵⣻⡺⡮⣿⢽⣿⢽⡽⡽⡵⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """,
    "Atreus": """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⢶⡶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⡽⡳⡯⡞⡯⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡺⠨⡈⠣⡈⠢⢸⠀⠀⠠⡠⠄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢙⠔⡲⢃⠲⡳⢘⢠⡺⣏⢮⠐⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⡄⢌⣂⠥⣂⠪⡀⠾⢹⢜⠌⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⢌⡪⡓⡲⢵⢕⣽⡚⣮⢪⢀⠀⠀⠀⠀⠀⠀⠀
⠀⡀⠀⠀⠀⠀⠀⠀⢀⣤⡪⣗⢧⣇⢇⢧⢹⢡⢣⢻⣸⡜⡢⠀⠀⠀⠀⠀⠀⠀
⠀⡇⠀⠀⠀⠀⠀⠀⠘⢵⣯⡪⡆⡳⣕⢏⢖⠅⢇⠣⠳⡑⡑⠀⠀⠀⠀⠀⠀⠀
⠀⣵⢀⠀⠀⠀⠀⠀⠀⢸⢪⣟⣿⣜⡜⣎⠳⡩⡪⡜⡭⡰⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢪⡀⠑⢀⠀⠀⠀⢀⢯⡳⣽⢝⣞⣷⢸⢘⢜⢬⡺⣪⡪⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣧⠀⠀⠐⢀⠀⣝⡵⣫⢯⣗⣗⡯⣟⣜⡼⡎⡖⣌⢯⢅⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠸⡥⠀⠀⠀⢨⣗⣯⣇⢯⡿⡮⣯⡻⡚⡜⡅⣇⣜⢮⡳⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⡥⡄⠀⢓⠣⣳⣻⣏⡯⣯⢗⢷⢽⣜⣞⣞⣞⣽⢮⢣⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢹⠄⠀⢸⢨⡂⠙⠺⣹⣪⢟⢯⣷⣫⣢⢪⡚⣞⢿⡕⡥⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠰⣓⠀⢱⢐⠀⢠⢝⢮⡾⣍⡷⢵⢵⢵⠳⡕⣟⣦⠽⡪⢅⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢣⡣⡸⡲⠀⡻⣜⣟⣯⡳⣝⣝⢽⢹⢱⢕⢽⣾⡣⢨⢀⠂⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢫⢽⢑⠰⡹⣮⣻⡺⡽⣜⣮⡳⡕⣕⢪⢲⠉⠀⠆⢑⠄⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠰⣹⢰⠱⣝⢷⣟⣾⡹⡼⣺⡺⣝⢮⡣⣫⡄⠀⠀⠎⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠑⠗⠿⣜⡝⡻⣺⡺⣹⣪⢻⣺⢽⣺⢼⣂⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢾⣻⡽⡶⣽⣢⢓⣗⡟⡽⣺⢷⣳⠑⢄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣨⡿⣿⢿⣻⣽⢾⠉⣿⣝⡻⣞⡿⡞⠛⠚⠶⢤⣄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢑⡿⡯⣟⣿⣽⠛⠀⢻⣽⣿⣽⣿⢏⠀⠀⠀⠀⠈⠳⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡻⡽⣗⡿⠀⠀⠘⣿⣿⣿⣾⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣺⣯⢿⣽⠃⠀⠀⠀⣿⢿⣗⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣷⣳⢿⡞⠀⠀⠀⢘⣟⣟⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢯⣿⣽⡇⠀⠀⠀⠨⣿⢾⢯⣿⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⣞⣿⠂⠀⠀⠀⠀⢝⣿⢯⣟⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣟⢿⣯⡇⠀⠀⠀⠀⠀⠸⡿⡯⣯⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⣟⣿⠁⠀⠀⠀⠀⠀⢨⢿⣻⣽⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣔⢯⢗⠀⠀⠀⠀⠀⠀⢨⣯⢷⣻⣣⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⢾⢯⣟⠄⠀⠀⠀⠀⠀⠀⠉⠙⢗⢯⣫⢧⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣏⣗⡽⡻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """
}