my_int = 10
my_float = 10.0
my_float2 = float(10)
my_string = "10"

#combination
x = 20
y = float(40)
z = x + y
print (z)

a = "my "
b = "name "
c = "is blitz"
d = a+b+c
print (d)

m, n = 10, 3
print (m, n)

#latihan
ini_string = "latihan python"
ini_integer = 20
ini_float = float(50)

#untuk statement pastikan pakai = 2 kali
if ini_string == "latihan python":
    print("String: %s" % ini_string)
if isinstance(ini_integer, int) and ini_integer == 20:
    print("Integer: %s" % ini_integer)
if isinstance(ini_float, float) and ini_float == float(50):
    print("Float: %s" % ini_float)