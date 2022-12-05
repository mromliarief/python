# Pemrograman Berbasis Objek
# Class dan Object

class anjing():
    def __init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    
    def vaksin(self):
        if self.umur>4:
            print("Sudah Waktunya Vaksin")
        else:
            print("Belum Waktunya Vaksin")

blacky = anjing("Blacky",4)
shiro = anjing("Shiro",5)

print(blacky.nama)
print(blacky.umur)
print(blacky.vaksin())

print(shiro.nama)
print(shiro.umur)
print(shiro.vaksin())




