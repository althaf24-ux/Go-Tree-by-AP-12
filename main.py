from database import DatabasePohon

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
    elif pilihan == "2":
        # TODO : Kerjakan disini (fitur2)
        else:
            print("\n🔍 Submenu:")
            print("a. Cek umur dari tanggal")
            print("b. Cek tanggal dari umur")
            sub = input("Pilih submenu (a/b/kembali): ")
            if sub == "a":
                try:
                    # TODO : Kerjakan disini (fitur3)
                except:
                    print("❌ Input tidak valid.")

            elif sub == "b":
                try:
                    # TODO : Kerjakan disini (fitur3)
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