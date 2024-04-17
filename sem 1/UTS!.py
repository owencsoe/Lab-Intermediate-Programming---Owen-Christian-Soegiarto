print("Wanna know you BMI?")
w= int(input("Please enter weight! kg "))
h= int(input("Please enter height! m "))

bmi= w/(h**2)

if bmi<18.5:
    print("You are underweight!")
elif 18.5<bmi<24.9:
    print("You are normal weight!")
elif 25<bmi<29.9:
    print("You are overweight!")
else: bmi>29.9
print("You are OBESE!")