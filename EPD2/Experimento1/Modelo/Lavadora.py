from Modelo.Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):

    def __init__(self, carga = 0):
        self.carga = carga

    @property
    def carga(self):
        return self._carga

    @carga.setter
    def pulgadas(self, carga):
        self._carga = carga