import pandas as pd
import time
from datetime import datetime

patient_data = pd.read_csv("imdb.csv", nrows=50000)
data_list = patient_data.values.tolist()
n = len(data_list)


def merge_sort(data_list):
    if len(data_list) > 1:
        center = len(data_list) // 2
        left_list = data_list[:center]
        right_list = data_list[center:]

        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i][1] < right_list[j][1]:
                data_list[k] = left_list[i]
                i += 1
            else:
                data_list[k] = right_list[j]
                j += 1
            k += 1

    while i < len(left_list):
        data_list[k] = left_list[i]
        i += 1
        k += 1

    while j < len(right_list):
        data_list[k] = right_list[j]
        j += 1
        k += 1


now = time.time() * 1000
merge_sort(data_list)
then = time.time() * 1000

print(then - now)
