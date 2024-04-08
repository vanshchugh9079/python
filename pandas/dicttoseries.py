import pandas as pd
dict={
    "name":["vansh","gamer","chugh","pubg","minecraft","gta5"],
    "class":[1,2,3,4,5,6]
}
series=pd.Series(dict["name"])
print(series)