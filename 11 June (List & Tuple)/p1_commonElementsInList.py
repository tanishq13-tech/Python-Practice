l1 = [10,20,30,40,20]
l2 = [20,30,50,60]
l3 = []
for i in l1:
    for j in l2:
        if i == j and i not in l3:
            l3.append(i)
print(l3)
            