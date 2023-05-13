# Write a program in python to find out maximum and minimum number out of three
#user entered number
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if a>b and a>c:
    print("a is maximum")
elif b>a and b>c:
    print("b is maximum")
else:
    print("c is maximum")

# for minimum number
if a<b and a<c:
    print("a is minimum")
elif b<a and b<c:
    print("b is minimum")
else:
    print("c is minimum")