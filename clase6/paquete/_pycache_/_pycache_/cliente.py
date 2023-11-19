#Crear una nueva terminal bash
#(pwd) => Donde se encuentra el sistema actualmente
#(ls) => Lugares disponibles donde entrar
#(cd Clase6) => Para que entre a la carpeta de clase6
#(python cliente.py) => para correr los ejemplos de post

import requests

url = 'https://cuddly-telegram-7vppw459wxjfp57r-8000.app.github.dev/'

# ejemplo request en GET
r = requests.get(url)
print(r.text)

# ejemplo request en POST
r = requests.post(url + 'encolar', json={'nombre': 'Juan', 'productos': ['manzana', 'pera'],"Documento":123456})
r = requests.post(url + 'encolar', json={'nombre': 'Sebastian', 'productos': ['Melon'],"Documento":654321})
r = requests.post(url + 'encolar', json={'nombre': 'Tomas', 'productos': ['Aguacate'],"Documento":741258})
r = requests.post(url + 'encolar', json={'nombre': 'Jafir', 'productos': ['Morcilla'],"Documento":369852})
print(r.text)