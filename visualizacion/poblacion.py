import matplotlib.pyplot as plt 
import seaborn as sns 

def temp_poblacion(temp): 
    fig, ax=plt.subplots(figsize=(12,5))
    sns.lineplot(temp) 
    plt.show()