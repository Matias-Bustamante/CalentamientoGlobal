import pandas as pd 

def CO2EliminarColumna(data:pd.DataFrame)->pd.DataFrame: 
    temp=data[["Year", "CO2Mean"]]
    return temp 

def CO2ConvertirASerieDeTiempo(data:pd.DataFrame)->pd.DataFrame: 
    temp=data 
    indice=pd.to_datetime(temp["Year"], format="%Y")
    temp=temp.set_index(indice) 
    temp=temp.drop(columns='Year')
    return temp 

def CO2FiltrarCO2(data:pd.DataFrame)->pd.DataFrame: 
    temp=data[data["Polutant:text"]=="CO2 (ppm)"]
    temp=temp.drop(columns="Polutant:text")
    return temp

def CO2RenombrarColumna(data:pd.DataFrame)->pd.DataFrame: 
    temp=data.rename(columns={ 
        "Year:year":"Year", 
        "Value:number":"CO2Mean"
    })
    return temp 

def CO2Remuestrear(data:pd.DataFrame): 
    temp=data.resample('1YS').ffill() 
    return temp 

def Concatenar(co2_2:pd.DataFrame, co2_1:pd.DataFrame): 
    return pd.concat([co2_2[:'1958'], co2_1])