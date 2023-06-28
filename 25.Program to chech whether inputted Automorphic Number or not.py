#Program to chech whether inputted Automorphic Number or not
import math
num = int(input("Enter a Number to check for perfect square or Not "))
square = pow(num, 2)
mod = pow(10, len(str(num)))

if square%mod == num:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")
    
