#Write a program in python to swap two variables without using temporary variable

# take two variables
a = 5
b = 10
# print original values
print("Before swapping:")
print(f"a = {a}")
print(f"b = {b}")

# swap the values
a = a + b #5+10=15
b = a - b #15-10=5
a = a - b #15-5=10
# print swapped values
print("After swapping:")
# print(f"a = {a}")
# print(f"b = {b}")
print("a is = ",a)
print("b is = ",b)
