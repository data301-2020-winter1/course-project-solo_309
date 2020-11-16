import pandas as pd
import os
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import seaborn as sns


def import_and_clean():
    path = os.path.abspath('{}/data/raw/AirQualityUCIFix.csv'.format(os.pardir))
    df1 = pd.read_csv(path).drop(columns=['Unnamed: 15', 'Unnamed: 16']).dropna(subset=['Date', 'Time']).reset_index(drop=True).loc[lambda x: x['CO(GT)'] >= 0].loc[lambda x: x['PT08.S1(CO)'] >= 0].loc[lambda x: x['NMHC(GT)'] >= 0].loc[lambda x: x['C6H6(GT)'] >= 0].loc[lambda x: x['PT08.S2(NMHC)'] >= 0].loc[lambda x: x['NOx(GT)'] >= 0].loc[lambda x: x['PT08.S3(NOx)'] >= 0].loc[lambda x: x['NO2(GT)'] >= 0].loc[lambda x: x['PT08.S4(NO2)'] >= 0].loc[lambda x: x['PT08.S5(O3)'] >= 0]
    return df1


def only_temperature_and_humidity(df):
    return df[["Date", "Time", "T", "RH", "AH"]]


def eda(df):
    print("Rows, Columns\n {}".format(df.shape))
    print("\nFirst Five rows\n{}".format(df.head()))
    print("\nNames of columns\n{}".format(df.columns))
    print("\nUnique counts of each column\n{}".format(df.nunique(axis=0)))
    print(df.describe().apply(lambda s: s.apply(lambda x: format(x, 'f'))))
