from Modelo.Electrodomestico import Electrodomestico

class Televisor(Electrodomestico):


    def __init__(self, pulgadas = 0, fullHD = False):
        self.pulgadas = pulgadas
        self.fullHD = fullHD

    @property
    def pulgadas(self):
        return self._pulgadas

    @pulgadas.setter
    def pulgadas(self, pulgadas):
        self._pulgadas = pulgadas

    @property
    def fullHD(self):
        return self._fullHD

    @fullHD.setter
    def fullHD(self, fullHD):
        self._fullHD = fullHD