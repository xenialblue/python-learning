cukup = False
tidak = True
harga = 1000000

if cukup:
    jumlah = 0.1 * harga
    print(f"Biaya: ${jumlah}")
elif tidak:
    jumlah = 0.2 * harga
    print(f"Biaya: ${jumlah}")
else:
    print("Silahkan Coba Lagi")
print("Terimakasih")