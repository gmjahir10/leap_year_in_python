year = int(input("Enter to the year to check = "))
if((year%4==0)) and (year%100!=0) or (year%400==0):
    print(year, "Is a leap year")
else:
    print(year,"Is a not leap year")

