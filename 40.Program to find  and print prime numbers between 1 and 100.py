# Program to find prime numbers in between range

def isprime(num):
    if num < 2:
        return 0
    else:
        x = int(num/2)
        for i in range (2,x):
            if num %i == 0:
                return 0
    return 1 

lower = int(input("Enter the lower range "))    
upper = int(input("Enter the upper range "))    
for i in range(lower,upper):
    if isprime(i):
        print(i, end = " ")
    