#Yoan Adhitama
#UG12_A_71210814

#Variabel
a = [] #Nama
b = [] #Nomor Kursi
C = 0

#Case
while(C < 1) :
    x = input("Masukkan nama : ")
    if x == "STOP" :
        break
    else:
        y = int(input("Masukkan nomor kursi " + x + " : "))

    if y in b :
        print("Mohon maaf kursi tersebut telah terisi!")
    else :
        a . append(x)
        b . append(y)

print("\n List kursi yang telah terisi : ")

for xy in range (0,len(b), 1 ) :
    print("Kursi nomor", b [xy], "telah diisi oleh", a [xy])