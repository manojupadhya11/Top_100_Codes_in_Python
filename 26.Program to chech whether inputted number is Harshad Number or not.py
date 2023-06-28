#Program to chech whether inputted number is Harshad Number or not
import math

def isharshad(num):
    temp = num
    sum = 0
    while(temp!=0):
        sum = sum + temp%10
        temp = temp//10
    
    if(num%sum==0):
        print("Harshad Number")
    else:
        print("Not a Harshad Number")

num = int(input("Enter a Number to check for perfect square or Not "))
isharshad(num)
    
