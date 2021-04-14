import pandas as pd


# returns dataframe of data from csv file
def csv_to_df(filename):
    return pd.read_csv(filename)


# writes dataframe to csv file
def df_to_csv(df, filename):
    df.to_csv(filename)
