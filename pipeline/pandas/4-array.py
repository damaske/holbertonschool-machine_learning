#!/usr/bin/env python3

'''
This module selects last 10 rows and
converts them into array
'''


import pandas as pd

def array(df):
    '''
    This fumction does same thing like above
    '''
    df_somecolums = df.loc[:, ["High", "Close"]].tail(10)
    arr = df.to_numpy()
    return arr
