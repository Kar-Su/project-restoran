from utils import *

def main():
    print("Hello from project-restorant!")


if __name__ == "__main__":
    pesan = PesanItem(nama="Nasi Goreng", harga=12_000, jumlah=10, kategori="makanan")
    list_pesanan = [
        pesan,
        PesanItem(nama="Matcha", harga=10_000, jumlah=5, kategori="minuman"),
    ]

    hitung_pesanan(list_pesanan)

    
    
