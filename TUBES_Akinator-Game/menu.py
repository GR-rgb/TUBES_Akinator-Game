# menu.py
# Tampilan menu utama Akinator di terminal
# Navigasi: Start, Lihat Skor, Tentang, Exit


import os # Opsional - hanya untuk clear_screen() di terminal
import time # Opsional - hanya untuk delay di halaman about
from score import display_top_scores
from characters import CHARACTERS_BY_GAME # Untuk menampilkan daftar karakter setiap game di halaman about

BANNER = r"""
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
✨                                                                              ✨
✨        █████╗ ██╗  ██╗██╗███╗   ██╗ █████╗ ████████╗ ██████╗ ██████╗         ✨
✨       ██╔══██╗██║ ██╔╝██║████╗  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗        ✨
✨       ███████║█████╔╝ ██║██╔██╗ ██║███████║   ██║   ██║   ██║██████╔╝        ✨
✨       ██╔══██║██╔═██╗ ██║██║╚██╗██║██╔══██║   ██║   ██║   ██║██╔══██╗        ✨
✨       ██║  ██║██║  ██╗██║██║ ╚████║██║  ██║   ██║   ╚██████╔╝██║  ██║        ✨
✨       ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝        ✨
✨                                                                              ✨
✨------------------------------------------------------------------------------✨
✨                                                                              ✨
✨                    🧞 AKU BISA MEMBACA PIKIRANMU 🧞                          ✨
✨                                                                              ✨
✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨
"""


def clear_screen():
    """Bersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_separator(char='─', length=52):
    print("  " + char * length)


def show_main_menu(username=None):
    """ Menampilkan menu utama dan mengembalikan pilihan dari user."""

    clear_screen()
    print(BANNER)

    if username:
        print(f"  👤  Halo, {username}!")
        print()

    print_separator()
    print()
    print("  [ 1 ] ▶  Mulai Bermain")
    print("  [ 2 ] 🏆  Lihat Top Skor")
    print("  [ 3 ] ℹ️   Tentang Game")
    if username:
        print("  [ 4 ]  🔄  Ganti User")
    print("  [ 0 ] ✖  Keluar")
    print()
    print_separator()
    print()

    options = {'1': 'start', '2': 'scores', '3': 'about', '0': 'exit'}
    if username:
        options['4'] = 'change_user'

    while True:
        choice = input("  Pilih menu [0-{}]: ".format('4' if username else '3')).strip()
        if choice in options:
            return options[choice]
        print("  ⚠️  Pilihan tidak valid. Coba lagi.")


def ask_username():
    """Minta nama user di awal program (opsional)."""

    clear_screen()
    print(BANNER)
    print("  ─────────────────────────────────────────")
    print("  Masukkan namamu untuk menyimpan skor,")
    print("  atau tekan Enter untuk main tanpa akun.")
    print("  ─────────────────────────────────────────")
    print()

    name = input("  Nama kamu: ").strip()
    if not name:
        return None

    # Validasi nama (hanya huruf, angka, spasi)
    if not name.replace(" ", "").isalnum():
        print("  ⚠️  Nama tidak valid. Main tanpa akun.")
        time.sleep(1.2)
        return None

    return name[:20]  # Batasi 20 karakter


def show_about():
    """Tampilkan halaman 'Tentang Game'."""
    clear_screen()
    print()
    print("  ══════════════════════════════════════")
    print("  ℹ️   TENTANG AKINATOR")
    print("  ══════════════════════════════════════")
    print()
    print("  Game tebak-tebakan karakter menggunakan")
    print("  Binary Decision Tree.")
    print()
    print("  Cara bermain:")
    print("  1. Pikirkan satu tokoh")
    print("  2. Jawab pertanyaan dengan Ya / Tidak")
    print("  3. Akinator akan menebak tokohmu!")
    print()
    print("  ──────────────────────────────────────")
    print("  Karakter yang tersedia: 65 tokoh")
    print("  Anime, fiksi, pahlawan, sains, & lainnya")
    print("  Game dan karakter yang tersedia :")
    print()

    for game,characters in CHARACTERS_BY_GAME.items():
        print(f" 🎮 {game}")
        print(f"  {game}: {', '.join(characters)}")
        print()

    print("  ──────────────────────────────────────")
    print("  Struktur data : Binary Decision Tree")
    print("  Algoritma     : Recursive Tree Traversal")
    print("  Bahasa        : Python 3.12.12")
    print()
    print("  ──────────────────────────────────────")
    print("  Tugas Besar SG Basic 2026")
    print("  Computing Laboratory GEN 10.0")
    print("  Universitas Telkom")
    print("  ══════════════════════════════════════")
    print()
    input("  Tekan Enter untuk kembali ke menu...")


def show_scores_page():
    """Tampilkan halaman top skor."""
    clear_screen()
    print()
    display_top_scores()
    input("  Tekan Enter untuk kembali ke menu...")


def run_menu():
    """
    Jalankan loop menu utama.
    Ini adalah fungsi yang dipanggil dari main.py.
    """
    from game import start_game

    # Tanya username di awal
    username = ask_username()

    # Loop menu
    while True:
        choice = show_main_menu(username)

        if choice == 'start':
            start_game(username)

        elif choice == 'scores':
            show_scores_page()

        elif choice == 'about':
            show_about()

        elif choice == 'change_user':
            username = ask_username()

        elif choice == 'exit':
            clear_screen()
            print()
            print("  Sampai jumpa! 👋")
            print()
            break
