#Program to find the smallest and largest element in the given array 
import sys
def getsecondsmallest(arr, len):
    small = arr[0]
    for i in range(0,len):
        if(arr[i]<small):
            small = arr[i]
        
    sec_small = sys.maxsize
    for i in range(0,len):
        if(arr[i] != small and arr[i]<sec_small):
            sec_small = arr[i]
    print("The second Smallest element in the given array",sec_small)
    
arr = [10,20,5,9,1,2,5,6,8,98,7,5,6,9,8,20,8,98]
len = len(arr)
getsecondsmallest(arr, len)


