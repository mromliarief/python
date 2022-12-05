# args dan kwargs (keyword args)
from pandas import options


def math(*args,**kwargs):
    output = 0
    if kwargs["options"]=="tambah":
        print("Operasi Penjumlahan")
        for angka in args:
            output += angka
    elif kwargs["options"]=="kali":
        print("Operasi Perkalian")
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Operasi tidak ditemukan !")
    return output

hasil = math(1,2,3,4,5,6, options="kali")
print(f"Hasil kali = {hasil}")
print("===================")
hasil = math(1,2,3,4,5,6, options="tambah")
print(f"Hasil jumlah = {hasil}")