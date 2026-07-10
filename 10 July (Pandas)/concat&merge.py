import pandas as pd

data1 = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "day": ["day1", "day2", "day3"],
    "year": [2020, 2021, 2022]
}
data2 = {
    "calories": [400, 350, 300],
    "duration": [45, 35, 30],
    "day": ["day1", "day2", "day3"],
}
df1 = pd.DataFrame(data1)
print(df1)
df2 = pd.DataFrame(data2)
print(df2)

df3 = pd.concat([df1, df2])
print(df3)

df4 = pd.merge(df1, df2, on="day")
print(df4)
