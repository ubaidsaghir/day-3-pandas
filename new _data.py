import pandas as pd
df = pd.read_csv("StudentPerformanceFactors.csv")
# print(df.head())

# df.tail()

# print(df)

print(df.describe())
print(df.info())