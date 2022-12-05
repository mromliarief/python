
# Online Python - IDE, Editor, Compiler, Interpreter
# List Dua Dimensi / Array Dua Dimensi
list_1 = [[1,2],[3,4]]
print(list_1[0][1])

print("--------------------------")

list_2 = [1,2,3,4]
for x in list_2:
    print(x)
    
print("--------------------------")

listku = ['p','y','t','h','o','n']
print('Elemen index ke 0 adalah '+listku[0])
print('Elemen index ke 1 adalah '+listku[1])
print('Elemen index ke 2 adalah '+listku[2])
print('Elemen index ke 5 adalah '+listku[5])

#fungsi concat berjalan karena string digabung dengan char
#jika dengan int tidak berjalan/error

print("--------------------------")

ganjil = [1,3,5,7]
ganjil.append(9)
print(ganjil)

print("--------------------------")

#sorting elemen
huruf = ['a','b','f','g','d','e','c']
huruf.sort()
print(huruf)

#sorting dibalik
huruf.reverse()
print(huruf)