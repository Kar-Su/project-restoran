import math
from utils.models import PesanItem

def hitung_pesanan(pesanan: list[PesanItem]) -> int:
    total = 0
    for item in pesanan:
        total += item.harga*item.jumlah
    
    return total


def hitung_service(sub_total: int) -> int:
    biaya_service = sub_total * 0.05
    biaya_service_bulat = math.ceil(biaya_service)
    return biaya_service_bulat
    


def hitung_diskon(sub_total: int, member: bool) -> int:
    diskon = 0
    if member:
        diskon += sub_total * 0.10
    if sub_total >= 300_000:
        diskon += sub_total * 0.05
    return math.floor(diskon)


def hitung_pajak(sub_total: int, biaya_service: int) -> int:
    biaya_pajak = (sub_total + biaya_service) * 0.10
    total_pajak = math.ceil(biaya_pajak)
    return total_pajak


def buat_struk(
    nama_pelanggan: str, meja: int, total: int, pesanan: list[PesanItem]
) -> str:
    garis = "=" * 30
    teks = f"\n{garis}\nRESTORAN KELOMPOK 2\n{garis}\n"
    teks += f"Meja : {meja}\n"
    teks += f"Nama : {nama_pelanggan}\n"
    teks += "-" * 30 + "\n"

    for item in pesanan:
        teks += f"{item.nama} (x{item.jumlah})\n"

    teks += "-" * 30 + "\n"
    teks += f"TOTAL BAYAR: Rp {total:,}\n"
    teks += f"{garis}\nTerima Kasih!\n"
    return teks
