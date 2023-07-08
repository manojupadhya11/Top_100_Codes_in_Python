#Program to find the occurence of a digit in a given user input Number
number = int(input("ENter the Number "))
digit = int(input("Enter the digit to find its occurences "))
temp = number
count = 0
while(number>0):
    rem = int(number%10)
    if rem == digit:
        count= count +1
    number = number // 10

print("the digit",digit,"in number",temp,"occurs",count,"Times")

