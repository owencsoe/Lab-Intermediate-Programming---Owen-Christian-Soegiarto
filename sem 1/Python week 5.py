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


  
