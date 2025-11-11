

def Kunjungan(id, jenis_kelamin, lokasi, kondisi, tanggal, pesan):
    return {
        "id": id,
        "jenis_kelamin": jenis_kelamin,
        "lokasi": lokasi,
        "kondisi": kondisi,
        "tanggal": tanggal,
        "pesan": pesan
    }

def Kunjungan_id(id):
    return f"KJ-{id:03d}"

def Kunjungan_jenis_kelamin(jenis_kelamin):
    jenis_kelamin = jenis_kelamin.lower()
    if jenis_kelamin in ['l', 'pria', 'laki-laki']:
        return 'Laki-laki'
    elif jenis_kelamin in ['p', 'wanita', 'perempuan']:
        return 'Perempuan'
    else:
        return 'Tidak Diketahui'
    
def Kunjungan_lokasi(lokasi):
    lokasi = lokasi.title()
    return lokasi

def Kunjungan_kondisi(kondisi):
    kondisi = kondisi.lower()
    if kondisi in ['sehat', 'baik']:
        return 'Sehat'
    elif kondisi in ['sakit', 'tidak sehat']:
        return 'Sakit'
    else:
        return 'Tidak Diketahui'
    
def Kunjungan_tanggal(tanggal):
    return tanggal

def Kunjungan_pesan(pesan):
    return pesan


def tampilkan_kunjungan(kunjungan):
    print(f"{'ID':<10} {'Jenis Kelamin':<15} {'Lokasi':<20} {'Kondisi':<10} {'Tanggal':<15} {'Pesan':<30}")
    print("-" * 100)

