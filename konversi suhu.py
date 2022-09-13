#input
suhu = input("Masukkan nilai suhu : ")
satuan = str(input("Masukkan satuan suhu : "))
hasil = str(input("Masukkan satuan suhu tujuan : "))

#perbandingan
perbandingan = {"celsius": 5, "reamur": 4, "fahrenheit": 9, "kelvin": 5}

#hitung
if(satuan == "kelvin"):
    print(int(perbandingan[hasil])/int(perbandingan[satuan])*(int(suhu)-273))
elif(hasil == "kelvin"):
    print((int(perbandingan[hasil])/int(perbandingan[satuan])*int(suhu))+273)
elif(satuan == "fahrenheit"):
    print(int(perbandingan[hasil])/int(perbandingan[satuan])*(int(suhu)-32))
elif(hasil == "fahrenheit"):
    print((int(perbandingan[hasil])/int(perbandingan[satuan])*int(suhu))+32)
else:
    print(int(perbandingan[hasil])/int(perbandingan[satuan])*int(suhu))