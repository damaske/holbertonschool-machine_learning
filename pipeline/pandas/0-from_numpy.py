#!/usr/bin/env python3
import pandas as pd
import numpy as np

# s = pd.Series([1, 2.6, 2],
#               index=["i", "r", "a"])
# def from_numpy(array):
#     return pd.DataFrame(array)
#print(s)

dict_arr = { 'key': 5,
            'key2': 7,
            'key3': 9
            }

seriesFromDict = pd.Series(dict_arr,
                           index=['key', 'key3'],
                           )
print(seriesFromDict)