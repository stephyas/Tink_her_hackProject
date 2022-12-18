import pandas as pd

df = pd.read_csv('items.csv')
df["content"]=df["content"].str.replace(",","")
print(df.to_string())
