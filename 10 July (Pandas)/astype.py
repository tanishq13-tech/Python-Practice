import pandas as pd

data = {
    "calories": [420, 380, 390, None],
    "duration": [50, 40, 45, None],
    "day": ["day1", "day2", "day3", None],
    "year": [2020, 2021, 2022, None]
}
df = pd.DataFrame(data)
print(df)
df['calories'] = df['calories'].astype('str')
print(df)

print(df["calories"].dtypes)