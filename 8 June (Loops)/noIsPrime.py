n = int(input("Enter the value of n: "))
flag = -1
for i in range(2,n//2+1):
    if(n%i==0):
        flag = 1
        break
if(flag == -1):
    print("Number is prime")
else:
    print("Number is not prime")