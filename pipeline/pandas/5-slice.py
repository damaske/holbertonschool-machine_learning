#!/usr/bin/env python3

'''
This module selects every 60th row of these columns
'''


def slice(df):
    
    df_somecolumns = df.loc[::60, ["High", "Low", "Close", "Volume_(BTC)"]]
    return df_somecolumns
