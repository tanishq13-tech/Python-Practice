n = int(input("Enter the value of n: "))
sum = 0
mul = 1
for i in range(1,n+1):
    sum += i
    mul *= i
print("Sum of numbers:",sum)
print("Multiplication of numbers:",mul)