#Tuples
numbers = (1,2,3,4,5)

##
pets={}
pets["Adam"]="cat"
pets["Mark"]="dog"
pets["James"]="turtle"
print(pets)
print(pets["Adam"])
##

dictionary = {"cat":"chat","dog":"chien","horse": "cheval"}
for english, french in dictionary.items():
    print(english,">>",french)
for french in dictionary.values():
    print(french)

## Write a code to input following student grade to dictionary, input done by user.
classs={}
while True:
    name = input("Enter your name (enter 0 to stop): ")
    if name == "0":
        break
    grade = int(input("Enter your grade: "))
    classs[name] = grade

    print(classs)

##
while True:
    grade = int(input("Enter your grade: "))
    if 0<= grade >100:
        break  
    
##Week 10
    
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

##Week 12

balance = 10000 #global balance

def withdraw(amount):
    global balance
    if balance >= amount:
        balance = balance - amount

withdraw(1000)
print (balance)

##

def multiply(values, factor):
    for i in range(len(values)):
        values[i] = values[i] * factor
values = [1,2,3,4,5]
multiply(values,3)
print (values)

##
def multiply(values, factor):
   values = values * factor
values = 4
multiply(values,3)
print (values)

##
def main():
    x = 3 
    print (computeResults(x + 1 ))

def computeResults(value):
    results = value**2
    results = results + 3
    return results

main ()
##

def max(a,b):
    if a < b:
        return a
    else:
        return b

max(5, max(3,10))

##
from math import sqrt
y = sqrt(16)
print (y)

#Tuples

#Structure similar with list but cannot be modified => immutable
# Example
# 	numbers = (1,2,3,4,5)
# numbers[1] = 2
# Apa saja elemen yang ada di numbers sekarang?
# numbers = (1,2,3,4,5) -> BENAR!!
# numbers = (2,2,3,4,5)  SALAH!!


########################################################################


# Set

# Container with unique element and no index
# Example
# cast = { "Luigi", "Gumbys", "Spiny" }
# len(cast)


########################################################################


# Adding and Removing Elements

# cast = {"Luigi", "Gumbys", "Spiny"} cast.add("Arthur“)
# cast.remove(“Luigi”)
# cast.clear()


########################################################################


# Dictionary

# Container used to save keys and values
# Keys are uniques while values can be associated with multiple keys
# Dictionary values can be modified later
# Access values with keys (not index)
# Example
# korean = {“one”:“hana”, “two”:“dul”, “three”:“set”, “four” : “net”}
# phonebook= {“manager”: 777, “director”: 123, “secretary”: 231}


########################################################################


# Functions

# Sometimes in a program, a piece of code is repeated many times
# If it happens, considers to move it to a function
# A good function acts as a black box
# Others can use a function without knowing the detail implementation
# Built in functions : print(), input()
# https://docs.python.org/3/library/functions.html
# User defined function


########################################################################


# Argument and Return Value

# A function usually has arguments received from calling functions (fungsi yang memanggil) -> optional
# A function is called or invoked
# A function can return value/s to the calling function -> optional

# #This is where the function is implemented
# def function_name(arguments):
# 	statements
# 	return variables
# #This is where the function is called/invoked
# function_name(arguments) 


########################################################################


# Passing arguments to a function can be
# Variable
# Literal value


########################################################################


# Variable Scope

# Scope of a variable is the part of the program in which you can access it
# Local variable is one defined within a function or code block

# Global scope is defined outside a function


########################################################################


# Modules

# In Python tutorial module defines it as a file containing Python definitions and statements, which can be later imported and used when necessary.
# Python’s standard library is organized into modules. 
# Example : in math modules contained functions related with math operation
# Use keyword import
# 	import math