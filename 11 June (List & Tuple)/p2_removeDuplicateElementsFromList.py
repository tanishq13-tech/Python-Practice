l1 = [0,0,10,20,20,50,60,80,60,60,60,90,90]
l2 = []

for i in l1:
    if i not in l2:
        l2.append(i)
    else:
        pass
print("Unique list:",l2)