#   Practica para ver la diferencia de una funcion normal y una funcion generador
class genera_pares:

    def __init__(self):
        self.__lista = []

    def lista(self):
        return self.__lista

    def generaPares1(self): #  Funcion normal para obtener numeros pares

        num1 = 1
        num2 = int(input("Ingresa el tamanyo de la lista:"))
        listaPares = []
        while num1 <= num2:
            listaPares.append(num1*2)

            num1= num1 + 1
        self.__lista = listaPares


    # print(generaPares1(10)) #Devuelve lista de numeros pares

    #   Funcion generadora para obtener numeros pares
    def generaPares2(Limite):

        num = 1
        while num < Limite:
            yield  num*2
            num= num +1
    devuelvePares = generaPares2(10) # Objeto generador

    # for i in devuelvePares:
    #     print(i) #Devuelve lista de numeros pares


    #   Misma funcion generadora
    def generaPares3(Limite):

        num = 1
        while num < Limite:
            yield  num*2
            num= num +1
    devuelvePares = generaPares3(10) # Objeto generador

    print(next(devuelvePares)) #Se llama al generador y luego este entra en estado de pausa
    print("Lineas de codigo...")
    print(next(devuelvePares)) #Se  vuelve a llamar al generador y luego entra nuevamente en estado de pausa
    print("Lineas de codigo...")
    print(next(devuelvePares)) # Misma situacion que en la anterior llamada y asi sucesivamente
    print("Lineas de codigo...")
    # Por tanto, en cada llamada no generaria la lista entera, sino que generaria valor tras valor.

# Ejemplo y explicacion: https://www.youtube.com/watch?v=TLVnoqXGWpY&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=19&t=194s