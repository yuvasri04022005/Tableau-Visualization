import pandas as pd
df1 = pd.DataFrame({'ID':[1,2,3], 'Name':['A','B','C']})
df2 = pd.DataFrame({'ID':[1,2,3], 'Marks':[80,90,85]})
out = pd.merge(df1, df2, on='ID')
print(out)