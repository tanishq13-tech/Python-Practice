n = int(input("Enter the value of n: "))

# break
print("Break")
for i in range(1,n):
    if(i == 3):
        break
    print(i)

# continue
print("Continue")
for i in range(1,n):
    if(i == 3):
        continue
    print(i)

# pass
print("Pass")
for i in range(1,n):
    pass
print(i)
