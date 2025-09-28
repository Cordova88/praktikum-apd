
print("\n=== Silahkan Login Terlebih Dahulu ===")
username = (input("Username:"))
password = (input("Password:"))

if username == "Cordova" and password == "055":
    print("== Berhasil Login ==")
    print("\n-----Konversi-----")
    print("1. Panjang")
    print("2. Massa")
    print("3. Suhu")
    print("4. Waktu")
    print("5. Mata Uang")
    pilihan = (input("\nPilih nomor diatas untuk satuan yang ingin anda Konversi: "))
# konversi panjang
    if pilihan == "1":
        print (" Satuan Panjang yang dapat di konversi","\n - Feet (ft)", "\n - Kilometer (km)", "\n - Centimeter (cm)")
        panjang = input("\n== Masukkan satuan yang ingin anda konversi ke Meter: ")
        if  panjang == "ft":
            ft = float(input("Masukkan angka (ft) untuk di konversi ke Meter:"))
            hasil = ft * 0.3048 
            print (f"{ft} ft ==> {hasil} Meter")
        if panjang == "km" :
            km = float(input("Masukkan angka (km) untuk di konversi ke Meter:"))
            hasil = km * 1000
            print (f"{km} km ==> {hasil} Meter")
        if panjang == "cm" :
            cm = float(input("Masukkan angka (cm) untuk di konversi ke Meter:"))
            hasil = cm / 100
            print (f"{cm} cm ==> {hasil} Meter")
# konversi massa
    elif pilihan == "2":
        print (" Satuan Massa yang dapat di konversi","\n - Pound (lb)", "\n - Ton (t)", "\n - Gram (gr)", "\n - Centigram (cg)", "\n - Milligram (mg)")
        massa = input("\n== Masukkan satuan yang ingin anda konversi ke Kilogram: ")
        if  massa == "lb":
            lb = float(input("Masukkan angka (lb) untuk di konversi ke Kilogram:"))
            hasil = lb / 2.2046
            print (f"{lb} lb ==> {hasil} Kilogram")
        if massa == "t" :
            t = float(input("Masukkan angka (t) untuk di konversi ke Kilogram:"))
            hasil = t * 1000
            print (f"{t} t ==> {hasil} Kilogram")
        if massa == "gr" :
            gr = float(input("Masukkan angka (gr) untuk di konversi ke Kilogram:"))
            hasil = gr / 1000
            print (f"{gr} gr ==> {hasil} Kilogram")
        if massa == "cg" :
            cg = float(input("Masukkan nangka (cg) untuk di konversi ke Kilogram:"))
            hasil = cg / 100000
            print (f"{cg} cg ==> {hasil} Kilogram")
        if massa == "mg" :
            mg = float(input("Masukkan angka (mg) untuk di konversi ke Kilogram:"))
            hasil = mg / 1000000
            print (f"{mg} mg ==> {hasil} Kilogram")
# konversi suhu
    elif pilihan == "3":
        print (" Satuan Suhu yang dapat di konversi","\n - Celcius (C)", "\n - Farhenheit (F)", "\n - Reamur (R)")
        suhu = input("\n== Masukkan satuan yang ingin anda konversi ke Kelvin: ")
        if suhu == "C":
            C = float(input("Masukkan suhu (C) untuk di konversi ke Kelvin:"))
            hasil = C + 273.15
            print (f"{C} Celcius ==> {hasil} Kelvin")
        if suhu == "F" :
            F = float(input("Masukkan suhu (F) untuk di konversi ke Kelvint:"))
            hasil = (F - 32) * 5/9 + 273.15
            print (f"{F} Farhenheit ==> {hasil} Kelvin")
        if suhu == "R" :
            R = float(input("Masukkan suhu (R) untuk di konversi ke Kelvin:"))
            hasil = (5/4) * R + 273.15
            print (f"{R} Reamur ==> {hasil} Kelvin")
# konversi Waktu
    elif pilihan == "4":
        print (" satuan Waktu yang dapat di konversi","\n - Menit (min)", "\n - Jam (h)")
        waktu = input("\n== Masukkan satuan yang ingin anda konversi ke Detik: ")
        if  waktu == "min":
            min = float(input("Masukkan Menit untuk di konversi ke Detik:"))
            hasil = min * 60
            print (f"{min} Menit ==> {hasil} Detik")
        if waktu == "h" :
            h = float(input("Masukkan Jam untuk di konversi ke Detik:"))
            hasil = h * 3600
            print (f"{h} Jam ==> {hasil} Detik")
# konversi mata uang
    elif pilihan == "5":
        print (" Mata Uang yang dapat di konversi","\n 1. IDR to USD", "\n 2. USD to IDR","\n 3. IDR to EUR", "\n 4. ERU to IDR","\n 5. IDR to MYR", "\n 6. MYR to IDR")
        MataUang = input("\n== Pilih nomor sesuai dengan yang diatas untuk mengkonversi mata uang:")
        if MataUang == "1":
            idrtousd = float(input("Masukkan Rupiah: "))
            hasil = idrtousd * 0.00005996
            print (f"{idrtousd} Rupiah ==> {hasil} Dolar")
        if MataUang == "2":
            usdtoidr = float(input("Masukkan Dolar: "))
            hasil = usdtoidr * 16.680
            print (f"{usdtoidr} Dolar ==> {hasil} Rupiah")
        if MataUang == "3":
            idrtoeur = float(input("Masukkan Rupiah: "))
            hasil = idrtoeur * 0.00005124
            print (f"{idrtoeur} Rupiah ==> {hasil} Euro")
        if MataUang == "4":
            eurtoidr = float(input("Masukkan Euro: "))
            hasil = eurtoidr * 19.520
            print (f"{eurtoidr} Euro ==> {hasil} Rupiah")
        if MataUang == "5":
            idrtomyr = float(input("Masukkan Rupiah: "))
            hasil = idrtomyr * 0.0002531
            print (f"{idrtomyr} Rupiah ==> {hasil} Ringgit")
        if MataUang == "6":
            myrtoidr = float(input("Masukkan Ringgit: "))
            hasil = myrtoidr * 3.9510
            print ((f"{myrtoidr} Ringgit ==> {hasil} Rupiah"))

elif username != "Cordova" and  password == "055":
    print("Username salah")
elif username == "Cordova" and password != "055":
    print("Password salah")
else:
    print("Gagal Login")
