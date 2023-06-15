#Program to find the prime factors of the inputted Number
num = int(input("Enter Number to find its prime factors "))
print("Prime Factors of number", num, "is:", end = " ")
for i in range(2,num):
    while num % i ==0:
        print(i, end = " ")
        num /= i

