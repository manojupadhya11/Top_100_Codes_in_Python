#Program to find sum of digits in a number using recursion

def getsum(num, sum):
    if num == 0:
        return sum

    sum += num%10
    return getsum(int(num/10), sum)
    

if __name__ == "__main__":
    num = int(input('Enter the number ' ))
    sum = 0;
    print("the sum of of digits is ", getsum(num, sum))   
