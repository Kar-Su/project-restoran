from typing import Literal

from pydantic import BaseModel, PositiveInt


class PesanItem(BaseModel):
    nama: str
    harga: PositiveInt
    jumlah: PositiveInt
    kategori: Literal["makanan", "minuman"]


class InformasiPesanan(BaseModel):
    nomor_meja: PositiveInt
    nama_pelanggan: str
    member: bool = False


class Bill(BaseModel):
    biaya_service: int
    diskon: int
    pajak: int
    sub_total: int
    total: int


if __name__ == "__main__":
    pesan = PesanItem(nama="Nasi Goreng", harga=12_000, jumlah=10, kategori="makanan")
    list_pesanan = [
        pesan,
        PesanItem(nama="Matcha", harga=10_000, jumlah=5, kategori="minuman"),
    ]

    print(list_pesanan[1].nama)
