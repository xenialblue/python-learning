class kelas:
    variable = "tes"
    
    def function(self):
        print("Pesan dari Kelas")
        
myobjectx = kelas()
myobjecty = kelas()

myobjecty.variable = "kitty"

print(myobjectx.variable)
print(myobjecty.variable)
myobjectx.function()