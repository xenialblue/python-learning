from enum import Enum
no1 = 2+3j
no2 = complex(2,3)

print(no2.real, no2.imag)
print(round(5.6))
print(abs(-2.5))

class State(Enum):
    ACTIVE = 1
    INACTIVE = 0
    
print(State.ACTIVE.value)
print(list(State))
print(len(State))