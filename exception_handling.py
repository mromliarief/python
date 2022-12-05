# Exception Try Except
# cara 1
print("--PROGRAM PEMBAGIAN PERTAMA--")

while True:
    try:
        angka_1 = int(input("Masukkan angka pertama : "))
        angka_2 = int(input("Masukkan angka kedua : "))
        hasil = angka_1/angka_2
        break
    except ValueError:
        print("Yang anda masukkan bukan angka")
    except ZeroDivisionError:
        print("Angka tidak bisa dibagi dengan nol")

print("Hasil pembagian adalah : ",hasil)

# cara 2
print("--PROGRAM PEMBAGIAN KEDUA")
while True:
    try:
        angka_1 = int(input("Masukkan angka pertama : "))
        angka_2 = int(input("Masukkan angka kedua : "))
        hasil = angka_1/angka_2
        break
    except Exception as error_message:
        print(error_message)

print("Hasil pembagian adalah : ",hasil)
