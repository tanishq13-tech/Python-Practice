def rev(num):
    rev = 0
    while num > 0:
        rem = num%10
        num = num//10
        rev = rev*10 + rem
    return rev

print(rev(345))