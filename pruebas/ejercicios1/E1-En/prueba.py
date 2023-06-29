#   Practica para ver la diferencia de una funcion normal y una funcion generador
from typing import Any

class genera_pares():
    # Metodo constructor de la clase
    def __init__(self):
        self.__lista = []
        self.__mensaje = "Tu lista generada es:"

    def mensaje(self):
        return self.__mensaje

    def lista(self):
        return self.__lista

    # Funcion normal para obtener numeros pares
    def generaPares1(self):

        num1 = 1
        num2 = int(input("Ingresa el tamanyo de la lista:"))
        listaPares = []
        while num1 <= num2:
            listaPares.append(num1*2)

            num1= num1 +1
        self.__lista = listaPares





