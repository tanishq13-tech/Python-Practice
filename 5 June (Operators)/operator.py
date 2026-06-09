a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))

#Arithmatic
print("Arithmatic")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)
print("\n")



#Relational
print("Retional")
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print("\n")



#logical
print("logical")
print((a%b==0) and (a<b))
print((a%b==0) or (a<b))
print(not(a%b==0))
print("\n")


#assignment
print("assignment")
a+=a
print(a)
b+=b
print(b)
a/=2
print(a)
b*=2
print(b)
b-=2
print(b)
print("\n")



#identity
print("identity")
print(a is b)
print(a is not b)
print("\n")


#Membership
print("Membership")
L1 = [10, 20, 30, 40]
print(10 in L1)
print(90 in L1)
print(10 not in L1)
print(90 not in L1)
print("\n")


#Swaping
print("Swaping ---- 1")
c = int(input("Enter the value of c "))
d = int(input("Enter the value of d "))
temp = c
c = d
d = temp
print("The value of c = ", c, "and d = ", d)
print("\n")

print("Swaping ---- 2")
c = int(input("Enter the value of c "))
d = int(input("Enter the value of d "))
c = c + d
d = c - d
c = c - d
print("The value of c = ", c, "and d = ", d)
print("\n")

