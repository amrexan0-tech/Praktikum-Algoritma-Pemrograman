print("=== Kalkulator Patungan Makan ===")


nama = input("Masukkan nama Anda: ")

tagihan_awal = float(input("Total tagihan (Rp): "))
persen_tip = int(input("Persentase tip/pajak (misal: 10): "))
jumlah_orang = int(input("Jumlah orang yang ikut patungan: "))


nominal_tip = tagihan_awal * (persen_tip / 100)

total_tagihan = tagihan_awal + nominal_tip

bayar_per_orang = total_tagihan / jumlah_orang

print("\n=== Ringkasan Tagihan ===")
print("Halo, " + nama + "!")
print("Total tagihan beserta tip adalah: Rp", total_tagihan)
print("Setiap orang harus membayar: Rp", bayar_per_orang)

