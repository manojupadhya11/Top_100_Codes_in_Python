#Program to calculate the sum of first n natural number using recursion

def getSum(n):
    if n == 1:
        return 1
    return n + getSum(n-1)
    
if __name__ == "__main__":
    n = int(input("Enter the value of n "))
    print(getSum(n))