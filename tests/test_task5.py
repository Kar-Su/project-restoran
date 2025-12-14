import pytest

from utils import *


@pytest.fixture
def items() -> list[PesanItem]:
    return [
        PesanItem(nama="Nasi Goreng", harga=12_000, jumlah=10, kategori="makanan"),
        PesanItem(nama="Matcha", harga=10_000, jumlah=5, kategori="minuman"),
    ]


def test_informasi_struk(items: list[PesanItem]):
    struk = buat_struk("Huda", 1, 100_000, items)

    assert "Huda" in struk, "nama pelanggan tidak ada"
    assert "100,000" in struk, "total harga tidak ada"
    assert "Nasi Goreng" in struk, "nama makanan tidak ada"
    assert "Matcha" in struk, "nama minuman tidak ada"
