from lectura.CargaDatos import LeerAPI, LeerExcel, LeerCSV 
from config.config import VerificarNAN 
from procesamiento.proc_temperatura import ObtenerColumnas, ObtenerTemperaturaPromedio, EliminarColumnas, ConvertirDateTimeAIndice, TemperaturaAyD1950 
from procesamiento.proc_poblacion import FiltrarWorld, PoblacionObtenerColumnas, PoblacionRenombrarColumna, ConvertirASerieDeTiempo
from procesamiento.proc_dioxido_carbono import CO2EliminarColumna, CO2ConvertirASerieDeTiempo, CO2FiltrarCO2, CO2RenombrarColumna, CO2Remuestrear, Concatenar
from procesamiento.analisis_combinado import cambio_porcentual
from visualizacion.diferencia import ControlDiferencia
from visualizacion.temperatura import temperatura_promedio, temperatura_promedio_anual
from visualizacion.poblacion import temp_poblacion 
from visualizacion.concentracion import temp_concentracion, temp_concentracion_anual
from visualizacion.analisis_combinado import cambio

if __name__=='__main__':
    columnas= ['Year','Month', 'AnomalyMonth', 'UncMonth' , 
               'AnomalyAnnual', 'UncAnomaly','AnomalyFiveYear', 'UncFiveYear', 
               'AnomalyTenYear', 'UncTenYear','AnomalyTwentyYear', 'UncTwentyYear'
               ]
    temperatura=LeerAPI('https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Complete_TAVG_complete.txt', 
                        espacioBlanco=True, 
                        salto=34, 
                        columnsName=columnas
                        ) 
    poblacion=LeerExcel('C:/Users/Matias Bustamante/Desktop/Proyecto ciencia de datos/CalentamientoGlobal/data/WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx', salto=16)

    dioxido=["Year", "CO2Mean", "CO2Unc"]

    co2_1=LeerAPI(
                    'https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.txt', 
                    espacioBlanco=True, 
                    salto=45, 
                    columnsName=dioxido

    )
    co2_2=LeerCSV('C:/Users/Matias Bustamante/Desktop/Proyecto ciencia de datos/CalentamientoGlobal/data/atmospheric-concentration-of-carbon-dioxide-5.csv')

    temperatura=ObtenerColumnas(temperatura)
    temperatura=ObtenerTemperaturaPromedio(temperatura)

    ##Verificar si existen datos faltantes 
    print(VerificarNAN(temperatura))

    ##Verificamos la columna temp_avg 
    temp_avg=temperatura[temperatura["temp_avg"].isna()]
    temperatura["temp_avg"]=temperatura["temp_avg"].interpolate() ## aplicamos interpolación a la columna de temp_avg 
    print(temperatura[temperatura["temp_avg"].isna()])

    ##Eliminar columna AnomalyMonth
    temperatura=EliminarColumnas(temperatura, ['AnomalyMonth'])
    temperatura=ConvertirDateTimeAIndice(temperatura)
    temperatura=EliminarColumnas(temperatura, ["Year", "Month"])
    temperatura=temperatura.sort_index() ## Ordenamos de menor a mayor el indice  
    diferencia=temperatura.index-temperatura.index.shift(freq='ME') 
    ControlDiferencia(diferencia) 

    poblacion=FiltrarWorld(poblacion) 
    poblacion=PoblacionObtenerColumnas(poblacion)
    poblacion=PoblacionRenombrarColumna(poblacion)

    ##Verificar si existen datos faltantes 
    print(VerificarNAN(poblacion))

    poblacion=ConvertirASerieDeTiempo(poblacion) 
    poblacion=poblacion.sort_index() 
    PDiferencia=poblacion.index-poblacion.index.shift(freq='1YS')
    ControlDiferencia(PDiferencia)

    ##Dataset de dioxido de carbono 
    co2_1=CO2EliminarColumna(co2_1) 
    co2_1=CO2ConvertirASerieDeTiempo(co2_1)

    co2_2=CO2FiltrarCO2(co2_2)
    co2_2=CO2RenombrarColumna(co2_2) 
    co2_2=CO2ConvertirASerieDeTiempo(co2_2)
    co2_2=CO2Remuestrear(co2_2)
    co2=Concatenar(co2_2=co2_2, co2_1=co2_1)
    
    ##Visualización
    temperatura_promedio(temperatura=temperatura, media_movil=12)
    temp_1950=TemperaturaAyD1950(temperatura=temperatura)
    temperatura_promedio_anual(temperatura=temperatura, media_movil=12, anio=10, temp=temp_1950)

    temp_poblacion(temp=poblacion)

    temp_concentracion(co2)
    temp_concentracion_anual(co2,10)
    
    cambioPorcentual=cambio_porcentual(temp=temperatura, co2=co2) 
    cambio(cambioPorcentual, 12)

   
    
    