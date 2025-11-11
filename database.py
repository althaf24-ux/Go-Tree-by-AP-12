class DatabasePohon:
    def __init__(self):
        self.data = []

    # TODO : Kerjakan disini (Fitur 1)
    def tambah_data_pohon (self, pohon):
        self.data.append(pohon)
        print("✅ Data pohon berhasil ditambahkan!")
    
    # TODO : Kerjakan disini (Fitur 2)

    # TODO : Kerjakan disini (Fitur 4)
    def hapus_pohon(self, id_pohon):
        for pohon in self.data:
            if pohon.id == id_pohon:
                self.data.remove(pohon)
                return True
        return False