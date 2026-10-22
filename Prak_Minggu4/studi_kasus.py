#267006111060
#Anggian Fauzi
#Kelas F

umur = int(input("Masukkan Umur: "))

if umur < 15:
    print("Maaf, usia minimal mendaftar adalah 15 tahun")
else:
    kelas = input("Masukkan Pilihan Kelas (ketik: 'yoga', 'boxing', atau 'zumba'): ")

    if kelas == 'yoga':
        tarif_kelas = 300000
    elif kelas == 'boxing':
        tarif_kelas = 400000
    elif kelas == 'zumba':
        tarif_kelas = 250000
    else:
        tarif_kelas = 200000
        kelas = "Reguler"
        print("Info: Kelas tidak dikenali, dialihkan ke Kelas Reguler.")

    sewa_loker = input("Sewa Loker (ketik: 'y' atau 't'): ")

    if sewa_loker == 'y':
        biaya_loker = 50000
    else:
        biaya_loker = 0

    total_bayar = tarif_kelas + biaya_loker

    print("\n--- Rincian Tagihan ---")
    print(f"Nama Kelas: {kelas}")
    print(f"Biaya Kelas: Rp {tarif_kelas}")
    print(f"Biaya Loker: Rp {biaya_loker}")
    print(f"Total Bayar: Rp {total_bayar}")