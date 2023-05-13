#Write a Python program to check if the number provided by the user is an Armstrong
#number.
# 153 = 1*1*1 + 5*5*5 + 3*3*3 =1+125+27=153
# 234 = 2*2*2 + 3*3*3 + 4*4*4 =8+27+64=99

num=int(input("enter the number")) #153  153%10=3 15%10=5 1%10=1 0%10=0
sum=0 #0+27+125+1=153
temp=num #153
while temp>0: #153>0 15>0 1>0 0>0 
    digit=temp%10 #3 5 1 
    sum+=digit**3 #27+125+1 =153  
    temp//=10 #15 1 0 153//10=15 15//10=1 1//10=0
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")



