# Write a Python program to perform following operation on given string input:
# a) Count Number of Vowel in given string
# b) Count Length of string (do not use Len ())
# c) Reverse string
# d) Find and replace operation
# e) check whether string entered is a palindrome or not

#a
a=input("enter the string")
count=0
for i in a:
    if i in "aeiouAEIOU":
        count+=1
print("number of vowels in given string is",count)
#b
count=0
for i in a:
    count+=1
print("length of string is",count)
#c
print("reverse of string is",a[::-1])
#d
b=input("enter the string to be replaced")
c=input("enter the string to be replaced with")
print("after replacing",a.replace(b,c))
#e
# check if the string is a palindrome
is_palindrome = True
for i in range(count//2):
 if a[i] != a[count-1-i]:
    is_palindrome = False
 break
if is_palindrome:
 print("The string is a palindrome")
else:
 print("The string is not a palindrome")