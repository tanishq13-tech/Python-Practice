n = int(input("Enter the value of n"))
temp = n
rev = 0 
while n > 0:
    rem = n%10
    rev = rev*10 + rem
    n = n//10
if(temp == rev):
    print("Number is palindrom.")
else:
    print("Number is not palindrom.")