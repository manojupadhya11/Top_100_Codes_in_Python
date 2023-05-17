#Program to find reverse of user input number

def getreverse(num, rev):
    rem = 0
    reverse = 0
    while(num!=0):
         rem = int(num)%10
         reverse = reverse*10+rem
         num = int(num/10)
    return reverse

if __name__ == "__main__":
    num = int(input('Enter the number ' ))
    rev = 0
    print("the reverse of given number is ")
    print(getreverse(num, rev))
