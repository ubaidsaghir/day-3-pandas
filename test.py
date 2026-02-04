import pandas as pd
df = pd.read_csv("train_and_test2.csv")
print(df)
print(df.head(10))
print(df.shape) 
# /show rows and columns
print(df.columns) 
# /show column names
print(df.info()) 
# /dataset info 
print(df.describe()) 
# / numerical summary
print(df["Passengerid"].head())


df.head()
df.tail()

