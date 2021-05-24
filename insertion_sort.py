import pandas as pd
import time
from datetime import datetime

data=pd.read_csv("imdb.csv",nrows=2000)
list=data.values.tolist()
n=len(list)

start=time.time()*1000
for i in range(1,n):
    pos=i
    val=list[i]
    while pos>0 and val[1]<list[pos-1][1]:
        list[pos]=list[pos-1]
        pos-=1
    list[pos]=val
stop=time.time()*1000
print(stop-start)

