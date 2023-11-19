"""
Crear una pila donde podamos eliminar un dato dentro de esta y se muestren el resto de resultados.
"""

# la creacion de un nodo comun
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# se definen la clase pila con sus funciones de apilar, imprimir esa pila y eliminar el dato especifico dentro de la pila
class Pila:
    def __init__(self):
        self.superior = None

    def apilar(self, dato):
        print(f"Agregando {dato} en la cima de la pila")  # aqui imprimimos los datos almacendos que le pasamos como parametro
        # Si no hay datos, agregamos el valor en el elemento superior y regresamos
        if self.superior == None:
            self.superior = Nodo(dato)
            return
        # en estas tres lineas se crea un objeto que llama al nodo y el dato almacenado y le asignamos la primera posicion de la estructura
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.superior
        self.superior = nuevo_nodo

    def imprimir(self):
        print("Imprimiendo pila:")
        # Recorrer la pila e imprimir valores
        nodo_temporal = (self.superior)  # nuevo objeto creado el cual le asignamos el valor del .superior, que vendria siendo la posicion superior en todo momento
        while nodo_temporal != None:
            print(f"{nodo_temporal.dato}", end=",")
            nodo_temporal = nodo_temporal.siguiente
        print("")

    #Creamos una funcion donde si el dato eliminado es el dato superior de la pila se mostrara de primero el dato que le sigue
    def eliminar_nodo(self, dato_a_eliminar):
        # Si el nodo a eliminar está en la parte superior de la pila
        if self.superior.dato == dato_a_eliminar:
            self.superior = self.superior.siguiente
            return

        # Buscar el nodo a eliminar
        nodo_temporal = self.superior
        while (nodo_temporal.siguiente is not None and nodo_temporal.siguiente.dato != dato_a_eliminar):
            nodo_temporal = nodo_temporal.siguiente

        # Si el nodo a eliminar se encuentra en la pila
        if nodo_temporal.siguiente is not None:
            nodo_temporal.siguiente = nodo_temporal.siguiente.siguiente
        else:
            print(f"No se encontró el dato {dato_a_eliminar} en la pila.")

#Datos dentro de las pilas
pila1 = Pila()
pila1.apilar(0)
pila1.apilar(1)
pila1.apilar(2)
pila1.apilar(3)
pila1.apilar(4)
pila1.apilar(5)
pila1.apilar(6)
pila1.apilar(7)
pila1.apilar(8)
pila1.apilar(9)
pila1.apilar(10)

#Se imprime la pila original, donde muestra los numeros del punto mas alto hasta el mas bajo
print("-"*50)
print("Pila original:")
pila1.imprimir()
print("-"*50)

#Se elige el numero de la pila que se desea eliminar dentro de un rango de 0-10
dato_a_eliminar = int(input("Ingrese el numero de la pila que desea eliminar dentro del rango de 0-10: "))  
pila1.eliminar_nodo(dato_a_eliminar)

#Se imprime la pila despues de eliminar el numero
print(f"Pila después de eliminar el dato {dato_a_eliminar}:")
pila1.imprimir()
print("-"*50)