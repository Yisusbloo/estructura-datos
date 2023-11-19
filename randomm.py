"""
vamos a crear una funcion recursiva en donde se creen por un parametro un cierto numero de nodos
luego crear otra funcion recursiva donde muestre una lista con el numero de nodos que se crearon
y por ultimo dentro de los nodos debe haber un dato aleatorio, este debe ser llamado desde la biblioteca random y debemos decirle 
que nos pase un numero entero de la siguente manera:::: numero = random.randint()
"""
import random

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

def crear_nodo(num_nodos):
    if num_nodos <= 0:
        return None
    dato = random.randint(1, 100)  # Genera un número aleatorio entre 1 y 100
    nodo = Nodo(dato)
    num_nodos -= 1
    if num_nodos > 0:
        nodo.hijos.append(crear_nodo(num_nodos))
    return nodo

def contar_nodos(nodo):
    if nodo is None:
        return 0
    contador = 1
    for hijo in nodo.hijos:
        contador += contar_nodos(hijo)
    return contador

def listar_datos(nodo):
    if nodo is None:
        return []
    datos = [nodo.dato]
    for hijo in nodo.hijos:
        datos.extend(listar_datos(hijo))
    return datos

# Solicitar al usuario la cantidad de nodos a crear
try:
    numero_de_nodos = int(input("Ingrese la cantidad de nodos a crear: "))
except ValueError:
    print("Por favor, ingrese un número válido.")
    exit(1)

if numero_de_nodos <= 0:
    print("La cantidad de nodos debe ser mayor que cero.")
else:
    raiz = crear_nodo(numero_de_nodos)
    numero_total_de_nodos = contar_nodos(raiz)
    datos_nodos = listar_datos(raiz)

    print(f"Número total de nodos creados: {numero_total_de_nodos}")
    print(f"Datos de los nodos: {datos_nodos}")