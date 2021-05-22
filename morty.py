#Library 
from scipy.stats import chisquare
from benfordslaw import benfordslaw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import folium

class Morty:

    def __init__(self, alpha=0.05):
        """
        _df = dataset 
        _bl = function benfords law 
        """
        self._bl = benfordslaw(alpha=alpha)
        self._df = ""
    
    def add_df(self, df):
        self._df = df

    def benford(self, X):
        result = self._bl.fit(X)

        return result
    
    def call_benford(self, column_name):       
        X = self._df[column_name].values

        result = self.benford(X)

        return result

    def all_estados_br(self, column_name, title, var_state, label_Empirical, path, fontsize=20):
        df = self._df
        state_aux = var_state
        result_por_state = {}

        for state in df[state_aux].unique():
           
            Iloc = (df[state_aux]==state)
           
            X = df[column_name].loc[Iloc].values

            t = title + " - Estado: " + state 

            name = column_name+'-'+state

            result = self.benford(X)

            self.make_plot(path+name, title=t, fontsize=fontsize, label_Empirical=label_Empirical)

            result_por_state[state] = {'p': result['P'], 't': result['t']}
        
        return result_por_state
           

    def por_periodo(self, column_name, title, data_name, time_start, time_stop, label_Empirical, path):
        df = self._df

        Iloc = (df[data_name] >= time_start) & (df[data_name] <= time_stop)
    
        X = df[column_name].loc[Iloc].values
    
        periodo = time_start + ':' + time_stop 
    
        title += ' Período: ' + periodo

        name = column_name + '-' + periodo

        result = self.benford(X)

        self.make_plot(path+name, title=title, label_Empirical=label_Empirical)

        return result


    def heatmap(self, titleCor, path):
        df = self._df

        dfCor = df.corr()

        outcomeCor = abs(dfCor[titleCor])

        plt.figure(figsize=(10,8))
        sns.heatmap(dfCor,cmap='rocket_r',annot=True)
        plt.savefig(path+titleCor+'.jpeg')

    #função de plot em Pt-BR da função de benfordslaw
    def make_plot(self, path, title='', fontsize=16, barcolor='black', barwidth=0.3, figsize=(15, 8), label_Empirical='Distribuição Empírica', ylabel='Frequências (%)', xlabel='Primeiro Dígito'):
        bl = self._bl
        data_percentage = bl.results['percentage_emp']
        x = data_percentage[:, 0]

        # Make figures
        fig, ax = plt.subplots(figsize=figsize)

        # Plot Empirical percentages
        rects1 = ax.bar(x, data_percentage[:, 1], width=barwidth, color=barcolor, alpha=0.8, label=label_Empirical)
        plt.plot(x, data_percentage[:, 1], color='black', linewidth=0.8)

        # ax.scatter(x, data_percentage, s=150, c='red', zorder=2)
        # attach a text label above each bar displaying its height
        for rect in rects1:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height, '{:0.1f}'.format(height), ha='center', va='bottom', fontsize=13)
        
        # Plot expected benfords values
        ax.scatter(x, bl.leading_digits, s=150, c='red', zorder=2, label='Distribuição de Benford')
       
        # ax.bar(x + width, BENFORDLD, width=width, color='blue', alpha=0.8, label='Benfords distribution')
        # plt.plot(x + width, BENFORDLD, color='blue', linewidth=0.8)
        P_result = str(round(bl.results['P'],4)).replace(".", ",")
        T_result = str(round(bl.results['t'],4)).replace(".", ",")
    
        if bl.results['P']<=bl.alpha:
            title = title + "\nAnomalia detectada! P=" + P_result + ", X²=" + T_result
        else:
            title = title + "\nNenhuma anomalia detectada. P=" + P_result + ", X²=" + T_result
        
        # Add some text for labels, title and custom x-axis tick labels, etc.
        fig.canvas.set_window_title('Porcentagem dos Primeiros Dígitos')
        ax.set_title(title, fontsize=fontsize)
        ax.set_ylabel(ylabel, fontsize=fontsize)
        ax.set_xlabel(xlabel, fontsize=fontsize)
        ax.set_xticks(x)
        ax.set_xticklabels(x, fontsize=fontsize)
        ax.grid(True)
        ax.legend()
        
        # Hide the right and top spines & add legend
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.legend(prop={'size': 15}, frameon=False)
        plt.savefig(path+'.jpeg', format='jpeg')
        plt.show()

class Benfords_Law_Two:

    _total_count = _observed = _data_percentage = _expected = 0

    def __init__(self):
        """
        Parameters
        ----------
        N : list or numpy array
            Input data.
        """

        self._N = 0
        self._alpha = 0
        self._tabulated = 0
        
    def init(self, N, tabulated, alpha=0.05):
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

       return [self._chi_square_test(), self._expected, self._total_count, self._observed, self._data_percentage]

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

    def bar_chart(self,title):

        data_pct = self._data_percentage
        BENFORD = self._benford()

        fig, ax = plt.subplots()

        index = [i + 1 for i in range(len(data_pct))]  

        fig.canvas.set_window_title('Porcentagem do Primeiro Dígito')

        ax.set_title(title, fontsize=15)

        ax.set_ylabel('Frequência (%)', fontsize=16)

        ax.set_xticks(index)

        ax.set_xticklabels(index, fontsize=14)


        # build bars    

        rects = ax.bar(index, data_pct, width=0.95, color='black', label='Dados')


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
        rects1 = ax.bar(x - width, data_pct, width=0.95, color='black', label='Dados')
        rects2 = ax.bar(x + width, BENFORD,width,label='Benford')
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Frequência (%)', fontsize=16)
        ax.set_title(title)
        ax.set_xticks(x)
        ax.legend()
        plt.show()


def choropleth(
    df, 
    url_geojson, 
    columns, 
    key_on, 
    legend_name, 
    fill_color='YlOrRd', 
    location=[-15.8267, -47.9218], 
    zoom_start=3, 
    fill_opacity=0.7,
    line_opacity=0.2
    ):

    # Criar o mapa base
    m = folium.Map(location=location, zoom_start=zoom_start)

    #Criar a camada Choroplet
    folium.Choropleth(
        geo_data=url_geojson,
        name='choropleth',
        data=df,
        columns=columns,
        key_on=key_on,
        fill_color=fill_color,
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name=legend_name
    ).add_to(m)
    # Visualizar
    return m