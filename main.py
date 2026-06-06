# Simple Calculator by Natnael

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Welcome to my Simple Calculator!")
print("Addition: 5 + 3 =", add(5, 3))
print("Subtraction: 10 - 4 =", subtract(10, 4))
print("Multiplication: 6 x 7 =", multiply(6, 7))
print("Division: 15 / 3 =", divide(15, 3))
