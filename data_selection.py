import pandas as pd 
df = pd.read_csv("data.csv")
print(df.describe())

print(df["Attendance"].dtype)

print(df["Parental_Involvement"].dtype)


# /show two columns
print(df[["Attendance","Parental_Involvement"]].head(1))

# show first row data

print(df.iloc[0].dtype)

print(df.head())

print(df.dropna())

print(df.fillna(2))
print(df.shape)

# rename column 
# print(df.rename(columns={"Parental_Involvement":"parent"}))

# change type of column 
print(df["Hours_Studied"].astype(str))
print(df["Hours_Studied"])
# print(df.info())
# print(df)
