numbers = [1,2,3]

def double(a):
    return a * 2

def isEven(n):
    return n % 2 == 0

result = map(double, numbers)
even = filter(isEven, numbers)

print(list(result))
print(list(even))

