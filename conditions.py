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
number = 10
second_number = 10
first_array = []
second_array = [1,2,3]

if number > 15:
    print("1")

if