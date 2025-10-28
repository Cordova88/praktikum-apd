import os
def clear():
    os.system("cls||clear")
clear()

daftar_game = {
    "Capcom" : ["Street Fighter", "Marvel vs. Capcom", "Darkstalkers", "Rival Schools", "Powerstone"],
    "Bandai Namco" : ["Tekken", "Soulcalibur", "Rise of Incarnates", "Pokken Tournament"],
    "Arc System Works" : ["Guilty Gear", "BlazBlue", "Granblue Fantasy Versus", "Hunter x Hunter: Nen x Impact", "Marvel Tokon: Fighting Souls (UPCOMING)"]
}

batas1 = "="*50
batas2 = "+"*50
user_baru = {
    "usn" : "d",
    "pw" : "d"
    }
tiket = {
    "request" : [],
    "laporan" : [],
    "kritik" : []
}

def akhir():
    clear()
    print()
    print(batas1)
    print(batas2)
    print("🥊TERIMA KASIH ATAS KUNJUNGANNYA🥊".center(45))
    print()
    print("SAMPAI JUMPA".center(45))
    print(batas2)
    print(batas1)

def user():
    global user_baru
    print(batas2)
    print("LOGIN USER".center(50))
    print(batas2)
    usn = input("\nUsername: ")
    pw = input("Password: ")
    if user_baru["usn"] == usn and user_baru["pw"] == pw:
        print()
        print(batas2)
        print("LOGIN BERHASIL".center(50))
        print(f"SELAMAT DATANG {usn}")
        print(batas2)
        print()
        input("Silahkan Tekan ENTER untuk Melanjutkan")
        tampilan_user()
    else:
        print(f"{usn} Belum terdaftar Harap Mendaftarkan Username di halama Register Terlebih dahulu!!!")
        input("\nSilahkan Tekan ENTER untuk mengulang")

def admin():
    print(batas2)
    print("LOGIN ADMIN".center(50))
    print(batas2)
    usn = input("\nUsername: ").lower()
    pw = input("Password: ").lower()
    if usn == "admin" and pw == "admin123":
        print()
        print(batas2)
        print(f"LOGIN BERHASIL, selamat datang {usn}")
        print(batas2)
        print()
        input("Silahkan Tekan ENTER")
        tampilan_admin()
    else:
        print(f"{usn} tidak terdaftar sebagai Admin !!!")
        input("\nSilahkan Tekan ENTER untuk mengulang")

def register():
        print(batas2)
        print("DAFTAR USER BARU".center(50))
        print(batas2)
        newusn = input("\nUsername: ")
        newpw = input("Password: ")
        user_baru["usn"] = newusn
        user_baru["pw"] = newpw
        print(f"\nSelamat {newusn}, anda telah terdaftar")
        input("\nHarap Tekan ENTER untuk Login")


def capcom_games(tanggal, pendiri,):
    clear()
    print("INFORMASI CAPCOM".center(50))
    print(batas1)
    print(f"Berdiri pada tanggal {tanggal}") # 30 Mei 1979
    print(f"\nPendiri Namco: {pendiri}") # Kenzo Tsujimoto
    print(f"\nGame Fighting Terbaru: {daftar_game["Capcom"][0]} 6 (2023)")
    print(batas1)
    print(batas2)
    print(f"Fighting Game Capcom".center(50))
    print()
    capgames = list(daftar_game.get("Capcom"))
    for i, games in enumerate(capgames):
        print(f"{i + 1}. {games}")
    input ("\nTekan ENTER Untuk Kembali: ")

def namco_games(tanggal1, tanggal2, pendiri):
    clear()
    print("INFORMASI BANDAI NAMCO".center(50))
    print(batas1)
    print(f"Berdiri pada tanggal {tanggal1} dengan nama Namco") # 1 Juni 1955
    print(f"\nMengganti nama nya pada {tanggal2} dengan nama Bandai Namco") # 29 September 2005
    print(f"\nPendiri: {pendiri}") # Masaya Nakamura
    print(f"\nGame Fighting Terbaru: {daftar_game["Bandai Namco"][0]} 8 (2024)")
    print(batas1)
    print(batas2)
    print(f"Fighting Game Bandai Namco".center(50))
    print()
    namcogames = list(daftar_game.get("Bandai Namco"))
    for i, games in enumerate(namcogames):
        print(f"{i + 1}. {games}")
    input ("\nTekan ENTER Untuk Kembali: ")

def arcsys_games(tanggal, pendiri):
    clear()
    print("INFORMASI ARC SYSTEM WORKS".center(50))
    print(batas1)
    print(f"Berdiri pada tanggal {tanggal}") # 12 Mei 1988
    print(f"\nPendiri: {pendiri}") # Minoru Kidooka
    print(f"\nGame Fighting Terbaru: {daftar_game["Arc System Works"][0]} -STRIVE- (2021)")
    print(batas1)
    print(batas2)
    print(f"Fighting Game Arc System Works".center(50))
    print()
    arcgames = list(daftar_game.get("Arc System Works"))
    for i, games in enumerate(arcgames):
        print(f"{i + 1}. {games}")
    input ("\nTekan ENTER Untuk Kembali: ")

def kirim_tiket():
    clear()
    print(batas1)
    print(batas2)
    print("Pengiriman Tiket".center(45))
    print()
    print("""Pilih Jenis Tiket
        1. Request
        2. Laporan
        3. Kritik & Saran""")
    print(batas2)
    print(batas1)
    pilihan = input("\nPilih Jenis Tiket Untuk Dikirim:  ")
    if pilihan == "1":
        req = input("\nMasukkan Isi pesan: ")
        tiket["request"].append(req)
    elif pilihan == "2":
        lapor = input("\nMasukkan Isi Pesan: ")
        tiket["laporan"].append(lapor)
    elif pilihan == "3":
        krisar = input("\nMasukkan Isi Pesan: ")
        tiket["kritik"].append(krisar)
    else:
        print("Pilihan Yang Anda Input Tidak Ada!!!")
        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
    print("\nTerima Kasih Atas Pesan yang anda kirim kami akan Segera Menanggapi nya")
    input("\nTekan ENTER untuk kembali")

def baca_keluhan():
    clear()
    print (batas1)
    print()
    print("Tiket Dari User".center(50))
    print()
    print(batas1)
    print(batas2)
    print(f"\nTerdapat {len(tiket["request"])} Pesan Request")
    if len(tiket["request"]) > 0:
        pesanreq = list(tiket.get("request"))
        for pesan in pesanreq:
            print(f"Pesan Dari {user_baru["usn"]}: {pesan}")
    if len(tiket["request"]) == 0:
        print("Tidak ada Pesan Request")
    print(f"\nTerdapat {len(tiket["laporan"])} Pesan Laporan")
    if len(tiket["laporan"]) > 0:
        pesanlapor = list(tiket.get("laporan"))
        for pesan in pesanlapor:
            print(f"Pesan Dari {user_baru["usn"]}: {pesan}")
    if len(tiket["laporan"]) == 0:
        print("Tidak ada Pesan Laporan")
    print(f"\nTerdapat {len(tiket["kritik"])} Pesan Kritik & Saran")
    if len(tiket["request"]) > 0:
        pesankritik = list(tiket.get("kritik"))
        for pesan in pesankritik:
            print(f"Pesan Dari {user_baru["usn"]}: {pesan}")
    if len(tiket["kritik"]) == 0:
        print("Tidak ada Pesan Request")
    input("\nTekan ENTER untuk Kembali")



def tambah_game():
    clear()
    print(batas1)
    print("PENAMAMBAHAN GAME FIGHTING BARU".center(50))
    print(batas1)
    print(batas2)
    print()         
    print("Developer Fighting Game".center(50),"\n")
    print(batas2)
    print(batas1)
    dev_list = list(daftar_game.keys())
    for i, dev in enumerate(dev_list):
        print(f"{i+1}. {dev}")
    print(batas1)
    try:
        pilihan_tambah = int(input("\nPilih Developer untuk menambah Game: ")) -1
    except ValueError:
        print("\nINVALID Input Wajib sebuah Angka")
        input("\nTekan ENTER Untuk Kembali")
    else:
        if 0 <= pilihan_tambah < len(dev_list):
            nom_dev = dev_list[pilihan_tambah]
            newcap = input("\nMasukkan Judul Game baru yang akan ditambahkan: ").upper()
            daftar_game[nom_dev].append(newcap)
            print(f"\n{newcap} Berhasil ditambahkan")
            input("\nTekan ENTER Untuk Kembali")
        else:
            print("Pilihan Yang Anda Input Tidak Ada!!!")
            input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

def edit_game():
    clear()
    print(batas1)
    print("EDIT FIGHTING GAME".center(50))
    print(batas1)
    print(batas2)
    print()         
    print("Daftar Developer Fighting Game".center(50),"\n")
    print(batas2)
    print(batas1)
    dev_list = list(daftar_game.keys())
    for i, dev in enumerate(dev_list):
        print(f"{i+1}. {dev}")
    print(batas1)
    try:
        pilihan_edit = int(input("\nPilih Developer untuk Mengedit Game nya: ")) -1
        print()
    except ValueError:
        print("\nINVALID Input Wajib sebuah Angka")
        input("\nTekan ENTER Untuk Kembali")
        return
    except UnboundLocalError:
        print("\nINVALID Input Wajib sebuah Angka")
        input("\nTekan ENTER Untuk Kembali")
        return
    if 0 <= pilihan_edit < len(dev_list):
        nom_dev = dev_list[pilihan_edit]
        for i, games in enumerate(daftar_game[nom_dev]):
            print(f"{i + 1}. {games}")
        try:
            edit_game = int(input("\nPilih Nomor Game yang ingin di Edit: ")) -1
        except ValueError:
            print("\nINVALID Input Wajib sebuah Angka")
            input("\nTekan ENTER Untuk Kembali")
            return
        except UnboundLocalError:
            print("\nINVALID Input Wajib sebuah Angka")
            input("\nTekan ENTER Untuk Kembali")
            return
        if 0 <= edit_game < len(daftar_game[nom_dev]):
                edited_game = str(input("Masukkan isi Edit: "))
                daftar_game[nom_dev][edit_game] = edited_game
                print(f"Perubahan Judul Baru {edited_game} Berhasil dimuat")
                input("\nTekan ENTER Untuk Kembali")
        else:
                print("Pilihan Yang Anda Input Tidak Ada!!!")
                input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
    else:
            print("Pilihan Yang Anda Input Tidak Ada!!!")
            input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

def hapus_game():
    clear()
    print(batas1)
    print("HAPUS SERI FIGHTING GAME".center(50))
    print(batas1)
    print(batas2)
    print()         
    print("Daftar Katalog Fighting Game".center(50),"\n")
    print(batas2)
    print(batas1)
    dev_list = list(daftar_game.keys())
    for i, dev in enumerate(dev_list):
        print(f"{i+1}. {dev}")
    print(batas1)
    try:
        pilihan_hapus = int(input("\nPilih Developer untuk menambah Game: ")) -1
        print()
    except ValueError:
        print("\nINVALID Input Wajib sebuah Angka")
        input("\nTekan ENTER Untuk Kembali")
        return
    except UnboundLocalError:
        print("\nINVALID Input Wajib sebuah Angka")
        input("\nTekan ENTER Untuk Kembali")
        return
    if 0 <= pilihan_hapus < len(dev_list):
        nom_dev = dev_list[pilihan_hapus]
        for i, games in enumerate(daftar_game[nom_dev]):
            print(f"{i + 1}. {games}")
        try:
            del_game = int(input("\nPilih Judul Game yang ingin di Hapus: ")) -1
        except ValueError:
            print("\nINVALID Input Wajib sebuah Angka")
            input("\nTekan ENTER Untuk Kembali")
            return
        except UnboundLocalError:
            print("\nINVALID Input Wajib sebuah Angka")
            input("\nTekan ENTER Untuk Kembali")
            return
        if 0 <= del_game < len(daftar_game[nom_dev]):
            del daftar_game[nom_dev][del_game]
            print(f"Game Berhasil di Hapus")
            input("\nTekan ENTER Untuk Kembali")
        else:
            print("Pilihan Yang Anda Input Tidak Ada!!!")
            input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
    else:
        print("Pilihan Yang Anda Input Tidak Ada!!!")
        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

def katalog_admin():
    clear()
    print(batas1)
    print("DAFTAR DEVELOPER FIGHTING GAME".center(50))
    print(batas1)
    print("""
    1. Capcom
    2. Bandai Namco
    3. Arc System Works""")
    menu_user = input("\nMasukkan Pilihan Yang Anda Inginkan: ")
# capcom
    if menu_user == "1":
        print(batas1)
        print(batas2)
        print(f"Fighting Game Capcom".center(50))
        print()
        capgames = list(daftar_game.get("Capcom"))
        for i, games in enumerate(capgames):
            print(f"{i + 1}. {games}")
        input ("\nTekan ENTER Untuk Kembali: ")
# namco
    elif menu_user == "2":
        print(batas1)
        print(batas2)
        print(f"Fighting Game Bandai Namco".center(50))
        print()
        namcogames = list(daftar_game.get("Bandai Namco"))
        for i, games in enumerate(namcogames):
            print(f"{i + 1}. {games}")
        input ("\nTekan ENTER Untuk Kembali: ")
# arc sys
    elif menu_user == "3":
        print(batas1)
        print(batas2)
        print(f"Fighting Game Arc System Works".center(50))
        print()
        arcgames = list(daftar_game.get("Arc System Works"))
        for i, games in enumerate(arcgames):
            print(f"{i + 1}. {games}")
        input ("\nTekan ENTER Untuk Kembali: ")
    else:
        print("Pilihan Yang Anda Input Tidak Ada!!!")
        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

def menuawal():
    while True:
        clear()
        print(batas1)
        print(batas2)
        print()
        print(" LOGIN SEBAGAI".center(50))
        print()
        print(batas2)
        print("""
        1. User
        2. Admin
        3. User Baru (daftar)
        4. Keluar""")
        print(batas1)
        menu = input("\nPilihan Anda (1/2/3)\t: ")
        if menu == "1":
            user()
        elif menu == "2":
            admin()
        elif menu == "3":
            register()
        elif menu == "4":
            akhir()
            exit()
        else:
            print("Pilihan Yang Anda Input Tidak Ada!!!")
            input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

def tampilan_user():
    while True:
        clear()
        print(batas1)
        print("DAFTAR DEVELOPER FIGHTING GAME".center(50))
        print(batas1)
        print("""
    1. Capcom
    2. Bandai Namco
    3. Arc System Works
    4. Kirim Tiket Ke Admin
    5. Log Out""")
        menu_user = input("\nMasukkan Pilihan Yang Anda Inginkan: ")
        if menu_user == "1":
            capcom_games("30 Mei 1979", "Kenzo Tsujimoto")
        elif menu_user == "2":
            namco_games("1 Juni 1955", "29 September 2005", "Masaya Nakamura")
        elif menu_user == "3":
            arcsys_games("12 Mei 1988", "Minoru Kidooka")
        elif menu_user == "4":
            kirim_tiket()
        elif menu_user == "5":
            konfir = input("\nApakah Anda yakin (Y/N): ").lower()
            if konfir == "y":
                menuawal()
                return
            if konfir == "n":
                continue
            else:
                pass
                print("Pilihan Yang Anda Input Tidak Ada!!!")
                input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
        else:
            print("Pilihan Yang Anda Input Tidak Ada!!!")
            input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

def tampilan_admin():
    while True:
        clear()
        print(batas1)
        print("PILIHAN MENU".center(50))
        print(batas1)
        print("""
    1. Tambah Fighting Game
    2. Edit Judul Fighting Game
    3. Hapus Game
    4. Daftar Developer & Fighting Game
    5. Baca Tiket dari User
    6. Log Out""")
        menu_admin = input("\nMasukkan Pilihan Yang Anda Inginkan: ")
        if menu_admin == "1":
            tambah_game()
        elif menu_admin == "2":
            edit_game()
        elif menu_admin == "3":
            hapus_game()
        elif menu_admin == "4":
            katalog_admin()
        elif menu_admin == "5":
            baca_keluhan()
        elif menu_admin == "6":
            konfir = input("\nApakah Anda yakin (Y/N): ").lower()
            if konfir == "y":
                menuawal()
                return
            if konfir == "n":
                continue
            else:
                pass
                print("Pilihan Yang Anda Input Tidak Ada!!!")
                input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
        else:
            print("Pilihan Yang Anda Input Tidak Ada!!!")
            input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

clear()
print(batas1)
print(batas2)
print()
print("SELAMAT DATANG DI KATALOG GAME FIGHTING🥊".center(45))
print()
print(batas1)
input("\n Tekan ENTER Untuk Melanjutkan !!")

menuawal()