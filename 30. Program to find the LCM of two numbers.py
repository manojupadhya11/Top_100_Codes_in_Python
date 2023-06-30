#Program to find the LCM of two numbers
import math

num1 = int(input("Enter a Number 1  "))
num2 = int(input("Enter a Number 2  "))

max = max(num1, num2)

for i in range(max, num1 * num2):
    if i%num1==0 and i%num2 ==0:
        lcm = i
        break
print("LCM of",num1,"and",num2,"is", lcm)
