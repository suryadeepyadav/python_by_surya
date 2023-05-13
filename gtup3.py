# Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal

# take decimal number as input
decimal = int(input("Enter a decimal number: "))
# convert decimal to binary, octal, and hexadecimal
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
# print the results
print(f"The binary representation of {decimal} is: {binary}")
print(f"The octal representation of {decimal} is: {octal}")
print(f"The hexadecimal representation of {decimal} is: {hexadecimal}")