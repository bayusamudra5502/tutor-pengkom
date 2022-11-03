a = float(input("a = "))  # Bilangan rill
b = float(input("b = "))
x = float(input("x = "))
n = int(input("n = "))  # Bilangan bulat

# Inisialisasi
sum = 0

for i in range(1, n+1):  # Kita iterasi dari 1 sampai n
    polinom = a * (x ** i) + b  # a x^i + b
    sum = sum + polinom

print(f"Hasil = {sum}")
