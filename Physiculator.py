print("Selamat datang di Physiculator")
import time
time.sleep(1)

#BAB
bab = float(input("""1 : Gerak lurus
2 : Kalor
3 : Listrik statis
soalmu termasuk bab apa (ketik angka sesuai petunjuk)?"""))

if(bab==1):
    print("termasuk dalam subbab apakah soalmu itu?")
    print("masukkan data di bawah ini dalam satuan SI untuk data yang ditanyakan isi dengan x")

    subbab = float(input("""1 : GLB
2 : GLBB
3 : GMB"""))
    
    if(subbab==1):
        jarak = input("Masukkan jarak dalam m : ")
        kecepatan = input("masukkan kecepatan dalam m/s : ")
        waktu = input("Masukkan waktu dalam s : ")
        
        if(jarak=="x"):
            print(str(float(kecepatan)*float(waktu)))
        elif(kecepatan=="x"):
            print(str(float(jarak)/float(waktu)))
        elif(waktu=="x"):
            print(str(float(jarak)/float(kecepatan)))

    elif(subbab==2):
        print("termasuk dalam subbab apakah soalmu itu?")
        