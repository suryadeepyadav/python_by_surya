#Write a program which will allow user to enter 10 numbers and display largest odd
#number from them. It will display appropriate message in case if no odd number is
#found

# take user input for 10 numbers
numbers = []
for i in range(10):
 num = int(input(f"Enter number {i+1}: "))
 numbers.append(num)
# find largest odd number
largest_odd = None
for num in numbers:
 if num % 2 != 0: # check if number is odd
    if largest_odd is None or num > largest_odd:
        largest_odd = num
# print the results
if largest_odd is not None:
 print(f"The largest odd number is {largest_odd}")
else:
 print("No odd number found")