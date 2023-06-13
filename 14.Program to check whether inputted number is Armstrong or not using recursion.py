#Program to check whether inputted number is Armstrong or notusing recursion
number  = int(input("Enter the Number to check for Armstrong or not "))
num = number
sum = 0
length = len(str(num))
def checkarmstrong(num, length, sum):
    if int(num) == 0:
        return sum
    digit = int(num%10)
    sum = sum + pow(digit,length)
    return checkarmstrong(num/10, length,sum)
if checkarmstrong(num, length, sum) == number:
    print("Armstrong")
else:
    print("Not Armstrong Number")