#Yoan Adhitama
#UG12_A_71210814

#Variabel
a = input("Masukkan deret angka : ")
b = a . split(",")
c =  0
bil = ''

#Case
for x in b :
    if int(x) % 2 == 0 :
        angka = 0 + int(x)
    else :
        angka = 0 - int(x)
    c = c + angka
print("Total: ", end = '')

for y in b :
    if int(y) % 2 == 0 :
        angka = ("+" + str(y) + " ")
    else :
        angka = ("-" + str(y) + " ")
    bil += angka
if bil[0] == "+" :
    print(bil[2 : len(bil)])
else :
    print(bil)

#Hasil case
print("Hasil perhitungan di atas ialah: ", c )