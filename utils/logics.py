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
    ...


def hitung_service(sub_total: int) -> int:
    """Task 2
    fungsi hitung_service

    details:
        Sebuah fungsi untuk menghitung biaya service restoran.
        perhitungan biaya service adalah 5% dari sub total pelanggan.

    params:
        sub_total(int): Merupakan sub total (harga sebelum service, diskon, pajak) dari pelanggan.

    returns (int):
        Berupa harga biaya service restoran.
    """
    ...


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
    ...


def hitung_pajak(sub_total: int, biaya_service: int) -> int:
    """Task 4
    fungi hitung_pajak

    details:
        Sebuah fungsi untuk menghitung pajak yang harus dibayarkan pelanggan.
        Pajak dihitung berdasarkan 10% dari sub total ditambah biaya service

    params:
        sub_total(int): Merupakan sub total (harga sebelum service, diskon, pajak) dari pelanggan.
        biaya_service(int): Merupakan biaya service restoran.

    returns (int):
        Berupa pajak yang harus dibayar oleh pelanggan
        akan tetapi pemerintah juga tidak menerima angka recehan
        berdasarkan regulasi, angka decimal akan dibulatkan keatas menggunakan fungsi 'ceil'
    """
    ...


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
    ...
