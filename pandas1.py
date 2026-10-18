import pandas as pd
print(pd.__version__)

data=  [1,2,3,4,5]
series = pd.Series(data, index=["i","ii","iii","iv","v"])
series.loc["iv"] = 7
print(series.iloc[2])
# print(series.loc["iv"])
print(series[series%2==0])
