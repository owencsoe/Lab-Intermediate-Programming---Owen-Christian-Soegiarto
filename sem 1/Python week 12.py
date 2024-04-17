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