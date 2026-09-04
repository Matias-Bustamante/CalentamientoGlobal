import matplotlib.pyplot as plt 
import seaborn as sns 
import matplotlib.dates as mDates 

def temperatura_promedio(temperatura, media_movil:int | None): 
    '''Return de temperatura promedio'''
    fig,ax=plt.subplots(figsize=(12,5))
    if media_movil != None: 
        ax=sns.lineplot(temperatura.rolling(window=media_movil).mean()) 
        titulo="Temperatura promedio " + str("media movil: ")+str(media_movil)
    else: 
        ax=sns.lineplot(temperatura)
        titulo="Temperatura promedio" 

    ax.legend_.texts[0].set_text("Temperatura promedio")
    ax.set_title(titulo)
    plt.show()


def temperatura_promedio_anual(temperatura, media_movil, anio, temp):
    fig, ax=plt.subplots(figsize=(12,5))
    diferencia=temp[1]-temp[0] 
    if diferencia>0: 
        icono='▲'
        color='red'
    else: 
        icono='▼'
        color='green'

    sns.lineplot(temperatura.rolling(window=media_movil).mean(), ax=ax)
    ax.xaxis.set_major_locator(mDates.YearLocator(anio)) 
    plt.xticks(rotation=90)
    ax.annotate(
        f"Variación A1950-D1950: {icono} {diferencia:+.2f}°C", 
        xy=(0, 10),
       xytext=(0,10), textcoords="offset points", 
       fontsize=14, color=color, fontweight="bold", ha="center"
    )
    ax.set_title("Temperatura promedio")
    
    plt.show()


