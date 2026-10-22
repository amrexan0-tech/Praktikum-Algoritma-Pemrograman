bulan = 5
hari = 4
match bulan:
    case 1 | 2 | 3 | 4 | 5 if bulan == 4:
        print("Hari kerja di bulan April")
    case 1 | 2 | 3 | 4 | 5 if bulan == 5:
        print("Hari kerja di bulan Mei")
    case _:
        print("Bukan bulan kerja")