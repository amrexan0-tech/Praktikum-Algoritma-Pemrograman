print("=== Pengecekan Tiket Rollercoaster ===")
umur = int(input("Masukkan Umur: "))

if umur < 12:
    print("Maaf anda belum cukup umur, 12 tahun ke atas yang boleh!")
else:
    tinggi = int(input("Masukkan Tinggi Badan: "))
    if tinggi < 140:
        print("Anda tidak boleh masuk, tinggi badan tidak mencukupi!")
    else:
        print("\nSyarat Terpenuhi Anda Boleh Naik!")
        membership = input("Punya membership? (y/t): ").lower()

        harga_dasar = 50000
        if membership == "y":
            print("Anda dapat diskon, RP 10.000!")
            total_tiket = harga_dasar - 10000
        else:
            total_tiket = harga_dasar

        print("Total tiket: RP", total_tiket)
        uang = int(input("Masukan Uang Anda RP: "))

        if uang >= total_tiket:
            kembalian = uang - total_tiket
            print("Berhasil, Kembalian anda RP: ", kembalian)
        else:
            print("Uang anda tidak cukup!")