class Kelas:
    def __init__(self, kode, mata_kuliah, dosen_pengajar):
        self.kode = kode
        self.mata_kuliah = mata_kuliah
        self.dosen_pengajar = dosen_pengajar
        self.mahasiswa_terdaftar = []

    def tambahkan_mahasiswa(self, mahasiswa):
        self.mahasiswa_terdaftar.append(mahasiswa)
