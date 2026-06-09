n = int(input("Enter the number of n: "))
temp = n
dc =n
arm = 0
count = 0
while dc > 0:
    rem = dc%10
    count += 1
    dc = dc//10
print("Number of digits:",count)
while n > 0:
    rem = n%10
    arm = arm + rem**count
    n = n//10
if temp == arm:
    print("Number is armstrong.")
else:
    print("Number is not armstrong.")