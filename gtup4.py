#Write a program to make a simple calculator (using functions).

# define functions for basic operations
def add(x, y):
 return x + y
def subtract(x, y):
 return x - y
def multiply(x, y):
 return x * y
def divide(x, y):
 return x / y
# take user input for two numbers and operation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")
# perform operation using functions
if op == '+':
 result = add(num1, num2)
elif op == '-':
 result = subtract(num1, num2)
elif op == '*':
 result = multiply(num1, num2)
elif op == '/':
 result = divide(num1, num2)
else:
 print("Invalid operation")
# print the result
print(f"{num1} {op} {num2} = {result}")
