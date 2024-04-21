class StafAdministrasi:
    def __init__(self, nama, jabatan, email):
        self.nama = nama
        self.jabatan = jabatan
        self.email = email

    def perbarui_informasi_mahasiswa(self, mahasiswa, nama_baru, nim_baru, email_baru):
        mahasiswa.nama = nama_baru
        mahasiswa.nim = nim_baru
        mahasiswa.email = email_baru
        print(f"Informasi mahasiswa {mahasiswa.nama} berhasil diperbarui oleh {self.nama}.")

