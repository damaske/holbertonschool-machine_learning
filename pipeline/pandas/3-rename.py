#!/usr/bin/env python3

'''
This module converts and renames Timestamp column
'''
import pandas as pd


def rename(df):
    '''
    This function renames the columns of a DataFrame
    '''
    df = df.rename(columns={"Timestamp": "Datetime"},)
    df["Datetime"] = pd.to_datetime(df["Datetime"], unit='s')
    updated_df = df[["Datetime", "Close"]]
    return updated_df
