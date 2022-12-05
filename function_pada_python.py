#contoh TANPA nilai return

def data_diri(nama,jurusan,kota):
    print('Halo nama saya '+nama)
    print('Jurusan saya '+jurusan)
    print('Saya berasal dari kota '+kota)

data_diri('Josep','Teknik Informatika','Kupang')

#contoh DENGAN nilai return
def penjumlahan(x,y):
    z = x + y
    print('Hasil penjumlahan nilai :',z)
    return z

penjumlahan(4,9)

#Membuat fungsi dengan inputan dari user-->fungsi scanner

def identitas ():
    namalengkap = input(str('Masukkan nama : '))
    asalkota = input(str('Masukkan asal kota : '))
    usia = input(str('Masukkan usia : '))
    pekerjaan = input(str('Pekerjaan : '))
    status = input(str('Status Perkawinan : '))
    print('-- DATA ANDA SUDAH TERINPUT --')
    print('Nama :',namalengkap,'\n''Kota :',asalkota,'\n''Usia :',usia,'\n''Pekerjaan :',pekerjaan,'\n''Status :',status)


identitas()