d1 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
print(d1)
d1[1] = "aaa"
d1[5] = "xyz"
print(d1)

# Delete
print("\n","Delete")
d2 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
del d2
#print(d2)

# Pop
print("\n","Pop")
d3 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
d3.pop(3)
print(d3)

# Pop-Item
print("\n","Pop-Item")
d4 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
d4.popitem()
print(d4)

# Clear
print("\n","Clear")
d5 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
d5.clear
print(d5)

# Get
print("\n","Get")
d6 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
print(d6.get(1))

# Update
print("\n","Update")
d7 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
d7.update({5:"aaa", 6:"bb"})
print(d7)


# Keys, Values, Items
print("\n","Keys, Values, Items")
d8 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
print(d8.keys())
print(d8.values())
print(d8.items())

# Copy
print("\n","Copy")
d9 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
d10 = d9.copy()
print(d10)

# Iteration
print("\n","Iteration")
d11 = {1:"abc", 2:"def", 3:"ghi", 4:"jkl"}
for i in d11:
    print(i, ":", d11[i])

# Length
print("\n","Length")
print(len(d11))

# Membership
print("\n","Membership")
print(1 in d11)
print(1 not in d11)


# Run-time dictionary
print("\n","Run-time dictionary")
d = {}
d['name'] = input("Enter the name: ")
d['rollNo'] = input("Enter the roll number: ")
d['course'] = input("Enter the course: ")
d['dept'] = input("Enter the department: ")
print(d)