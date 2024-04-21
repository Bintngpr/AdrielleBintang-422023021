class Dosen:
    def __init__(self, nama, nidn, email):
        self.nama = nama
        self.nidn = nidn
        self.email = email
        self.kelas_diampu = []

    def tambahkan_kelas_diampu(self, kelas):
        self.kelas_diampu.append(kelas)

    def masukkan_nilai(self, mahasiswa, nilai):
        # Implementasi untuk memasukkan nilai mahasiswa
        pass
