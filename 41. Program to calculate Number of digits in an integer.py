# Program to calculate Number of digits in an integer
temp = 0
count = 0
number = int(input("Enter a Numbe "))
temp = number
while(number > 0):
    number = number //10
    count += 1
print("The count of digits in ",temp,"integer is: ", count)
    
    