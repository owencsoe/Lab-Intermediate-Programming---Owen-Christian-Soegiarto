print("Wanna know you BMI?")
w= int(input("Please enter weight! kg "))
h= int(input("Please enter height! cm ",))

h1 = h/100

bmi= w/(h1**2)

if bmi<18.5:
    print("You are underweight!")
elif 18.5<bmi<24.9:
    print("You are normal weight!")
elif 25<bmi<29.9:
    print("You are overweight!")
else:
    print("You are OBESE!")

