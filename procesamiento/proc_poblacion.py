import pandas as pd 

def FiltrarWorld(data:pd.DataFrame)->pd.DataFrame: 
    return data[data["Region, subregion, country or area *"]=="World"]

def PoblacionObtenerColumnas(data:pd.DataFrame)->pd.DataFrame: 
    return data[["Year","Total Population, as of 1 January (thousands)"]]

def PoblacionRenombrarColumna(data:pd.DataFrame)->pd.DataFrame: 
    return data.rename(columns={ 
        "Year":"Year", 
        "Total Population, as of 1 January (thousands)":"total_pop_1k"
    }) 

def ConvertirASerieDeTiempo(data:pd.DataFrame)->pd.DataFrame: 
    temp=data 
    indice=pd.to_datetime(temp["Year"], format="%Y")
    temp=temp.set_index(indice)
    temp=temp.drop(columns='Year')
    return temp 
