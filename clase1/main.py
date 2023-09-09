class Vehiculo:

    marca = ""
    combustible = ""

    def encender(self):
        return f"se enciende el vehiculo con gasolina o combustible {self.combustible}"

    def arrancar(self):
        pass

    def __init__(self,combustible,marca):
        self.combustible = combustible
        self.marca = marca


carro = Vehiculo("coriente","Mazda")
print(carro.marca)
print("="*10)
print(carro.encender())
