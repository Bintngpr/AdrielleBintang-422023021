class Mahasiswa:
    def __init__(self, nama, nim, email):
        self.nama = nama
        self.nim = nim
        self.email = email
        self.jadwal_kuliah = []

    def __str__(self):
        return f"Mahasiswa: {self.nama}, NIM: {self.nim}, Email: {self.email}"

    def tambahkan_jadwal_kuliah(self, jadwal):
        self.jadwal_kuliah.append(jadwal)

    def lihat_jadwal_kuliah(self):
        pass

    def mendaftar_mata_kuliah(self, mata_kuliah):
        pass