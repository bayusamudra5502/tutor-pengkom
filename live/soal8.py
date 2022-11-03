x = int(input("X = "))

# Nilai euler
"""
Trik inisialisasi:
1. Kalau penjumlahan, si penyimpan jumlah totalnya inisialisasi dulu sama 0
2. Kalau perkalian, si penyimpan hasil total perkalian inisialisasi sama 1
"""
# Inisialisasi
e = 0
faktorial = 1

# Perhitungan nilai e
e = e + 1

for i in range(1, 100 + 1):
    faktorial = faktorial * i
    e = e + 1/faktorial

# Prediksi
P0 = 1.2
k = 0.015

print("Perkiraan populasi penduduk A")
for t in range(1, x+1):
    prediksi = P0 * (e ** (k*t))
    print(f"Tahun ke-{t} : {prediksi} juta")
