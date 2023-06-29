class Coche():

    def desplazamiento(self):
        print("Me desplazo utilizando 4 ruedas")

class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando 2 ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando 6 ruedas")

# Polimorfismo
def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Coche()
desplazamientoVehiculo(miVehiculo)
miVehiculo2=Camion()
desplazamientoVehiculo(miVehiculo2)
