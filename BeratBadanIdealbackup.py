print("""Selamat datang di program penghitungan berat badan ideal
""")
import time
time.sleep(1)

lagi = "Y"
while(str(lagi) == "Y" or "y"):
    A = input("Masukkan nama kamu disini :")
    B = input("Ketik P jika kamu perempuan atau L jika kamu laki-laki :")
    C = input("Masukkan tinggi badan kamu disini :")

    if(str(B) == "L" or str(B) == "l"):
        print("Berat badan ideal "+A+" adalah "+str((float(C)-100)-10*(float(C)-100)/100)+" Kilogram")
    elif(str(B) == "P" or str(B) == "p"):
        print("Berat badan ideal "+A+" adalah "+str((float(C)-100)-15*(float(C)-100)/100)+" Kilogram")
    else:
        print("Kesalahan input")
    lagi = str(input("ketik Y jika ingin mengulang atau sembarang untuk keluar dari program :"))
    
print("Terimakasih sudah menggunakan layanan kami")
time.sleep(3)