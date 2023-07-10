#Program to find the largest element in the given array 
import math
def getlargest(arr, len):
    max = arr[0]
    for i in range(0,len):
        if(arr[i]>max):
            max = arr[i]
    
    return max
    
arr = [10,20,5,9,0,5,6,8,98,7,5,6,9,8,20,8,98]
len = len(arr)
large = getlargest(arr, len)
print("The largest element among the given array is", large)

