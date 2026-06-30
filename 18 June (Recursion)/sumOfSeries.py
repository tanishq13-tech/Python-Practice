def sum_series(n):
    if n <= 0:
        return 0
    return n + sum_series(n - 1)

n = int(input("Enter the value of n: "))
print("Sum of series 1 to", n, "is", sum_series(n))