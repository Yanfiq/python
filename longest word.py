txt = input()

#fungsi buat ngilangin koma
def removecommas(x):
    return x.rstrip(",")

#misah-misah teks nya + ngilangin koma
x = (txt.split(" "))
word = list(map(removecommas, x))

#nyari jumlah per kata
y = []
for i in word:
    jumlah=len(i)
    y.append(jumlah)

#nyari kata terpanjang
z = max(y)

#print kata terpanjang
for i in x:
    if len(i) == z:
        print(i)
    else:
        None