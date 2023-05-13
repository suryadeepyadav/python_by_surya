#Write a program in python to implement Fibonacci series up to user entered number.
#(Use recursive Function)
#what is fibonacci series?
#fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers.
#The simplest is the series 1, 1, 2, 3, 5, 8, etc.
#Example: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
#8
#8 
#8-1=7 + 8-2=6
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter the number"))
if n<=0:
    print("enter the positive number")
else:
    print("fibonacci series is =:")
    for i in range(n):
        print(fib(i))



