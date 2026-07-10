import pandas as pd

a = [1,2,3,5,9,7]
myVal = pd.Series(a)
print(a)
print(myVal)

# adding labels to the series
myVal = pd.Series(a, index=['a','b','c','d','e','f'])
print(myVal)

# Example
cal = {"day1": 420, "day2": 380, "day3": 390}
mycal = pd.Series(cal, index=["day1", "day2", "day3", "day4"])
mycall = pd.Series(cal, index=["day1", "day2"])
print(mycal)
print(mycall)