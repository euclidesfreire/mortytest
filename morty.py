#Library 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from benfordslaw import benfordslaw

def sum_data_date(df):
    df_aux = df
    df_tmp = []
    for state in df_aux['state'].unique():
        Iloc = df_aux['state']==state
        for date in df_aux['date'].loc[Iloc].unique():
            new_confirmed_aux = df_aux['new_confirmed'].loc[df_aux['date']==date].sum()
            new_deaths_aux = df_aux['new_deaths'].loc[df_aux['date']==date].sum()
            df_tmp.append([state, date, new_confirmed_aux, new_deaths_aux])
    
    df_new = pd.DataFrame(data = df_tmp, 
                  columns = ['state', 'date', 'new_confirmed', 'new_deaths'])
    
    df_new.to_csv('datasets/sumdatadate/caso_full_new.csv')

    return df_new

def delete_isnull_city(df):
    df_no_city_null = df
    df_no_city_null.drop(df_no_city_null[df_no_city_null.city.isnull()].index,inplace=True)
    
    return df_no_city_null

def heatmap(df, titleCor):
    dfCor = df.corr()
    outcomeCor = abs(dfCor[titleCor])
    plt.figure(figsize=(10,8))
    sns.heatmap(dfCor,cmap='rocket_r',annot=True)