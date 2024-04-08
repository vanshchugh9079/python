import pandas as pd
list=[1,2,3,4,5,6]
index=["one","two","three","four","five","six"]
series=pd.Series(list,index=index,dtype="int",copy=True)
list[1]=3
print(series.iloc[1])