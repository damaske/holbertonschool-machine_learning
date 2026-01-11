#!/usr/bin/env python3

'''
This module fills data
'''


def high(df):
    '''
    This fumction does same thing like above
    '''
    df_sort = df.sort_values(["High"], ascending=False, inplace=True)
    return df_sort
