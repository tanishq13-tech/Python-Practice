import pandas as pd

myFile = pd.read_excel("10 July (Pandas)/sample-simple.xlsx", index_col=0)
print(myFile)
head=myFile.head(5)
print(head)
tail=myFile.tail(5)
print(tail)