s1 = [1,5,6,8,9,7]
sum = 0
product = 1
for i in s1:
    sum += i
    product *= i
avg = sum / (len(s1))
print("The sum of numbers in a list =", sum)
print("The average of numbers in a list =", avg)
print("The product of numbers in a list =", product)