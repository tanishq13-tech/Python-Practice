days = {"Monday", "Tuesday", "Wednesday"}
print(days)

# ----- Methods ---- #

# Add 
days.add("Thrusday")
print(days)

# Update
days.update(["Friday", "Saturday", "Sunday"])
print(days)

# Remove
days.remove("Thrusday")
print(days)

# Discard
days.discard("Thrrusday")
print(days)

# Copy
d2 = days.copy
print(d2)

###--------- Difference between remove and discard is that whenever there is no element which has to remove or discard then remove shows the error but discard not. ----- 

# Pop
days.pop()
print(days)

#clear
days.clear()
print(days)

# ------ Operations ------- #

a = {1,2,3}
b = {4,5,3}
c = {1,2,5}
d = {4,5,3}
# Union
print("Union of A & B", a|b)
print("Union of A & B", a.union(b))

# Intersection
print("Intersection of A & B", a|b)
print("Intersection of A & B", a.intersection(b))

# Intersection update
c.intersection_update(a)
print("C after intersection-update of C & A", c)

# Difference
print("Difference of A & B", a|b)
print("Difference of A & B", a.difference(b))

# Difference Update
d.difference_update(a)
print("D after difference-update of D & A", d)

# Symmetric Difference ([a-b]U[b-a])
print("Symmetric-difference of A & B", a^b)
print("Symmetric-difference of A & B", a.symmetric_difference(b))

# Symmetric Difference Update
a.symmetric_difference_update(b)
print("A after Symmetric-difference-update of A & B", a)