from database import DatabasePohon
from pohon import Pohon
from utils import validasi_tanggal
from datetime import datetime, timedelta

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
        # TODO : Kerjakan disini (Fitur 1)
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
        # TODO : Kerjakan disini (Fitur 2)
        else:
            print("\n🔍 Submenu:")
            print("a. Cek umur dari tanggal")
            print("b. Cek tanggal dari umur")
            sub = input("Pilih submenu (a/b/kembali): ")
            if sub == "a":
                try:
                    # (fitur3)
                    id_input = int(input("Masukkan ID pohon: "))
                    id = next((pohon for pohon in db.data if pohon.id == id_input), None)
                    if id :
                        tanggal_input = input("Masukkan tanggal (YYYY-MM-DD): ")
                        tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d").date()
                        if tanggal >= pohon.tanggal_tanam:
                            umur = (tanggal - pohon.tanggal_tanam).days
                            print(f"Umur pohon: {umur} hari")
                        else:
                            print("❌ Tanggal harus setelah tanggal penanaman pohon.")
                    else:
                        print("❌ ID pohon tidak ditemukan.")
                except:
                    print("❌ Input tidak valid.")

            elif sub == "b":
                try:
                    # (fitur3)
                    id_input = int(input("Masukkan ID pohon: "))
                    id = next((pohon for pohon in db.data if pohon.id == id_input), None)
                    if id :
                        umur = int(input("Masukkan umur pohon (dalam hari): "))
                        if umur >= 0:
                            tanggal_tanam = pohon.tanggal_tanam
                            tanggal_hitung = tanggal_tanam + timedelta(days=umur)
                            print(f"Tanggal penanaman pohon: {tanggal_hitung}")
                        else:
                            print("❌ Umur tidak boleh negatif.")
                    else:
                        print("❌ ID pohon tidak ditemukan.")
                except:
                    print("❌ Input tidak valid.")
            else:
                continue

    elif pilihan == "4":
        # TODO : Kerjakan disini (Fitur 4)

    elif pilihan == "3":
        # TODO : Kerjakan disini (Fitur 5)
        if not db.data:
            print("❌ Belum ada data pohon untuk dianalisis.")
            continue

        print("\n🔎 Analisis Pemeliharaan Pohon")
        pohon.tampilkan()

        try:
            id_input = int(input("Masukkan ID pohon yang ingin dianalisis: "))
            pohon = None
            for p in db.data:
                if p.id == id_input:
                    pohon = p
                    break

            if pohon is None:
                print("❌ ID pohon tidak ditemukan.")
                continue

            pohon.analisis_pemeliharaan()

        except ValueError:
            print("❌ Input ID tidak valid.")

    elif pilihan == "5":
        # TODO (Fitur 6)
        print("\n📥 Input Kondisi & Kunjungan")
        db.tambah_data_pohon()

        if not db.data:
            continue

        try:
            id_pohon = int(input("Masukkan ID pohon yang dikunjungi: "))
            pohon_terpilih = None
            for pohon in db.data:
                if pohon.id == id_pohon:
                    pohon_terpilih = pohon
                    break

            if pohon_terpilih is None:
                print("❌ ID pohon tidak ditemukan.")
                continue

            tanggal_input = input("Masukkan tanggal kunjungan (YYYY-MM-DD): ")
            tanggal = validasi_tanggal(tanggal_input)
            if tanggal is None:
                print("❌ Tanggal tidak valid atau melewati hari ini.")
                continue

            kondisi = input("Masukkan kondisi pohon (subur/kering/layu): ")
            if kondisi not in ["subur", "kering", "layu"]:
                print("❌ Kondisi tidak valid. Gunakan: subur / kering / layu.")
                continue

            pohon_terpilih.tambah_kunjungan(tanggal, kondisi)
        except ValueError:
            print("❌ ID pohon tidak ditemukan.")
        
        except Exception:
            print("❌ Terjadi kesalahan input.")

    elif pilihan == "6":
        # TODO : Kerjakan disini (Fitur 7)
        
    elif pilihan == "0":
        print("👋 Terima kasih telah menjaga lingkungan bersama Go Tree!")
        break

    else:
        print("❌ Pilihan tidak valid.")