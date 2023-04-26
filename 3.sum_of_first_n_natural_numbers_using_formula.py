#Program to calculate the sum of first n natural number using formula

def getSum(n):
    sum = n*(n+1)/2
    return int(sum)
if __name__ == "__main__":
    n = int(input("Enter the value of n "))
    print(getSum(n))