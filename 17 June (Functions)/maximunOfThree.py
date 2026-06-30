def maximum(a,b,c) :
    if a > b :
        if a > c : 
            return a
        else :
            return c 
    else :
        if b>c :
            return b 
        else :
            return c
        
a = int(input("Enter the value: "))
b = int(input("Enter the value: "))
c = int(input("Enter the value: "))
print(f"The maximmun of {a},{b},{c}:", maximum(a,b,c))