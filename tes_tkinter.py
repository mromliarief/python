import tkinter as tk
from tkinter import Button, ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
# set warna
window.configure(bg="light blue")
#set ukuran
window.geometry("300x200")
# set can not resize window
# window.resizable(False,False)
# set judul
window.title("Python GUI Message")

# frame input
input_frame = ttk.Frame(window)
# Penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, expand=True, fill="x")

#komponen
# 1. Label
nama_depan_label = ttk.Label(input_frame, text="Nama Depan : ")
nama_depan_label.pack(padx=10, pady=10, expand=True, fill="x")

# 2. Entry Nama Depan
NAMA_DEPAN = tk.StringVar()
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, pady=10, expand=True, fill="x")

# 3. Label Kedua
nama_belakang_label = ttk.Label(input_frame, text="Nama Belakang : ")
nama_belakang_label.pack(padx=10, pady=10, expand=True, fill="x")

# 4. Entry Nama Belakang
NAMA_BELAKANG = tk.StringVar()
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, pady=10, expand=True, fill="x")

# 5. Tombol
def tombol_klik():
    pesan = f"Selamat Datang, {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} !"
    showinfo(title="Alert", message=pesan)

tombol = ttk.Button(input_frame, text="Klik!", command=tombol_klik)
tombol.pack(fill="x", expand=True, padx=10, pady=10)

window.mainloop()