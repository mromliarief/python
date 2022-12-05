# Ekspresi lambda

# Contoh fungsi kuadrat biasa
def fungsi_kuadrat(angka):
    return angka**2

print(f"Hasil kuadrat dari = {fungsi_kuadrat(3)}")

# Contoh fungsi kuadrat Lambda
# Output = lambda argument: expression
kuadrat = lambda angka: angka**2
print(f"Hasil lambda kuadrat = {kuadrat(5)}")

pangkat = lambda num,pow : num**pow
print(f"Hasil pangkat lambda = {pangkat(5,2)}")

# fungsi lain dari lambda
# sorting list biasa

data_list = ["Ucup","Dudung","Otong"]
data_list.sort()
# Cetak hasil berdasarkan alfabet
print(f"Sorted data list = {data_list}")

# Sorting list menggunakan lambda
data_list = ["Ucup","Dudung","Otong"]
data_list.sort(key = lambda nama:len(nama))
print(f"Sorted data list dengan lambda = {data_list}")

# Sorting angka menggunakan lambda
data_angka = [1,2,3,4,5,6,7,8,9,10,11,12]

# sorting angka genap menggunakan lambda
print('==================================')
print("Sorting Genap menggunakan Lambda")
angka_genap = list(filter(lambda x:(x%2==0),data_angka))
print("Angka Genap =",angka_genap)

# sorting angka ganjil menggunakan lambda
print('==================================')
print("Sorting Ganjil menggunakan Lambda")
angka_ganjil = list(filter(lambda x:(x%2!=0),data_angka))
print("Angka Ganjil =",angka_ganjil)

# sorting angka ganjil menggunakan lambda
print('==================================')
print("Sorting Kelipatan 3 menggunakan Lambda")
angka_3 = list(filter(lambda x:(x%3==0),data_angka))
print("Angka Kelipatan 3 =",angka_3)
