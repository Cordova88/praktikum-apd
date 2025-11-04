import os
from data import daftar_game, tiket, user_baru
from prettytable import PrettyTable
from InquirerPy import inquirer

def clear():
    os.system("cls||clear")
clear()

batas1 = "="*50
batas2 = "+"*50


def tampilan_user(kembali):
    while True:
        clear()
        print(batas1)
        print("DAFTAR DEVELOPER FIGHTING GAME".center(50))
        print(batas1)
        menu_user = inquirer.select(message="\nAnda Mengakses: ",
                                    choices=["Capcom", "Bandai Namco", "Arc System Works", "Kirim Tiket", "Log Out"],
                                    qmark="="*50,
                                    pointer="👉"
                                    ).execute()
        if menu_user == "Capcom":
            capcom_games("30 Mei 1979", "Kenzo Tsujimoto")
        elif menu_user == "Bandai Namco":
            namco_games("1 Juni 1955", "29 September 2005", "Masaya Nakamura")
        elif menu_user == "Arc System Works":
            arcsys_games("12 Mei 1988", "Minoru Kidooka")
        elif menu_user == "Kirim Tiket":
            kirim_tiket()
        elif menu_user == "Log Out":
            konfir = input("\nApakah Anda yakin (Y/N): ").lower()
            if konfir == "y":
                kembali
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

def tampilan_admin(kembali):
    while True:
        clear()
        print(batas1)
        print("PILIHAN MENU".center(50))
        print(batas1)
        menu_admin = inquirer.select(message="\nAnda Mengakses: ",
                                    choices=["Tambah Fighting Game", "Edit Judul Game", "Hapus Game", "Daftar Developer dan Game", "Baca Tiket", "Log Out"],
                                    qmark="="*50,
                                    pointer="👉"
                                    ).execute()
        if menu_admin == "Tambah Fighting Game":
            tambah_game()
        elif menu_admin == "Edit Judul Game":
            edit_game()
        elif menu_admin == "Hapus Game":
            hapus_game()
        elif menu_admin == "Daftar Developer dan Game":
            katalog_admin()
        elif menu_admin == "Baca Tiket":
            baca_tiket()
        elif menu_admin == "Log Out":
            konfir = input("\nApakah Anda yakin (Y/N): ").lower()
            if konfir == "y":
                kembali
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
    table = PrettyTable()
    table.field_names = ["No", "Judul Game"]
    capgames = list(daftar_game.get("Capcom"))
    for i, games in enumerate(capgames, start=1):
        table.add_row([i,games])
    print(table)
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
    table = PrettyTable()
    table.field_names = ["No", "Judul Game"]
    namcogames = list(daftar_game.get("Bandai Namco"))
    for i, games in enumerate(namcogames, start=1):
        table.add_row([i,games])
    print(table)
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
    table = PrettyTable()
    table.field_names = ["No", "Judul Game"]
    arcgames = list(daftar_game.get("Arc System Works"))
    for i, games in enumerate(arcgames, start=1):
        table.add_row([i,games])
    print(table)
    input ("\nTekan ENTER Untuk Kembali: ")

def kirim_tiket():
    clear()
    print(batas1)
    print(batas2)
    print("Pengiriman Tiket".center(45))
    print()
    pilihan = inquirer.select(message="\nAnda Mengakses: ",
                            choices=["Request", "Laporan"],
                            qmark="="*50,
                            pointer="👉"
                            ).execute()
    if pilihan == "Request":
        req = input("\nMasukkan Isi pesan: ")
        tiket["request"].append(req)
    elif pilihan == "Laporan":
        lapor = input("\nMasukkan Isi Pesan: ")
        tiket["laporan"].append(lapor)
    else:
        print("Pilihan Yang Anda Input Tidak Ada!!!")
        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
    print("\nTerima Kasih Atas Pesan yang anda kirim kami akan Segera Menanggapi nya")
    input("\nTekan ENTER untuk kembali")

def baca_tiket():
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
    pilihan_tambah = inquirer.select(message="\nPilih Developer: ",
                                    choices= dev_list,
                                    qmark="🎮"*5,
                                    pointer="👉"
                                    ).execute()
    newcap = inquirer.text(message="\nMasukkan Judul Game Baru:").execute()
    daftar_game[pilihan_tambah].append(newcap)
    print(f"\n{newcap} Berhasil ditambahkan")
    input("\nTekan ENTER Untuk Kembali")

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
    print(batas1)
    pilihan_edit = inquirer.select(message="\nPilih Developer: ",
                                    choices= dev_list,
                                    qmark="🎮"*5,
                                    pointer="👉"
                                    ).execute()
    print()
    nom_dev = daftar_game[pilihan_edit]
    if not nom_dev:
        print("\nTidak ada Game yang dapat di edit")
        input("\nTekan ENTER Untuk Kembali")
        return
    edit_game = inquirer.select(message=f"\nPilih Judul Game dari {pilihan_edit} yang ingin diedit: ",
                                    choices= nom_dev,
                                    qmark="🎮"*5,
                                    pointer="👉"
                                    ).execute()
    edited_game = inquirer.text(message=f"Masukkan Judul Baru: ").execute()
    index = nom_dev.index(edit_game)
    daftar_game[pilihan_edit][index] = edited_game
    print(f"Perubahan Judul Baru {edited_game} Berhasil dimuat")
    input("\nTekan ENTER Untuk Kembali")

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
    print(batas1)
    pilihan_hapus = inquirer.select(message="\nPilih Developer: ",
                                    choices= dev_list,
                                    qmark="🎮"*5,
                                    pointer="👉"
                                    ).execute()
    print()
    nom_dev = daftar_game[pilihan_hapus]
    if not nom_dev:
        print("\nTidak ada Game yang dapat di edit")
        input("\nTekan ENTER Untuk Kembali")
        return
    del_game = inquirer.select(message=f"\nPilih Judul Game dari {pilihan_hapus} yang ingin dihapus: ",
                                    choices= nom_dev,
                                    qmark="🎮"*5,
                                    pointer="👉"
                                    ).execute()
    daftar_game[pilihan_hapus].remove(del_game)
    print(f"Game Berhasil di Hapus")
    input("\nTekan ENTER Untuk Kembali")

def katalog_admin():
    clear()
    print(batas1)
    print("DAFTAR DEVELOPER FIGHTING GAME".center(50))
    print(batas1)
    menu_user = inquirer.select(message="\nAnda Mengakses: ",
                                choices=["Capcom", "Bandai Namco", "Arc System Works"],
                                qmark="🎮"*5,
                                pointer="👉"
                                ).execute()
# capcom
    if menu_user == "Capcom":
        print(batas1)
        print(batas2)
        print(f"Fighting Game Capcom".center(50))
        print()
        table = PrettyTable()
        table.field_names = ["No", "Judul Game"]
        capgames = list(daftar_game.get("Capcom"))
        for i, games in enumerate(capgames, start=1):
            table.add_row([i,games])
        print(table)
        input ("\nTekan ENTER Untuk Kembali: ")
# namco
    elif menu_user == "Bandai Namco":
        print(batas1)
        print(batas2)
        print(f"Fighting Game Bandai Namco".center(50))
        print()
        table = PrettyTable()
        table.field_names = ["No", "Judul Game"]
        namcogames = list(daftar_game.get("Bandai Namco"))
        for i, games in enumerate(namcogames, start=1):
            table.add_row([i,games])
        print(table)
        input ("\nTekan ENTER Untuk Kembali: ")
# arc sys
    elif menu_user == "Arc System Works":
        print(batas1)
        print(batas2)
        print(f"Fighting Game Arc System Works".center(50))
        print()
        table = PrettyTable()
        table.field_names = ["No", "Judul Game"]
        arcgames = list(daftar_game.get("Arc System Works"))
        for i, games in enumerate(arcgames, start=1):
            table.add_row([i,games])
        print(table)
        input ("\nTekan ENTER Untuk Kembali: ")
    else:
        print("Pilihan Yang Anda Input Tidak Ada!!!")
        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")