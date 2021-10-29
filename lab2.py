a = input("masukan nilai a : ")
b = input("masukan nilai b : ")
print("variable a = ", a)
print("variable b = ", b)
print("Hasil penggabungan {1}&{0}=%s".format(a, b) % (a+b))

# konversi nilai variable
a = int(a)
b = int(b)
print("hasil penjumlahan {1}+{0}=%s".format(a, b) % (a+b))
print("hasil pembagian {0}/{1}=%d".format(a, b) % (a/b))
