#Program to Replace all 0's with 1's in a given integer number as user input

num1 = int(input("Enter value for num1: "))
num2 = 0

if num1 == 0:
    num2 = 1 

while num1 > 0:
    rem = num1%10
    if rem ==0:
        rem = 1
    num1 //= 10
    num2 = num2*10+rem

num = 0   
while num2 > 0:
    r = num2%10
    num = num*10+r
    num2 //= 10
    
print("The number after conversion is", num)