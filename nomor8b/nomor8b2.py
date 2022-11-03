"""
" Prakiraan populasi
"
" Input : x
" Output : Prakiraan populasi
"
" Asumsi x adalah bilangan bulat > 0
"""

# Konstanta
N = 100
K = 0.015
P0 = 1.2

# Input
x = int(input("Nilai x = "))

# Perhitungan nilai e
invers_factorial = 1
e = 1

for i in range(N):
    invers_factorial *= 1/(i+1)
    e += invers_factorial

# Perhitungan dan output
print("Perkiraan populasi penduduk kota A")

for i in range(x):
    prakiraan = P0 * (e ** (K * (i+1)))
    print(f"Tahun ke-{i+1} : {prakiraan} juta")
