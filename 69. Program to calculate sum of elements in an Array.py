#Program to calculate sum of given array

def getsum(arr, len):
    sum = 0
    for i in range(0,len):
        sum = sum+arr[i]
    
    print("The Sum of elements in an array is ", sum)
    
arr = [10,20,5,9,1,2,5,6,8,98,7,5,6,9,8,20,8,98]
len = len(arr)
getsum(arr, len)


