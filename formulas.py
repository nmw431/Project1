import sys
import random

def add(values):
    #add positive numbers
    total = 0
    for value in values:
        value = float(value)
        
        if value > 0:
            total = total + value
    return total
    
def subtract(values):
    #add negative numbers
    total = 0
    for value in values:
        value = float(value)
        
        if value < 0:
            total = total + value
    return total

def multiply(values):
    product = 1
    for value in values:
        value = float(value)
        
        if value != 0:
            product = product * value
    return product

def divide(values):
    divisor = float(values[0])
    values = values[1:]
    for value in values:
        value = float(value)

        if value == 0:
            sys.exit("Cannot divide by 0.")
        else:
            divisor = divisor / value
    return divisor
     
def choose(values):
    return float(values[random.randint(0, len(values) - 1)])
