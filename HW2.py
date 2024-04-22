from mahasiswa import Mahasiswa
from dosen import Dosen
from mata_kuliah import MataKuliah
from kelas import Kelas
from sistem_informasi import SistemInformasi
from staf_administrasi import StafAdministrasi
from lowongan import Lowongan
from pusat_karir import PusatKarir
from authenticator import Authenticator

sistem = SistemInformasi()
authenticator = Authenticator()

authenticator.add_user("user1", "password1")
authenticator.add_user("user2", "password2")

username = input("Masukkan username: ")
password = input("Masukkan password: ")

mahasiswa1 = Mahasiswa("Adrielle Bintang Pratama", "422023021", "bintang@ukrida.com")
mahasiswa2 = Mahasiswa("Yobel Kimtoputra", "422023001", "yobel@ukrida.com")
sistem.tambahkan_mahasiswa(mahasiswa1)
sistem.tambahkan_mahasiswa(mahasiswa2)

dosen1 = Dosen("Pak. Hendrik Tampubolon S.TI., M.Sc., Ph.D.", "40231023", "Hendrik@ukrida.com")
dosen2 = Dosen("Pak. Tubagus Ahmad Marzuqi S.Kom, MTI.", "30918231", "Tubagus@ukrida.com")
sistem.tambahkan_dosen(dosen1)
sistem.tambahkan_dosen(dosen2)

staf_admin = StafAdministrasi("Admisi Ukrida", "Admin", "Haryanto@ukrida.com")
staf_admin.perbarui_informasi_mahasiswa(mahasiswa1, "Adrielle Bintang Pratama", "422023021", "john@example.com")

mata_kuliah1 = MataKuliah("MK101", "Pemrograman Python", 3)
mata_kuliah2 = MataKuliah("MK102", "Analisis Sistem Informasi", 3)
sistem.tambahkan_mata_kuliah(mata_kuliah1)
sistem.tambahkan_mata_kuliah(mata_kuliah2)

kelas1 = Kelas("MK101", mata_kuliah1, dosen1)
kelas2 = Kelas("MK102", mata_kuliah2, dosen2)
kelas1.tambahkan_mahasiswa(mahasiswa1)
kelas2.tambahkan_mahasiswa(mahasiswa2)
sistem.tambahkan_kelas(kelas1)
sistem.tambahkan_kelas(kelas2)

pusat_karir = PusatKarir()

mahasiswa1 = Mahasiswa("Elbert.K", "42202204", "Elbert@ukrida.com")
mahasiswa2 = Mahasiswa("Beatrice", "42202209", "Beatrice@Ukrida.com")
pusat_karir.daftar_mahasiswa(mahasiswa1)
pusat_karir.daftar_mahasiswa(mahasiswa2)

lowongan1 = Lowongan("Software Engineer", "Bekerja di perusahaan teknologi terkemuka", ["Pengalaman dengan Python", "Kemampuan komunikasi yang baik"])
lowongan2 = Lowongan("Data Analyst", "Menganalisis data untuk menghasilkan wawasan bisnis", ["Menguasai SQL", "Pengalaman dengan analisis data"])
pusat_karir.daftar_lowongan(lowongan1)
pusat_karir.daftar_lowongan(lowongan2)

pusat_karir.tampilkan_mahasiswa_terdaftar()
pusat_karir.tampilkan_lowongan_terdaftar()

if authenticator.login(username, password):
    print("Login berhasil!")
else:
    print("Login gagal! Username atau password salah.")

print("\n***Daftar Mahasiswa:***")
for mahasiswa in sistem.daftar_mahasiswa:
    print(mahasiswa.nama)

print("\n***Daftar Dosen:***")
for dosen in sistem.daftar_dosen:
    print(dosen.nama)

print("\n***Daftar Kelas:***")
for kelas in sistem.daftar_kelas:
    print(kelas.kode)

print("\n***Daftar Mata Kuliah:***")
for mata_kuliah in sistem.daftar_mata_kuliah:
    print(mata_kuliah.nama)
