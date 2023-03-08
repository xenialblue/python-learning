def my_function(nama = "Halo ", umur = "Kawan"):
    nama = input("Isi Nama Anda : ")
    umur = input("Umur Anda : ")
    print("Halo " + nama + " Umur kamu " + umur + " Tahun")
    
my_function()

#Nested Function
def talk(phrase):
    def say(word):
        print(word)
        
    words = phrase.split(" ")
    for word in words:
        say(word)
        
talk("I'm going to buy a milk today")

#Memanggil Variabel diluar Function Local menggunakan perintah NONLOCAL
def count():
    jumlah = 0
    
    def increment():
        nonlocal jumlah
        jumlah = jumlah + 1
        print(jumlah)
        
    return increment
    
increment = count()