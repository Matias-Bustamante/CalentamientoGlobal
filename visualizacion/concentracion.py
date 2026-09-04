import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib.dates as mDates 

def temp_concentracion(temp): 
    fig, ax=plt.subplots(figsize=(12,5)) 
    ax=sns.lineplot(temp)
    ax.legend_.texts[0].set_text("Promedio de dioxido de carbono")
    ax.set_title("Promedio de dioxido de carbono")
    plt.show()

def temp_concentracion_anual(temp, anio:int): 
    fig, ax=plt.subplots(figsize=(12,5))

    ax=sns.lineplot(temp) 
    ax.xaxis.set_major_locator(mDates.YearLocator(anio)) 
    ax.legend_.texts[0].set_text("Promedio dioxido de carbono")
    ax.set_title("Promedio dioxido de carbono")
    
    plt.xticks(rotation=90) 
    plt.show()