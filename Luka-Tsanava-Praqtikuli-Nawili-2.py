import pandas as pd

# 3

csvFile = pd.read_csv("pandas.csv")
print(csvFile.sort_values("Type 1", ascending=False))
print(csvFile.sort_values("HP", ascending=False))


# 4

print(csvFile.sort_values("Type 1", ascending=True))
print(csvFile.sort_values("HP", ascending=True))

# 5

print(csvFile.loc[csvFile["Type 1"] == "Fire"])

# 6

myDictionary = {"name": "Jonathan", True: "Tokyo", 6: False, 3.14: ["Pi", "Euler"], "dict": {"first": 1, "second": 2}}
print(myDictionary)
myDictionary.pop("dict")
print(myDictionary)

# 7

myFile = open("myFile.txt", "w")
myFile.writelines('''
iyo arabets rostevan
mefe gmrtisagan sviani
magali uxvi mdabali
lashqarmravali ymiani
''')

# 8

myTuple = (1, 5, 87)
print(myTuple)

# Tuple ტიპის სიის ცვლილება არ შეიძლება
