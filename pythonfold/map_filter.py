def kali10(bilangan):
    return bilangan*10

print(kali10(10))

kumpulan = [10,11,20,21,30]
for i in map(kali10, kumpulan):
    print(i)

hasil = list(map(kali10, kumpulan))
print(hasil)

def cekgenap(angka):
    return angka%2 == 0

hasilnya = list(filter(cekgenap, kumpulan))
print(hasilnya)

fungsiku = lambda x: x*2
print(fungsiku(3))