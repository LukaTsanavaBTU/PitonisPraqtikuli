import pandas as pd

#1

csvFile = pd.read_csv("pandas.csv")
print(csvFile.head(5))

#2

csvFile.pop("HP")
print(csvFile)
