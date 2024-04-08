import pandas as pd
info={
    "name":["vansh","rohan","rahul","chugh"],
    "age":[1,2,3,4],
    "id":[1,2,3,4]
}
df=pd.DataFrame(info,index=[1,2,3,4],copy=False)
# df["class"]=["first","second","third","fourth"]
# print(df)
# li=[1,2,3,4,5,6]
# print(pd.Series(li,index=[1,2,3,4,5,6,78]))
# df["pro"]=df["age"]+df["id"]
# df.append({"name":"ajay"})  wrong

# info = {
#     "name": ["vansh", "rohan", "rahul", "chugh"],
#     "age": [1, 2, 3, 4],
#     "id": [1, 2, 3, 4]
# }
# Add a new row to the DataFrame
new_row = {"name": "ajay", "age": 5, "id": 5}
df.loc["my"]=["hello",10,5]
print(df)
print(df.drop(4),True)
print(df)

