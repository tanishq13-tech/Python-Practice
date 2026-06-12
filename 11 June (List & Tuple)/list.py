# Repeating
n = int(input("Enter the number of times to repeat the list: "))
l1 = [10,20,30]
print(l1*n)

# Concatination
l2 = [10,20]
l3 = [30,40]
print(l2+l3)

# Iteration
for i in l1:
    print(i)

# Membership
print(10 in l1)
print(10 not in l1)

#Length
print("The length of list l1:", len(l1))

# Append
l4 = []
a = int(input("Enter the no. of elements to append: "))
for i in range(1, a+1):
    l4.append(input("Enter the elements"))
    print(l4)
print(l4)

# Count
print(l1.count(10))

# Copy
l5 = l1.copy()
print(l5)

# Clear
l5.clear()
print(l5)

# Extend
l2.extend([70,80,90])
print(l2)

# Index
print(l1.index(20))

# Insert
l3.insert(1,100)
print(l3)

# Pop
l3.pop()
print(l3)

# Remove
l3.remove(30)
print(l3)

# Reverse
l1.reverse()
print(l1)

# Sort
l6 = [2,3,5,4,7,8,0]
print(l6)
l6.sort()
print(l6)

# Indexing
print(l6[2])
print(l6[-5])

# Slicing
print(l6[2:5])
print(l6[:5])
print(l6[2:])
print(l6[2:6:2])
print(l6[:])