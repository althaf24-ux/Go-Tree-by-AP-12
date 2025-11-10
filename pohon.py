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

    # TODO : Kerjakan disini (FItur 5)
    def analisis_pemeliharaan(self):
        umur = (datetime.today().date() - self.tanggal_tanam).days
        bulan_ini = datetime.today().month
        umur_tahun = umur // 365
        umur_bulan = (umur % 365) // 30
        musim = "kemarau" if 5 >= bulan_ini >= 9 else "hujan"
        kategori = "tua" if umur_tahun >= 20 else "muda"

        print(f"\n🌳 Analisis Pohon ID {self.id}")
        print(f"Jenis: {self.jenis}")
        print(f"Lokasi: {self.lokasi}")
        print(f"Tanggal Tanam: {self.tanggal_tanam}")
        if umur_bulan != 0:
            print(f"Umur: {umur_tahun} tahun {umur_bulan} bulan ({kategori})")
        else:
            print(f"Umur: {umur_tahun} tahun ({kategori})")
        print(f"Musim saat ini: {musim}")

        if musim == "kemarau":
            if kategori == "tua":
                print("\n💡 Saran:")
                print("- Siram 2x seminggu secara mendalam.")
                print("- Tambahkan mulsa untuk menjaga kelembaban.")
                print("- Periksa akar secara rutin.")
            else:
                print("\n💡 Saran:")
                print("- Siram 3–4x seminggu secara teratur.")
                print("- Lindungi dari sinar matahari langsung di siang hari.")
                print("- Tambahkan pupuk organik secukupnya.")
        else:
            if kategori == "tua":
                print("\n💡 Saran:")
                print("- Kurangi penyiraman.")
                print("- Periksa sistem drainase agar tidak tergenang.")
                print("- Pangkas cabang mati untuk mencegah jamur.")
            else:
                print("\n💡 Saran:")
                print("- Pastikan area tanam tidak tergenang.")
                print("- Gunakan penyangga agar batang tidak roboh.")
                print("- Hindari pupuk cair berlebihan.")

    # TODO (Fitur 6)
    def tambah_kunjungan(self, tanggal_kunjungan, kondisi):
        self.kunjungan.append({
        "tanggal": tanggal_kunjungan,
        "kondisi": kondisi
    })
    # TODO : Kerjakan disini (Fitur 7)
    
    # TODO : Kerjakan disini (Fitur 7)