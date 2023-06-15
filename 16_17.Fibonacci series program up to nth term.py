#Program to find fibonacci series upto nth term
a=0
b=1
nextTerm = 0
n = 10
print("Fibonacci Series:", a, b, end = " ")
for i in range(2, n):
    nextTerm = a + b 
    a=b 
    b= nextTerm
    print(nextTerm, end = " ")
