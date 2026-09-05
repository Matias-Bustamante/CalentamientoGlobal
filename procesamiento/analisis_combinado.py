import pandas as pd 

def cambio_porcentual(temp:pd.Series, co2:pd.Series): 
    temp_base=temp[:'1954']['temp_avg'].mean() 
    temp_base=100*(temp-temp_base)/temp_base 

    co2_base=co2[:'1954']['CO2Mean'].mean() 
    co2_base=100*(co2-co2_base)/co2_base

    return temp_base, co2_base