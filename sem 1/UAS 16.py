def main(v1, v2, v3):
    sum=0
    for i in range(v1, v2, v3):
        sum = sum + i
    return sum
print("Sum of integer from 1 to 10:" ,main(1, 11, 1))
print("Sum of integer from 10 to 100:",main(10, 101, 1))
print("Sum of integer from 5 to 100 (Divisable by 5):",main(5, 101, 5)) 