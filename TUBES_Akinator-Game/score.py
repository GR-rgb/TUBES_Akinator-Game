# score.py
# Manajemen user dan top score (fitur opsional)
# Data disimpan di file data/scores.txt


import os # Opsional - hanya untuk memastikan folder data/ ada

SCORES_FILE = os.path.join(os.path.dirname(__file__), 'data', 'scores.txt')


def _ensure_data_dir():
    """Pastikan folder data/ ada."""
    os.makedirs(os.path.dirname(SCORES_FILE), exist_ok=True)


def load_scores():
    """
    Baca semua skor dari file.

    Returns:
        list of dict: [{'username': str, 'score': int}, ...]
    """
    _ensure_data_dir()
    scores = []

    if not os.path.exists(SCORES_FILE):
        return scores

    with open(SCORES_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) == 2:
                try:
                    scores.append({
                        'username': parts[0].strip(),
                        'score': int(parts[1].strip())
                    })
                except ValueError:
                    continue  # Lewati baris yang tidak valid

    return scores


def save_score(username, score):
    """
    Simpan skor baru ke file. Jika username sudah ada,
    update hanya jika skor baru lebih tinggi.

    Args:
        username (str): Nama user
        score    (int): Skor yang didapat
    """
    _ensure_data_dir()
    scores = load_scores()

    # Cek apakah username sudah ada (linear search)
    found = False
    for entry in scores:
        if entry['username'].lower() == username.lower():
            if score > entry['score']:
                entry['score'] = score  # Update jika lebih tinggi
            found = True
            break

    if not found:
        scores.append({'username': username, 'score': score})

    # Tulis ulang file
    with open(SCORES_FILE, 'w', encoding='utf-8') as f:
        for entry in scores:
            f.write(f"{entry['username']},{entry['score']}\n")


def get_top_scores(limit=5):
    """
    Ambil top N skor, diurutkan dari tertinggi.

    Args:
        limit (int): Jumlah entri yang ditampilkan

    Returns:
        list of dict: Top skor
    """
    scores = load_scores()
    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)
    return sorted_scores[:limit]


def display_top_scores():
    """Tampilkan top 5 skor di terminal."""
    top = get_top_scores(5)

    print()
    print("  ─────────────────────────────────")
    print("  🏆   TOP 5 PEMAIN TERBAIK")
    print("  ─────────────────────────────────")

    if not top:
        print("  Belum ada skor. Jadilah yang pertama!")
    else:
        medals = ['🥇', '🥈', '🥉', '4️⃣ ', '5️⃣ ']
        for i, entry in enumerate(top):
            medal = medals[i] if i < len(medals) else f"  {i+1}."
            name  = entry['username'][:20].ljust(20)
            score = str(entry['score']).rjust(5)
            print(f"  {medal}  {name}  {score} poin")

    print("  ─────────────────────────────────")
    print()