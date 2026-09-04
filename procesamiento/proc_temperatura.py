import pandas as pd 

def ObtenerColumnas(data:pd.Dataframe)->pd.Dataframe: 
    temp=data[["Year", "Month", "AnomalyMonth"]]
    return temp 

def ObtenerTemperaturaPromedio(data:pd.DataFrame)->pd.DataFrame: 
    proms_ref = [2.59, 3.21, 5.30, 8.29, 11.28, 13.43, 14.31, 13.84, 12.04, 9.20, 6.07, 3.63]
    temp=data 
    temp["temp_avg"]=temp.apply(lambda fila: fila["AnomalyMonth"]+proms_ref[int(fila["Month"])-1], axis=1) 
    return temp 

def EliminarColumnas(data:pd.DataFrame,column:list[str])->pd.DataFrame: 
    for item in column: 
        data.drop(columns=item, inplace=True)
    return data 

def ConvertirDateTimeAIndice(data:pd.DataFrame)->pd.DataFrame: 
    indice=pd.to_datetime(data[["Year", "Month"]].assign(day=1))
    data=data.set_index(indice) 
    return data 

def TemperaturaAyD1950(temperatura:pd.Series): 
    temp_A1950=temperatura[:'1949']["temp_avg"].mean() 
    temp_D1950=temperatura['1950':]["temp_avg"].mean() 
    return temp_A1950, temp_D1950
