#267006111060
#Anggian Fauzi
#Kelas F

print("=== Pengecekan Tiket Rollercoaster ===")

umur = int(input("Masukkan umur: "))
tinggi = float(input("Masukkan tinggi badan (cm): "))
harga = 50000

# 1. Pengecekan Utama (if-else)
if umur >= 12:

    # 2. Nested If (Kondisi Bersarang di dalam umur >= 12)
    if tinggi >= 150:
        print("\nSyarat terpenuhi! Anda boleh naik.")

        member = input("Punya member? (y/t): ")
        # Nested If kedua
        if member == "y":
            harga = harga - 10000  # Operator Assignment
            print("Anda dapat diskon, RP 10.000!")

        print("Total tiket: Rp", harga)
        uang = float(input("Masukkan uang Anda: Rp "))

        # 3. Pengecekan Pembayaran (Operator Perbandingan & Aritmatika)
        if uang == harga:
            print("Berhasil! Uang Pas!")
        elif uang > harga:
            print("Berhasil! Kembalian Anda: Rp", uang - harga)
        else:
            print("Gagal! Uang Anda kurang Rp", harga - uang)

    else:
        print("Maaf, tinggi badan Anda belum mencukupi (Minimal 150 cm).")

else:
    print("Maaf, wahana ini khusus untuk usia 12 tahun ke atas.")