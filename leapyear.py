n = int(input("Enter a year : "))
if(n%4==0 or n%100==0 or n%400==0):
    print("leap year")
else:
    print("Not a leap year")