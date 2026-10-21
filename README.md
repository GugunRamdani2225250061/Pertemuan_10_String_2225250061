### Pertemuan 10 - String dan Pengolahan Teks

- Nama: Gugun Ramdani
- NIM: 2225250061
- Kelas: 3A
- Mata Kuliah: Algoritma dan Pemrograman
- Program Studi: S1 Pendidikan Matematika FKIP Untirta

## 1. Tujuan
Mempelajari penggunaan string dalam Python, meliputi indeks,
slicing, method string, pembersihan teks, split, join,
pencarian kata, dan penerapan fungsi untuk normalisasi
data mahasiswa.

## 2. Struktur Proyek
- `latihan/01_dasar_string.py`
- `latihan/02_indeks_slicing.py`
- `latihan/03_method_string.py`
- `latihan/04_bersihkan_teks.py`
- `latihan/05_split_join.py`
- `latihan/06_pencarian_kata.py`
- `tugas/normalisasi_data_mahasiswa.py`
- `.gitignore`
- `README.md`
- `kuis formatif_pertemuan 10`

## 3. Cara Menjalankan
Pastikan Python 3 sudah terpasang.

Jalankan setiap latihan dengan perintah:
```bash
python latihan/01_dasar_string.py
python latihan/02_indeks_slicing.py
python latihan/03_method_string.py
python latihan/04_bersihkan_teks.py
python latihan/05_split_join.py
python latihan/06_pencarian_kata.py
```

Jalankan tugas utama dengan perintah:
```bash
python tugas/normalisasi_data_mahasiswa.py
```

## 4. Algoritma Tugas 4
1. Membaca nama lengkap dan kode kelas.
2. Membersihkan spasi nama menggunakan strip, split, dan join.
3. Mengubah nama menjadi title case.
4. Memecah nama menjadi kata-kata.
5. Menghitung jumlah kata dan membentuk inisial.
6. Mengubah kode kelas menjadi huruf kapital.
7. Menggabungkan bagian kode kelas menggunakan tanda hubung.
8. Menampilkan seluruh hasil normalisasi.

## 5. Hasil Pengujian

| No. | Input Nama | Input Kode | Nama Bersih | Kode Bersih | Jumlah Kata | Inisial | Status |
|---|---|---|---|---|---:|---|---|
| 1 | aan hendrayana | pmat a 2026 | Aan Hendrayana | PMAT-A-2026 | 2 | AH | Sesuai |
| 2 | fATHIYYAH mUTHMAINNAH | kelas b | Fathiyyah Muthmainnah | KELAS-B | 2 | FM | Sesuai |
| 3 | BUDI | pmtk 01 | Budi | PMTK-01 | 1 | B | Sesuai |
| 4 | siti nur aisyah | kelas c | Siti Nur Aisyah | KELAS-C | 3 | SNA | Sesuai |

Catatan: status akhir ditetapkan setelah seluruh pengujian
dijalankan di VS Code.

## 6. Refleksi
Kesulitan yang ditemukan adalah menangani spasi berlebih
dan kapitalisasi nama yang tidak konsisten. Masalah tersebut
diatasi dengan strip(), split(), join(), dan title().

Saya juga mempelajari bahwa string bersifat immutable,
sehingga hasil method string perlu disimpan kembali
ke variabel jika ingin digunakan pada proses berikutnya.
