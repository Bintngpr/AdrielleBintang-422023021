class Lowongan:
    def __init__(self, judul, deskripsi, requirements):
        self.judul = judul
        self.deskripsi = deskripsi
        self.requirements = requirements

    def __str__(self):
        return f"Lowongan: {self.judul}, Deskripsi: {self.deskripsi}, Persyaratan: {', '.join(self.requirements)}"
