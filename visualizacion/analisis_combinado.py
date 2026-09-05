import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib.dates as mDates 
import pandas as pd 

def cambio(data, media_movil:int): 
    fig, ax=plt.subplots(figsize=(12,5))
    sns.lineplot(data[0]['temp_avg'].rolling(window=media_movil).mean(), label="% Cambio de temperatura promedio", ax=ax )

    sns.lineplot(data[1]['CO2Mean'], color='r', label='% Cambio concentración CO2 promedio', ax=ax)
    ax.lines[1].set_linestyle("--")

    ax.set_xlabel("Año")
    ax.set_ylabel("Porcentaje de variación (%)")
    ax.xaxis.set_major_locator(mDates.YearLocator(10))
    plt.xticks(rotation=90)
    ax.axhline(y=0, alpha=0.7, color='black', linestyle='-.', linewidth=0.7)
    ax.axvline(pd.to_datetime('1954-01-01'), color='black', linestyle='-.', lw=0.7);

    plt.show() 