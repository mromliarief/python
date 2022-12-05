#Perintah Dasar
#INGAT Penulisan syntax di phyton harus memperhatikan indentasi
#karena nya spasi pun sangat diperhatikan
 
print("Hello World")
print([1,2,3,"abc"]) #ini contoh List
print(("xyz",1,2)) #ini contoh Tuple
print({"Nama : Adi","Id : 01"}) #ini contoh Dictionary

#Aritmatika
pangkat = 8**2 #contoh penulisan operator perpangkatan
print(pangkat)

#Pengkondisian If Else
nilai = 10
if(nilai>=7):
    print("Anda Lulus")
else:
    print("Harus Mengulang")

#Pengkondisian If elseif
kondisi = "Tanggal Merah"
if(kondisi == "Tanggal Merah"):
    print("Libur")
elif(kondisi != "Tanggal Merah"):
    print("Masuk")

#Perulangan While
kondisi = 1
while(kondisi <= 5):
    print("Cetak Angka = ",kondisi)
    kondisi = kondisi + 1 #increment

#Perulangan For
angka = [1,2,3,4,5]
for x in angka:
    print(x)

#String
nama = "John"
print("Index ke 0 : ", nama[0]) #mengakses karakter di index ke(n)
print("Index ke-0 s/d 3 :",nama[0:4])

#Update Nilai String
message = "Hello "
print("Update Message = ", message[:6] + "World")

#memunculkan tipe data pada variabel
print(type(message))



