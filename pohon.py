from datetime import datetime

class Pohon:
    _id_counter = 1

    def __init__(self, jenis, lokasi, tanggal_tanam):
        self.id = Pohon._id_counter
        Pohon._id_counter += 1
        self.jenis = jenis
        self.lokasi = lokasi
        self.tanggal_tanam = tanggal_tanam
        # TODO (Fitur 6)
        self.kunjungan = []

    # TODO : Kerjakan disini (Fitur 2)

    # TODO : Kerjakan disini (Fitur 2)

    # TODO (Fitur 6)
    def tambah_kunjungan(self, tanggal_kunjungan, kondisi):
        self.kunjungan.append()
        "tanggal": tanggal_kunjungan
        "kondisi": kondisi

    # TODO : Kerjakan disini (Fitur 7)
    
    # TODO : Kerjakan disini (Fitur 7)