print("=== Sistem Pelatihan Kebugaran ===")

bulan = int(input("Masukkan bulan saat ini (1-12): "))
hari = int(input("Masukkan hari (1-7, 1=Senin): "))

# 1. MATCH CASE (Evaluasi Hari, Operator OR, If-Guard, dan Default Case)
match hari:
    case 1 | 2 | 3 | 4 | 5 if bulan == 8:
        print("Hari kerja di bulan Agustus! Fokus latihan Kardio intens.")
        jenis_latihan = "Kardio"
    case 1 | 2 | 3 | 4 | 5:
        print("Hari kerja biasa. Fokus latihan Beban.")
        jenis_latihan = "Beban"
    case 6 | 7:
        print("Akhir pekan! Waktunya pemulihan ringan.")
        jenis_latihan = "Yoga"
    case _:
        print("Input hari tidak valid. Anda butuh istirahat total.")
        jenis_latihan = "Istirahat"

# 2. WHILE TRUE DENGAN BREAK (Validasi Input)
if jenis_latihan != "Istirahat":
    target_set = 0
    while True:
        target_set = int(input(f"Berapa set {jenis_latihan} yang ingin dilakukan? (1-5): "))
        if target_set > 0 and target_set <= 5:
            break
        print("Jumlah set tidak valid. Harap masukkan angka 1 hingga 5.")

    print("\n--- Memulai Latihan ---")
    
    # 3. PERULANGAN FOR BERLAPIS (Nested Loop), CONTINUE, BREAK, PASS, dan ELSE DALAM LOOP
    # Loop Luar (For Loop dengan Range)
    for set_ke in range(1, target_set + 1):
        print(f"\nMenyiapkan Set {set_ke}...")
        
        # Penggunaan CONTINUE untuk melewati satu iterasi
        if set_ke == 2:
            print("Set 2 adalah istirahat aktif. Kita lewati repetisi berat ini.")
            continue
            
        # Penggunaan BREAK untuk menghentikan program jika batas lelah tercapai
        if set_ke == 4:
            print("Peringatan: Risiko cedera! Latihan dihentikan lebih awal.")
            break
            
        print(f"Mulai Set {set_ke}:")
        repetisi = 0
        
        # Loop Dalam (While Loop)
        while repetisi < 10:
            tambahan = 2
            repetisi += tambahan
            print(f"- Melakukan repetisi ke-{repetisi}...")
            
            # Penggunaan PASS (Blok kosong untuk diisi logika nantinya)
            if repetisi == 10:
                pass 
                
    # Penggunaan ELSE dalam perulangan FOR
    else:
        print("\nLuar biasa! Anda berhasil menyelesaikan target set tanpa berhenti di tengah jalan.")

print("\nProgram Selesai. Tetap sehat!")