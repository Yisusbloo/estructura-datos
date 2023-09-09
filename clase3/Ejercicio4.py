import random

def crear_lista_con_for(num_nodos):
    lista_generada = []
    for i in range(num_nodos):
        numero_aleatorio = random.randint(i, i + 10)
        lista_generada.append(numero_aleatorio)
    return lista_generada

num_nodos = int(input("Ingrese el número de nodos a crear: "))
lista_generada = crear_lista_con_for(num_nodos)
print("Lista generada:",lista_generada)