import os
from login import user, admin, register
from sistem import *
from InquirerPy import inquirer


def clear():
    os.system("cls||clear")
clear()

batas1 = "="*50
batas2 = "+"*50

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

def menuawal():
    while True:
        clear()
        print(batas1)
        print(batas2)
        print()
        print(" LOGIN SEBAGAI".center(50))
        print()
        menu = inquirer.select(message="\nPilihan Anda: ",
                                choices=["User", "Admin", "Register", "Keluar"],
                                qmark="💻",
                                pointer="👉"
                                ).execute()
        if menu == "User":
            user(menuawal)
        elif menu == "Admin":
            admin(menuawal)
        elif menu == "Register":
            register()
        elif menu == "Keluar":
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
        menu_user = inquirer.select(message="\nAnda Mengakses: ",
                                    choices=["Capcom", "Bandai Namco", "Arc System Works", "Kirim Tiket", "Log Out"],
                                    qmark="👤",
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
        menu_admin = inquirer.select(message="\nAnda Mengakses: ",
                                    choices=["Tambah Fighting Game", "Edit Judul Game", "Hapus Game", "Daftar Developer dan Game", "Baca Tiket", "Log Out"],
                                    qmark="🧑‍💻",
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