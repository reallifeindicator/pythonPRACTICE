import json
import os

# Fungsi untuk memuat menu dari file JSON
def load_menu():
    
    try:
        with open("menu.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("File menu.json tidak ditemukan.")
        return None

    except json.JSONDecodeError as e:
        print(f"Format JSON salah: {e}")
        return None

# Menampilkan menu
def tampilkan_menu(menu):

    print("\n========== MENU ==========")

    print("\nMakanan")
    for nama, harga in menu["makanan"].items():
        print(f"- {nama:<15} Rp {harga:,}")

    print("\nMinuman")
    for nama, harga in menu["minuman"].items():
        print(f"- {nama:<15} Rp {harga:,}")

    print("===========================")

# Menghitung diskon
def hitung_diskon(total):

    if total > 100000:
        return total * 0.10

    return 0

# Cetak struk
def cetak_struk(keranjang, total, diskon, nama):

    print("\n========== STRUK ==========")

    for item, data in keranjang.items():

        subtotal = data["harga"] * data["jumlah"]

        print(f"{item:<15}{data['jumlah']} x Rp {data['harga']:,} = Rp {subtotal:,}")

    print("----------------------------")
    print(f"Total Harga : Rp {total:,.0f}")

    if diskon > 0:
        print("Diskon      : 10%")
        print(f"Potongan    : Rp {diskon:,.0f}")
    else:
        print("Diskon      : Tidak ada")

    print(f"Total Bayar : Rp {total-diskon:,.0f}")
    print("----------------------------")
    print(f"Terima kasih telah berbelanja, {nama}!")

# PROGRAM UTAMA
def main():

    menu = load_menu()

    nama = input("Masukkan nama pelanggan : ")

    print(f"\nSelamat datang, {nama}")

    keranjang = {}

    while True:

        tampilkan_menu(menu)

        while True:

            kategori = input("\nPilih kategori (makanan/minuman): ").lower()

            if kategori in menu:
                break

            print("Kategori tidak tersedia.")

        while True:

            item = input("Masukkan nama menu : ").title()

            if item in menu[kategori]:
                break

            print("Menu tidak tersedia.")

        while True:

            try:

                jumlah = int(input("Jumlah : "))

                if jumlah > 0:
                    break

                print("Jumlah harus lebih dari 0.")

            except ValueError:

                print("Masukkan angka.")

        harga = menu[kategori][item]

        if item in keranjang:
            keranjang[item]["jumlah"] += jumlah
        else:
            keranjang[item] = {
                "harga": harga,
                "jumlah": jumlah
            }

        while True:

            lanjut = input("\nTambah pesanan lagi? (ya/tidak): ").lower()

            if lanjut in ["ya", "tidak"]:
                break

            print("Perintah tidak valid.")

        if lanjut == "tidak":
            break

    total = 0

    for data in keranjang.values():
        total += data["harga"] * data["jumlah"]

    diskon = hitung_diskon(total)

    cetak_struk(
        keranjang,
        total,
        diskon,
        nama
    )

# Menjalankan program
if __name__ == "__main__":
    main()