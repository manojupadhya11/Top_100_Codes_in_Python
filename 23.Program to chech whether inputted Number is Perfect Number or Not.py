#Program to chech whether inputted Number is Perfect Number or Not


num = int(input("Enter a Number to check for Strong Number or Not "))
sum = 0
for i in range(1, num):
    
    if num % i == 0:
        sum += i
if(sum==num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
    
