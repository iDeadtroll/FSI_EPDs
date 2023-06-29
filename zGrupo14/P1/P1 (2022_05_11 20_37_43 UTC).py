
print("Bienvenido al programa de gestion de equipos de futbol\n")
salir = False
#Diccionario a utilizar
diccionario = {}
while salir is False:

    print(" 1.Agregar un nuevo registro\n 2.Buscar un registro por su clave y mostrar sus valores\n 3.Borrar un registro a partir de su clave\n 4.Listar todos los registros en formato de tabla \n 5.Salir")
    opcion_elegida = int(input(" Introduzca la operacion que desea hacer: "))

    if (opcion_elegida == 1):
        print("\n Introduzca los valores del nuevo registro:\n")
        
        clave = int(input(" Introduzca la clave: "))
        
        nombre_club = input("\n Introduzca el nombre del club: ")
        nombre_competicion = input("\n Introduzca el nombre de la competicion: ")
        tamanio_equipo = int(input("\n Introduzca el tamanio del equipo: "))
        media_edad = int(input("\n Introduzca la media de edad de los jugadores: "))
        valor_mercado_equipo = int(input("\n Introduzca el valor en el mercado del equipo: "))
        valor_mercado_jugadores = int(input("\n Introduzca el valor en el mercado de los jugadores: "))
        valor_mercado_jugadores_top = int(input("\n Introduzca el valor en el mercado de los jugadores top: "))
        diccionario[clave] = clave,nombre_club,nombre_competicion,tamanio_equipo,media_edad,valor_mercado_equipo,valor_mercado_jugadores,valor_mercado_jugadores_top
        
    elif (opcion_elegida == 2):
        clave_buscar = int(input("\n Introduzca la clave a buscar: "))
        for i in diccionario[clave_buscar]:
            print(i)
    elif(opcion_elegida == 3):
        clave_borrar = int(input("\n Introduzca la clave a borrar: "))
        del(diccionario[clave_borrar])
    elif (opcion_elegida == 4):
        print(diccionario)
    elif (opcion_elegida == 5):
        print("\n Saliendo del programa")
        salir = True
    else:
        print("Por favor escoja una opcion de las que le ofrecemos: \n")
        

print(" Gracias por usar el programa!")


        