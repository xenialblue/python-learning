class NumberHolder:
    def __init__(self, number):
        self.number = number
        
    def returnNumber(self):
        return self.number
    
var = NumberHolder(7)
print(var.returnNumber())

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "Red"
car1.kind = "Convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "Blue"
car2.kind = "Van"
car2.value = 10000.00

print(car1.description())
print(car2.description())