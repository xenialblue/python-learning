testing = 'Sebuah kalimat untuk pengingat'
kedua = testing[1:-1]
print(kedua)

#string format bisa pakai variabel
x = "Nanda"
print("My Name, %s!" % x)

#dua argumen untuk string dalam variabel
nama = "nanda"
umur = 23
print("%s berumur %d tahun. " % (nama, umur))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s your current balance is $%s"
print(format_string % data)

