# 🧞 Akinator Game
> Tugas Besar SG Basic 2026 — Computing Laboratory GEN 10.0
> Kelompok 2
> Universitas Telkom

---

## 📖 Deskripsi

Program ini adalah implementasi game **Akinator** berbasis terminal yang menebak karakter yang dipikirkan user melalui serangkaian pertanyaan Ya/Tidak. Game ini menggunakan **Binary Decision Tree** sebagai struktur data utama dengan **Recursive Tree Traversal** sebagai logika mesin penebaknya.

---

## 👥 Anggota Kelompok

|           Nama           |     NIM      |
|--------------------------|--------------|
| Ezzar Kaysan Gumilar     | 103012500139 |
| Fadhlan Anargya Agustian | 103012400006 |
| Fakhri Nur Ramdhani      | 103012400214 |
| Fatih Akram Wicaksono    | 103012500318 |
| Ghifar Anshari Rabbani   | 103012400003 |

---

## 🎮 Cara Bermain

1. Jalankan program dan pilih **Start** dari menu utama
2. **Pikirkan** satu tokoh (jangan diucapkan!)
3. Jawab setiap pertanyaan dari Akinator dengan:
   - `1` atau `y` → **Ya**
   - `2` atau `n` → **Tidak**
4. Akinator akan menebak karakter yang kamu pikirkan
5. Konfirmasi apakah tebakan benar atau salah

---

## 🌳 Implementasi Binary Decision Tree

Program ini menggunakan **Binary Decision Tree** sebagai struktur data utama.

### Struktur Node
Setiap node dalam tree memiliki:
- `question` — pertanyaan yang ditampilkan ke user (node internal)
- `character` — nama karakter jika node ini adalah daun (leaf node)
- `yes` — pointer/referensi ke anak kiri (jawaban Ya)
- `no` — pointer/referensi ke anak kanan (jawaban Tidak)

### Recursive Tree Traversal
Logika penebakan menggunakan fungsi **rekursif** yang menelusuri tree berdasarkan input user:

```
traverse(node):
    if node adalah leaf:
        tebak karakter node
    else:
        tampilkan node.question
        if input == "ya":
            traverse(node.yes)   ← rekursif ke kiri
        else:
            traverse(node.no)    ← rekursif ke kanan
```

---

## 🎭 Daftar Karakter (20+)

Program ini dapat menebak karakter-karakter berikut:

**Karakter Game**
| Franchise               | Karakter                                                                       |
| :---                    | :---                                                                           |
| **Resident Evil**       | Leon S. Kennedy, Chris Redfield, Jill Valentine, Ada Wong, Albert Wesker       |
| **Honkai: Star Rail**   | Acheron, Kafka, Dan Heng, March 7th, Jing Yuan                                 |
| **Red Dead Redemption** | Arthur Morgan, John Marston, Dutch van der Linde, Sadie Adler, Micah Bell      |
| **Umamusume**           | Agnes Tachyon, Special Week, Silence Suzuka, Tokai Teio, Gold Ship             |
| **Crash Bandicoot**     | Crash Bandicoot, Coco Bandicoot, Dr. Neo Cortex, Aku Aku, Dingodile            |
| **Devil May Cry**       | Vergil, Dante, Nero, Trish, Lady                                               |
| **Assassin's Creed**    | Ezio Auditore, Altaïr Ibn-La'Ahad, Desmond Miles, Edward Kenway, Connor Kenway |
| **NieR: Automata**      | 2B, 9S, A2, Pascal, Emil                                                       |
| **Tekken**              | Kazuya Mishima, Jin Kazama, Heihachi Mishima, Nina Williams, Yoshimitsu        |
| **Tomb Raider**         | Lara Croft, Winston Smith, Jonah Maiava, Jacqueline Natla, Amanda Evert        |
| **Call of Duty**        | John Price, Ghost, John "Soap" MacTavish, Kyle "Gaz" Garrick, Vladimir Makarov |
| **Mortal Kombat**       | Scorpion, Sub-Zero, Liu Kang, Johnny Cage, Baraka                              |
| **God of War**          | Kratos, Atreus, Mimir, Freya, Baldur                                           |


* Total: **65 karakter** yang dapat ditebak melalui jalur Ya/Tidak di dalam tree dan dapat bertambah selama masa pengembangan
---

## 🧪 Contoh Alur Pertanyaan

```
Akinator: Apakah tokoh yang kamu pikirkan adalah karakter fiksi?
User: Ya

Akinator: Apakah tokoh tersebut berasal dari sebuah game?
User: Ya

Akinator: Apakah tokoh tersebut memiliki senjata khas berupa rantai?
User: Ya

Akinator: Apakah tokoh tersebut sering disebut sebagai "God of War"?
User: Ya

Akinator: Apakah itu... KRATOS?!
User: Ya

Akinator: Yatta Aku Berhasil Menebaknya >w<
```

---

## ✅ Fitur yang Diimplementasi

- [x] Tampilan berjalan di terminal
- [x] Menu utama (judul, Start, Exit)
- [x] Binary Decision Tree sebagai struktur data utama
- [x] Recursive Tree Traversal untuk logika penebakan
- [x] Minimal 20 karakter sebagai leaf node
- [x] Input validasi (Ya/Tidak)
- [x] Tampilan hasil tebakan
- [x] Sistem user & top score *(opsional)*

---

## 📝 Catatan Pengembangan

Program ini dikembangkan sebagai tugas akhir **SG Basic 2026** di Computing Laboratory GEN 10.0, Universitas Telkom. 
---
