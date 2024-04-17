MIN_SPEED = 60 
MAX_SPEED = 100 
speed = 110 

if not (speed < MAX_SPEED) : 
   speed = int(speed / 2) 

if not (speed > MIN_SPEED) : 
   speed = speed + 30 

print(speed)
################################################################

lst = [1,3,5,7]
for i in lst:
   print('Hello')
################################################################
kata = 'Hello'
kata2 = ''
i = 0

while i<len(kata):
    kata2 += kata[-1-i]
    i+=1

print(kata2)

################################################################
str="Python"
for c in str:
   if c=="h":
      break
   print(c, end='')