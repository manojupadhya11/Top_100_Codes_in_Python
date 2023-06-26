#Program to chech whether inputted Number is Strong Number or Not
def getfactorial(n):
    fact = 1 
    for i in range(1, n+1):
        fact = fact * i
    return fact
    
def checkstrong(num):
    sum = 0
    digit = 0
    temp = num
    
    while(temp!=0):
        digit = temp % 10;
        sum = sum + getfactorial(digit);
        temp = temp // 10
    return sum == num
    

num = int(input("Enter a Number to check for Strong Number or Not "))
if(checkstrong(num)):
    print("Strong Number")
else:
    print("Not a Strong Number")
    
