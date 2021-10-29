print("="*50)
print("\tHitung luas dan keliling lingkaran")
print("""\tRumus luas lingkaran = phi*(r*r)
\tRumus keliling lingkaran = 2*phi*r
\tphi = 3.14""")
print("="*50)

r = int(input("Masukan jari-jari : "))
phi = 3.14

luas = phi*(r*r)
keliling = 2*phi*r

print("Luas lingkaran dengan jari-jari {} adalah {} ".format(r, luas))
print("Keliling lingkaran dengan jari-jari {} adalah {} ".format(r, keliling))
print("="*50)
