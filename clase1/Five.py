"""
Ejerccior libre. 
Debes hacer un ejercicio donde por medio de un metodo, el vehiculo de marcha 
y haga un consumo de combustible a medida que este funcione, 
cuando llegue a los niveles de combustible definidos en el mensaje anterior, 
muestre la advertencia y si esta llega a cero, detenga la marcha 
"""

class Vehiculo:
    def __init__(self, nivel_combustible):
        self.nivel_combustible = nivel_combustible
        self.encendido = False

    def encender(self):
        if self.encendido:
            print("El vehículo ya está encendido.")
        else:
            print("Encendiendo el vehículo.")
            self.encendido = True

    def apagar(self):
        if not self.encendido:
            print("El vehículo ya está apagado.")
        else:
            print("Apagando el vehículo.")
            self.encendido = False

    def avanzar(self, distancia):
        if not self.encendido:
            print("El vehículo está apagado. Enciéndelo antes de avanzar.")
        else:
            consumo = distancia * 0.3  #Consumo de combustible por kilometros
            if self.nivel_combustible >= consumo:
                self.nivel_combustible -= consumo
                print(f"Avanzando {distancia} km. Nivel de combustible restante: {self.nivel_combustible:.2f} litros")
                if self.nivel_combustible <= 10:
                    print("Advertencia: Nivel de combustible bajo.")
                if self.nivel_combustible <= 0:
                    print("El vehículo se quedó sin combustible. Deteniendo la marcha.")
                    self.apagar()
            else:
                print("No hay suficiente combustible para avanzar esa distancia.")

# Vehiculo con 50 litros de combustible
vehiculo = Vehiculo(nivel_combustible=50)

# Encender el vehículo
vehiculo.encender()

# Avanzar algunas distancias
vehiculo.avanzar(0)
vehiculo.avanzar(10)
vehiculo.avanzar(20)
vehiculo.avanzar(30)
vehiculo.avanzar(40)
vehiculo.avanzar(50)
# Apagar el vehículo
vehiculo.apagar()