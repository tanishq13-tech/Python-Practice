l1 = [20,5,6,8,81,1,1,1,0,0,7,9,9,7]
item = int(input("Enter the number for whose you want to find the occurence: "))
count = 0
for i in l1:
    if i == item:
        count += 1
print("",count)