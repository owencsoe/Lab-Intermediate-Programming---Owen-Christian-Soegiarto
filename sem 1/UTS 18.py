grades =[86, 43, 74, 90, 75, 38, 55, 98, 64, 84] #a

print(grades[1]) #b

grades[1], grades[7] = grades[7], grades[1] #c
print("Grade after switching = ",(grades))

max(grades) #d
print("Max grade = ", max(grades))