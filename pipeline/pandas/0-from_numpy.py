#!/usr/bin/env python3

'''
This module creates np array and assign it to df
Before that we need to upload pandas library
'''
import pandas as pd
import string

def from_numpy(array):
    '''
    This function creates orders then assign them to dataframe as columns
    '''
    df = pd.DataFrame(array, columns=list(string.ascii_uppercase[:array.shape[1]]))
    return df