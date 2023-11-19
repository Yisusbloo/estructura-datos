"""
vamos a crear una funcion recursiva en donde se creen por un parametro un cierto numero de nodos
luego crear otra funcion recursiva donde muestre una lista con el numero de nodos que se crearon
y por ultimo dentro de los nodos debe haber un dato aleatorio, este debe ser llamado desde la biblioteca random y debemos decirle 
que nos pase un numero entero de la siguente manera:::: numero = random.randint()
"""

#Libreria random para los numeros aleatorios
import random

#Clase nodo, cada uno tiene un dato y una dirección
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.direccion = None

#En este bloque se crea una funcion recursiva para crear a los nodos
def crear_nodo_aleatorio(n):
    if n <= 0:
        return None
    else:
        # Genera número aleatorio entre 1 y 50
        dato_aleatorio = random.randint(1,50)  
        nodo = Nodo(dato_aleatorio)
        #Aqui resta uno al numero total de nodos, para seguir con el otro
        nodo.direccion = crear_nodo_aleatorio(n - 1)
        return nodo

#En este bloque creamos otra funcion recursiva donde muestra ahora cada nodo, y el =1 es para empezar por el primer numero
def mostrar_nodos(nodo, numero_nodo=1):
    if nodo is None:
        return []
    else:
        resultado_actual = f"Nodo {numero_nodo}: {nodo.dato}"
        return [resultado_actual] + mostrar_nodos(nodo.direccion, numero_nodo + 1)

num_nodos = int(input("Ingrese la cantidad de nodos a crear: "))
print("-"*45)
print(f"La cantidad de nodos creados son: {num_nodos}")
nodo_inicial = crear_nodo_aleatorio(num_nodos)
datos_nodos = mostrar_nodos(nodo_inicial)

for dato in datos_nodos:
    print(dato)
print("-"*45)