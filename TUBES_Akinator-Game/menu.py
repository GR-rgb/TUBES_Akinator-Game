# menu.py
# Tampilan menu utama Akinator di terminal
# Navigasi: Start, Lihat Skor, Tentang, Exit


import os
import time
from score import display_top_scores

BANNER = r"""
  ╔══════════════════════════════════════════════════╗
  ║                                                  ║
  ║    ___   _  _____ _   _   _ _____ ___  ____     ║
  ║   / _ \ | |/ /_ _| \ | | / \_   _/ _ \|  _ \   ║
  ║  | | | || ' / | ||  \| |/ _ \| || | | | |_) |  ║
  ║  | |_| || . \ | || |\  / ___ \ | || |_| |  _ <  ║
  ║   \__\_\|_|\_\___|_| \_/_/   \_\_| \___/|_| \_\ ║
  ║                                                  ║
  ║         Aku bisa membaca pikiranmu! 🔮           ║
  ║                                                  ║
  ╚══════════════════════════════════════════════════╝
"""


def clear_screen():
    """Bersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_separator(char='─', length=52):
    print("  " + char * length)


def show_main_menu(username=None):
    """
    Tampilkan menu utama dan kembalikan pilihan user.

    Args:
        username (str|None): Nama user yang sedang login

    Returns:
        str: Pilihan menu ('start', 'scores', 'about', 'exit',
             'change_user')
    """
    clear_screen()
    print(BANNER)

    if username:
        print(f"  👤  Halo, {username}!")
        print()

    print_separator()
    print()
    print("  [ 1 ]  ▶  Mulai Bermain")
    print("  [ 2 ]  🏆  Lihat Top Skor")
    print("  [ 3 ]  ℹ️   Tentang Game")
    if username:
        print("  [ 4 ]  🔄  Ganti User")
    print("  [ 0 ]  ✖  Keluar")
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
    """
    Minta nama user di awal program (opsional).

    Returns:
        str|None: Nama user, atau None jika dilewati
    """
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
    clean = ''.join(c for c in name if c.isalnum() or c == ' ').strip()
    if not clean:
        print("  ⚠️  Nama tidak valid. Main tanpa akun.")
        time.sleep(1.5)
        return None

    return clean[:20]  # Batasi 20 karakter


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
    print()
    print("  Struktur data : Binary Decision Tree")
    print("  Algoritma     : Recursive Tree Traversal")
    print("  Bahasa        : Python 3")
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