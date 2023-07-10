#Program to find the smallest element in the given array 
import math
def getsmallest(arr, len):
    small = arr[0]
    for i in range(0,len):
        if(arr[i]<small):
            small = arr[i]
    
    return small
    
arr = [10,20,5,9,1,5,6,8,98,7,5,6,9,8,20,8,98]
len = len(arr)
smallest = getsmallest(arr, len)
print("The largest element among the given array is", smallest)

