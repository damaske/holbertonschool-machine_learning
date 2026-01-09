#!/usr/bin/env python3

'''
This module flips data
'''


def flip_switch(df):
    '''
    This fumction does same thing like above
    '''
    df_flipped = df.iloc[:, ::-1].T
    return df_flipped
