from database import DatabasePohon
from pohon import Pohon
from utils import validasi_tanggal

db = DatabasePohon()

def menu():
    print("\n🌱 GO TREE – Kontrol Bibit Pohon")
    print("1. Tambah Data Pohon")
    print("2. Lihat Data Pohon")
    print("3. Analisis Pemeliharaan")
    print("4. Hapus Data Pohon")
    print("5. Input Kondisi & Kunjungan")
    print("6. Tampilkan Tabel Kondisi")
    print("0. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        # TODO : Kerjakan disini (fitur1)
        print("\n📥 Tambah Data Pohon")
        jenis = input("Jenis Pohon : ")
        lokasi = input("Tempat Penanaman Pohon : ")
        tanggal_input = input("Tanggal Penanaman Pohon (YYYY-MM-DD) : ")
        tanggal = validasi_tanggal(tanggal_input)
        if tanggal is not None:
            pohon = Pohon(jenis, lokasi, tanggal)
            db.tambah_data_pohon(pohon)
        else:
            print("❌ Input tidak valid atau tanggal tidak boleh melewati hari ini.")


    elif pilihan == "2":
        # TODO : Kerjakan disini (fitur2)
        else:
            print("\n🔍 Submenu:")
            print("a. Cek umur dari tanggal")
            print("b. Cek tanggal dari umur")
            sub = input("Pilih submenu (a/b/kembali): ")
            if sub == "a":
                try:
                    # (fitur3)
                    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
                    umur = db.cek_umur_dari_tanggal(tanggal)
                    print(f"Umur pohon: {umur} tahun")

                except:
                    print("❌ Input tidak valid.")

            elif sub == "b":
                try:
                    # (fitur3)
                    umur = int(input("Masukkan umur pohon (dalam tahun): "))
                    tanggal = db.cek_tanggal_dari_umur(umur)
                    print(f"Tanggal penanaman pohon: {tanggal}")

                except:
                    print("❌ Input tidak valid.")
            else:
                continue

    elif pilihan == "3":
        # TODO : Kerjakan disini (fitur4)

    elif pilihan == "4":
        # TODO : Kerjakan disini (fitur5)

    elif pilihan == "5":
        # TODO : Kerjakan disini (fitur6)

    elif pilihan == "6":
        # TODO : Kerjakan disini (fitur7)
        
    elif pilihan == "0":
        print("👋 Terima kasih telah menjaga lingkungan bersama Go Tree!")
        break

    else:
        print("❌ Pilihan tidak valid.")