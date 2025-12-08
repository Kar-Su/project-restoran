import pytest

from utils import *


@pytest.fixture
def items():
    return [
        PesanItem(nama="Nasi Goreng", harga=12_000, jumlah=10, kategori="makanan"),
        PesanItem(nama="Matcha", harga=10_000, jumlah=5, kategori="minuman"),
    ]


def test_pesan(menu_items: list[PesanItem]):
    total_pesan = hitung_pesanan(menu_items)
    assert total_pesan == 170_000, "total pesanan harga dikali jumlah"
