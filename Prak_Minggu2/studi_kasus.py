#Profil Mahasiswa
universitas = "Universitas Siliwangi"
program_studi = "Informatika"
fakultas = "Teknik"
status_aktif = True
nama = input('Masukan Nama Anda :')
npm = int(input("Masukan NPM Anda :"))
umur = int(input("Masukan Umur Anda :"))
tinggi_badan = float(input("Masukan Tinggi Badan Anda :"))


print("\n=== PROFIL MAHASISWA ===")
print(f"Universitas: {universitas}")
print(f"Program Studi: {program_studi}")
print(f"Fakultas: {fakultas}")
print(f"Status Aktif: {status_aktif}")
print(f"Nama :{nama}")
print("NPM Anda Adalah", npm)
print("Umur Anda Adalah", umur,"Tahun")
print("Tinggi Badan Anda Adalah", tinggi_badan,"cm")

print("\n=== TIPE DATA ===")
print(type(universitas))
print(type(status_aktif))
print(type(nama))
print(type(npm))
print(type(umur))
print(type(tinggi_badan))

