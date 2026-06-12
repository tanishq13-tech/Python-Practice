s1 = [20,5,6,8,9,7]
min = s1[0]
max =  0
for i in s1:
    if i > max:
        max = i
    elif i < min:
        min = i
print("The minimun number in set =", min)
print("The maximun number in set =", max)
