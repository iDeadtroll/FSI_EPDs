# Practica de herencia multiple!
class Vehiculos():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha=True

    def acelerar(self):
        self.acelera=True

    def frenar(self):
        self.acelera=True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enmarcha, "\nAcelerando: ", self.acelera, "\nFrena: ", self.frena)

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

class Moto(Vehiculos):
    hcaballito = ""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"

class VElectricos(Vehiculos):
    def __init__(self, marca , modelo):
        super().__init__(marca, modelo)
        self.autonomia=100

    def cargaEnergia(self, carga):
        self.cargado=carga
    def estado(self):
        print(Vehiculos.estado(self), "\nCarga de Energia:", self.cargado, "\nAutonomia: ", self.autonomia)

class BiciElectrica(VElectricos,Vehiculos):
    pass

miMoto= Moto("Honda", "CBR")
miMoto.arrancar()
miMoto.caballito()
miMoto.estado()
print(miMoto.hcaballito)
print("-----------------------")
miFrugoneta = Furgoneta("Renault", "Reno")
miFrugoneta.arrancar()
miFrugoneta.estado()
print(miFrugoneta.carga(True))
print("------------------------")
miBici=BiciElectrica("Xiaomi", "X365")
miBici.cargaEnergia(True)
miBici.estado()

