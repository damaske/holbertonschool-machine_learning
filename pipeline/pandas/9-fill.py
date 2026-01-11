#!/usr/bin/env python3

'''
This module fills data
'''


def fill(df):
    '''
    This fumction does same thing like above
    '''
    df.drop('Weighted_Price', axis=1, inplace=True)
    df['Close'].fillna(method='ffill', inplace=True)
    for col in ['High', 'Low', 'Open']:
        df[col].fillna(df['Close'], inplace=True)
    df['Volume_(BTC)', 'Volume_(Currency'].fillna(0, inplace=True)
    return df
