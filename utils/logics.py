import math
from utils.models import PesanItem

def hitung_pesanan(pesanan: list[PesanItem]) -> int:
    """Task 1
    fungsi hitung_pesan

    details:
        Sebuah fungsi untuk menghitung total harga yang dipesan oleh pelanggan

    params:
        menu(list[PesanItem]) :sebuah array yang menyimpan data pesanan

    returns (int):
        Berupa integer total harga pesanan pelanggan

    """
    total = 0;
    for item in pesanan:
        total += item.harga*item.jumlah
    
    return total


def hitung_service(sub_total: int) -> int:
    biaya_service = sub_total * 0.05
    biaya_service_bulat = math.ceil(biaya_service)
    return biaya_service_bulat
    


def hitung_diskon(sub_total: int, member: bool) -> int:
    """Task 3
    Fungsi hitung_diskon

    details:
        Sebuah fungsi untuk menghitung diskon yang didapatkan pelanggan.
        Restoran mempunyai 2 skema diskon.
        - skema 1:
            Ketika sub_total pelanggan >= 300_000
            maka pelanggan mendapatkan diskon 5% dari harga sub total
        - Skema 2:
            Restoran mempunyai program membership. Sehingga pelanggan yang merupakan member mendapat diskon
            diskon yang didapatkan yaitu 10% dari harga sub total
            member juga tetap bisa mendapatkan diskon skema 1 sesuai ketentuannya.

    params:
         sub_total(int): Merupakan sub total (harga sebelum service, diskon, pajak) dari pelanggan.
         member(bool): Identifikasi apakah pelanggan member atau tidak (True or False).

    returns (int):
        Berupa total diskon yang didapatkan pelanggan.
        akan tetapi restoran tidak menerima angka recehan.
        Sehingga diskon angka decimal akan dibulatkan kebawah menggunakan fungsi 'floor'.
    """
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
    """Task 5
    fungsi buat_struk

    details:
        Sebuah fungsi untuk membuat struk pembelian di restoran.
        Didalam struk harus ada  informasi minimal:
        - nama pelanggan
        - nama makanan/minuman
        - harga makanan/minuman

        Bentuknya bebas, bisa ambil referensi struk di google.
        parameter bisa diubah sesuai kebutuhan struk

    params:
        nama_pelanggan(str): nama pelanggan yang memesan
        meja(int): nomor meja
        total(int): total harga yang harus dibayar pelanggan
        pesanan(PesanItem): List item yang dipesan pelanggan

    returns (str):
        Berupa string dari struk.
    """
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
