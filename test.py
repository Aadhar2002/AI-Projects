# Create a function that calculates BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
print(calculate_bmi(70, 1.75))

#create a function that checks if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
print(is_prime(7))

#create a simple calculator with add, subtract, multiply, and divide functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
print(add(5, 3))
