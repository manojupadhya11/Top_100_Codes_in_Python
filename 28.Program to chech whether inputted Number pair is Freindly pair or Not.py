#Program to chech whether inputted Number Abundant Number or Not

def getdivisorsum(num):
    sum = 0
    for i in range(1,num):
        if num %i == 0:
            sum +=i
    return sum
num1 = int(input("Enter a Number 1  "))
num2 = int(input("Enter a Number 2  "))

sum1 = getdivisorsum(num1)
sum2 = getdivisorsum(num2)

if(sum1/num1 == sum2/num2):
    print(num1, num2, "are Freindly pair")
else:
    print(num1, num2, "are not Freindly pair")

    
