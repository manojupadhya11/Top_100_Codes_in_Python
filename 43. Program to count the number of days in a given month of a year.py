# Program to count the number of days in a given month of a year

year = int(input("Enter year "))
month = int(input("Enter Month Number "))
if((month == 2) and ((year%400==0)or(year%100!=0) and (year%4==0))):
    print("Number of days is 29")
elif(month == 2):
    print("Number of days is 28")
elif (month ==1 or month ==3 or month ==5 or month==7 or month==8 or month==10 or month ==12):
    print("Number of days is 31")
elif(month ==4 or month==6 or month==9 or month==11):
    print("Number of days is 30")


