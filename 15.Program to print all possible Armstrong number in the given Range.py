#Program to print all possible Armstrong number in the given Range
low  = int(input("Enter the low Range "))
high = int(input("Enter the high Range "))
for num in range(low, high+1):
    length = len(str(num))
    sum = 0 
    temp = num 
    while temp > 0:
        digit = temp%10
        sum += digit**length
        temp //= 10
    if num == sum:
        print(num, end = ", ")
