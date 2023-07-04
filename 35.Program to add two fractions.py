# Program to add two fractions 


numerator1 = int(input("Enter value for numerator1: "))
denominator1 = int(input("Enter value for denominator1: "))
numerator2 = int(input("Enter value for numerator2: "))
denominator2 = int(input("Enter value for denominator2: "))

x = (numerator1*denominator2)+(numerator2*denominator1)
y = denominator1*denominator2

for c in range(1,min(x,y)):
    if x%c ==0 and y%c == 0:
        gcd_no = c
print(numerator1 ,"/",denominator1 ,"+",numerator2 ,"/",denominator2 ,"=",int(x/gcd_no),"/", int(y/gcd_no))