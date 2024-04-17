Age = int(input("Please input your age: "))

while Age > 150 or Age < 0:
  Age = int(input("Your age is invalid. Please input your age again: "))

Age_in_50_years = Age + 50

output = f"{Age_in_50_years:03d}"

print(f"Your age in 50 years will be",output)