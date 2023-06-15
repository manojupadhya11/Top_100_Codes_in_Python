#Program to find factorial of a number
def getfactorial(num):
    if num == 0:
        return 1
    else:
        return num*getfactorial(num-1)

number = int(input("Enetr the number to find its factorial "))
fact = getfactorial(number)
print("Factorial of ", number, "is :", fact)
