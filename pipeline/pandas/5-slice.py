#!/usr/bin/env python3

'''
This module selects every 60th row of these columns
'''


def slice(df):
    '''
    This fumction does same thing like above
    '''
    df_somecolumns = df.loc[::60, ["High", "Low", "Close", "Volume_(BTC)"]]
    return df_somecolumns
