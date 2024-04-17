lst = ["hello"] * 5 #1
lst[-5] = "bye"

print(lst[-5]) 

lst = ["hello"] * 5#2

print(lst[0][-1])

def funk1(x,y): #3
    x = 5
    y[0] = x

lst = [1,2,3,4,5]
x = 10
funk1(x,lst)

print (x + lst[0])

x = [1,2,3,4,5]#4
x[0] = 0

print (x[0] + x[3])