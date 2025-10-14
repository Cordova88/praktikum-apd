import os
os.system('cls')

akses_login = 3

franchise =["Street FIghter",
            "Tekken",
            "Mortal Kombat",
            "Guilty Gear",
            "Virtua Fighter"
            ]
sf_games = ["Street Fighter",
            "Street II",
            "Street Fighter Alpha",
            "Street Fighter III",
            "Street Fighter IV",
            "Street Fighter V",
            "Street Fighter 6"]
tk_games = ["Tekken",
            "Tekken 2",
            "Tekken 3",
            "Tekken 4",
            "Tekken 5",
            "Tekken 6",
            "tekken 7",
            "Tekken 8"]
mk_games = ["Mortal Kombat",
            "Mortal Kombat II",
            "Mortal Kombat II",
            "Mortal Kombat 3",
            "Mortal Kombat 4",
            "Mortal Kombat Deadly Alliance",
            "Mortal Kombat Deception",
            "Mortal Kombat Armageddon",
            "Mortal Kombat 9",
            "Mortal Kombat X",
            "Mortal Kombat 11",
            "Mortal Kombat 1"
            ]
gg_games = ["Guilty Gear",
            "Guilty Gear X",
            "Guilty Gear XX",
            "Guilty Gear Xrd -SIGN-",
            "Guilty Gear Xrd -REVELATOR-",
            "Guilty Gear -STRIVE-",
            ]
vf_games = ["Virtua Fighter",
            "Virtua Fighter 2",
            "Virtua Fighter 3",
            "Virtua Fighter 4",
            "Virtua Fighter 5",
            "New Virtua Fighter Project (Upcoming)",
            ]
dev = ["Capcom", "Bandai Namco","NetherRealm Studio", "Arcys System Works", "Sega"]
karakter = ["Ryu","Ken","Chun li",
            "Jin Kazama", "Kazuya Mishima", "Steve Fox",
            "Scorpion", "Sub-Zero", "Raiden",
            "Sol Badguy", "KY Kiske", "Baiken",
            "Akira Yuki", "Sarah Bryant", "Jacky Bryant" 
            ]
# total_karakter= ["87", "71", "76", "36", "20"]


batas1 = "="*50
batas2 = "+"*50
user_baru = []
user = True
admin = True

os.system('cls')
print(batas1)
print(batas2)
print()
print("SELAMAT DATANG DI KATALOG GAME FIGHTING🥊".center(45))
print()
print(batas1)
input("\n Tekan ENTER Untuk Melanjutkan !!")

# form login
while akses_login > 0:
    os.system('cls')
    # print(batas1)
    print(batas2)
    print()
    print(" LOGIN SEBAGAI".center(50))
    print()
    print(batas2)
    print("""
        1. User
        2. Admin
        3. User Baru (daftar)""")
    print(batas1)
    menu = input("\nPilihan Anda (1/2/3)\t: ")
# login user
    if menu =="1":
        print(batas2)
        print("LOGIN USER".center(50))
        print(batas2)
        usn = input("\nUsername: ")
        pw = input("Password: ")
        if usn in user_baru and pw in user_baru:
            print()
            print(batas2)
            print("LOGIN BERHASIL".center(50))
            print(f"SELAMAT DATANG {newusn}")
            print(batas2)
            print()
            input("Silahkan Tekan ENTER")
            user = True
            admin = False
            break
        else:
            print()
            akses_login -= 1
            if akses_login == 0:
                print(batas1)
                print("MAAF, Akses Login anda telah habis!!")
                print(batas2)
                input("Silahkan Tekan ENTER")
                user = False
                admin = False
                break
            else:
                print(f"Login Gagal!!, anda masih bisa login {akses_login} kali lagi")
                input("\nSilahkan Tekan ENTER untuk mengulang")
# login admin
    elif menu == "2":
        print(batas2)
        print("LOGIN ADMIN".center(50))
        print(batas2)
        usn = input("\nUsername: ").upper()
        pw = input("Password: ").upper()
        if usn == "RYU" and pw == "HADOUKEN":
            print()
            print(batas2)
            print(f"LOGIN BERHASIL, selamat datang {usn}")
            print(batas2)
            print()
            input("Silahkan Tekan ENTER")
            admin = True
            user = False
            break
        else:
            print()
            akses_login -= 1
            if akses_login == 0:
                print(batas1)
                print("MAAF, Akses Login anda telah habis!!")
                print(batas2)
                input("Silahkan Tekan ENTER")
                user = False
                admin = False
                break
            else:
                print(f"Login Gagal!!, anda masih bisa login {akses_login} kali lagi")
                input("\nSilahkan Tekan ENTER untuk mengulang")
# register
    elif menu =="3":
        print(batas2)
        print("DAFTAR USER BARU".center(50))
        print(batas2)
        newusn = input("\nUsername: ")
        newpw = input("Password: ")
        user_baru.append(newusn)
        user_baru.append(newpw)
        print(f"\nSelamat {newusn} anda telah terdaftar")
        input("\nHarap Tekan ENTER untuk Login")
# input kosong
    else:
        print("Pilihan Yang Anda Input Tidak Ada")
        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

# user interface
while True:
    if user:
        while user:
            os.system('cls')
            print(batas1)
            print("PILIHAN MENU".center(50))
            print(batas1)
            print("""
    1. Daftar Fighting Game
    2. Keluar""")
            menu_user = input("\nMasukkan Pilihan Yang Anda Inginkan: ")
# menu daftar
            if menu_user == "1":
                os.system('cls')
                print(batas1)
                print()         
                print("Daftar Katalog Fighting Game".center(50),"\n")
                print(batas1)
                print(batas2)
                for game in range(len(franchise)):
                    print(f"{game+1}. {franchise[game]}")
                print(batas1)
                akses_katalog = input("\nPilih Game yang Ingin Anda Akses?: ")
# sf
                if akses_katalog == "1":
                    os.system('cls')
                    print("INFORMASI FRANCHISE".center(50))
                    print(batas1)
                    print(f"Developer: {dev[0]}")
                    print(f"\nKarakter Populer:")
                    for i in karakter[0:3]:
                        print(f"-",i)
                    print(f"\nSeri Terbaik: {sf_games[3]} 3rd Thir Strike (1999)")
                    print(f"\nSeri Terbaru: {sf_games[-1]} (2023)")
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[0]}".center(45))
                    print()
                    for listsf in range(len(sf_games)):
                        print(f"{listsf + 1}. {sf_games[listsf]}")
                    input ("\nTekan ENTER Untuk Kembali: ")
# tekken
                elif akses_katalog == "2":
                    os.system('cls')
                    print("INFORMASI FRANCHISE".center(50))
                    print(batas1)
                    print(f"Developer: {dev[1]}")
                    print(f"\nKarakter Populer:")
                    for i in karakter[3:6]:
                        print(f"-",i)
                    print(f"\nSeri Terbaik {tk_games[-2]} (2015)")
                    print(f"\nGame Terbaru: {tk_games[-1]} (2024)")
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[1]}".center(45))
                    print()
                    for listtk in range(len(tk_games)):
                        print(f"{listtk + 1}. {tk_games[listtk]}")
                    input ("\nTekan ENTER Untuk Kembali: ")
# mk
                elif akses_katalog == "3":
                    os.system('cls')
                    print("INFORMASI FRANCHISE".center(50))
                    print(batas1)
                    print(f"Developer: {dev[2]}")
                    print(f"\nKarakter Populer:")
                    for i in karakter[6:9]:
                        print(f"-",i)
                    print(f"\nSeri Terbaik {mk_games[-2]} (2019)")
                    print(f"\nGame Terbaru: {mk_games[-1]} (2023)")
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[2]}".center(45))
                    print()
                    for listmk in range(len(mk_games)):
                        print(f"{listmk + 1}. {mk_games[listmk]}")
                    input ("\nTekan ENTER Untuk Kembali: ")
# gg
                elif akses_katalog == "4":
                    os.system('cls')
                    print("INFORMASI FRANCHISE".center(50))
                    print(batas1)
                    print(f"Developer: {dev[3]}")
                    print(f"\nKarakter Populer:")
                    for i in karakter[9:12]:
                        print(f"-",i)
                    print(f"\nSeri Terbaik {gg_games[-1]} (2021)")
                    print(f"\nGame Terbaru: {gg_games[-1]} (2021)")
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[3]}".center(45))
                    print()
                    for listgg in range(len(gg_games)):
                        print(f"{listgg + 1}. {gg_games[listgg]}")
                    input ("\nTekan ENTER Untuk Kembali: ")
# vf
                elif akses_katalog == "5":
                    os.system('cls')
                    print("INFORMASI FRANCHISE".center(50))
                    print(batas1)
                    print(f"Developer: {dev[4]}")
                    print(f"\nKarakter Populer:")
                    for i in karakter[12: ]:
                        print(f"-",i)
                    print(f"\nSeri Terbaik {vf_games[-2]} R.E.V.O (2021)")
                    print(f"\nGame Terbaru: {vf_games[-2]} R.E.V.O Update (2021)")
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[4]}".center(45))
                    print()
                    for listvf in range(len(vf_games)):
                        print(f"{listvf + 1}. {vf_games[listvf]}")
                    input ("\nTekan ENTER Untuk Kembali: ")

            elif menu_user == "2":
                input("Tekan ENTER untuk Keluar")
                user = False
                break

            else:
                print("Pilihan Yang Anda Input Tidak Ada")
                input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# admin interface
    elif admin:
        while admin:
            os.system('cls')
            print(batas1)
            print("PILIHAN MENU".center(50))
            print(batas1)
            print("""
    1. Tambah Seri Game
    2. Edit  Seri Game
    3. Hapus Game
    4. Katalog Game
    5. Keluar""")
            menu_admin = input("\nMasukkan Pilihan Yang Anda Inginkan: ")
# penambahan
            if menu_admin == "1":
                os.system('cls')
                print(batas1)
                print("PENAMAMBAHAN SERI BARU".center(50))
                print(batas1)
                print(batas2)
                print()         
                print("Daftar Katalog Fighting Game".center(50),"\n")
                print(batas2)
                print(batas1)
                for game in range(len(franchise)):
                    print(f"{game+1}. {franchise[game]}")
                print(batas1)
                penambahan_game = input("\nPilih Game Untuk Menambahkan Seri Baru:")
# tambah sf
                if penambahan_game == "1":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[0]}".center(50))
                    print()
                    for listsf in range(len(sf_games)):
                        print(f"{listsf + 1}. {sf_games[listsf]}")
                    newgamesf = input("\nMasukkan Judul Game yang Akan Ditambahkan:")
                    sf_games.append(newgamesf)
                    print(f"{newgamesf} Telah Ditambah ")
                    input("\nTekan ENTER Untuk Kembali")
# tambah tekken
                elif penambahan_game == "2":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[1]}".center(50))
                    print()
                    for listtk in range(len(tk_games)):
                        print(f"{listtk + 1}. {tk_games[listtk]}")
                    newgametk = input("\nMasukkan Judul Game yang Akan Ditambahkan:")
                    tk_games.append(newgametk)
                    print(f"{newgametk} Telah Ditambah ")
                    input("\nTekan ENTER Untuk Kembali")
# tambah mk
                elif penambahan_game == "2":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[2]}".center(50))
                    print()
                    for listmk in range(len(mk_games)):
                        print(f"{listmk + 1}. {mk_games[listmk]}")
                    newgamemk = input("\nMasukkan Judul Game yang Akan Ditambahkan:")
                    mk_games.append(newgamemk)
                    print(f"{newgamemk} Telah Ditambah ")
                    input("\nTekan ENTER Untuk Kembali")
# tambah gg
                elif penambahan_game == "4":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[3]}".center(50))
                    print()
                    for listgg in range(len(gg_games)):
                        print(f"{listgg + 1}. {gg_games[listgg]}")
                    newgamegg = input("\nMasukkan Judul Game yang Akan Ditambahkan:")
                    gg_games.append(newgamegg)
                    print(f"{newgamegg} Telah Ditambah ")
                    input("\nTekan ENTER Untuk Kembali")
# tambah vf
                elif penambahan_game == "5":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[4]}".center(50))
                    print()
                    for listvf in range(len(vf_games)):
                        print(f"{listvf + 1}. {vf_games[listvf]}")
                    newgamevf = input("\nMasukkan Judul Game yang Akan Ditambahkan:")
                    vf_games.append(newgamevf)
                    print(f"{newgamevf} Telah Ditambah ")
                    input("\nTekan ENTER Untuk Kembali")

                else:
                    print("Pilihan Yang Anda Input Tidak Ada")
                    input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# edit data
            elif menu_admin == "2":
                os.system('cls')
                print(batas1)
                print("EDIT SERI GAME".center(50))
                print(batas1)
                print(batas2)
                print()         
                print("Daftar Katalog Fighting Game".center(50),"\n")
                print(batas2)
                print(batas1)
                for game in range(len(franchise)):
                    print(f"{game+1}. {franchise[game]}")
                print(batas1)
                edit_game = input("\nPilih Game Untuk Menambahkan Seri Baru:")
# edit sf
                if edit_game == "1":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[0]}".center(50))
                    print()
                    for listsf in range(len(sf_games)):
                        print(f"{listsf + 1}. {sf_games[listsf]}")
                    editsf = int(input("\nMasukkan nomor Game yang Ingin di Edit: ")) -1
                    if 0 <= editsf < len(sf_games):
                        edited_sf = input("Masukkan Isi Edit: ")
                        sf_games[editsf] = edited_sf
                        print(f"Judul {sf_games[editsf]} Berhasil Dimuat Ke Dalam Katalog")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# edit tk
                elif edit_game == "2":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[1]}".center(50))
                    print()
                    for listtk in range(len(tk_games)):
                        print(f"{listtk + 1}. {tk_games[listtk]}")
                    edittk = int(input("\nMasukkan nomor Game yang Ingin di Edit: ")) -1
                    if 0 <= edittk < len(tk_games):
                        edited_tk = input("Masukkan Isi Edit: ")
                        tk_games[edittk] = edited_tk
                        print(f"Judul {tk_games[edittk]} Berhasil Dimuat Ke Dalam Katalog")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# edit mk
                elif edit_game == "3":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[2]}".center(50))
                    print()
                    for listmk in range(len(mk_games)):
                        print(f"{listmk + 1}. {mk_games[listmk]}")
                    editmk = int(input("\nMasukkan nomor Game yang Ingin di Edit: ")) -1
                    if 0 <= editmk < len(mk_games):
                        edited_mk = input("Masukkan Isi Edit: ")
                        mk_games[editmk] = edited_mk
                        print(f"Judul {mk_games[editmk]} Berhasil Dimuat Ke Dalam Katalog")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# edit gg
                elif edit_game == "4":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[3]}".center(50))
                    print()
                    for listgg in range(len(gg_games)):
                        print(f"{listgg + 1}. {gg_games[listgg]}")
                    editgg = int(input("\nMasukkan nomor Game yang Ingin di Edit: ")) -1
                    if 0 <= editgg < len(gg_games):
                        edited_gg = input("Masukkan Isi Edit: ")
                        gg_games[editgg] = edited_gg
                        print(f"Judul {gg_games[editgg]} Berhasil Dimuat Ke Dalam Katalog")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# edit vf
                elif edit_game == "5":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[4]}".center(50))
                    print()
                    for listvf in range(len(vf_games)):
                        print(f"{listvf + 1}. {vf_games[listvf]}")
                    editvf = int(input("\nMasukkan nomor Game yang Ingin di Edit: ")) -1
                    if 0 <= editvf < len(vf_games):
                        edited_vf = input("Masukkan Isi Edit: ")
                        vf_games[editvf] = edited_vf
                        print(f"Judul {gg_games[editvf]} Berhasil Dimuat Ke Dalam Katalog")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

                else:
                    print("Pilihan Yang Anda Input Tidak Ada")
                    input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# hapus game
            elif menu_admin == "3":
                os.system('cls')
                print(batas1)
                print("HAPUS SERI GAME".center(50))
                print(batas1)
                print(batas2)
                print()         
                print("Daftar Katalog Fighting Game".center(50),"\n")
                print(batas2)
                print(batas1)
                for game in range(len(franchise)):
                    print(f"{game+1}. {franchise[game]}")
                print(batas1)
                hapus_game = input("\nPilih 1 Game Untuk Dihapus judul Game nya:")
# hapus sf
                if hapus_game == "1":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[0]}".center(50))
                    print()
                    for listsf in range(len(sf_games)):
                        print(f"{listsf + 1}. {sf_games[listsf]}")
                    hapussf = int(input("\nMasukkan nomor Game yang Ingin di Hapus: ")) -1
                    if 0 <= hapussf < len(sf_games):
                        sf_judul = sf_games.pop(hapussf)
                        print(f"Game {sf_judul} Berhasil Dihapus")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# hapus tk
                elif hapus_game == "2":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[1]}".center(50))
                    print()
                    for listtk in range(len(tk_games)):
                        print(f"{listtk + 1}. {tk_games[listtk]}")
                    hapustk = int(input("\nMasukkan nomor Game yang Ingin di Hapus: ")) -1
                    if 0 <= hapustk < len(tk_games):
                        tk_judul = tk_games.pop(hapustk)
                        print(f"Game {tk_judul} Berhasil Dihapus")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# hapus mk
                elif hapus_game == "3":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[2]}".center(50))
                    print()
                    for listmk in range(len(mk_games)):
                        print(f"{listmk + 1}. {mk_games[listmk]}")
                    hapusmk = int(input("\nMasukkan nomor Game yang Ingin di Hapus: ")) -1
                    if 0 <= hapusmk < len(mk_games):
                        mk_judul = mk_games.pop(hapusmk)
                        print(f"Game {mk_judul} Berhasil Dihapus")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# hapus gg
                elif hapus_game == "4":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[3]}".center(50))
                    print()
                    for listgg in range(len(gg_games)):
                        print(f"{listgg + 1}. {gg_games[listgg]}")
                    hapusgg = int(input("\nMasukkan nomor Game yang Ingin di Hapus: ")) -1
                    if 0 <= hapusgg < len(gg_games):
                        gg_judul = gg_games.pop(hapusgg)
                        print(f"Game {gg_judul} Berhasil Dihapus")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# hapus vf
                elif hapus_game == "5":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[4]}".center(50))
                    print()
                    for listvf in range(len(vf_games)):
                        print(f"{listvf + 1}. {vf_games[listvf]}")
                    hapusvf = int(input("\nMasukkan nomor Game yang Ingin di Hapus: ")) -1
                    if 0 <= hapusvf < len(vf_games):
                        vf_judul = vf_games.pop(hapusvf)
                        print(f"Game {vf_judul} Berhasil Dihapus")
                        input("ENTER Untuk Kembali")
                    else:
                        print("Pilihan Yang Anda Input Tidak Ada")
                        input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

                else:
                    print("Pilihan Yang Anda Input Tidak Ada")
                    input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")
# lihat katalog
            elif menu_admin == "4":
                os.system('cls')
                print(batas1)
                print()         
                print("Daftar Katalog Fighting Game".center(50),"\n")
                print(batas1)
                print(batas2)
                for game in range(len(franchise)):
                    print(f"{game+1}. {franchise[game]}")
                print(batas1)
                admin_katalog = input("\nPilih Game yang Ingin Anda Akses?: ")

                if admin_katalog == "1":
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[0]}".center(50))
                    print()
                    for listsf in range(len(sf_games)):
                        print(f"{listsf + 1}. {sf_games[listsf]}")
                    input("ENTER Untuk Kembali")
                elif admin_katalog == "2":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[1]}".center(50))
                    print()
                    for listtk in range(len(tk_games)):
                        print(f"{listtk + 1}. {tk_games[listtk]}")
                    input("ENTER Untuk Kembali")
                elif admin_katalog == "3":       
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[2]}".center(50))
                    print()
                    for listmk in range(len(mk_games)):
                        print(f"{listmk + 1}. {mk_games[listmk]}")
                    input("ENTER Untuk Kembali")
                elif admin_katalog == "4":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[3]}".center(50))
                    print()
                    for listgg in range(len(gg_games)):
                        print(f"{listgg + 1}. {gg_games[listgg]}")
                    input("ENTER Untuk Kembali")
                elif admin_katalog == "5":
                    os.system('cls')
                    print(batas1)
                    print(batas2)
                    print(f"Seri Utama {franchise[4]}".center(50))
                    print()
                    for listvf in range(len(vf_games)):
                        print(f"{listvf + 1}. {vf_games[listvf]}")
                    input("ENTER Untuk Kembali")
                else:
                    print("Pilihan Yang Anda Input Tidak Ada")
                    input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

            elif menu_admin == "5":
                input("\nTekan ENTER Untuk Konfirmasi")
                admin = False
                break

            else:
                print("Pilihan Yang Anda Input Tidak Ada")
                input("\nHarap Tekan Enter untuk Input Ulang Pilihan Anda")

    else:
        os.system('cls')
        print()
        print(batas1)
        print(batas2)
        print("TERIMA KASIH ATAS KUNJUNGANNYA".center(45))
        print()
        print("SAMPAI JUMPA".center(45))
        print(batas2)
        print(batas1)
        break