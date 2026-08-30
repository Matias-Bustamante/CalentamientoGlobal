import pandas as pd 

def LeerAPI(path: str, espacioBlanco:bool,  salto:int, columnsName:list[str]): 
    if espacioBlanco: 
        data=pd.read_csv(path,sep=r'\s+' ,skiprows=salto, names=columnsName) 
    else: 
        data=pd.read_csv(path, sep=r'\s+' ,skiprows=salto, names=columnsName) 

    return data 

def LeerExcel(path:str, salto:int)->pd.DataFrame: 
    data=pd.read_excel(path,skiprows=salto)
    return data 

def LeerCSV(path:str)->pd.DataFrame: 
    data=pd.read_csv(path) 
    return data 

