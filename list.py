matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item)

#list number and string
angka = []
huruf = []
nama = ["Jonathan", "Vincent", "Joe"]

angka.append(1)
angka.append(2)
angka.append(3)

huruf.append("satu")
huruf.append("dua")

nama_kedua = nama[1]
print(angka)
print(huruf)
print(repr(angka))
print("Nama kedua dari list adalah %s" % nama_kedua)

dogs = ["Roger", "Syd", "Quincy", "james"]
dogs[1] = "Beau" #menggantikan salah satu index yang ada di atas
dogs.extend(["Walt", "Lea"]) # menambah isi untuk index diatas atau menggunakan perintah +=
dogs.remove("Quincy")
dogs[1:1] = ("Jo", "Fabio")
dogscopy = dogs[:]
dogs.sort(key=str.lower)
print(sorted(dogs, key=str.lower))
print(dogs)
print(dogscopy)