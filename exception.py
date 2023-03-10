try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divided by Zero')
finally:
    result = 1
    
print(result)

class DogNotFound(Exception):
    pass

try:
    raise DogNotFound()
except DogNotFound:
    print("dog not found")
    
filename = 'draw.py'

with open (filename, 'r') as file:
    content = file.read()
    print(content)