"""
Hacer control de encendido de los vehiculos, 
para esto al momento de usar el método encender, 
se debe validar el nivel de combustible del vehiculo (medida dada en galones) no este por debejo de un 10%, 
si este tiene un nivel muy bajo, mostrar la advertencia que necesita ir a la gasolinera. 
"""

class Vehiculo:
  marca: str
  combustible: str
  tipo: str
  capacidad_maxima: float
  nivel_combustible: float

  def __init__(self, marca, combustible):
    self.marca = marca 
    self.combustible = combustible

  def encender(self):
    if (self.nivel_combustible * 100) / self.capacidad_maxima < 10:
      print("Advertencia, nivel de combustible bajo")
    else:
      print("El nivel de combustible es optimo")
    
  def arrancar(self):
    pass

  def __str__(self):
    return "El vehiculo tipo {} {} necesita gasolina {} para operar".format(self.tipo, self.marca, self.combustible)


class Moto(Vehiculo):
  
  def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Moto'
      self.capacidad_maxima = 2.3
      self.nivel_combustible = 1

class Carro(Vehiculo):
  
  def __init__(self, marca, combustible):
      super().__init__(marca, combustible)
      self.tipo = 'Carro'
      self.capacidad_maxima = 24
      self.nivel_combustible = 2.2


carro = Carro('Mazda', 'Extra')
carro.encender()

moto = Moto('Suzuki', 'Corriente')
moto.encender()