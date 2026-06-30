def fact(num):
    fact = 1
    for i in range(1, num+1):
        fact *= i
    return fact
print("The factorial of number:", fact(int(input("Enter the value: "))))