l1 = [20,5,6,8,9,7]
print(l1)
a = l1.index(int(input("Enter the 1st element from list ")))
b = l1.index(int(input("Enter the 2nd element from list ")))
c = l1[a]
l1[a] = l1[b]
l1[b] = c
print(l1)