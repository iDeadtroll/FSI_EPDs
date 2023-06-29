# Funcionamiento del bucle while implementando un contador para cortar
# la ejecucion infinita.

import math
class raiz:
    def calcular_raiz(self):

        print("Cálculo de raíz cuadrada")
        numero = int(input("Introduce un número: "))

        intentos = 0

        while numero < 0:
            print("No se puede hallar raíz de un numero negativo")

            # Si se alcanza el numero de intento maximo, el programa termina.
            if intentos == 2:
                print("Has consumido demasiados intentos. El programa ha finalizado")
                break

            # Despues de haber introducido un numero negativo se vuelve a pedir un numero.
            numero = int(input("Introduce un número: "))

            #  Si el número introducido es negativo, el numero de intentos aumentará.
            if numero < 0:
                intentos = intentos + 1
        # Si el número de intentos es menor que dos, se ejecutará la operación.
        if intentos < 2:
            solucion=math.sqrt(numero)
            print("La raíz cuadrada de " + str(numero) + " es " + str(solucion))
