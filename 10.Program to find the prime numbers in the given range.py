#Program to find whether the number is prime numbers in range

def isprime(num):
    if num < 2:
        return 0
    else: 
        x = int(num/2)
        for i in range(2, x+1):
            if num%i == 0:
                return 0
        
    return 1
    

if __name__ == "__main__":
    num1 = int(input('Enter the low range' ))
    num2 = int(input('Enter the high range' ))
    for i in range(num1, num2):
        
        if isprime(i):
            print(i)


    
    
