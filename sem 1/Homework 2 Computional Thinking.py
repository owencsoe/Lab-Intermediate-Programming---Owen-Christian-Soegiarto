year=int(input("What year?"))

if year%4!= 0:
    print("it's a common year!")
elif year%100!=0:
    print("it's a leap year!")
elif year%400!=0:
    print("it's a common year!")
else:
    print("it's a leap year!")