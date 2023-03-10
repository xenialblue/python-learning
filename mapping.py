from functools import reduce

numbers = [1,2,3,4,5,6,7,8,9]
expenses = [
    ("Dinner", 80),
    ("Car Repair", 120)
]

def double(a):
    return a * 2

def isEven(n):
    return n % 2 == 0

sum = reduce(lambda a, b : a[1] + b[1], expenses)

result = map(double, numbers)
even = filter(isEven, numbers)

print(list(result))
print(list(even))
print(sum)
