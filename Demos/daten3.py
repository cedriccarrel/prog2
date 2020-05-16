import pandas as pd

d = {'col1': [1, 2], 'col2': [3, 4]}

'''
df = pd.DataFrame(data=d)
df.to_csv("Einnahmen3.csv", sep=";")

print(df)
'''

newdata = pd.read_csv("Einnahmen3.csv", sep=";")
print(newdata)

print(newdata.loc[1, "col1"]) #über name

print(newdata.iloc[1, 1]) #position --> besser für iterrierung

newdata.iloc[1, 1] = 8

print(newdata)

newdata.to_csv("Einnahmen3.csv", sep=";")