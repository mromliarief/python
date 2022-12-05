print("== Selamat Datang di ATM Bersama ==")
print("Masukkan Pilihan Anda :")
print("1. Lihat Saldo")
print("2. Tarik Tunai")
print("3. Setor Tunai")
option=int(input("Silahkan Masukkan Pilihan Anda : "))

if option==1:
    print("Uang Anda Berjumlah Rp. 150.000")
elif option==2:
    uang_anda=150000
    print("Uang Anda Berjumlah Rp. 150.000, Berapa nominal yang akan diambil ?")
    print("1. Rp.50.000")
    print("2. Rp.100.000")

    # Input data dari user
    option_2=int(input("Pilihan : "))
    if option_2==1:
        hasil=uang_anda-50000
        print("Uang Anda Sekarang : ",hasil)
    elif option_2==2:
        hasil=uang_anda-100000
        print("Uang Anda Sekarang : ",hasil)
    else:
        print("Keyword Salah, Mohon Ulangi !")
elif option==3:
    uang_anda=150000
    print("== Masukkan Nominal Uang Yang Akan Anda Setorkan ==")

    #Input data dari user
    option_3=(int(input("Nominal : ")))
    hasil_1=uang_anda+option_3
    print("Uang Anda Sekarang : ",hasil_1)
else:
    print("Keyword Salah, Mohon Ulangi !")
