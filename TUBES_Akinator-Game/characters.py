# characters.py
# Data 65 karakter game dan pembangunan Binary Decision Tree
# Setiap leaf node = 1 karakter yang bisa ditebak Akinator

from tree import Node, DecisionTree

def build_character_tree():

    # ─────────────────────────────────────────────
    # LEAF NODES — 65 karakter
    # ─────────────────────────────────────────────
    # --- Resident Evil ---
    leon_kennedy   = Node(character="Leon S. Kennedy")
    chris_redfield = Node(character="Chris Redfield")
    jill_valentine = Node(character="Jill Valentine")
    ada_wong       = Node(character="Ada Wong")
    albert_wesker  = Node(character="Albert Wesker")

    # --- Honkai: Star Rail ---
    acheron        = Node(character="Acheron")
    kafka          = Node(character="Kafka")
    dan_heng       = Node(character="Dan Heng")
    march_7th      = Node(character="March 7th")
    jing_yuan      = Node(character="Jing Yuan")

    # --- Red Dead Redemption ---
    arthur_morgan  = Node(character="Arthur Morgan")
    john_marston   = Node(character="John Marston")
    dutch          = Node(character="Dutch van der Linde")
    sadie_adler    = Node(character="Sadie Adler")
    micah_bell     = Node(character="Micah Bell")

    # --- Uma Musume: Pretty Derby ---
    agnes_tachyon  = Node(character="Agnes Tachyon")
    special_week   = Node(character="Special Week")
    silence_suzuka = Node(character="Silence Suzuka")
    tokai_teio     = Node(character="Tokai Teio")
    gold_ship      = Node(character="Gold Ship")

    # --- Crash Bandicoot ---
    crash          = Node(character="Crash Bandicoot")
    coco           = Node(character="Coco Bandicoot")
    neo_cortex     = Node(character="Dr. Neo Cortex")
    aku_aku        = Node(character="Aku Aku")
    dingodile      = Node(character="Dingodile")

    # --- Devil May Cry ---
    vergil         = Node(character="Vergil")
    dante          = Node(character="Dante")
    nero           = Node(character="Nero")
    trish          = Node(character="Trish")
    lady           = Node(character="Lady")

    # --- Assassin's Creed ---
    ezio           = Node(character="Ezio Auditore")
    altair         = Node(character="Altaïr Ibn-La'Ahad")
    desmond        = Node(character="Desmond Miles")
    edward_kenway  = Node(character="Edward Kenway")
    connor_kenway  = Node(character="Connor Kenway")

    # --- NieR: Automata ---
    twob           = Node(character="2B")
    nines          = Node(character="9S")
    atwo           = Node(character="A2")
    pascal         = Node(character="Pascal")
    emil           = Node(character="Emil")

    # --- Tekken ---
    kazuya         = Node(character="Kazuya Mishima")
    jin_kazama     = Node(character="Jin Kazama")
    heihachi       = Node(character="Heihachi Mishima")
    nina_williams  = Node(character="Nina Williams")
    yoshimitsu     = Node(character="Yoshimitsu")

    # --- Tomb Raider ---
    lara_croft     = Node(character="Lara Croft")
    winston        = Node(character="Winston Smith")
    jonah          = Node(character="Jonah Maiava")
    natla          = Node(character="Jacqueline Natla")
    amanda         = Node(character="Amanda Evert")

    # --- Call of Duty (Modern Warfare) ---
    john_price     = Node(character="John Price")
    ghost          = Node(character="Ghost")
    soap           = Node(character="John \"Soap\" MacTavish")
    gaz            = Node(character="Kyle \"Gaz\" Garrick")
    makarov        = Node(character="Vladimir Makarov")

    # --- Mortal Kombat ---
    scorpion       = Node(character="Scorpion")
    sub_zero       = Node(character="Sub-Zero")
    liu_kang       = Node(character="Liu Kang")
    johnny_cage    = Node(character="Johnny Cage")
    baraka         = Node(character="Baraka")

    # --- God of War ---
    kratos         = Node(character="Kratos")
    atreus         = Node(character="Atreus")
    mimir          = Node(character="Mimir")
    freya          = Node(character="Freya")
    baldur         = Node(character="Baldur")

    # ─────────────────────────────────────────────
    # INTERNAL NODES — dari bawah ke atas
    # ─────────────────────────────────────────────

    # ── Cabang Mortal Kombat ──
    mk_warna = Node(question="Apakah kostum atau auranya identik dengan warna biru / es?")
    mk_warna.yes, mk_warna.no = sub_zero, scorpion

    mk_tarkatan = Node(question="Apakah dia memiliki gigi panjang menjijikkan / pisau dari tangannya (Tarkatan)?")
    mk_tarkatan.yes, mk_tarkatan.no = baraka, johnny_cage

    mk_biksu = Node(question="Apakah dia seorang petarung bergelar Earthrealm Champion dengan elemen api?")
    mk_biksu.yes, mk_biksu.no = liu_kang, mk_tarkatan

    mk_root = Node(question="Apakah dia seorang ninja atau memakai penutup wajah ala ninja?")
    mk_root.yes, mk_root.no = mk_warna, mk_biksu

    # ── Cabang Tekken ──
    tekken_devil = Node(question="Apakah dia bisa berubah menjadi Devil dan sangat membenci ayahnya (Heihachi)?")
    tekken_devil.yes, tekken_devil.no = kazuya, jin_kazama

    tekken_botak = Node(question="Apakah dia kakek tua ahli bela diri dengan potongan rambut botak di tengah?")
    tekken_botak.yes, tekken_botak.no = heihachi, tekken_devil

    tekken_pedang = Node(question="Apakah dia menggunakan pedang dan memakai armor canggih/robot/alien?")
    tekken_pedang.yes, tekken_pedang.no = yoshimitsu, tekken_botak

    tekken_root = Node(question="Apakah tokoh ini adalah seorang perempuan pembunuh bayaran?")
    tekken_root.yes, tekken_root.no = nina_williams, tekken_pedang

    # ── Cabang Resident Evil ──
    re_cewek2 = Node(question="Apakah dia identik dengan gaun merah dan bekerja sebagai agen rahasia?")
    re_cewek2.yes, re_cewek2.no = ada_wong, jill_valentine

    re_villain = Node(question="Apakah dia memakai kacamata hitam dan merupakan antagonis utama?")
    re_villain.yes, re_villain.no = albert_wesker, Node(question="Apakah rambutnya berponi belah tengah khas (Leon)?")
    re_villain.no.yes, re_villain.no.no = leon_kennedy, chris_redfield

    re_root = Node(question="Apakah tokoh ini adalah karakter perempuan?")
    re_root.yes, re_root.no = re_cewek2, re_villain

    # ── Cabang Call of Duty ──
    cod_mask = Node(question="Apakah dia selalu memakai topeng bermotif tengkorak?")
    cod_mask.yes, cod_mask.no = ghost, Node(question="Apakah dia dipanggil 'Soap' dan punya gaya rambut cepak/mohawk?")
    cod_mask.no.yes, cod_mask.no.no = soap, Node(question="Apakah dia kapten yang memakai topi boonie dan berkumis tebal?")
    cod_mask.no.no.yes, cod_mask.no.no.no = john_price, gaz

    cod_root = Node(question="Apakah dia merupakan pimpinan teroris asal Rusia (Antagonis)?")
    cod_root.yes, cod_root.no = makarov, cod_mask

    # ── Cabang Uma Musume ──
    uma_gila = Node(question="Apakah dia ilmuwan jenius/nyentrik yang sering membawa tabung reaksi?")
    uma_gila.yes, uma_gila.no = agnes_tachyon, Node(question="Apakah rambutnya putih/silver dan dijuluki pembuat onar (Gold Ship)?")
    uma_gila.no.yes, uma_gila.no.no = gold_ship, Node(question="Apakah dia karakter utama berambut coklat dengan sejumput rambut putih di dahi?")
    uma_gila.no.no.yes, uma_gila.no.no.no = special_week, Node(question="Apakah rambutnya dominan orange terang berponi?")
    uma_gila.no.no.no.yes, uma_gila.no.no.no.no = silence_suzuka, tokai_teio

    uma_root = uma_gila # Root langsung mengarah ke struktur ini

    # ── Cabang Honkai: Star Rail ──
    hsr_cowok = Node(question="Apakah dia laki-laki yang memimpin Luofu dan memiliki elemen Lightning (Petir)?")
    hsr_cowok.yes, hsr_cowok.no = jing_yuan, dan_heng

    hsr_cewek = Node(question="Apakah dia membawa pedang panjang dengan elemen kilat ungu gelap?")
    hsr_cewek.yes, hsr_cewek.no = acheron, Node(question="Apakah dia menggunakan senjata api ganda (Dual SMG) dan berjaket kulit?")
    hsr_cewek.no.yes, hsr_cewek.no.no = kafka, march_7th

    hsr_root = Node(question="Apakah tokoh ini adalah laki-laki?")
    hsr_root.yes, hsr_root.no = hsr_cowok, hsr_cewek

    # ── Cabang God of War ──
    gow_botak = Node(question="Apakah dia manusia / kepala terpenggal yang bijaksana?")
    gow_botak.yes, gow_botak.no = mimir, Node(question="Apakah dia dewa perang berkepala botak dengan tato merah tebal?")
    gow_botak.no.yes, gow_botak.no.no = kratos, Node(question="Apakah dia anak kecil/remaja laki-laki yang membawa busur panah?")
    gow_botak.no.no.yes, gow_botak.no.no.no = atreus, Node(question="Apakah dia Dewi perempuan yang menguasai sihir Vanir?")
    gow_botak.no.no.no.yes, gow_botak.no.no.no.no = freya, baldur

    gow_root = gow_botak

    # ── Cabang NieR: Automata ──
    nier_mesin2 = Node(question="Apakah dia berbentuk kepala tengkorak bulat yang sering menyeringai?")
    nier_mesin2.yes, nier_mesin2.no = emil, pascal

    nier_android = Node(question="Apakah dia android laki-laki yang memakai celana pendek (Scanner)?")
    nier_android.yes, nier_android.no = nines, Node(question="Apakah dia android perempuan berambut putih pendek yang memakai blindfold/penutup mata?")
    nier_android.no.yes, nier_android.no.no = twob, atwo

    nier_root = Node(question="Apakah wujud tubuhnya adalah mesin usang/aneh (bukan wujud menyerupai manusia)?")
    nier_root.yes, nier_root.no = nier_mesin2, nier_android

    # ── Cabang Devil May Cry ──
    dmc_cewek = Node(question="Apakah dia membawa senjata berat/bazooka besar bernama Kalina Ann?")
    dmc_cewek.yes, dmc_cewek.no = lady, trish

    dmc_cowok = Node(question="Apakah dia memakai mantel biru bersenjata katana (Yamato)?")
    dmc_cowok.yes, dmc_cowok.no = vergil, Node(question="Apakah dia memakai mantel merah bersenjata pedang besar (Rebellion)?")
    dmc_cowok.no.yes, dmc_cowok.no.no = dante, nero

    dmc_root = Node(question="Apakah tokoh ini adalah perempuan?")
    dmc_root.yes, dmc_root.no = dmc_cewek, dmc_cowok

    # ── Cabang Red Dead Redemption ──
    rdr_main = Node(question="Apakah dia perempuan pejuang (bounty hunter) berambut pirang?")
    rdr_main.yes, rdr_main.no = sadie_adler, Node(question="Apakah dia pemimpin geng yang licik dan selalu bilang 'I have a plan!'?")
    rdr_main.no.yes, rdr_main.no.no = dutch, Node(question="Apakah dia pengkhianat menyebalkan dan antagonis utama game kedua?")
    rdr_main.no.no.yes, rdr_main.no.no.no = micah_bell, Node(question="Apakah dia protagonis utama di game kedua yang terkena TBC?")
    rdr_main.no.no.no.yes, rdr_main.no.no.no.no = arthur_morgan, john_marston

    rdr_root = rdr_main

    # ── Cabang Assassin's Creed ──
    ac_modern = Node(question="Apakah dia hidup di era modern sebagai subjek tes mesin Animus?")
    ac_modern.yes, ac_modern.no = desmond, Node(question="Apakah dia seorang Kapten Bajak Laut dari Karibia?")
    ac_modern.no.yes, ac_modern.no.no = edward_kenway, Node(question="Apakah dia merupakan ras penduduk asli Amerika (Native American)?")
    ac_modern.no.no.yes, ac_modern.no.no.no = connor_kenway, Node(question="Apakah dia Assassin legendaris dari zaman Renaissance Italia?")
    ac_modern.no.no.no.yes, ac_modern.no.no.no.no = ezio, altair

    ac_root = ac_modern

    # ── Cabang Crash Bandicoot ──
    crash_human = Node(question="Apakah dia ilmuwan manusia jahat dengan huruf N besar di dahinya?")
    crash_human.yes, crash_human.no = neo_cortex, Node(question="Apakah wujudnya hanyalah sebuah topeng kayu terbang ajaib?")
    crash_human.no.yes, crash_human.no.no = aku_aku, Node(question="Apakah dia mutan perpaduan Dingo dan Buaya yang membawa penyembur api?")
    crash_human.no.no.yes, crash_human.no.no.no = dingodile, Node(question="Apakah dia bandicoot perempuan berambut pirang peliharaan laptop?")
    crash_human.no.no.no.yes, crash_human.no.no.no.no = coco, crash

    crash_root = crash_human

    # ── Cabang Tomb Raider ──
    tr_main = Node(question="Apakah dia protagonis utamanya (wanita penjelajah makam)?")
    tr_main.yes, tr_main.no = lara_croft, Node(question="Apakah dia antagonis abadi / penguasa ras dari Atlantis?")
    tr_main.no.yes, tr_main.no.no = natla, Node(question="Apakah dia teman masa lalu Lara yang kembali sebagai musuh memakai entitas mistis?")
    tr_main.no.no.yes, tr_main.no.no.no = amanda, Node(question="Apakah dia pelayan tua (butler) keluarga Croft yang sering dikurung di kulkas?")
    tr_main.no.no.no.yes, tr_main.no.no.no.no = winston, jonah

    tr_root = tr_main

    # ==========================================
    # 3. ROUTING UTAMA / ROOT NODE (LEVEL 1 & 2)
    # ==========================================

    # Pemisah History & Open World
    is_rdr = Node(question="Apakah gamenya memiliki tema Wild West / Koboi Amerika?")
    is_rdr.yes, is_rdr.no = rdr_root, ac_root

    # Pemisah Hack & Slash
    is_nier = Node(question="Apakah karakter/semesta di gamenya difokuskan pada Android dan Mesin buatan manusia?")
    is_nier.yes, is_nier.no = nier_root, dmc_root

    is_gow = Node(question="Apakah gamenya berlatar belakang mitologi Dewa-dewa kuno (Yunani / Nordik)?")
    is_gow.yes, is_gow.no = gow_root, is_nier

    # Pemisah Anime / Gacha
    is_uma = Node(question="Apakah inti dari game tersebut berfokus pada balapan gadis kuda idol?")
    is_uma.yes, is_uma.no = uma_root, hsr_root

    # Pemisah Shooter
    is_re = Node(question="Apakah game shooter ini bertema horor kelangsungan hidup (membasmi Zombie/Bio-weapon)?")
    is_re.yes, is_re.no = re_root, cod_root

    # Pemisah Fighting
    is_mk = Node(question="Apakah franchise gamenya sangat brutal, sadis, dan identik dengan 'Fatality'?")
    is_mk.yes, is_mk.no = mk_root, tekken_root

    # --- KATEGORI BESAR (ROUTING LEVEL 1) ---
    is_platformer = Node(question="Apakah karakternya merupakan hewan antropomorfik / platformer klasik dari era PS1?")
    is_platformer.yes, is_platformer.no = crash_root, tr_root # Jika bukan platformer di ujung ini, sisa Tomb Raider

    is_history = Node(question="Apakah game tersebut mengambil inspirasi kuat dari sejarah dunia (Zaman kuno / Koboi)?")
    is_history.yes, is_history.no = is_rdr, is_platformer

    is_hackslash = Node(question="Apakah karakter ini berasal dari game aksi 'Hack and Slash' yang menggunakan kombo jarak dekat?")
    is_hackslash.yes, is_hackslash.no = is_gow, is_history

    is_gacha = Node(question="Apakah karakter ini memiliki grafis ala Anime dan berasal dari game Gacha buatan Asia?")
    is_gacha.yes, is_gacha.no = is_uma, is_hackslash

    is_shooter = Node(question="Apakah karakter ini dominan bertarung menggunakan senjata api militer (Shooter FPS/TPS)?")
    is_shooter.yes, is_shooter.no = is_re, is_gacha

    root = Node(question="Apakah karakter ini berasal dari game pertarungan 1 lawan 1 (Fighting Game Arena)?")
    root.yes, root.no = is_mk, is_shooter

    # Build dan Return Tree
    tree = DecisionTree()
    tree.build(root)
    
    return tree # <--- Wajib dikembalikan agar tidak menghasilkan None Error

# Daftar karakter yang dapat dicari (diletakkan di luar fungsi)
CHARACTER_LIST = [
    # Resident Evil
    "Leon S. Kennedy",
    "Chris Redfield",
    "Jill Valentine",
    "Ada Wong",
    "Albert Wesker",

    # Honkai: Star Rail
    "Acheron",
    "Kafka",
    "Dan Heng",
    "March 7th",
    "Jing Yuan",

    # Red Dead Redemption
    "Arthur Morgan",
    "John Marston",
    "Dutch van der Linde",
    "Sadie Adler",
    "Micah Bell",

    # Uma Musume: Pretty Derby
    "Agnes Tachyon",
    "Special Week",
    "Silence Suzuka",
    "Tokai Teio",
    "Gold Ship",

    # Crash Bandicoot
    "Crash Bandicoot",
    "Coco Bandicoot",
    "Dr. Neo Cortex",
    "Aku Aku",
    "Dingodile",

    # Devil May Cry
    "Vergil",
    "Dante",
    "Nero",
    "Trish",
    "Lady",

    # Assassin's Creed
    "Ezio Auditore",
    "Altaïr Ibn-La'Ahad",
    "Desmond Miles",
    "Edward Kenway",
    "Connor Kenway",

    # NieR: Automata
    "2B",
    "9S",
    "A2",
    "Pascal",
    "Emil",

    # Tekken
    "Kazuya Mishima",
    "Jin Kazama",
    "Heihachi Mishima",
    "Nina Williams",
    "Yoshimitsu",

    # Tomb Raider
    "Lara Croft",
    "Winston Smith",
    "Jonah Maiava",
    "Jacqueline Natla",
    "Amanda Evert",

    # Call of Duty (Modern Warfare)
    "John Price",
    "Ghost",
    "John \"Soap\" MacTavish",
    "Kyle \"Gaz\" Garrick",
    "Vladimir Makarov",

    # Mortal Kombat
    "Scorpion",
    "Sub-Zero",
    "Liu Kang",
    "Johnny Cage",
    "Baraka",

    # God of War
    "Kratos",
    "Atreus",
    "Mimir",
    "Freya",
    "Baldur"
]