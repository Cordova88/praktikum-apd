import os
from data import user_baru
from sistem import tampilan_user,  tampilan_admin

def clear():
    os.system("cls||clear")
clear()

batas1 = "="*50
batas2 = "+"*50

def user(kembali):
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
        # from sistem import tampilan_user
        tampilan_user(kembali)
    else:
        print(f"{usn} Belum terdaftar Harap Mendaftarkan Username di halama Register Terlebih dahulu!!!")
        input("\nSilahkan Tekan ENTER untuk mengulang")

def admin(kembali):
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
        # from sistem import tampilan_admin
        tampilan_admin(kembali)
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