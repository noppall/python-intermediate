#*args atau argument digunakan untuk menggantikan parameter yang banyak dan panjang
def jumlah(*args):
    return sum((args))

print(jumlah(1,2,3,4,5,6,7,8,9))

#**kwargs adalah keywords argument berisi dictionary
def definisikan(**kwargs):
    print(kwargs)

definisikan(jerapah="tinggi")
