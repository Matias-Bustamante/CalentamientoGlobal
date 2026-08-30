import pandas as pd 

def VerificarNAN(data:pd.DataFrame):
    return data.isna().sum() 