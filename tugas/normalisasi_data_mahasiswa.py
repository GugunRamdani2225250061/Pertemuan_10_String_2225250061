
# Tugas 4: Normalisasi Data Mahasiswa

def normalisasi_nama(nama):
    nama = nama.strip()
    nama = " ".join(nama.split())
    return nama.title()


def buat_inisial(nama):
    kata = normalisasi_nama(nama).split()
    return "".join(k[0] for k in kata)


def normalisasi_kode(kode):
    kata = kode.strip().upper().split()
    return "-".join(kata)


# Input data mahasiswa
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Pengolahan data
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama)

# Menampilkan hasil
print("\nHasil Normalisasi")
print(f"Nama bersih : {nama_bersih}")
print(f"Kode kelas  : {kode_bersih}")
print(f"Jumlah kata : {jumlah_kata}")
print(f"Inisial     : {inisial}")