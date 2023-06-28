#Program to chech whether inputted Number is Perfect Square or Not
import math
def isperfectsquare(x):
    if x >= 0:
        sr = int(math.sqrt(x))
        return (sr * sr ) == x
    return False
    
num = float(input("Enter a Number to check for perfect square or Not "))
if isperfectsquare(num):
    print("Perfect Square Number")
else:
    print("Not a Perfect Square Number")
    
