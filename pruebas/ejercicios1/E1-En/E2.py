from E1 import raiz
from E3 import genera_pares as gp
#   Ejemplo de if "algo" in "algo"
#   Para este ejemplo se considera que un correo es correcto si contiene "@"
def mail_correcto1():
    correo = input("Introduzca una direccion de correo: ")

    if "@" in correo:
        print("Correo correcto!")
    else:
        print("Correo incorrecto!")

#   Ejemplo de uso para la función "continue":
#   Contar caracteres excluyendo los espacios en blanco
def contar_caractares():
    frase = input("Introduce una frase: ")
    contador = 0

    for i in frase:
        if i == " ":
            continue
        contador += 1
    print(f"Tu frase contiene {contador} caracteres", end="\n\n")


#   Ejemplo 1: de "for i in range(parametros)"
#   El bucle se repetira "n" veces e imprimirá una frase y el valor de la variable "i"
def ejemplo1_for():

    frase = input("Introduzca una frase: ")
    n = int(input("Indique el numero de veces que desea imprimir la frase: "))
    for i in range(n):
        j = i+1
        print(f"{frase} {j}")


#   Ejemplo 2: de "for i in range(parametros)"
#   El recorrido de la función "for" hará el recorrido según los parametros de "range"
def ejemplo2_for():
    print("Numeros desde 'n' hasta 'm' con 'x' saltos entre cada valor ")
    valorInicio = int(input("Indique un valor inicial (n): "))
    valorFin = int(input("Indique un valor final (m): "))
    if valorFin > valorInicio:

        saltos = int(input("Indique saltos entre cada valor (x): "))
        for i in range(valorInicio,valorFin,saltos):
            print(i)
        if (i == valorFin-saltos):
            print(f"'{valorFin}'  Forma parte del patrón!")
        else:
            print(f"'{valorFin}'  No forma parte del patrón!")

    else:
        print("El valor final no valido!")

#   Ejemplo for para recorrido de cadena
#   Se considera que el correo es correcto si contiene un caracter "@"
def ejemplo4_for():
    valido = False
    correo = input("Introduzca una direccion de correo: ")

    for i in correo:
        if i == "@":
            valido = True
    if valido:
        print("Correo correcto!")
    else:
        print("Correo incorrecto!")


#   Ejemplo de uso para las funciones haciendo un menú:

while True:
    print("Programa para probar funciones de Python", end="\n\n")
    print("1. Contar caracteres presentes en una frase")
    print("2. Calcular la raiz cuadrada de un numero")
    print("3. Verificar direccion de correo")
    print("4. Imprimir una frase 'n' veces")
    print("5. Números siguiendo un patrón")
    print("6. Generar numeros pares")
    print("7. Salir del programa")
    eleccion = input("Elige una opción: ")
    if eleccion == "7":
        print("Fin del programa")
        break
    elif eleccion == "1":
        contar_caractares()
    elif eleccion == "2":
        raiz.calcular_raiz(raiz)
    elif eleccion == "3":
        ejemplo4_for()
    elif eleccion == "5":
        ejemplo2_for()
    elif eleccion == "4":
        ejemplo1_for()
    elif eleccion == "6":
        gp.generaPares1(gp)
        print(gp.lista(gp))
    else :
        print("Opcion no valida!")

    input("Presiona 'Enter' para volver al menu...\n")
