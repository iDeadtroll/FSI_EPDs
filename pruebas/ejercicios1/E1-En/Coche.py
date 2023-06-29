import time
class Coche():

    def __init__(self, gasolina, aceite, puertas):
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False
        self.gasolina = gasolina
        self.aceite = aceite
        self.puertas = puertas

    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos
        if(self.__enmarcha):
            chequeo = self.chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and not chequeo):
            return "Algo a ido mal en el chequeo. No podemos arrancar el coche"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)

    def chequeo_interno(self):
        print("realizando chequeo interno...")
        time.sleep(1)


        if (self.gasolina):
            time.sleep(1)
            print("Gasolina: ok")
        else:
            print("No hay gasolina")


        if (self.aceite):
            time.sleep(1)
            print("Aceite: ok")
        else:
            print("No hay aceite")


        if (self.puertas):
            time.sleep(1)
            print("Puertas: ok")
        else:
            print("Hay alguna puerta abierta")

        if (self.gasolina and self.aceite and self.puertas):
            return  True
        else:
            return False

print("Probando coche 1")
coche1 = Coche(False,True,True)
print(coche1.arrancar(True))

print("Probando coche 2")
coche2 = Coche(True,False,True)
print(coche2.arrancar(True))

print("Probando coche 3")
coche3 = Coche(True,True,False)
print(coche3.arrancar(True))

print("Probando coche 4")
coche4 = Coche(True,True,True)
print(coche4.arrancar(True))

