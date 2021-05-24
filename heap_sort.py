import pandas as pd
import time
from datetime import datetime

patient_data=pd.read_csv("imdb.csv",nrows=50000)
patient_list=patient_data.values.tolist()
n=len(patient_list)

def heapify(n,i,patient_list):
    max_val_pos=i
    left_pos=2*i+1
    right_pos=2*i+2

    if left_pos<n and patient_list[i][1]<patient_list[left_pos][1]:
        max_val_pos=left_pos
    if right_pos<n and patient_list[max_val_pos][1]<patient_list[right_pos][1]:
        max_val_pos=right_pos

    if max_val_pos!=i:
        (patient_list[i], patient_list[max_val_pos]) = (patient_list[max_val_pos], patient_list[i])
        heapify(n,max_val_pos,patient_list)

def build_heap(n,patient_list):
    for i in range(n//2,-1,-1):
        heapify(n,i,patient_list)

    for i in range(n-1,0,-1):
        (patient_list[i], patient_list[0]) = (patient_list[0], patient_list[i])
        heapify(i,0,patient_list)

now=time.time()*1000
build_heap(n,patient_list)
then=time.time()*1000


print(then-now)
