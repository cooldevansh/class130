import pandas as pd
import csv

df=pd.read_csv("final.csv")
print(df.shape)

del df["pl_name"]
print(df.shape)

df