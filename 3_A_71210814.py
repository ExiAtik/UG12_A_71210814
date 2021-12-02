#Yoan Adhitama
#UG12_A_71210814

#Variabel
a = input("Input : ")
b = len(a)

#Case
print("Output : ")
for x in range(b):
    print(a[:x])
for y in range(b, 0, -1):
    print(a[:y])