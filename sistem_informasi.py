class SistemInformasi:
    def __init__(self):
        self.daftar_mahasiswa = []
        self.daftar_dosen = []
        self.daftar_kelas = []
        self.daftar_mata_kuliah = []

    def tambahkan_mahasiswa(self, mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)

    def tambahkan_dosen(self, dosen):
        self.daftar_dosen.append(dosen)

    def tambahkan_kelas(self, kelas):
        self.daftar_kelas.append(kelas)

    def tambahkan_mata_kuliah(self, mata_kuliah):
        self.daftar_mata_kuliah.append(mata_kuliah)
