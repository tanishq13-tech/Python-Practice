s1 = {1,5,6,8,9,7}

for i in s1:
    min = i 
    max = i
    break

for i in s1:
    if i > max:
        max = i
    if i < min:
        min = i
print("The minimun number in set =", min)
print("The maximun number in set =", max)
