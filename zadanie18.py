import math

def is_first_value(val):
    for i in range(2, val):
        if val % i == 0:
            return False
    return True

print(is_first_value(2))