ix = input("ix = ")
iy = input("iy = ")

# Inisialisasi
gol_darah_anak = ""

if ix == "IA":
    if iy == "IA":
        gol_darah_anak = "A"
    elif iy == "IB":
        gol_darah_anak = "AB"
    else:  # iy == "IO"
        gol_darah_anak = "A"
elif ix == "IB":
    if iy == "IA":
        gol_darah_anak = "AB"
    elif iy == "IB":
        gol_darah_anak = "B"
    else:  # iy == "IO"
        gol_darah_anak = "B"
else:  # ix == "IO"
    if iy == "IA":
        gol_darah_anak = "A"
    elif iy == "IB":
        gol_darah_anak = "B"
    else:  # iy == "IO"
        gol_darah_anak = "O"

print(f"Gol darah anak = {gol_darah_anak}")
