print("Hello")

a=1 #int
print(a)
print("The type of a is ", type(a))
b = str(a)
print(type(b))

a=12.2 #float
print(a)
print("The type of a is ", type(a))

a= 12+13j  #complex
print(a)
print("The type of a is ", type(a))
print(a+10+10j)
print("The real part is ",a.real)  #real part
print("The imaginary part is ",a.imag)  #imaginary part

a="Hello" #string
print(a)
print("The type of a is ", type(a))

a= True   #boolean
print(a)
print("The type of a is ", type(a))

a= False
print(a)
print("The type of a is ", type(a))


l1 = [10, 20, 30, 40]   #list 
l3= l1
l3.append(4)
print(a)

print(l1)
print("The type of l1 is ", type(l1))
print("\n")
l1.append(50)
print(l1)
l2 = [10, 30, 20, 40]
print(l2)
print("The type of l2 is ", type(l2))

print(l1==l2)

print(l2[2]) 
print("The type of l2 is ", type(l2))


s1 = {10, 20, 30, 40}   #set
print(s1)
print("The type of s1 is ", type(s1))
print(s1)

s2 = {10, 30, 20, 40}
print(s2)
print("The type of s2 is ", type(s2))

print(s1==s2)


t1 = (10, 20, 30, 40) #tuple
print(t1)
print("The type of t1 is ", type(t1))

t2 = ()
print(t2)
print("The type of t2 is ", type(t2))

t3 = ()
print(t3)
print("The type of t3 is ", type(t3))


d1 = {'name': "Tanishq", 'course': "B.tech", 'age': 20}      #dictionary
print(d1)
print("The type of d1 is ", type(d1))

print (d1['name'])


d1['roll_no'] = 24
print(d1)
del d1['age'] #------------------------
print(d1)

print(type([]))
print(10%3)

var = "James Bond"
print(var[2::-1])


listOne = [20, 40, 30, 10]
listTwo = [20, 40, 30, 10]
print(listOne == listTwo)
print(listOne is listTwo)