import pandas as pd

archivo = "http://medata.gov.co/sites/default/files/medata_harvest_files/encuesta_cultura_2013.csv"
df = pd.read_csv(archivo, sep=";")

#Esto es un filtro, el primero busca en la columna "acu_cal_cla" los que digan siempre
#El segundo el cual busca en la columna "acu_id_culp" los que digan Nunca
print(df[(df.acu_cal_cla =="Siempre")& (df.acu_id_culp == "Nunca")])
#print(df[(df.acu_cal_cla =="Siempre")& (df.acu_id_culp == "Nunca")])
 