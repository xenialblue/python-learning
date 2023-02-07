#boolean operator ("TRUE" or "FALSE")
x = 2
print(x == 2)
print(x == 3)
print(x < 3)

#condition with boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("His name is John and he is 23 years old")
    
if name == "John" or name == "Rick":
    print("His name is Rick or John")
    
#"in" operators
nama = "John"
if nama in ["John", "Rick"]:
    print("Your name is John or Rick")
    
#contoh indentasi
x = 2
if x <= 2:
    print("Benar")
else:
    print("Salah")
    
#"IS" Operator
x = [1,2,3]
y = [1,2,3]
print(x == y)
print(x is y)

#"NOT" operator
print(not False)
print((not False) == (False))

#Exercise
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")
    
if len(second_array) == 2:
    print("3")
    
if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")