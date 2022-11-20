# Mengimport modul yang akan digunakan
import turtle
from random import randint
from tkinter import messagebox as m

# Pengaturan awal turtle
turtle.screensize(1080, 800, "GREEN")
turtle.title("Candi Warna-Warni")
turtle.speed(0)
turtle.colormode(255)
turtle.penup()
turtle.tracer(False)

# Menerima dan melakukan validasi input dari pengguna
while True:
    jumlah_bata_lapisan_bawah = turtle.numinput("Input", "Masukkan jumlah batu bata untuk lapisan paling bawah: ")
    if jumlah_bata_lapisan_bawah != jumlah_bata_lapisan_bawah // 1:
        m.showwarning("Input invalid", "Input tidak setara terhadap nilai suatu bilangan bulat. Mohon coba lagi.")
    else:
        if jumlah_bata_lapisan_bawah < 1:
            m.showwarning("Terlalu kecil", "Nilai terkecil yang dibolehkan adalah 1. Mohon coba lagi.")
        elif jumlah_bata_lapisan_bawah > 25:
            m.showwarning("Terlalu besar", "Nilai terbesar yang dibolehkan adalah 25. Mohon coba lagi.")
        else:
            break
while True:
    jumlah_bata_lapisan_atas = turtle.numinput("Input", "Masukkan jumlah batu bata untuk lapisan paling atas: ")
    if jumlah_bata_lapisan_atas != jumlah_bata_lapisan_atas // 1:
        m.showwarning("Input invalid", "Input tidak setara terhadap nilai suatu bilangan bulat. Mohon coba lagi.")
    else:
        if jumlah_bata_lapisan_atas < 1:
            m.showwarning("Terlalu kecil", "Nilai terkecil yang dibolehkan adalah 1. Mohon coba lagi.")
        elif jumlah_bata_lapisan_atas > jumlah_bata_lapisan_bawah:
            m.showwarning("Terlalu besar", f"Nilai terbesar yang dibolehkan adalah {int(jumlah_bata_lapisan_bawah)}. Mohon coba lagi.")
        else:
            break
while True:
    panjang_bata = turtle.numinput("Input", "Masukkan panjang satu buah batu bata (dalam piksel): ")
    if panjang_bata != panjang_bata // 1:
        m.showwarning("Input invalid", "Input tidak setara terhadap nilai suatu bilangan bulat. Mohon coba lagi.")
    else:
        if panjang_bata < 2:
            m.showwarning("Terlalu kecil", "Nilai terkecil yang dibolehkan adalah 2. Mohon coba lagi.")
        elif panjang_bata > 35:
            m.showwarning("Terlalu besar", "Nilai terbesar yang dibolehkan adalah 35. Mohon coba lagi.")
        else:
            break
while True:
    lebar_bata = turtle.numinput("Input", "Masukkan lebar satu buah batu bata (dalam piksel): ")
    if lebar_bata != lebar_bata // 1:
        m.showwarning("Input invalid", "Input tidak setara terhadap nilai suatu bilangan bulat. Mohon coba lagi.")
    else:
        if lebar_bata < 2:
            m.showwarning("Terlalu kecil", "Nilai terkecil yang dibolehkan adalah 2. Mohon coba lagi.")
        elif lebar_bata > 25:
            m.showwarning("Terlalu besar", "Nilai terbesar yang dibolehkan adalah 25. Mohon coba lagi.")
        else:
            break

# Mengatur posisi untuk memulai menggambar candi (batu bata paling kiri)
jumlah_lapisan = int(jumlah_bata_lapisan_bawah - jumlah_bata_lapisan_atas + 1)
koordinat_x = -(jumlah_bata_lapisan_bawah * panjang_bata / 2)
koordinat_y = -(jumlah_lapisan * lebar_bata / 2)
turtle.goto(koordinat_x, koordinat_y)

# Inisialisasi untuk menghitung total batu bata yang digunakan
total_bata = 0

# Menggambar candi
for lapisan in range(jumlah_lapisan):
    jumlah_bata_suatu_lapisan = int(jumlah_bata_lapisan_bawah - lapisan)
    for bata in range(jumlah_bata_suatu_lapisan):
        # Menentukan warna batu bata
        if (
            bata == 0 # Batu bata berada di paling kiri pada suatu lapisan
            or bata == jumlah_bata_suatu_lapisan - 1 # Batu bata berada di paling kanan pada suatu lapisan
            or lapisan == 0 # Batu bata berada pada lapisan paling bawah
            or lapisan == jumlah_lapisan - 1 # Batu bata berada pada lapisan paling atas
        ):
            turtle.color("BLACK", "#BC4A3C")
        else:
            # Memastikan warna batu bata yang berdada di tengah berbeda dengan warna batu bata biasa
            while True:
                merah = randint(0, 255)
                hijau = randint(0, 255)
                biru = randint(0, 255)
                if merah != 188 or hijau != 74 or biru != 60:
                    break
            turtle.color("BLACK", (merah, hijau, biru))
        # Menggambar batu bata dan menghitung total batu bata
        turtle.pendown()
        turtle.begin_fill()
        turtle.forward(panjang_bata)
        turtle.left(90)
        turtle.forward(lebar_bata)
        turtle.left(90)
        turtle.forward(panjang_bata)
        turtle.left(90)
        turtle.forward(lebar_bata)
        turtle.left(90)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(koordinat_x + panjang_bata * (bata + 1), koordinat_y)
        total_bata += 1
    # Mengatur posisi untuk menggambar lapisan berikutnya
    koordinat_x += panjang_bata / 2
    koordinat_y += lebar_bata
    turtle.goto(koordinat_x, koordinat_y)

# Menyembunyikan ikon dan mencetak total batu bata yang digunakan
turtle.hideturtle()
turtle.goto(0, -(jumlah_lapisan * lebar_bata / 2 + 35))
if jumlah_lapisan <= 2: # Candi hanya menggunakan satu warna batu bata
    turtle.write(f"Candi dengan {total_bata} batu bata", align="center", font=(12))
else: # Candi menggunakan batu bata berwarna warni
    turtle.write(f"Candi warna-warni dengan {total_bata} batu bata", align="center", font=(12))
turtle.exitonclick()
