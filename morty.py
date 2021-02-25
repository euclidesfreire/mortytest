#Library 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
from scipy.stats import chisquare
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


class teste:

    _total_count = _observed = _data_percentage = _expected = 0

    def __init__(self, N, tabulated, alpha=0.05):
        """
        Parameters
        ----------
        N : list or numpy array
            Input data.
        """

        self._N = N
        self._alpha = alpha
        self._tabulated = tabulated
        
    #função chisquare da biblioteca scipy
    def func_chisquare(self):
        x2 = chisquare(self._observed, f_exp=self._expected)

        return x2

    def quiquadrado(self):
       self._total_count, self._observed, self._data_percentage = self._count_first_digit()

       self._expected = self._get_expected_counts()

       return self._chi_square_test()

    def _count_first_digit(self):
        N = self._N
        mask = N>1.
        data = list(N[mask])
        
        for i in range(len(data)):
            while data[i] >= 10:
                data[i] = data[i]/10
        
        first_digits = [int(x) for x in sorted(data)]
        
        unique = (set(first_digits))
        
        observed = []
        
        for i in unique:
            count = first_digits.count(i)
            observed.append(count)
        
        total_count = sum(observed)
        
        data_percentage = [(i/total_count)*100 for i in observed]
        
        return  total_count, observed, data_percentage

    def _benford(self):
        leading_digits = np.array(list(map(lambda x: math.log(1 + (1 / x), 10), np.arange(1, 10)))) * 100

        return leading_digits
    
    #Return list of expected Benford's Law counts for total sample count.
    def _get_expected_counts(self):
        total_count = self._total_count
        benford = self._benford()

        return [round(p * total_count / 100) for p in benford]
    
    def _chi_square_test(self):
        observed = self._observed
        expected = self._expected
        alpha = self._alpha
        tabulated = self._tabulated
        x2 = 0  

        for o, e in zip(observed,expected):

            d = math.pow(o - e, 2)

            x2 += d / e
        
        compare = x2 < tabulated  

        return x2, compare

    def bar_chart(self):

        data_pct = self._data_percentage
        BENFORD = self._benford()

        fig, ax = plt.subplots()

        index = [i + 1 for i in range(len(data_pct))]  

        fig.canvas.set_window_title('Percentage First Digits')

        ax.set_title('Data vs. Benford Values', fontsize=15)

        ax.set_ylabel('Frequency (%)', fontsize=16)

        ax.set_xticks(index)

        ax.set_xticklabels(index, fontsize=14)


        # build bars    

        rects = ax.bar(index, data_pct, width=0.95, color='black', label='Data')


        # attach a text label above each bar displaying its height

        for rect in rects:

            height = rect.get_height()

            ax.text(rect.get_x() + rect.get_width()/2, height,

                    '{:0.1f}'.format(height), ha='center', va='bottom', 

                    fontsize=13)



        # plot Benford values as red dots

        ax.scatter(index, BENFORD, s=150, c='red', zorder=2, label='Benford')



        # Hide the right and top spines & add legend

        ax.spines['right'].set_visible(False)

        ax.spines['top'].set_visible(False)

        ax.legend(prop={'size':15}, frameon=False)



        plt.show()

        #2nd_bar_chart
        labels=list(data_pct)
        width = 0.35 
        x = np.arange(len(data_pct)) # the label locations
        width = 0.35  # the width of the bars
        fig, ax = plt.subplots()
        rects1 = ax.bar(x - width, data_pct, width=0.95, color='black', label='Data')
        rects2 = ax.bar(x + width, BENFORD,width,label='Benford')
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Frequency (%)', fontsize=16)
        ax.set_title('Benford')
        ax.set_xticks(x)
        ax.legend()
        plt.show()