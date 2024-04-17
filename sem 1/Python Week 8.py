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