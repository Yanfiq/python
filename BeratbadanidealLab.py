lagi = "Y"
while(str(lagi) == "Y"):
    print("""Selamat datang di program penghitungan berat badan ideal""")
    import time
    time.sleep(1)
    Nama = input("Masukkan nama kamu disini :")
    Kelamin = input("Ketik P jika kamu perempuan atau L jika kamu laki-laki :")
    Tinggi = input("Masukkan tinggi badan kamu disini :")
    Konfirmasi = input("Ketik sembarang jika data sudah benar atau N jika ada kesalahan :")
    while(str(Konfirmasi) == "N" or str(Konfirmasi) == "n"):
        time.sleep(2) 
        print("""
        """) 
        Nama = input("Masukkan nama kamu disini :")
        Kelamin = input("Ketik P jika kamu perempuan atau L jika kamu laki-laki :")
        Tinggi = input("Masukkan tinggi badan kamu disini :")
        Konfirmasi = input("Ketik sembarang jika data sudah benar atau N jika ada kesalahan :")
    time.sleep(1)
    print("""
    Sebentar, sedang menghitung...
    """)
    time.sleep(2)
    if(str(Kelamin) == "L" or str(Kelamin) == "l"):
        print("Berat badan ideal "+Nama+" adalah "+str((float(Tinggi)-100)-10*(float(Tinggi)-100)/100)+" Kilogram")
    elif(str(Kelamin) == "P" or str(Kelamin) == "p"):
        print("Berat badan ideal "+Nama+" adalah "+str((float(Tinggi)-100)-15*(float(Tinggi)-100)/100)+" Kilogram")
    else:
        raise ValueError
    lagi = input("ketik Y jika ingin mengulang atau sembarang untuk keluar dari program :")
print("Terimakasih sudah menggunakan layanan kami")
