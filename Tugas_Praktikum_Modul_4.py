# =========================================================
# CLASS & METHOD (Materi OOP/Method)
# =========================================================
class Transaksi:

    def __init__(self, nama_pembeli):
        self.nama_pembeli = nama_pembeli
        self.daftar_belanja = []

    # 1. Method Return Type Berparameter
    def hitung_diskon(self, total_harga):
        # Pengkondisian (If-Elif-Else)
        if total_harga >= 100000:
            return total_harga * 0.10  # Diskon 10%
        elif total_harga >= 50000:
            return total_harga * 0.05  # Diskon 5%
        else:
            return 0.0

    # 2. Method Non-Return Type (Void Method)
    def cetak_struk(self, total_awal, diskon, total_akhir):
        print("\n" + "=" * 40)
        print(f"         STRUK BELANJA - {self.nama_pembeli.upper()}")
        print("=" * 40)

        # Perulangan (For Loop)
        for idx, item in enumerate(self.daftar_belanja, start=1):
            print(
                f"{idx}. {item['nama']:<15} x{item['jumlah']:<3} = Rp{item['subtotal']:,}"
            )

        print("-" * 40)
        print(f"Total Awal   : Rp{total_awal:,}")
        print(f"Diskon       : Rp{int(diskon):,}")
        print(f"Total Bayar  : Rp{int(total_akhir):,}")
        print("=" * 40)
        print("    Terima kasih telah berbelanja!    \n")


# =========================================================
# FUNCTION (Di luar class)
# =========================================================


# 3. Function Non-Return Type
def tampilkan_header():
    print("========================================")
    print("      PROGRAM KASIR MINIMARKET          ")
    print("========================================")


# 4. Function Return Type Tanpa Parameter
def dapatkan_katalog_harga():
    # Mengembalikan dictionary daftar barang dan harga
    return {"Minyak": 18000, "Beras": 65000, "Gula": 15000, "Roti": 12000}


# =========================================================
# PROGRAM UTAMA (Perulangan & Logika Eksekusi)
# =========================================================
def main():
    tampilkan_header()  # Memanggil Function Non-Return Type

    nama = input("Masukkan nama pembeli: ")
    transaksi = Transaksi(nama)
    katalog = dapatkan_katalog_harga()  # Memanggil Function Return Type Tanpa Parameter

    # Perulangan (While Loop) untuk input belanjaan
    satu_lagi = "y"
    while satu_lagi.lower() == "y":
        print("\n--- Catalog Barang ---")
        for item, harga in katalog.items():
            print(f"- {item:<10} : Rp{harga:,}")

        pilihan = input("\nMasukkan nama barang yang dibeli: ").title()

        # Pengkondisian pengecekan barang
        if pilihan in katalog:
            try:
                jumlah = int(input(f"Masukkan jumlah {pilihan}: "))
                if jumlah > 0:
                    subtotal = katalog[pilihan] * jumlah
                    transaksi.daftar_belanja.append(
                        {"nama": pilihan, "jumlah": jumlah, "subtotal": subtotal}
                    )
                    print(f"-> {pilihan} berhasil ditambahkan!")
                else:
                    print("[!] Jumlah barang harus lebih dari 0.")
            except ValueError:
                print("[!] Input jumlah harus berupa angka.")
        else:
            print("[!] Barang tidak ditemukan dalam katalog.")

        satu_lagi = input("\nTambah barang lagi? (y/n): ")

    # Pengecekan apakah ada barang yang dibeli
    if len(transaksi.daftar_belanja) > 0:
        # Hitung total harga awal menggunakan loop
        total_awal = sum(item["subtotal"] for item in transaksi.daftar_belanja)

        # Memanggil Method Return Type Berparameter
        diskon = transaksi.hitung_diskon(total_awal)
        total_akhir = total_awal - diskon

        # Memanggil Method Non-Return Type
        transaksi.cetak_struk(total_awal, diskon, total_akhir)
    else:
        print("\nTidak ada barang yang dibeli. Program selesai.")


if __name__ == "__main__":
    main()