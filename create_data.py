import pandas as pd

data = {
    "name":["Ubaid","Usman","Umer","Awais"],
    "age":[25,38,22,32],
    "city":["Islamabad","Multan","Karachi","Lahore"],
}
df = pd.DataFrame(data)
print(df)
