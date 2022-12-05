dictio = {'NIM': 3130020073, 'Nama': 'M Romli Arief', 'Jurusan': 'Sistem Informasi'}

#cara pertama dalam memanggil elemen
print(dictio['NIM'])

#cara kedua dalam memanggil elemen
print(dictio.get('Nama'))
print(dictio.get('Jurusan'))

#contoh pasangan bilangan dan pangkatnya
kuadrat = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}
print(kuadrat)

#menghapus elemen pada dictionary dan menampilkan kembali isinya
del kuadrat[1]
print(kuadrat)

#mengetahui elemen tersisa
kuadrat.values()
print(kuadrat)