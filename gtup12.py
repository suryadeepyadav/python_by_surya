#Write a program in python to implement Factorial series up to user entered number.
#(Use recursive Function)
#factorial of 5 is 5*4*3*2*1=120
#factorial of 4 is 4*3*2*1=24 ======== 5*4*3*2*1=120
def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1) #5*4*3*2*1=120
    
n=int(input("enter the number"))
if n<0:
    print("enter the positive number")
elif n==0:
    print("factorial of 0 is 1")
else:
    print("factorial of",n,"is",fact(n))

