"""
Crear una clase llamada Vehículo, esta clase debe recibir 2 parámetros, marca y combustible; la también debe contener dos métodos encender y arrancar. 
Instanciar la clase y usar el método mágico __str__ para imprimir la marca y el combustible usado
"""

class Vehiculo:

    marca =""
    combustible =""

    def encender (self):
        return f"Se enciende el vehiculo con combustible  {self.combustible}"
    
    def arrancar (self):
        pass

    def __init__(self,combustible,marca):
        self.marca=marca
        self.combustible=combustible
        
    def __str__(self):
        return "El vehiculo {} necesita gasolina {} para operar".format(self.marca, self.combustible)

carro = Vehiculo("corriente", "Mazda")
print("-"*45)
print(carro)
print("-"*45)