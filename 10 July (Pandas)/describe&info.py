import pandas as pd

data = {
    "calories": [420, 380, 390, None],
    "duration": [50, 40, 45, None],
    "day": ["day1", "day2", "day3", None],
    "year": [2020, 2021, 2022, None]
}
df = pd.DataFrame(data)
print(df)
ddf=df.describe()
print(ddf)

myFile = pd.read_excel("10 July (Pandas)/sample-simple.xlsx", index_col=0)
print(myFile)
ddf=myFile.fillna(0)
print(ddf)