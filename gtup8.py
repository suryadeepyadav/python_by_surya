#Write a Python program to check if the number provided by the user is a palindrome or
#not.
# 121 = 121  3549534759834
# 123 = 321
num=int(input("enter the number")) #121
temp=num
rev=0  #121
while temp>0:
    digit=temp%10  #1 2 1
    rev=rev*10+digit #0*10+1=1 1*10+2=12 12*10+1=121
    temp//=10 #12 1 0
if num==rev:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")
