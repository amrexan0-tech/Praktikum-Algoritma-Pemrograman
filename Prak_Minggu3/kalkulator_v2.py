angka1 = float(input("Masukan Angka Pertama :"))
operator = input("Masukan Operator (+, -, *, /) :")
angka2 = float(input("Masukan Angka Kedua :"))

hasil = {
    "+": (angka1 + angka2),
    "-": (angka1 - angka2),
    "*": (angka1 *angka2),
    "/": (angka1 / angka2)
}

print("hasil:", hasil[operator])