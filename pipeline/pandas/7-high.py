#!/usr/bin/env python3

'''
This module fills data
'''


def high(df):
    '''
    This fumction does same thing like above
    '''
    df_sort = df.sort_values(by="High", ascending=False)
    return df_sort
