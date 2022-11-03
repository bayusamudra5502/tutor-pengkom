"""
" Prediksi Alel
"
" Input : Ix, Iy
" Output : Golongan darah anak
"
" Asumsi, Ix dan Iy hanya menerima IA, IB, dan IO
"""

# Ambil input dari layar
ix = input("Ix = ")
iy = input("Iy = ")

# Menentukan golongan darah anak
golongan_darah_anak = ""

if ix == "IA":
    if iy == "IB":
        golongan_darah_anak = "AB"
    else:
        golongan_darah_anak = "A"
elif ix == "IB":
    if iy == "IA":
        golongan_darah_anak = "AB"
    else:
        golongan_darah_anak = "B"
else:
    if iy == "IA":
        golongan_darah_anak = "A"
    elif iy == "IB":
        golongan_darah_anak = "B"
    else:
        golongan_darah_anak = "O"

# Print solusi
print(f"Golongan darah anak = {golongan_darah_anak}")
