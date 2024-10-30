# Implisit Typecasting
angka = 8
bilangan_koma = 4.2
hasil = angka + bilangan_koma
print(hasil)
print(type(hasil))

# Eksplisit Typecasting
angka_string = '24'
angka_integer = 2

print("Tipe data dari 'angka_string'  sebelum melakukan Typecasting:",type(angka_string))

angka_string = int(angka_string)

print("Tipe data dar 'angka_string' setelah melakukan Typecasting:",type(angka_string))

hasil_penjumlahan = angka_integer + angka_string

print("Hasil:", hasil_penjumlahan)
print("Tipe Data  dari 'hasil_penjumlahan':",type(hasil_penjumlahan))