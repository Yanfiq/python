print("selamat datang di penerjemah QDJY")
import time
time.sleep(2)
#dictionary qdjy
qdjy = {" ":" ", "a":"4", "b":"B", "c":"tj", "d":"the", "e":"3", "f":"v", "g":"6", "h":"kh", "i":"y", "j":"dj", "k":"q", "l":"l", "m":"m", "n":"n", "o":"oo", "p":"v", "q":"q", "r":"12", "s":"x", "t":"7", "u":"w", "v":"v", "w":"u", "x":"s", "y":"i", "z":"s"}

#input text
text = str(input("masukkan teks disini:"))

#terjemahkan
y = []
for i in text:
    y.append(qdjy[i])

print(''.join(map(str, y)))

