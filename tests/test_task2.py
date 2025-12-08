import pytest

from utils import *

# Biaya Service diganti seusai ketentuan yang dibuat
biaya_service: float = 0.05


def test_hitung_service():
    sub_total: int = 100_000

    assert hitung_service(sub_total) == pytest.approx(
        sub_total * biaya_service
    ), "Hitung Service merupakan berapa persennya sub total"
