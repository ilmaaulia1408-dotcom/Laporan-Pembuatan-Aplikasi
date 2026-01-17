# Nama : ILMA AULIA
# NPM : 250305005
# Kelas : 1b (Pendidikan Informatika)
# Dsen Pengampu : Hery Kuswanto, M.Pd.


print("Program Menghitung Keliling  & Luas Bngun Datar") 
print("-----------------------------------------------")
print('[1] Keliling dan Luas Persegi')
print('[2] Keliling dan Luas Persegi Panjang')
print('[3] Keliling dan Luas Segitiga')
print('[4] Keliling dan Luas Lingkaran')
print("-----------------------------------------------")
pilihan = int(input('Pilih Salah Satu Program (1-4):'))


if pilihan == 1:
    print('Program Menghitung Keliling & Luas Persegi ')
    print("-------------------------------------------")

    s = int(input('Masukkan nilai Sisi :'))

    luas = s*s
    keliling = 4*s
    print('\nLuasnya = ', str(luas))
    print('keliling =', str(keliling))
    

elif pilihan == 2:
    print('Program Menghitung Keliling & Luas Persegi Panjang')
    print("--------------------------------------------------")

    p = int(input('Masukkan nilai panjang :'))
    l = int(input('Masukkan nilai lebar :'))

    luas = p*l
    keliling = 2*(p+l)
    print('\nLuasnya =', str(luas))
    print('Keliling =', str(keliling))
   

elif pilihan == 3:
    print('rogram Menghitung Keliling & Luas Segitiga')
    print("------------------------------------------")

    a = float(input('Masukkan nilai Alas :'))
    t = float(input('Masukkan nilai Tinggi :'))

    luas = 0.5*a*t
    keliling = a+a+a
    print('\nLuasnya =', str(luas))
    print('Keliling =', str(keliling))
    

elif pilihan == 4:
    print('rogram Menghitung Keliling & Luas Lingkaran')
    print("-------------------------------------------")

    r = float(input('Masukkan nilai Jri-jari :'))

    phi = 3.14
    diameter = 2*r

    luas = phi*r*r
    keliling = phi*diameter
    print('\nLuasnya =', str("%.2f" % luas))
    print('Keliling =', str("%.2f" %keliling))
    

else:
    print("thank you")

