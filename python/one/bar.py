from matplotlib import pyplot as pd
y=[1,2,3,4,5]
x=["py","C++","c","java","js"]
pd.xlabel("language",color="green",fontsize=20)
pd.bar(x,y,color="r",label="trend",width=0.5,align="edge",alpha=0.5,edgecolor="purple",linewidth=2,linestyle=":")
pd.legend()
pd.show()
