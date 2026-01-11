#!/usr/bin/env python3

'''
This module sets index
'''


def index(df):
    '''
    This fumction does same thing like above
    '''
    df.set_index('Timestamp', inplace=True)
    return df
