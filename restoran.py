import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, IntPrompt, Confirm
from rich.progress import track
from random import randint

from utils import *

console = Console()

MENU_RESTO = {
    1: {"nama": "Nasi Goreng Special", "harga": 25000, "kategori": "makanan"},
    2: {"nama": "Ayam Bakar Madu", "harga": 30000, "kategori": "makanan"},
    3: {"nama": "Es Teh Manis", "harga": 5000, "kategori": "minuman"},
    4: {"nama": "Jus Alpukat", "harga": 15000, "kategori": "minuman"},
    5: {"nama": "Kentang Goreng", "harga": 12000, "kategori": "makanan"},
}

class Restoran:
    def __init__(self):
        self.keranjang = []

    def tampilan_menu(self):
        table = Table(title="[bold green]DAFTAR MENU RESTORAN[/bold green]")

        table.add_column("ID", justify="center", style="cyan", no_wrap=True)
        table.add_column("Nama Menu", style="magenta")
        table.add_column("Kategori", justify="center", style="yellow")
        table.add_column("Harga", justify="center", style="green")

        for idx, info in MENU_RESTO.items():
            table.add_row(str(idx), info['nama'], info['kategori'], f"Rp {info['harga']:,}")

        console.print(table)

    def pesan(self):
        console.clear()
        console.rule("[bold red]Selamat Datang Pelanggan Terhormat[/bold red]")
        
        nama = Prompt.ask("[bold cyan]Siapa nama Anda?[/bold cyan]")
        is_member = Confirm.ask("Apakah Anda memiliki kartu member?")
        
        while True:
            console.print("\n")
            self.tampilan_menu()
            
            user = IntPrompt.ask("\nPilih Nomor Menu ([bold red]0[/bold red] untuk checkout)", default=0)
            
            if user == 0:
                if not self.keranjang:
                    console.print("[bold red]Keranjang masih kosong![/bold red]")
                    time.sleep(1.5)
                    continue
                break
            
            if user not in MENU_RESTO:
                console.print("[bold red]Menu tidak ditemukan![/bold red]")
                time.sleep(1.5)
                continue
            
            item_data = MENU_RESTO[user]
            console.print(f"Memilih: [italic]{item_data['nama']}[/italic]")
            jumlah = IntPrompt.ask("Mau pesan berapa porsi?")
            
            self.keranjang.append({
                "nama": item_data['nama'],
                "harga": item_data['harga'],
                "jumlah": jumlah,
                "kategori": item_data['kategori']
            })
            
            console.print(f"[bold green]Sukses menambahkan {jumlah}x {item_data['nama']} ke keranjang![/bold green]")
            time.sleep(1.3)
            console.clear()

        return {
            "nama_pelanggan": nama,
            "is_member": is_member,
            "items": self.keranjang
        }

    def proses_pesanan(self):
        try:
            data = self.pesan()
            with console.status("[bold green]Sedang memvalidasi pesanan ke dapur...[/bold green]", spinner="dots"):
                pesanan_valid = InformasiPesanan(**data)
                time.sleep(2) # Simulasi delay jaringan/proses
            
            console.print("[bold blue]Pesanan Terkonfirmasi![/bold blue] \u2713")
            
            steps = ["Menghitung Subtotal...", "Cek Service Charge...", "Hitung Pajak...", "Cek Diskon Member...", "Finalisasi Struk..."]

            subtotal = 0
            service = 0
            pajak = 0
            diskon = 0
            
            for step in track(steps, description="Processing..."):
                time.sleep(0.5)
                if "Subtotal" in step:
                    subtotal = hitung_pesanan(pesanan_valid.items)
                elif "Service" in step:
                    service = hitung_service(subtotal)
                elif "Pajak" in step:
                    pajak = hitung_pajak(subtotal, service)
                elif "Diskon" in step:
                    diskon = hitung_diskon(subtotal, pesanan_valid.member)
            
            total = (subtotal + service + pajak) - diskon

            generate_struk = buat_struk(
                nama_pelanggan=pesanan_valid.nama_pelanggan,
                meja=randint(1,20),
                total=total,
                pesanan=pesanan_valid.items
            )
            
            console.clear()
            console.print(Panel(
                generate_struk, 
                title="[bold yellow]STRUK PEMBAYARAN[/bold yellow]", 
                subtitle="KELOMPOK 2",
                style="white on black",
                expand=False
            ))

        except Exception as e:
            console.print_exception(show_locals=True)