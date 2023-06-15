#Program to find power using base and exponent without builtin function
num = int(input("Enter the number to find its factors "))
print("Factors of number", num, "is:", end = " ")
for i in range(1,num):
    if num%i == 0:
        print(i, end =" ")
