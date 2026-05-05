# tree.py
# Implementasi Binary Decision Tree untuk Akinator
# Struktur data utama sesuai spesifikasi tugas besar


class Node:
    """
    Satu node dalam Binary Decision Tree.
    - Jika node internal: berisi pertanyaan, punya anak yes dan no
    - Jika leaf node: berisi nama karakter (jawaban akhir)
    """
    def __init__(self, question=None, character=None):
        self.question  = question   # Pertanyaan (untuk node internal)
        self.character = character  # Nama karakter (untuk leaf node)
        self.yes       = None       # Anak kiri  -> jawaban "Ya"
        self.no        = None       # Anak kanan -> jawaban "Tidak"

    def is_leaf(self):
        """Return True jika node ini adalah leaf (karakter akhir)."""
        return self.character is not None


class DecisionTree:
    """
    Binary Decision Tree untuk permainan Akinator.
    Menggunakan recursive traversal untuk menelusuri tree.
    """
    def __init__(self):
        self.root = None

    def build(self, root_node):
        """Set root node dari tree."""
        self.root = root_node

    def traverse(self, node, get_answer_func, on_guess_func):
        """
        Rekursif: telusuri tree berdasarkan jawaban user.

        Args:
            node            : Node saat ini
            get_answer_func : Fungsi untuk mendapat input Ya/Tidak dari user
            on_guess_func   : Fungsi dipanggil saat sampai di leaf (tebakan)

        Returns:
            str: nama karakter yang ditebak
        """
        # Base case: sampai di leaf node -> tebak karakter
        if node.is_leaf():
            return on_guess_func(node.character)

        # Tampilkan pertanyaan dan ambil jawaban
        answer = get_answer_func(node.question)

        # Rekursif ke cabang yang sesuai
        if answer:
            return self.traverse(node.yes, get_answer_func, on_guess_func)
        else:
            return self.traverse(node.no, get_answer_func, on_guess_func)

    def start_game(self, get_answer_func, on_guess_func):
        """Mulai traversal dari root."""
        if self.root is None:
            raise ValueError("Tree belum dibangun! Panggil build() terlebih dahulu.")
        return self.traverse(self.root, get_answer_func, on_guess_func)