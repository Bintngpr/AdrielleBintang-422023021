from mahasiswa import Mahasiswa
from dosen import Dosen
from mata_kuliah import MataKuliah
from kelas import Kelas
from sistem_informasi import SistemInformasi

# Inisialisasi objek Sistem Informasi
sistem = SistemInformasi()

# Tambahkan beberapa objek Mahasiswa
mahasiswa1 = Mahasiswa("Bintang", "422023021", "bintang@ukrida.com")
mahasiswa2 = Mahasiswa("Yobel", "422023001", "yobel@ukrida.com")
sistem.tambahkan_mahasiswa(mahasiswa1)
sistem.tambahkan_mahasiswa(mahasiswa2)

# Tambahkan beberapa objek Dosen
dosen1 = Dosen("Pak. Hendrik", "40231023", "Hendrik@ukrida.com")
dosen2 = Dosen("Pak. Tubagus", "30918231", "Tubagus@ukrida.com")
sistem.tambahkan_dosen(dosen1)
sistem.tambahkan_dosen(dosen2)

# Tambahkan beberapa objek Mata Kuliah
mata_kuliah1 = MataKuliah("MK101", "Pemrograman Python", 3)
mata_kuliah2 = MataKuliah("MK102", "Analisis Sistem Informasi", 3)
sistem.tambahkan_mata_kuliah(mata_kuliah1)
sistem.tambahkan_mata_kuliah(mata_kuliah2)

# Buat objek Kelas dan tambahkan mahasiswa ke dalamnya
kelas1 = Kelas("KelasA", mata_kuliah1, dosen1)
kelas2 = Kelas("KelasB", mata_kuliah2, dosen2)
kelas1.tambahkan_mahasiswa(mahasiswa1)
kelas2.tambahkan_mahasiswa(mahasiswa2)
sistem.tambahkan_kelas(kelas1)
sistem.tambahkan_kelas(kelas2)

# Contoh penggunaan fungsionalitas
print("Daftar Mahasiswa:")
for mahasiswa in sistem.daftar_mahasiswa:
    print(mahasiswa.nama)

print("\nDaftar Dosen:")
for dosen in sistem.daftar_dosen:
    print(dosen.nama)

print("\nDaftar Kelas:")
for kelas in sistem.daftar_kelas:
    print(kelas.kode)

print("\nDaftar Mata Kuliah:")
for mata_kuliah in sistem.daftar_mata_kuliah:
    print(mata_kuliah.nama)
