"""
TUGAS PEMROGRAMAN 4         
Kafe Daun-Daun Pacilkom v2.0 🌿  
                                 
Fahmi Ramadhan - 2206026473     
"""


import tkinter as tk
import tkinter.messagebox as tkmsg
import tkinter.ttk as ttk
import random


class Menu:
    def __init__(self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = int(harga)


class Meals(Menu):
    def __init__(self, kode, nama, harga, kegurihan):
        super().__init__(kode, nama, harga)
        self.kegurihan = kegurihan


class Drinks(Menu):
    def __init__(self, kode, nama, harga, kemanisan):
        super().__init__(kode, nama, harga)
        self.kemanisan = kemanisan


class Sides(Menu):
    def __init__(self, kode, nama, harga, keviralan):
        super().__init__(kode, nama, harga)
        self.keviralan = keviralan


class Main(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.minsize(400, 200)
        self.pack(expand=True)
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        # Membuat widgets
        tk.Button(self, text="Buat Pesanan", width=30, bg="#4472C4", fg="white",
                  command=self.buat_pesanan).grid(row=0, column=0, padx=10, pady=20)
        tk.Button(self, text="Selesai Gunakan Meja", width=30, bg="#4472C4", fg="white",
                  command=self.selesai_gunakan_meja).grid(row=1, column=0, padx=10, pady=20)
    
    def buat_pesanan(self):
        self.master.state(newstate="iconic")  # Minimize main window
        BuatPesanan(self.master)  # Membuka window buat pesanan

    def selesai_gunakan_meja(self):
        self.master.state(newstate="iconic")  # Minimize main window
        SelesaiGunakanMeja(self.master)  # Membuka window selesai menggunakan meja


class BuatPesanan(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.minsize(400, 200)

        # Membuat container untuk widgets
        self.frame_buat_pesanan = tk.Frame(self)
        self.frame_buat_pesanan.pack(expand=True)

        # Membuat widgets
        self.lbl_nama = tk.Label(self.frame_buat_pesanan, text="Siapa Nama Anda?")
        self.ent_nama = tk.Entry(self.frame_buat_pesanan)
        self.btn_kembali = tk.Button(self.frame_buat_pesanan, text="Kembali", width=20, bg="#4472C4", fg="white",
                                    # Kembali ke main window ketika diklik
                                    command=lambda:[self.destroy(), self.master.state(newstate="normal")])
        self.btn_lanjut = tk.Button(self.frame_buat_pesanan, text="Lanjut", width=20, bg="#4472C4", fg="white",
                                    command=self.cek_ketersediaan_meja)
        
        # Mengatur layout widgets
        self.lbl_nama.grid(row=0, column=0, padx=(40,5), pady=(40,0))
        self.ent_nama.grid(row=0, column=1, padx=(5,40), pady=(40,0))
        self.btn_kembali.grid(row=1, column=0, padx=(40,5), pady=(70,0))
        self.btn_lanjut.grid(row=1, column=1, padx=(5,40), pady=(70,0))
    
    def cek_ketersediaan_meja(self):
        if len(dict_meja) == 10:
            tkmsg.showwarning("Meja Penuh!", "Mohon maaf, meja sedang penuh. \
                Silakan datang kembali di lain kesempatan.")
            self.destroy()  # Menutup window buat pesanan
            self.master.state(newstate="normal")  # Unminimize main window
        else:
            while True:
                nmr = random.randint(0,9)  # Memberikan nomor meja secara acak
                if nmr not in dict_meja:
                    self.nmr = nmr
                    break
            self.cek_nama()
    
    def cek_nama(self):
        self.nama = self.ent_nama.get()
        if self.nama == "":
            tkmsg.showwarning("Nama Harus Diisi!", "Anda belum memasukkan nama.")
        else:
            lanjut = True
            # Mengecek kesamaan nama dengan nama yang sudah ada di meja
            for meja in dict_meja.values():
                if self.nama == meja["nama"]:
                    lanjut = False
                    break
            if lanjut:
                self.state(newstate="iconic")  # Menutup window buat pesanan
                self.pilih_pesanan()  # Membuka window pilih pesanan
            else:
                tkmsg.showwarning("Nama Harus Unik!", f"Sudah ada pembeli dengan nama {self.nama}. \
                    Masukkan nama yang berbeda.")

    def pilih_pesanan(self):
        self.window_pilih_pesanan = tk.Toplevel(self)

        # Container untuk widget nama, nomor meja, dan tombol ubah meja
        self.top_frame = tk.Frame(self.window_pilih_pesanan)
        self.top_frame.pack(padx=30)
        
        # Membuat widgets
        self.lbl_nama = tk.Label(self.top_frame, text=f"Nama pemesan: {self.nama}")
        self.lbl_nmr_meja = tk.Label(self.top_frame, text=f"No Meja: {self.nmr}")
        self.btn_ubah_nmr_meja = tk.Button(self.top_frame, text="Ubah", bg="#4472C4", fg="white",
                                            # Membuka window ubah nomor meja dan
                                            # minimize window pilih pesanan ketika diklik
                                            command=lambda:[self.ubah_nomor_meja(), 
                                            self.window_pilih_pesanan.state(newstate="iconic")])

        # Mengatur layout widgets
        self.lbl_nama.grid(row=0, column=0, columnspan=3, pady=(0,20), sticky="w")
        self.lbl_nmr_meja.grid(row=0, column=3, pady=(0,20), sticky="e")
        self.btn_ubah_nmr_meja.grid(row=0, column=4, pady=(0,20), sticky="w")
    
        # Membuat Tabel daftar menu
        self.row_lbl_jenis = 1  # Inisialisai variabel untuk posisi row setiap label jenis menu
        self.list_of_opsi_jumlah = []  # Inisialisai variabel list untuk diisi dengan combobox opsi jumlah
        for jenis_menu in menu:
            tk.Label(self.top_frame, text=f"{jenis_menu}").grid(row=self.row_lbl_jenis, column=0)
            # Membuat tabel menu untuk suatu jenis menu
            for i in range(len(menu[jenis_menu])):
                for j in range(4):
                    entry = tk.Entry(self.top_frame, width=20)
                    entry.grid(row = i + self.row_lbl_jenis + 2, column = j)
                    if i == 0:  # Menu pertama pada suatu jenis menu
                        header = tk.Entry(self.top_frame, width=20)
                        header.grid(row = i + self.row_lbl_jenis + 1, column = j)
                        # Memasukkan header dengan nama atribut suatu objek menu
                        header.insert(tk.END, list(menu[jenis_menu][i].__dict__.keys())[j].title())
                        # Memasukkan info menu dengan value dari atribut suatu objek menu
                        entry.insert(tk.END, list(menu[jenis_menu][i].__dict__.values())[j])
                    else:
                        # Memasukkan info menu dengan value dari atribut suatu objek menu
                        entry.insert(tk.END, list(menu[jenis_menu][i].__dict__.values())[j])
                    # Mengubah state header dan entry menjadi tidak bisa diubah
                    header["state"] = "readonly"
                    entry["state"] = "readonly"
                # Membuat header jumlah
                header_jumlah = tk.Entry(self.top_frame, width=20)
                header_jumlah.grid(row = self.row_lbl_jenis + 1, column = 4)
                header_jumlah.insert(tk.END, "Jumlah")
                header_jumlah["state"] = "readonly"
                # Membuat combobox untuk opsi jumlah
                values = tuple([k for k in range(10)])
                self.opsi_jumlah = ttk.Combobox(self.top_frame, values = values)
                self.opsi_jumlah.set(0)
                self.opsi_jumlah.grid(row = i + self.row_lbl_jenis + 2, column = 4)
                self.opsi_jumlah.bind("<<ComboboxSelected>>", self.hitung_harga)
                self.list_of_opsi_jumlah.append(self.opsi_jumlah)
            # Mengupdate row_lbl_jenis untuk posisi row jenis berikutnya
            self.row_lbl_jenis += len(menu[jenis_menu]) + 2
        
        # Membuat label total harga
        self.lbl_total_harga = tk.Label(self.top_frame, text=f"Total harga: 0", font="Helvetica 10 bold")
        self.lbl_total_harga.grid(row = self.row_lbl_jenis, column = 4, sticky="w")
        
        # Membuat widget tombol kembali dan tombol OK dalam container baru
        self.bottom_frame = tk.Frame(self.window_pilih_pesanan)
        self.bottom_frame.pack(pady=(60,15))
        tk.Button(self.bottom_frame, text="Kembali", width=20, 
                # Menutup window pilih pesanan dan membuka window buat pesanan ketika diklik
                command=lambda:[self.window_pilih_pesanan.destroy(),self.state(newstate="normal")],
                bg="#4472C4", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(self.bottom_frame, text="OK", width=20, command=self.confirm_pesanan,
                bg="#4472C4", fg="white").grid(row=0, column=1, padx=5)

    def hitung_harga(self, event):
        self.total_harga = 0
        # Iterasi untuk mendapatkan value dari setiap combobox opsi jumlah untuk menghitung total harga
        for i, opsi_jumlah in enumerate(self.list_of_opsi_jumlah):
            self.total_harga += int(opsi_jumlah.get()) * int(list_harga_menu[i])
        # Mengupdate label total harga dengan total harga yang baru
        self.lbl_total_harga.configure(text=f"Total harga: {self.total_harga}")

    def ubah_nomor_meja(self):
        self.window_ubah_nomor_meja = tk.Toplevel(self.window_pilih_pesanan)

        self.nmr_temp = self.nmr  # Nomor meja sementara untuk diubah ubah

        self.lbl_command = tk.Label(self.window_ubah_nomor_meja, text="Silakan klik meja kosong yang diinginkan:")
        self.lbl_command.pack(pady=10, padx=70)

        self.generate_gui_meja()

        tk.Label(self.window_ubah_nomor_meja, text="Info", font="Helvetica 10 bold").pack()
        tk.Label(self.window_ubah_nomor_meja, text="Merah: Terisi").pack()
        tk.Label(self.window_ubah_nomor_meja, text="Abu-abu: Kosong").pack()
        tk.Label(self.window_ubah_nomor_meja, text="Biru: Meja Anda").pack()

        # Membuat widget tombol kembali dan tombol OK dalam container baru
        self.navigation_frame = tk.Frame(self.window_ubah_nomor_meja)
        self.navigation_frame.pack(pady=(20,30))
        tk.Button(self.navigation_frame, text="Kembali", width=20, bg="#4472C4", fg="white",
                # Menutup window ubah nomor meja dan membuka window pilih pesanan ketika diklik
                command=lambda:[self.window_ubah_nomor_meja.destroy(), 
                self.window_pilih_pesanan.state(newstate="normal")]).grid(row=0, column=0, padx=(10,5))
        tk.Button(self.navigation_frame, text="OK", width=20, 
                command=self.confirm_ganti_meja, bg="#4472C4", fg="white").grid(row=0, column=1, padx=(5,10))
    
    def generate_gui_meja(self):
        # Container untuk meja
        self.frame_meja = tk.Frame(self.window_ubah_nomor_meja)
        self.frame_meja.pack(pady=(0,15))

        i = 0  # Inisialisasi variabel untuk teks pada meja
        self.list_meja = []  # Inisialisai variabel list untuk diisi dengan button meja
        
        # Iterasi untuk membuat meja
        for col in range(2):
            for row in range(5):
                if i in dict_meja:
                    meja = tk.Button(self.frame_meja, text=f"{i}", width=10, bg="red", fg="white")
                elif i == self.nmr:
                    meja = tk.Button(self.frame_meja, text=f"{i}", width=10, bg="#4472C4", fg="white",
                                    command=lambda i=i: self.ganti_meja(i))
                else:
                    meja = tk.Button(self.frame_meja, text=f"{i}", width=10, bg="#a6a6a6", fg="white",
                                    command=lambda i=i: self.ganti_meja(i))
                meja.grid(row=row+1, column=col, padx=5, pady=5)
                self.list_meja.append(meja)
                i += 1
    
    def ganti_meja(self, nmr_meja_baru):
        self.list_meja[nmr_meja_baru].configure(bg="#4472C4")  # Mengubah warna meja yang diklik menjadi biru
        self.list_meja[self.nmr_temp].configure(bg="#a6a6a6")  # Mengubah warna meja sebelumnya menjadi abu-abu
        self.nmr_temp = nmr_meja_baru
    
    def confirm_ganti_meja(self):
        # Mengubah nomor meja yang ditempati dengan nomor meja baru yang dipilih
        self.nmr = self.nmr_temp  
        self.lbl_nmr_meja.configure(text=f"No Meja: {self.nmr}")
        # Menutup window ubah nomor meja dan membuka window pilih pesanan
        self.window_ubah_nomor_meja.destroy()
        self.window_pilih_pesanan.state(newstate="normal")
    
    def confirm_pesanan(self):
        self.daftar_pesanan = []
        # Iterasi untuk mendapatkan value dari setiap combobox opsi jumlah
        for i, opsi_jumlah in enumerate(self.list_of_opsi_jumlah):
            if int(opsi_jumlah.get()) != 0:
                # Mengisi list daftar pesanan dengan tuple berupa index pesanan dan jumlahnya
                self.daftar_pesanan.append((i, opsi_jumlah.get()))
        if len(self.daftar_pesanan) != 0:
            # Memasukkan info pemesan dan pesanannya ke dictionary meja
            dict_meja[self.nmr] = {"nama": self.nama, "pesanan": self.daftar_pesanan, "harga": self.total_harga}
            # Menutup window buat pesanan dan membuka main window
            self.destroy()
            self.master.state(newstate="normal")
        else:
            tkmsg.showwarning("Pesanan Kosong!", f"Anda belum memesan apapun.")


class SelesaiGunakanMeja(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.minsize(370, 400)

        self.lbl_command = tk.Label(self, text="Silakan klik meja yang selesai digunakan:")
        self.lbl_command.pack(pady=10, padx=50)

        self.generate_gui_meja()

        tk.Label(self, text="Info", font="Helvetica 10 bold").pack()
        tk.Label(self, text="Merah: Terisi").pack()
        tk.Label(self, text="Abu-abu: Kosong").pack()

        tk.Button(self, text="Kembali", width=20,
                # Menutup window selesai menggunakan meja dan membuka main window ketika diklik
                command=lambda:[self.destroy(),self.master.state(newstate="normal")],
                bg="#4472C4", fg="white").pack(pady=(20,30))
    
    def generate_gui_meja(self):
        # Container untuk meja
        self.frame_meja = tk.Frame(self)
        self.frame_meja.pack(pady=(0,15))

        i = 0  # Inisialisasi variabel untuk teks pada meja
        self.list_meja = []  # Inisialisai variabel list untuk diisi dengan button meja

        # Iterasi untuk membuat meja
        for col in range(2):
            for row in range(5):
                if i in dict_meja:
                    meja = tk.Button(self.frame_meja, text=f"{i}", width=10, bg="red", fg="white",
                                    # Membuka window ringkasan dan minimize window selesai gunakan meja ketika diklik
                                    command=lambda i=i: [self.popup_ringkasan(i), self.state(newstate="iconic")])
                else:
                    meja = tk.Button(self.frame_meja, text=f"{i}", width=10, bg="#a6a6a6", fg="white")
                meja.grid(row=row+1, column=col, padx=5, pady=5)
                self.list_meja.append(meja)
                i += 1
            
    def popup_ringkasan(self, nmr_meja):
        self.window_ringkasan = tk.Toplevel(self)

        self.nmr_meja = nmr_meja
        self.nama = dict_meja[self.nmr_meja]["nama"]

        # Container untuk widget nama dan nomor meja
        self.top_frame = tk.Frame(self.window_ringkasan)
        self.top_frame.pack(padx=30)

        # Membuat widgets
        self.lbl_nama = tk.Label(self.top_frame, text=f"Nama pemesan: {self.nama}")
        self.lbl_nama.grid(row=0, column=0, columnspan=3, pady=(0,20), sticky="w")
        self.lbl_nmr_meja = tk.Label(self.top_frame, text=f"No Meja: {self.nmr_meja}")
        self.lbl_nmr_meja.grid(row=0, column=3, pady=(0,20), sticky="e")
    
        # Membuat tabel daftar menu
        self.row_lbl_jenis = 1  # Inisialisai variabel untuk posisi row setiap label jenis menu
        self.list_of_entry_jumlah = []  # Inisialisai variabel list untuk diisi dengan entry jumlah
        for jenis_menu in menu:
            tk.Label(self.top_frame, text=f"{jenis_menu}").grid(row=self.row_lbl_jenis, column=0)
            # Membuat tabel menu untuk suatu jenis menu
            for i in range(len(menu[jenis_menu])):
                for j in range(4):
                    entry = tk.Entry(self.top_frame, width=20)
                    entry.grid(row = i + self.row_lbl_jenis + 2, column = j)
                    if i == 0:  # Menu pertama pada suatu jenis menu
                        header = tk.Entry(self.top_frame, width=20)
                        header.grid(row = i + self.row_lbl_jenis + 1, column = j)
                        # Memasukkan header dengan nama atribut suatu objek menu
                        header.insert(tk.END, list(menu[jenis_menu][i].__dict__.keys())[j].title())
                        # Memasukkan info menu dengan value dari atribut suatu objek menu
                        entry.insert(tk.END, list(menu[jenis_menu][i].__dict__.values())[j])
                    else:
                        # Memasukkan info menu dengan value dari atribut suatu objek menu
                        entry.insert(tk.END, list(menu[jenis_menu][i].__dict__.values())[j])
                    # Mengubah state header dan entry menjadi tidak bisa diubah
                    header["state"] = "readonly"
                    entry["state"] = "readonly"
                # Membuat header jumlah
                header_jumlah = tk.Entry(self.top_frame, width=20)
                header_jumlah.grid(row = self.row_lbl_jenis + 1, column = 4)
                header_jumlah.insert(tk.END, "Jumlah")
                header_jumlah["state"] = "readonly"
                # Membuat entry box untuk jumlah menu
                self.entry_jumlah = tk.Entry(self.top_frame, width=20)
                self.entry_jumlah.grid(row = i + self.row_lbl_jenis + 2, column = 4)
                self.list_of_entry_jumlah.append(self.entry_jumlah)
            # Mengupdate row_lbl_jenis untuk posisi row jenis berikutnya
            self.row_lbl_jenis += len(menu[jenis_menu]) + 2

        # Membuat list yang berisi index-index pesanan yang dipesan
        daftar_index_pesanan = [pesanan[0] for pesanan in dict_meja[self.nmr_meja]["pesanan"]]
        # Iterasi untuk mengisi entry_jumlah dengan jumlah pesanan yang dipesan
        for idx_pesanan, entry_jumlah in enumerate(self.list_of_entry_jumlah):
            if idx_pesanan in daftar_index_pesanan:
                jumlah = dict_meja[self.nmr_meja]["pesanan"][daftar_index_pesanan.index(idx_pesanan)][1]
                entry_jumlah.insert(tk.END, f"{jumlah}")
            else:
                entry_jumlah.insert(tk.END, "0")
            entry_jumlah["state"] = "readonly"
        
        # Membuat label total harga
        self.total_harga = dict_meja[nmr_meja]["harga"]
        self.lbl_total_harga = tk.Label(self.top_frame, text=f"Total harga: {self.total_harga}",
                                        font="Helvetica 10 bold")
        self.lbl_total_harga.grid(row = self.row_lbl_jenis, column = 4, sticky="w")
        
        # Membuat widget tombol kembali dan tombol OK dalam container baru
        self.bottom_frame = tk.Frame(self.window_ringkasan)
        self.bottom_frame.pack(pady=(60,15))
        tk.Button(self.bottom_frame, text="Kembali", width=20,
                # Menutup window ringkasan dan membuka window selesai menggunakan meja ketika diklik
                command=lambda:[self.window_ringkasan.destroy(),self.state(newstate="normal")],
                bg="#4472C4", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(self.bottom_frame, text="Selesai Gunakan Meja", width=20, command=self.confirm_selesai,
                bg="#4472C4", fg="white").grid(row=0, column=1, padx=5)
    
    def confirm_selesai(self):
        # Membuat meja yang dipilih untuk selesai menjadi tersedia kembali
        self.list_meja[self.nmr_meja].configure(bg="#a6a6a6")
        dict_meja.pop(self.nmr_meja)
        # Menutup window ringkasan dan kembali ke window selesai menggukanan meja
        self.destroy()
        SelesaiGunakanMeja()


def main():
    # Inisialisasi variabel global agar bisa diakses pada semua class
    global menu, dict_meja, list_harga_menu
    menu = {"MEALS": [], "DRINKS": [], "SIDES": []}
    dict_meja = {}
    list_harga_menu = []
    # Inisialisasi variabel untuk mengecek keunikan nama dan kode menu
    list_nama_menu = []
    list_kode_menu = []

    # Mengolah file menu.txt
    try:
        with open("menu.txt") as file_menu:
            assert len(file_menu.readlines()) != 0  # Memastikan menu.txt ada isinya
        with open("menu.txt") as file_menu:
            for baris in file_menu:
                if "===" in baris[:3]:
                    jenis_menu = baris[3:].strip()
                else:
                    assert baris.count(";") == 3  # Memastikan ada 3 karakter pemisah info suatu menu
                    kode_menu, nama_menu, harga, info_tambahan = baris.strip().split(";")
                    # Memastikan ada info menu dan sesuai ketentuan
                    assert "." not in harga
                    assert int(harga) >= 0
                    assert len(kode_menu) != 0 and len(nama_menu) != 0
                    # Memasukkan info menu ke dalam list tanpa memperhatikan jenisnya
                    list_kode_menu.append(kode_menu)
                    list_nama_menu.append(nama_menu)
                    list_harga_menu.append(harga)
                    # Membuat objek menu dan memasukkannya ke dalam list pada dict menu sesuai jenisnya
                    if jenis_menu == "MEALS":
                        menu["MEALS"].append(Meals(kode_menu, nama_menu, harga, info_tambahan))
                    elif jenis_menu == "DRINKS":
                        menu["DRINKS"].append(Drinks(kode_menu, nama_menu, harga, info_tambahan))
                    elif jenis_menu == "SIDES":
                        menu["SIDES"].append(Sides(kode_menu, nama_menu, harga, info_tambahan))
            # Memastikan kode menu dan nama menu bersifat unik
            assert len(list_kode_menu) == len(set(list_kode_menu))
            assert len(list_nama_menu) == len(set(list_nama_menu))
            assert (set(list_kode_menu) & set(list_nama_menu)) == set()
    except: # Jika menu.txt tidak sesuai format
        print("Daftar menu tidak valid, cek kembali menu.txt!")

    # Mulai membuat GUI program
    window = tk.Tk()
    Main(window)
    window.mainloop()


if __name__ == '__main__':
    main()
