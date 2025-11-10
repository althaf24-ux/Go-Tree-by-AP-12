# TODO : Kerjakan disini (Fitur 1)
from datetime import datetime, timedelta

def validasi_tanggal(tanggal_input):
    try:
        tanggal = datetime.strptime(tanggal_input, "%Y-%m-%d").date()
        if tanggal > datetime.today().date():
            return None
        return tanggal
    except:
        return None

# TODO : Kerjakan disini (Fitur 5)