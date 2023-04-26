#Program to calculate the sum of number in range via for loop

num1 = int(input("Enter the value of num1 "))
num2 = int(input("Enter the value of num2"))
sum = 0
for i in range(num1, num2+1):
    sum+=i
print(sum)


#Program to calculate the sum of number in range via formula

num1 = int(input("Enter the value of num1 "))
num2 = int(input("Enter the value of num2 "))
sum = 0
sum = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print(sum)

    