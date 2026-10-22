print("=== Sistem Cek Belanja & Status Pembayaran ===")


nama_pembeli = input("Masukkan nama pembeli: ")
harga_satuan = int(input("Harga satuan barang (Rp): "))
jumlah_barang = int(input("Jumlah barang yang dibeli: "))
uang_diberikan = int(input("Uang yang diberikan ke kasir (Rp): "))

total_harga = harga_satuan * jumlah_barang
selisih_uang = uang_diberikan - total_harga

uang_cukup = uang_diberikan >= total_harga
uang_pas = uang_diberikan == total_harga
berhutang = uang_diberikan < total_harga

print("\n=== Ringkasan Transaksi ===")
print(f"Nama Pelanggan: {nama_pembeli}")
print(f"Total Harga: Rp {float(total_harga)}")
print(f"Selisih Uang (Kembalian/Kekurangan): Rp {float(selisih_uang)}")

print("\n=== Status Cek Sistem (True/False) ===")
print(f"Apakah uang yang dibayarkan cukup? : {uang_cukup}")
print(f"Apakah pembeli membayar uang pas?  : {uang_pas}")
print(f"Apakah pembeli berhutang?          : {berhutang}")