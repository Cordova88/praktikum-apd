
print("\n=== Silahkan Login Terlebih Dahulu ===")
username = (input("Username:"))
password = (input("Password:"))

if username == "Cordova" and password == "055":
    print("== Berhasil Login ==")
    print("\n ---Konversi---")
    print("1. Panjang")
    print("2. Massa")
    print("3. Suhu")
    print("4. Waktu")
    print("5. Mata Uang")
    pilihan = (input("\nPilih nomor diatas untuk satuan yang ingin anda Konversi: "))
# konversi panjang
    if pilihan == "1":
        print (" List satuan panjang yang dapat di konversi","\n Feet (ft)", "\n Kilometer (km)", "\n Centimeter (cm)")
        panjang = input("\n== Masukkan satuan yang ingin anda konversi ke Meter: ")
        if  panjang == "ft":
            ft = float(input("Masukkan nilai feet:"))
            hasil = ft * 0.3048 
            print (f"{ft} ft ==> {hasil} Meter")
        if panjang == "km" :
            km = float(input("Masukkan nilai km:"))
            hasil = km * 1000
            print (f"{km} km ==> {hasil} Meter")
        if panjang == "cm" :
            cm = float(input("Masukkan nilai cm:"))
            hasil = cm / 100
            print (f"{cm} cm ==> {hasil} Meter")
        # else:
        #     print("INVALID!!!")
# konversi massa
    elif pilihan == "2":
        print (" List satuan massa yang dapat di konversi","\n Pound (lb)", "\n Ton (t)", "\n Gram (gr)")
        massa = input("\n== Masukkan satuan yang ingin anda konversi ke Kilogram: ")
        if  massa == "lb":
            lb = float(input("Masukkan nilai Pound:"))
            hasil = lb / 2.2046
            print (f"{lb} lb ==> {hasil} Kilogram")
        if massa == "t" :
            t = float(input("Masukkan nilai Ton:"))
            hasil = t * 1000
            print (f"{t} lb ==> {hasil} Kilogram")
        if massa == "gr" :
            gr= float(input("Masukkan nilai Gram:"))
            hasil = gr / 1000
            print (f"{gr} lb ==> {hasil} Kilogram")
        # else:
        #     print("INVALID!!!")
# konversi suhu
    elif pilihan == "3":
        print (" List satuan suhu yang dapat di konversi","\n Celcius (C)", "\n Farhenheit (F)", "\n Reamur (R)")
        suhu = input("\n== Masukkan satuan yang ingin anda konversi ke Kelvin: ")
        if suhu == "C":
            C = float(input("Masukkan nilai Celcius:"))
            hasil = C + 273.15
            print (f"{C} Celcius ==> {hasil} Kelvin")
        if suhu == "F" :
            F = float(input("Masukkan nilai Farhenheit:"))
            hasil = 9/5 * (F - 32) + 273.15
            print (f"{F} Farhenheit ==> {hasil} Kelvin")
        if suhu == "R" :
            R = float(input("Masukkan nilai Reamur:"))
            hasil = (5/4) * R + 273.15
            print (f"{R} Reamur ==> {hasil} Kelvin")
        # else:
        #     print("INVALID!!!")





elif username != "Cordova" and  password == "055":
    print("Username salah")
elif username == "Cordova" and password != "055":
    print("Password salah")
else:
    print("Gagal Login")
