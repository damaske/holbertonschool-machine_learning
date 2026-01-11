#!/usr/bin/env python3
'''
This module computes desc() except Timestamp column
'''


def analyze(df):
    '''
    Same with above
    '''
    desc_df = df.drop(columns=['Timestamp']).describe()
    return desc_df
