#Program to check whether inputted number is Armstrong or not
number  = int(input("Enter the Number to check for Armstrong or not "))
num = number
digit, sum = 0, 0
length = len(str(num))
for i in range(length):
    digit = int(num%10)
    num = num/10
    sum = sum + pow(digit,length)
    
if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong Number")