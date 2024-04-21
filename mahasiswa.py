class Mahasiswa:
    def __init__(self, nama, nim, email):
        self.nama = nama
        self.nim = nim
        self.email = email
        self.jadwal_kuliah = []

    def tambahkan_jadwal_kuliah(self, jadwal):
        self.jadwal_kuliah.append(jadwal)

    def lihat_jadwal_kuliah(self):
        # Implementasi untuk melihat jadwal kuliah
        pass

    def mendaftar_mata_kuliah(self, mata_kuliah):
        # Implementasi untuk mendaftar mata kuliah
        pass