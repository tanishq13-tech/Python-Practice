import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "day": ["day1", "day2", "day3"],
    "year": [2020, 2021, 2022]
}
df = pd.DataFrame(data)
print(df)

print(df["calories"], "\n") # Accessing the "calories" column
print(df.loc[0], "\n") # Accessing the first row using loc
print(df.loc[[0, 1]], "\n") # Accessing the first two rows using loc
print(df.columns[[0, 1]], "\n") # Accessing the first two columns using columns
print(df.loc[0, "calories"], "\n") # Accessing the value in the first row and "calories" column
print(df.iloc[0, 3], "\n") # Accessing the value in the first row and fourth column
print(df)