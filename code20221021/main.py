import pandas as pd

data = [1,3,5,7,9]
output = pd.Series(data)
print(output)

DataUrl = 'https://raw.githubusercontent.com/Datamanim/pandas/main/lol.csv'
df = pd.read_csv(DataUrl,sep='\t')
print(df)
