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
