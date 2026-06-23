d = {}
sum = 0
product = 1
for i in range(1,16):
    d[i] = i**2
    print(i, ":", d[i])
    sum += d[i]
    product *= d[i]
print(d)
print(sum)
print(product)