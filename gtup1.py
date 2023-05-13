#Write a Python Program to Convert Celsius to Fahrenheit and vice –a-vers

def ctof(c):
    return (c * 9/5) + 32
def ftoc(f):
    return (f - 32) * 5/9
print("ctof",ctof(65))
print("ftoc",ftoc(213))

