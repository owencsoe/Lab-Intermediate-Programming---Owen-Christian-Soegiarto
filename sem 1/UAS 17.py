def circlearea(r):
    area = 3.14159 * r **2
    return area
def squarearea(p):
    areas = p **2
    return areas
radius= float(input("Enter the circle radius:"))
result1=circlearea(radius)
length= float(input("Enter the square length:"))
result2=squarearea(length)
print("A circle with a radius of", radius, "has an area of", result1)
print("A circle with a radius of", length, "has an area of", result2)