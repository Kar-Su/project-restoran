from math import ceil

from utils import *

# pajak diganti sesuai dengan ketentuan yang dibuat dalam fungsi
pajak: float = 0.10


def test_pajak():
    sub_total: int = 100_000
    biaya_service: int = 5_000

    assert hitung_pajak(sub_total, biaya_service) == ceil(
        10_500
    ), "Pajak 10% persen daripada sub total + biaya service"
