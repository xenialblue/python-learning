berat = input('Berat Badan : ')
tipe = input('(L)bs atau (K)g : ')

if tipe.upper() == "L":
    bb = int(berat) * 0.45
    print(f"Berat Badan {bb} Kilo")
elif tipe.upper() == "K":
    bb = int(berat) / 0.45
    print(f"Berat Badan {bb} Lbs")
else:
    print('Input tidak diketahui')