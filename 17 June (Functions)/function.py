# Functions


# Types:--------------------------------------------------------------------

# • In-built : print, add, etc.
# • User-defined : 
#                   def fname(arg):
#                       statements
#                   fname(arg)


# Types of calling:---------------------------------------------------------

# 1) Without Argument and Without Return Type
def add_1():
    a = int(input("Enter the value: "))
    b = int(input("Enter the value: "))
    c = a + b
    print("Sum is", c)
add_1()

# 2) With Argument and Without Return Type
def add_2(a,b):
    c = a + b
    print("Sum is", c)
add_2(5,5)

# 3) Without Argument and With Return Type
def add_3():
    a = int(input("Enter the value: "))
    b = int(input("Enter the value: "))
    c = a + b
    return c
c = add_3()
print("Sum is", c)

# 4) With Argument and With Return Type
def add_4(x, y):
    return x + y
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
add_4(a,b)


# Types of arguments:-------------------------------------------------------

# 1) Required Arguments / Positional Arguments
def greeting(name, age):
    print("Name is", name)
    print("Age is", age)
greeting("abc", 40)

# 2) Default Arguments
def greeting(name, age = 17):
    print("Name is", name)
    print("Age is", age)
greeting("abc", 44)
greeting("xyz")

# 3) Keyword Arguments
def greeting(name, age):
    print("Name is", name)
    print("Age is", age)
greeting(name="abc", age=40)

# 4) Variable-Length Arguments
def greeting(name, *a):
    print("Name is", name)
    print("Sum is", sum(a))
greeting("abc", 40, 40, 40)


# Lambda Function (Inline Function):---------------------------------------------
x = lambda a:a*a
print(x(10))

m = lambda a,b : a*b
print(m(20,40))
