#Program to calculate the sum of first n natural number

def getSum(n):
    sum = 0
    for i in range(n-1):
        sum = sum+n
    return sum
    
if __name__ == "__main__":
    n = int(input("Enter the value of n "))
    print(getSum(n))