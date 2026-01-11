#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
"""
This module visualizes the daily resampled data"
"""


def visualize(df):
    '''
    This function visualizes the daily resampled data
    '''
    df.drop('Weighted_Price', axis=1, inplace=True)
    df.rename(columns={'Timestamp': 'Date'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'], unit='s')
    df.set_index('Date', inplace=True)
    df['Close'].fillna(method='ffill', inplace=True)
    for col in ['High', 'Low', 'Open']:
        df[col].fillna(df['Close'], inplace=True)
        df[['Volume_(BTC)', 'Volume_(Currency)']].fillna(0, inplace=True)
        df = df[df.index >= '2017-01-01']
        df_daily = df.resample('D').agg({
            'High': 'max',
            'Low': 'min',
            'Open': 'mean',
            'Close': 'mean',
            'Volume_(BTC)': 'sum',
            'Volume_(Currency)': 'sum'
        })
    df_daily.plot(figsize=(10, 6))
    return df_daily
