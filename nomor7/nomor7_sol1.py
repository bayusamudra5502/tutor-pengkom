"""
" FUngsi f(x)
"
" Input : a, b, x, n
" Output : Hasil dari f(x). Lihat soal
"
" Asumsi, n > 0. 
" a,b,x adalah bilangan pecahan 
" n adalah bilangan bulat
"""

# Input
a = float(input("Nilai a = "))
b = float(input("Nilai b = "))
x = float(input("Nilai x = "))
n = int(input("Nilai n = "))

# Proses
hasil = 0

for i in range(1, n+1):
    hasil += a * (x ** i) + b

# Output
print(f"Hasil = {hasil}")
