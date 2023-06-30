#   Practica para ver la diferencia de una funcion normal y una funcion generador
from typing import Any

class Genera_Lista():
    # Metodo constructor de la clase
    def __init__(self):
        self.__lista = []
        self.__mensaje = "Tu lista generada es:"

    def mensaje(self):
        return self.__mensaje

    def lista(self):
        return self.__lista

    # Funcion normal para obtener numeros pares
    def genera_pares(self):

        num1 = 0
        num2 = int(input("Ingresa el tamanyo de la lista:"))
        listaPares = []

        while num1 < num2:
            listaPares.append(num1*2)
            num1 = num1 + 1
        self.__lista = listaPares

    # Funcion normal para obtener numeros pares
    def genera_impares(self):

        num1 = 0
        num2 = int(input("Ingresa el tamanyo de la lista: "))
        listaImpares = []

        while num1 < num2:
            listaImpares.append(num1*2 + 1)
            num1 = num1 + 1
        self.__lista = listaImpares

    def __str__(self):
        return f"{self.__mensaje} {self.__lista}"



