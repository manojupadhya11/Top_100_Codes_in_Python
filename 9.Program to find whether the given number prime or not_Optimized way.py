
    
    
#2. Program to find whether the number is prime or not optimized method
num1 = int(input('Enter the number to check prime or not ' ))
flag = 0
if num1 < 2:
    flag = 1
for i in range(2, int(num1/2)+1):
    if num1%i==0:
        flag = 1
        break
if flag == 1:
    print(num1,"is not prime number")
else:
    print(num1,"is a prime number")