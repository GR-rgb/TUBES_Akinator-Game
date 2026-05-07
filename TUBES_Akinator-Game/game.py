# game.py
# Game loop utama Akinator
# Mengurus sesi tanya-jawab, input user, dan hasil tebakan


import os # Opsional - hanya untuk clear_screen() di terminal
import time # Opsional - hanya untuk animasi berpikir dan delay di akhir
from characters import build_character_tree # Fungsi untuk membangun tree karakter
from score import load_scores, save_score  # Opsional - hapus jika tidak pakai score.py


def clear_screen(): 
    """Bersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_separator(char='─', length=50):
    """Cetak garis pemisah."""
    print(char * length)


def get_yes_no(question):
    """
    Tampilkan pertanyaan dan minta input Ya/Tidak dari user.

    Args:
        question (str): Pertanyaan yang ditampilkan

    Returns:
        bool: True jika Ya, False jika Tidak
    """
    print()
    print(f"  🤔  {question}")
    print()

    while True:
        print("       [1] Ya       [2] Tidak")
        answer = input("  >>> ").strip()

        if answer in ('1','y'):
            return True
        elif answer in ('2','n'):
            return False
        else:
            print("  ⚠️  Input tidak valid. Masukkan 1 (Ya) atau 2 (Tidak).")


def show_thinking_animation(duration=1.5):
    """Animasi 'Akinator sedang berpikir...'"""
    frames = ["🔮 Membaca pikiranmu .  ", "🔮 Membaca pikiranmu .. ", "🔮 Membaca pikiranmu ..."]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        print(f"\r  {frames[i % len(frames)]}", end='', flush=True)
        time.sleep(0.3)
        i += 1
    print("\r" + " " * 40 + "\r", end='')


def on_guess(character):
    """
    Dipanggil saat traversal tree mencapai leaf node.
    Menampilkan tebakan dan meminta konfirmasi.

    Args:
        character (str): Nama karakter yang ditebak

    Returns:
        tuple: (nama_karakter, benar/salah)
    """
    print()
    print_separator('═')
    show_thinking_animation()
    print()
    print("  🧞 AKU TAHU SIAPA YANG KAMU PIKIRKAN!")
    print()
    print(f"  ✨  Apakah itu...  » {character} «  ?!")
    print()
    print_separator('═')
    print()

    while True:
        print("  Apakah tebakanku benar?")
        print("  [1] Ya, benar!    [2] Tidak, salah")
        answer = input("  >>> ").strip()

        if answer in ('1','y'):
            return (character, True)
        elif answer in ('2','n'):
            return (character, False)
        else:
            print("  ⚠️  Input tidak valid.")


def show_question_counter(count):
    """Tampilkan nomor pertanyaan saat ini."""
    print(f"\n  [ Pertanyaan ke-{count} ]")


# Counter pertanyaan (dikelola sebagai list agar bisa dimodifikasi dari dalam closure)
_question_count = [0]


def get_answer_with_counter(question):
    """Wrapper get_yes_no yang menghitung pertanyaan."""
    _question_count[0] += 1
    show_question_counter(_question_count[0])
    return get_yes_no(question)


def play_round(username=None):
    """
    Jalankan satu ronde permainan.

    Args:
        username (str|None): Nama user jika fitur skor aktif

    Returns:
        bool: True jika user ingin main lagi
    """
    clear_screen()

    # Header ronde
    print()
    print_separator('═')
    print("  🧞  AKINATOR — Aku bisa membaca pikiranmu!")
    print_separator('═')
    print()
    print("  Pikirkan satu tokoh — bisa siapa saja:")
    print("  karakter anime, film, pahlawan, artis, atlet...")
    print("  Jangan bilang siapapun! Aku yang akan menebaknya.")
    print()
    input("  Tekan Enter jika sudah siap...")

    # Reset counter
    _question_count[0] = 0

    # Bangun tree dan mulai game
    tree = build_character_tree()

    result = tree.start_game(
        get_answer_func=get_answer_with_counter,
        on_guess_func=on_guess
    )

    character, is_correct = result

    # Hasil akhir
    print()
    print_separator('═')
    if is_correct:
        print(f"  🎉 YEAY! Aku berhasil menebak dalam {_question_count[0]} pertanyaan!")
        print(f"  ✅  Tokohnya adalah: {character}")

        # Simpan skor jika ada username
        if username:
            score = max(0, 100 - (_question_count[0] * 5))
            save_score(username, score)
            print(f"  ⭐  Skormu: {score} poin")
    else:
        print(f"  😅 Kamu mengalahkanku! Aku tidak bisa menebaknya.")
        print(f"  💭 Siapa tokoh yang kamu pikirkan?")
        nama = input("  >>> ").strip()
        if nama:
            print(f"  📝 Aku akan mengingat '{nama}' untuk lain kali!")
    print_separator('═')

    # Tanya main lagi
    print()
    while True:
        print("  Mau main lagi?  [1] Ya    [2] Tidak")
        again = input("  >>> ").strip()
        if again in ('1'):
            return True
        elif again in ('2','n'):
            return False
        else:
            print("  ⚠️  Input tidak valid.")


def start_game(username=None):
    """
    Entry point game — jalankan loop bermain.

    Args:
        username (str|None): Nama user dari menu
    """
    playing = True
    while playing:
        playing = play_round(username)

    clear_screen()
    print()
    print("  Terima kasih sudah bermain! Sampai jumpa 🧞")
    print()
    time.sleep(1.5)