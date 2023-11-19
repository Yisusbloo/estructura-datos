#Biblioteca Panda, es una biblioteca de python la cual permite manejar datos.
# Example http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2017.csv
import pandas as pd

class EncuestaCultura:

    url =str
    name    = str
    url_comillas = ""
    
    def __init__(self,url,name):
        self.url  =url
        self.name =name
    def calcular_Promedio(self):
        pass
    def calcular_suma(self):
        pass

print("-"*65)
name =input("Ingresa el nombre de la encuesta de MeData a trabajar: ")
print("-"*65)

url = input("Ingresa la url de la pagina MeData a trabajar: ")
url_Comillas = f'"{url}"'
print(url_Comillas)
print("-"*65)

columna =input("Ingresa la columna del archivo la cual deseas trabajar: ")
print(columna)
print("")

busqueda = input("Ingresa el filtro de lo que buscar en la columna: ")
print(busqueda)
print("-"*65)

columna1 =input("Ingresa la columna del archivo la cual deseas trabajar: ")
print(columna1)
print("")

busqueda1 = input("Ingresa el filtro de lo que buscar en la columna: ")
print(busqueda1)
print("-"*65)

df = pd.read_csv(url, sep=";")
print(df[(df.columna =="busqueda") & (df.columna1 == "busqueda1")])
#print(df[(df.acu_cal_cla =="Siempre")& (df.acu_id_culp == "Nunca")])