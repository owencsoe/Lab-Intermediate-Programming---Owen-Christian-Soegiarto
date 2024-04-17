def cubeVolume(sideLength):
    volume = sideLength**3
    return volume

result1=cubeVolume(2)
result2=cubeVolume(10)

print("A cube with side length 2 has volume", result1)
print("A cube with side length 10 has volume", result2)

##

def cubeVolume(sideLength):
    volume = sideLength**3
    return volume

length= float(input("Enter side length of cube:"))
result1=cubeVolume(length)
result2=cubeVolume(10)

print("A cube with side length", length, "has volume", result1)
print("A cube with side length 10 has volume", result2)

#Find the sum of integers from 1 to 10, from 20 - 27, and from 35 to 49, respectively.
def summ(awal, akhir):
    sum=0
    for i in range(awal, akhir):
        sum = sum + i
    return sum

print("Sum of integer from 1 to 10:" ,summ(1, 11))
print("Sum of integer from 20 to 38:",summ(20, 38))
print("Sum of integer from 35 to 50:",summ (35, 50))


def summ(v1, v2):
    sum=0
    for i in range(v1, v2):
        sum = sum + i
    return sum
print("Sum of integer from 1 to 10:" ,summ(1, 11))
print("Sum of integer from 20 to 38:",summ(10, 101))
print("Sum of integer from 35 to 50:",summ (5, 101, 5)) 
##

def greeting(first,sec):
    print("Hello my name is", first , sec)

first1= input("Enter your first name!")
sec2= input("Enter your last name!")

greeting(first1 , sec2)

##
def cubeVolume(sideLength):
    if(sideLength < 0):
        return 0
    return sideLength**3

##
def maxx(num1,num2):
    return max(num1,num2)

def avg(num1,num2):
    return (num1+num2)/2
	#return average of num1 and num2

print("Maximum and average of 2 and 5 is",maxx(2,5),avg(2,5))
print("Maximum and average of 10 and 100 is",maxx(10,100),avg(10,100))
