# Practica generadores 2: https://www.youtube.com/watch?v=ucaHqGII350&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=20
lista = []
city1=str(input("Ingresa nombre de ciudad: "))
lista.append(city1)
city1=str(input("Ingresa nombre de ciudad: "))
lista.append(city1)
print(lista)

def devuelve_ciudades1(*ciudades): #Generador que devuelve elemento a elemento
    for elemento in ciudades:
        yield elemento

ciudades_devevueltas1 = devuelve_ciudades1("Madrid", "Barcelona", "Bilbao", "Valencia")

# print(next(ciudades_devevueltas))
# print(next(ciudades_devevueltas))


def devuelve_ciudades2(*ciudades): #Generador que devuelve elemento con su respectivo subelemento.
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento

ciudades_devevueltas2 = devuelve_ciudades2("Madrid", "Barceloan", "Bilbao", "Valencia")

# print(next(ciudades_devevueltas))
# print(next(ciudades_devevueltas))

def devuelve_ciudades3(*ciudades): #Generador que devuelve elemento con su respectivo subelemento.
    for elemento in ciudades:
        # for subElemento in elemento:
            yield from elemento #Con "yield from" podemos presindir de un bucle "for" anidado.

ciudades_devevueltas3 = devuelve_ciudades3("Madrid", "Barceloan", "Bilbao", "Valencia")

for ciudades in ciudades_devevueltas1:
    print(ciudades)

