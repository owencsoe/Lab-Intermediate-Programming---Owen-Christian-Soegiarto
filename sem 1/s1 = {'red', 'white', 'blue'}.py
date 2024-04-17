s1 = {'red', 'white', 'blue'}
s2 = {'green', 'white', 'red'}

x = s1.intersection(s2)
y = s2.intersection(s1)

if (x == y):
    print('same')
else:
    print('not same')
    
d = {1:2, 3:4, 5:6}
x = 0
for i in d:
    x += i
print (x)

a = 1
b = 2
c= 3
x = {a:[1,2,3],b:[4,5,6],c:[7,8,9]}

print(x[1][1])

other_hash = {1:'Python'} 
other_hash[2] = 10

self_hash = {} 
self_hash[2] = other_hash 
self_hash[3] = 4 
self_hash["2"] = self_hash

print(self_hash["2"]["2"]["2"][3])