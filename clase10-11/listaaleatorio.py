import random
import time

# Crear una lista vacía para almacenar los datos aleatorios
lista_aleatoria = []

# Definir la cantidad de elementos que deseas en la lista
cantidad_elementos = 5000  # Puedes cambiar este valor según tus necesidades

# Llenar la lista con datos aleatorios
for _ in range(cantidad_elementos):
    numero_aleatorio = random.randint(1, 10000)  # Genera un número aleatorio entre 1 y 100
    lista_aleatoria.append(numero_aleatorio)

# Imprimir la lista con datos aleatorios
print(lista_aleatoria)

# Verificar si un elemento está presente en la lista
elemento_buscado = int(input("Escriba el dato que desea buscar: "))
inicio = time.time()
if elemento_buscado in lista_aleatoria:
    print(f"{elemento_buscado} está presente en la lista.")
else:
    print(f"{elemento_buscado} no está en la lista.")
fin = time.time()
print("Tiempo de ejecucion: ", fin-inicio)

posicion = lista_aleatoria.index(elemento_buscado)
print("La posicion de ", elemento_buscado, "en la lista es: ", posicion)