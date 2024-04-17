print("   +")
print(" +   +")
print("+-----+")
print("| .-. |")
print("| | | |")
print("+-+-+-+")

##
johnapple = int(input("How many apples does John have?"))   
maryapple = int(input("How many apples does Mary have?"))       
daveapple = int(input("How many apples does Dave have?"))
print ("In total they all have", johnapple+maryapple+daveapple, "apples")

##
year=int(input("What year?"))

if year%4!= 0:
    print("it's a common year!")
elif year%100!=0:
    print("it's a leap year!")
elif year%400!=0:
    print("it's a common year!")
else:
    print("it's a leap year!")

##
    kilometers = 12.25
miles = 7.38

miles_to_kilometers= miles*1.61
kilometers_to_miles = kilometers/1.61

print(miles, "miles is", miles_to_kilometers, "kilometers")
print(kilometers, "kilometers is", kilometers_to_miles, "miles")

##
print("====================")
print("|Table miles to km|")
print("====================")
for i in range(1,101):
    print("|", i*1,"miles| ",round(i*1.61,3),"km  |")

n=2
while n<10:
    n=2*n
    print(n)
print(n)

n=2
while n<10:
    print(n)
    n=2*n
print(n)


number=0
sum=0
while number != -1:
    sum=sum+number
    number = int(input("Enter a positive number or -1 to exit: "))
print(sum)

##

word = "computational"
for letter1 in word:
    count=0
    for letter2 in word:
        if letter1==letter2:
            count=count+1

    if count>1:
        print(letter1,":",count)

##

numberone = int(input("Enter the first number "))
numbertwo = int(input("Enter the second number "))
numberthree = int(input("Enter the third number "))

if numberone==numbertwo==numberthree:
    print("All the same!")
elif numberone!=numbertwo!=numberthree!=numberone:
    print("All different!")
else:
    print("Neither!")
##

temp=40
message_toohot= "weather is too hot, better stay home"
message_hot= "keep in mind of weather hot"
message_good= "let's go out and enjoy the good weather!"
if temp > 40:
    print(message_toohot)
else:
    if temp < 33:
        print (message_good)
    else:
        print(message_hot)

##

while True:
    oriprice = int(input("What's the price?"))

    disc20= round(oriprice*0.2)
    disc30= round(oriprice*0.3)
    disc70= round(oriprice*0.7)

    finalprice20 = oriprice - disc20

    finalprice30 = oriprice - disc30

    finalprice70 = oriprice - disc70
    
    if oriprice == 0:
        print("Thank You!")
        break
    else:
        print("Price after 20% discount =", finalprice20, "$")
        print("Price after 30% discount =", finalprice30, "$")
        print("Price after 70% discount =", finalprice70, "$")
 