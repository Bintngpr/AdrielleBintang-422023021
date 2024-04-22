class PusatKarir:
    def __init__(self):
        self.mahasiswa_terdaftar = []
        self.lowongan_terdaftar = []

    def daftar_mahasiswa(self, mahasiswa):
        self.mahasiswa_terdaftar.append(mahasiswa)

    def daftar_lowongan(self, lowongan):
        self.lowongan_terdaftar.append(lowongan)

    def tampilkan_mahasiswa_terdaftar(self):
        print("\n***Mahasiswa Terdaftar untuk Ketersediaan:***")
        for mahasiswa in self.mahasiswa_terdaftar:
            print(mahasiswa)

    def tampilkan_lowongan_terdaftar(self):
        print("\n***Pusat Karir:***")
        for lowongan in self.lowongan_terdaftar:
            print(lowongan)
