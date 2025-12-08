from math import floor

from utils import *

# Tolong diganti sesuai ketentuan diskon yang dibuat
diskon: float = 0.05
diskon_member: float = 0.10
sub_total: int = 0
member: bool = False


def test_diskon_non_member():
    sub_total = 300_000
    member = False

    assert (
        hitung_diskon(sub_total, member) == 15_000
    ), "Non member yang sub_total >= 300_000 mendapatkan diskon"


def test_non_diskon_non_member():
    sub_total: int = 50_000
    member = False

    assert hitung_diskon(sub_total, member) == 0, "Tidak ada diskon apapun"


def test_diskon_member():
    sub_total = 312_000
    member = True

    assert hitung_diskon(sub_total, member) == floor(15_600 + 31_200), "Semua Diskon"


def test_non_diskon_member():
    sub_total = 120_000
    member = True

    assert (
        hitung_diskon(sub_total, member) == 12_000
    ), "Member mempunyai diskon tersendiri"
