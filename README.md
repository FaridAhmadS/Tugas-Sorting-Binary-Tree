
# Tugas Struktur Data
## Advanced Sorting & Binary Tree

### Identitas Mahasiswa
- Nama: Farid Ahmad Santoso
- NIM: 25091397050
- Kelas: 2025B
- Mata Kuliah: Struktur Data

---

# Deskripsi Program

Project ini berisi implementasi beberapa algoritma penting pada mata kuliah Struktur Data, yaitu:

1. Merge Sort menggunakan virtual sublists dan single temporary array.
2. Merge Sort pada Singly Linked List menggunakan fast-slow pointer.
3. Quick Sort dengan strategi Median-of-Three Pivot.
4. Expression Tree Builder & Evaluator.
5. In-Place Heap Construction.
6. In-Place Heap Sort.
7. Complete Binary Tree Validator.

---

# Fitur Utama

## 1. Array Merge Sort
- Menggunakan satu `tmp_array`
- Tidak menggunakan slicing
- Stabil
- Kompleksitas:
  - Time: O(n log n)
  - Space: O(n)

## 2. Linked List Merge Sort
- Menggunakan fast-slow pointer
- Tidak membuat node baru
- Stabil
- Kompleksitas:
  - Time: O(n log n)
  - Space: O(log n)

## 3. Quick Sort
- Median-of-three pivot
- Mengurangi worst-case
- Fallback ke Merge Sort jika depth terlalu dalam

## 4. Expression Tree
- Parsing ekspresi fully-parenthesized
- Evaluasi operasi:
  - +
  - -
  - *
  - /

## 5. Heap Sort
- In-place
- Tidak menggunakan heapq
- Kompleksitas:
  - Time: O(n log n)
  - Space: O(1)

---

# Cara Menjalankan

```bash
python main.py
```

---

# Contoh Output

```text
Merge Sort: [1, 3, 4, 7, 8, 9]
Quick Sort: [1, 3, 4, 7, 8, 9]
Linked List Sorted: 1 2 4 7
Expression Result: 43.0
Heap Sort: [1, 9, 12, 18, 25, 33, 40]
```

---

# Analisis Singkat

## Mengapa Merge Sort cocok untuk Linked List?
Karena proses merge hanya membutuhkan manipulasi pointer `.next` tanpa perpindahan data fisik.

## Mengapa Quick Sort bisa O(n²)?
Jika pivot selalu menjadi elemen terkecil/terbesar, partisi menjadi tidak seimbang sehingga kedalaman rekursi mencapai O(n).

## Mengapa Radix Sort tidak melanggar lower bound comparison sort?
Karena Radix Sort bukan comparison sort. Algoritma ini memanfaatkan distribusi digit sehingga tidak bergantung pada decision tree comparison.

---

# Struktur File

```text
main.py
README.md
```

---



