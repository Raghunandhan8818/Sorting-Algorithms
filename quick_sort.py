import pandas as pd
import time
from datetime import datetime

patient_data=pd.read_csv("imdb.csv.csv",nrows=50000)
patient_list=patient_data.values.tolist()
n=len(patient_list)

def divide(start,end,patient_list):
    if start<end:

        pivot=quick_sort(start,end,patient_list)
        divide(start,pivot-1,patient_list)
        divide(pivot+1,end,patient_list)

def quick_sort(start,end,patient_list):
    pivot=end
    i=start-1

    for j in range(start,end):
        if patient_list[j][1]<=patient_list[pivot][1]:
            i+=1
            (patient_list[i],patient_list[j])=(patient_list[j],patient_list[i])
    (patient_list[i+1], patient_list[end]) = (patient_list[end], patient_list[i+1])
    return i+1


def insertion_sort(patient_list):
    n=len(patient_list)
    for i in range(1, n):
        pos = i
        val = patient_list[i]
        while pos > 0 and val[1] < patient_list[pos - 1][1]:
            patient_list[pos] = patient_list[pos - 1]
            pos -= 1
        patient_list[pos] = val


now=time.time()*1000
divide(0,n-1,patient_list)
then=time.time()*1000

print(then-now)
