from scipy.stats import kstest
from scipy import stats
import pandas as pd
import numpy as np
import seaborn as sns
import chardet
import pycountry
import csv
from pathlib import Path

   
def refactorGiniWorldBankDf(gini):
    
    print('ok')
    giniData = gini.copy()

    if 'Country Name' in giniData.columns and 'Country Code' in giniData.columns and 'Indicator Name' in giniData.columns and 'Indicator Code' in giniData.columns : 
        getOnlyDate = giniData.drop(columns=['Country Name', 'Country Code','Indicator Name','Indicator Code'])

        firstDateColumnGini = int(getOnlyDate.columns[0])
        lastDataColumnGini = int(getOnlyDate.columns[len(getOnlyDate.columns) - 1])
        
        giniData = giniData.melt(id_vars=['Country Name'], value_vars=[str(annee) for annee in range(firstDateColumnGini, lastDataColumnGini)], var_name='year', value_name='value')
        giniData = giniData.sort_values(['Country Name','year'])
        return giniData;
