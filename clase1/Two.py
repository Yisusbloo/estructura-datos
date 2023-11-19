"""
Crear dos clases, Moto y Carro, estas clases deben estar heradadas de la clase Vehiculo. 
Realizar dos instancias de las nuevas clases creadas e imprimir el objeto instanciado
"""

class Vehiculo:

    marca: str
    Combustible: str

    def __init__(self, marca, combustible):
        self.marca = marca 
        self.combustible = combustible

    def encender (self):
        pass

    def arrancar (self):
        pass

    def __str__(self):
        return "El vehiculo {} necesita gasolina {} para operar".format(self.marca, self.combustible)
    
class Moto(Vehiculo):
    pass
class Carro(Vehiculo):
    pass

print("-"*45)
carro = Carro('Mazda', 'Extra')
print(carro)

moto = Moto('Suzuki', 'Corriente')
print(moto)
print("-"*45)
