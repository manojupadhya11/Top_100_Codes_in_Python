#Program to check whether given nmber is palindrome or not

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
    
    revrse_num = getreverse(num, rev)
    if num == revrse_num:
        print("Palindrome Number")
    else:
        print("Not a Palindrome Number")