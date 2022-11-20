from datetime import datetime

def cetak_daftar_menu():
    """ Mencetak daftar menu sesuai format soal. """
    print("\nBerikut ini adalah menu yang kami sediakan:")
    for jenis_menu in menu:
        print(jenis_menu + ":")
        info_menu = [value for value in menu[jenis_menu].values()]
        for i in range(len(info_menu[0])):
            kode_menu, nama_menu, harga = tuple([info_menu[j][i] for j in range(len(info_menu))])
            print(f"{kode_menu} {nama_menu},", f"Rp{int(harga):,}".replace(",", "."))

def hitung_dan_cetak_pesanan(daftar_pesanan):
    """ Mencetak daftar pesanan dan menghitung total harganya. """
    total_harga_pesanan = 0
    for pesanan in list(dict.fromkeys(daftar_pesanan)):
        jumlah_pesanan = daftar_pesanan.count(pesanan)
        harga = int(list_harga_menu[list_nama_menu.index(pesanan)]) * jumlah_pesanan
        total_harga_pesanan += harga
        print(f"{pesanan} {jumlah_pesanan} buah,", f"Total Rp{harga:,}".replace(",", "."))
    return f"Rp{total_harga_pesanan:,}".replace(",", ".")

def buat_pesanan():
    """ Meminta input nama pelanggan dan menu yang ingin dipesan serta 
    mencetak ringkasan pesanan dan memberikan nomor meja"""
    # Meminta input nama dan pesanan
    nama = input("Siapa nama Anda? ").strip()
    cetak_daftar_menu()
    pesanan = input("\nMasukkan menu yang ingin Anda pesan: ").strip()
    if pesanan == "SELESAI":
        print("Anda tidak memesan apapun. Pesanan dibatalkan.")
        return True
    daftar_pesanan = []
    while pesanan != "SELESAI":
        if pesanan in list_nama_menu:
            daftar_pesanan.append(pesanan)
            print(f"Berhasil memesan {pesanan}.", end=" ")
        elif pesanan in list_kode_menu:
            pesanan = list_nama_menu[list_kode_menu.index(pesanan)]
            daftar_pesanan.append(pesanan)
            print(f"Berhasil memesan {pesanan}.", end=" ")
        else:
            print(f"Menu {pesanan} tidak ditemukan.", end=" ")
        pesanan = input("Masukkan menu yang ingin Anda pesan: ").strip()
    # Menentukan nomor meja
    for nmr in range(1, 11):
        if nmr not in meja:
            meja[nmr] = {"nama": nama, "pesanan": daftar_pesanan}
            break
    # Mencetak ringkasan pesanan dan memberikan nomor meja
    print("\nBerikut adalah pesanan Anda:")
    total_harga = hitung_dan_cetak_pesanan(daftar_pesanan)
    print(f"\nTotal Pesanan: {total_harga}")
    print(f"Pesanan akan kami proses. Anda bisa menggunakan meja nomor {nmr}. Terima kasih.")

def ubah_pesanan():
    """ Meminta input nomor meja, mencetak daftar menu dan daftar pesanan,
    melakukan pengubahan pesanan, serta mencetak ringkasan pesanan terbaru"""
    # Meminta input nomor meja dan memvalidasi inputnya
    try:
        nomor_meja = int(input("Nomor meja berapa? ").strip())
        assert nomor_meja in meja
    except:
        print("Nomor meja kosong atau tidak sesuai!")
        return True
    # Mencetak daftar menu dan daftar pesanan
    cetak_daftar_menu()
    print("\nBerikut adalah pesanan Anda:")
    hitung_dan_cetak_pesanan(meja[nomor_meja]["pesanan"])
    # Melakukan pengubahan pesanan
    to_do = input("\nApakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ").strip()
    if to_do == "SELESAI":
        print("Tidak jadi mengubah pesanan.")
        return True
    while to_do != "SELESAI":
        try:
            if to_do == "GANTI JUMLAH":
                yang_diganti = input("Menu apa yang ingin Anda ganti jumlahnya: ").strip()
                if yang_diganti in list_kode_menu:  # Jika memasukkan kode menu
                    yang_diganti = list_nama_menu[list_kode_menu.index(yang_diganti)]
                if yang_diganti in meja[nomor_meja]["pesanan"]:  # Jika memasukkan nama menu
                    jumlah_baru = int(input("Masukkan jumlah pesanan yang baru: ").strip())
                    assert jumlah_baru > 0  # Memastikan jumlahnya bilangan positif
                    while yang_diganti in meja[nomor_meja]["pesanan"]:
                        meja[nomor_meja]["pesanan"].remove(yang_diganti)
                    for _ in range(jumlah_baru):  # Mengganti jumlah menu
                        meja[nomor_meja]["pesanan"].append(yang_diganti)
                    print(f"Berhasil mengubah pesanan {yang_diganti} {jumlah_baru} buah.", end=" ")
                elif yang_diganti not in list_kode_menu and yang_diganti not in list_nama_menu:
                    print(f"Menu {yang_diganti} tidak ditemukan.", end=" ")
                else:
                    print(f"Menu {yang_diganti} tidak Anda pesan sebelumnya.", end=" ")
            elif to_do == "HAPUS":
                yang_dihapus = input("Menu apa yang ingin Anda hapus dari pesanan: ").strip()
                if yang_dihapus in list_kode_menu:  # Jika memasukkan kode menu
                    yang_dihapus = list_nama_menu[list_kode_menu.index(yang_dihapus)]
                if yang_dihapus in meja[nomor_meja]["pesanan"]:  # Jika memasukkan nama menu
                    jumlah_pesanan_sebelumnya = meja[nomor_meja]["pesanan"].count(yang_dihapus)
                    while yang_dihapus in meja[nomor_meja]["pesanan"]:
                        meja[nomor_meja]["pesanan"].remove(yang_dihapus)  # Menghapus menu yang dipilih
                    print(f"{jumlah_pesanan_sebelumnya} buah {yang_dihapus} dihapus dari pesanan.", end=" ")
                elif yang_dihapus not in list_kode_menu and yang_dihapus not in list_nama_menu:
                    print(f"Menu {yang_dihapus} tidak ditemukan.", end=" ")
                else:
                    print(f"Menu {yang_dihapus} tidak Anda pesan sebelumnya.", end=" ")
            elif to_do == "TAMBAH PESANAN":
                yang_ditambah = input("Menu apa yang ingin anda pesan? ").strip()
                if yang_ditambah in list_kode_menu:  # Jika memasukkan kode menu
                    yang_ditambah = list_nama_menu[list_kode_menu.index(yang_ditambah)]
                if yang_ditambah not in list_kode_menu and yang_ditambah not in list_nama_menu:
                    print(f"Menu {yang_ditambah} tidak ditemukan.", end=" ")
                else:
                    meja[nomor_meja]["pesanan"].append(yang_ditambah)  # Menambahkan menu yang dipilih
                    print(f"Berhasil memesan {yang_ditambah}.", end=" ")
        except:
            print("Jumlah harus bilangan positif!", end=" ")
        to_do = input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ").strip()
    # Mencetak ringkasan pesanan terbaru
    print("\nBerikut adalah pesanan terbaru Anda:")
    total_harga = hitung_dan_cetak_pesanan(meja[nomor_meja]["pesanan"])
    print(f"\nTotal Pesanan: {total_harga}")

def selesai_menggunakan_meja():
    """ Membuat resi jika ada pesanan dan menjadikan mejanya tersedia kembali. """
    # Meminta input nomor meja dan memvalidasi inputnya
    try:
        nomor_meja = int(input("Nomor meja berapa? ").strip())
        assert nomor_meja in meja
    except:
        print("Nomor meja kosong atau tidak sesuai!")
        return True
    # Mencetak pesan selesai menggunakan meja
    nama_pembeli = meja[nomor_meja]["nama"]
    print(f"Pelanggan atas nama {nama_pembeli} selesai menggunakan meja {nomor_meja}.")
    # Jika tidak ada pesanan
    if len(meja[nomor_meja]["pesanan"]) == 0:
        meja.pop(nomor_meja)
        return True
    # Jika ada pesanan
    waktu_selesai = datetime.now().strftime("%H.%M.%S")
    with open(f"receipt_{nama_pembeli}_{waktu_selesai}.txt", "w+") as receipt:
        total_harga_keseluruhan = 0
        for nama_menu in list(dict.fromkeys(meja[nomor_meja]["pesanan"])):
            kode_menu = list_kode_menu[list_nama_menu.index(nama_menu)]
            jumlah_pesanan = meja[nomor_meja]["pesanan"].count(nama_menu)
            harga_satuan = int(list_harga_menu[list_nama_menu.index(nama_menu)])
            total_harga = harga_satuan * jumlah_pesanan
            total_harga_keseluruhan += total_harga
            receipt.write(f"{kode_menu};{nama_menu};{jumlah_pesanan};{harga_satuan};{total_harga}\n")
        receipt.write(f"\nTotal {total_harga_keseluruhan}")
    meja.pop(nomor_meja)

try:
    with open("menu.txt") as file_menu:
        menu = {}  # Membuat dictionary untuk menu berdasarkan jenisnya
        for baris in file_menu:
            if "===" in baris[:3]:
                jenis_menu = baris[3:].strip()
                if jenis_menu not in menu:
                    menu[jenis_menu] = {"kode_menu": [], "nama_menu": [], "harga": []}
            else:
                assert baris.count(";") == 2  # Memastikan ada 2 karakter pemisah info suatu menu
                kode_menu, nama_menu, harga = baris.strip().split(";")
                # Memastikan ada info menu dan sesuai ketentuan
                assert "." not in harga
                assert int(harga) >= 0
                assert len(kode_menu) != 0 and len(nama_menu) != 0
                # Memasukkan tiap info menu ke dalam list pada dictionary
                menu[jenis_menu]["kode_menu"].append(kode_menu)
                menu[jenis_menu]["nama_menu"].append(nama_menu)
                menu[jenis_menu]["harga"].append(harga)
        # Membuat list untuk setiap info menu tanpa memperhatikan jenisnya
        list_kode_menu = []
        list_nama_menu = []
        list_harga_menu = []
        for jenis_menu, info_menu in menu.items():
            list_kode_menu += info_menu["kode_menu"]
            list_nama_menu += info_menu["nama_menu"]
            list_harga_menu += info_menu["harga"]
        # Memastikan kode menu dan nama menu bersifat unik
        assert len(list_kode_menu) == len(set(list_kode_menu))
        assert len(list_nama_menu) == len(set(list_nama_menu))
        assert (set(list_kode_menu) & set(list_nama_menu)) == set()
    
    meja = {}
    while True:
        print("Selamat datang di Kafe Daun Daun Pacilkom")
        fitur_pos = input("Apa yang ingin Anda lakukan? ").strip()
        if fitur_pos == "BUAT PESANAN":
            if len(meja) < 10:
                buat_pesanan()
            else:
                print("Mohon maaf meja sudah penuh, silakan kembali lagi nanti.")
        elif fitur_pos == "UBAH PESANAN":
            if ubah_pesanan():
                pass
        elif fitur_pos == "SELESAI MENGGUNAKAN MEJA":
            if selesai_menggunakan_meja():
                pass
        print("\n---")

except: # Jika menu.txt tidak sesuai format
    print("Daftar menu tidak valid, cek kembali menu.txt!")
