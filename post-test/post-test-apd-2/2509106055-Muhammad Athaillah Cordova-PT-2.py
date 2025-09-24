print("=== Ini adalah suhu dalam Celcius ===")
suhu = [27, 33, 46, 55, 67, 92]

# rumus konversi Celcius ke Farhenheit
farhenheit1 = (9/5) * suhu[0] + 32
farhenheit2 = (9/5) * suhu[1] + 32
# rumus konversi Celcius ke Kelvin
kelvin1 = suhu[-4] + 273.15
kelvin2 = suhu[-3] + 273.15
# rumus konversi Celcius ke Reamur
reamur1 = (4/5) * suhu[-2]
reamur2 = (4/5) * suhu[-1]

print (suhu)

print("\n== Hasil konversi suhu ke-1 dan ke-2 dari Celcius ke Farhenheit ==")
print(f"{suhu[0]} Celcius = {farhenheit1} Farhenheit")
print(f"{suhu[1]} Celcius = {farhenheit2} Farhenheit")

print("\n== Hasil konversi suhu ke-3 dan ke-4 dari Celcius ke Kelvin ==")
print(f"{suhu[-4]} Celcius = {kelvin1} Kelvin")
print(f"{suhu[-3]} Celcius = {kelvin2} Kelvin")

print("\n== Hasil konversi suhu ke-5 dan ke-6 dari Celcius ke Reamur ==")
print(f"{suhu[-2]} Celcius = {reamur1} Reamur")
print(f"{suhu[-1]} Celcius = {reamur2} Reamur")

jumlah = farhenheit1+farhenheit2+kelvin1+kelvin2+reamur1+reamur2
rata2 =  jumlah/len(suhu)

print (f"\nJumlah suhu setelah di konversi adalah {jumlah}")
print (f"Rata-rata dari jumlah keenam suhu tadi adalah {rata2}")

NIM = 55
print(f"\nNIM:  {NIM}")
boolean = NIM < rata2
print(f"NIM < rata-rata: {boolean}")