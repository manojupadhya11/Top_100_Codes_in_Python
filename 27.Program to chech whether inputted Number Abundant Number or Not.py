#Program to chech whether inputted Number Abundant Number or Not


num = int(input("Enter a Number to check for Abundant Number or Not "))
sum = 0
for i in range(1,num):
    if num %i == 0:
        sum +=i
if(sum>num):
    print("Abundant Number")
else:
    print("Not an Abundant Number")


    
