#Program to find sum of digits in a number 

def getsum(num, sum):
    while(num!=0):
        sum += num%10
        num = int(num/10)
    return sum
   

if __name__ == "__main__":
    num = int(input('Enter the number ' ))
    sum = 0;
    print("the sum of of digits is ", getsum(num, sum))   
