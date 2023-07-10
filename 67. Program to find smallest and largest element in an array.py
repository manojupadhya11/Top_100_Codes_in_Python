#Program to find the smallest and largest element in the given array 
import math
def getsmallestlargest(arr, len):
    large = small = arr[0]
    for i in range(0,len):
        if(arr[i]<small):
            small = arr[i]
        if(arr[i]>large):
            large = arr[i]
    print("The largest element in the given array",large)
    print("The Smallest element in the given array",small)
    
arr = [10,20,5,9,1,5,6,8,98,7,5,6,9,8,20,8,98]
len = len(arr)
getsmallestlargest(arr, len)


