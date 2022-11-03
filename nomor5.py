"""
" Menghitung SKS mata kuliah
"
" Input: NA, NB, NC, ND, NE
" Output: Nilai rata-rata
"
" Asumsi, NA, NB, NC, ND, NE adalah bilangan bulat
"""

# Mengambil semua input
na = int(input("Masukan NA: "))
nb = int(input("Masukan NB: "))
nc = int(input("Masukan NC: "))
nd = int(input("Masukan ND: "))
ne = int(input("Masukan NE: "))

# Menghitung nilai rata-rata
nr = (na * 4 + nb * 3 + nc * 2 + nd)/(na+nb+nc+nd+ne)

print(f"Nilai rata-rata = {nr}")
