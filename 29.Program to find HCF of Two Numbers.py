#Program to find HCF of Two Numbers


num1 = int(input("Enter a Number 1  "))
num2 = int(input("Enter a Number 2  "))
hcf = 1;
for i in range(1, num1 and num2):
    if num1%i==0 and num2%i ==0:
        hcf = i
print("HCF of",num1,"and",num2,"is", hcf)

    
