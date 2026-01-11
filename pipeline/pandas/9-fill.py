#!/usr/bin/env python3

'''
This module fills data
'''


def fill(df):
    '''
    Clean and fill missing values in the DataFrame
    '''
    if 'Weighted_Price' in df.columns:
        df = df.drop(columns=['Weighted_Price'])
    df['Close'].fillna(method='ffill', inplace=True)
    for col in ['High', 'Low', 'Open']:
        df[col].fillna(df['Close'], inplace=True)
    df[['Volume_(BTC)', 'Volume_(Currency)']].fillna(0, inplace=True)
    return df
