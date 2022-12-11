import seaborn as sns
import pandas as pd

df = sns.load_dataset('titanic')
print(df.head())

# df['COLUMN_NAME'] = True : add new column
df['vip'] = True
print(df.head())

# df1.drop(df1.index[0:10]) : delete row

