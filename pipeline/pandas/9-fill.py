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
    for col in ['Volume_(BTC)', 'Volume_(Currency)']:
        df[col] = df[col].fillna(0)
    return df
