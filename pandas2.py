import pandas as pd
# dict_ = {
#     "Name":"prasiddha",
#     "class":11,
#     "section":"H",
#     "roll":31
# }
# series = pd.Series(dict_)

# print(series["Name"])
# print(series.loc["Name"])

# data = {"Name:":["Prasiddha", "Suyog","Prajwal"], "Age:":[16,15,17]}
# df = pd.DataFrame(data, index=["1","2","3"])
# df["Class:"] = [11,11,11]
# new_data = pd.DataFrame({"Name:":"Ridam","Age:":12,"Class:":6, },index=["4"])
# df = pd.concat([df, new_data])
# print(df)
# print(df.iloc[0])

data = {"Name":["Prasiddha","Suyog","Rishav"],"Class":[11,11,11],"Age":[14,15,16]}
df = pd.DataFrame(data,index=[0,1,2])

new = pd.DataFrame({"Name":"Ridam","Class":6,"Age":12},index=[3])

df= pd.concat([df,new])
df["Sex"] = ["Male", "Male", "Male","Male"]
print(df)