nama = input('Siapa nama anda ? ')

if len(nama) > 50:
    print('Nama terlalu panjang')
elif len(nama) < 3:
    print('Nama terlalu pendek')
else:
    print('Nama sudah oke')