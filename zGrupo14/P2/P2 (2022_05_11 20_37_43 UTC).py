from tokenize import String

#Clase equipo de futbol
class EquipoFutbol():
    
    def __init__(self,id,nombreEquipo,nombreCompeticion,tamanioPlantilla,mediaEdadJugadores,valorMercadoClub,valorMercadoJugadores,valorMercadoTop18):
        self.id = id
        self.__nombreEquipo = nombreEquipo
        self.nombreCompeticion = nombreCompeticion
        self.__tamanioPlantilla = tamanioPlantilla
        self.__mediaEdadJugadores = mediaEdadJugadores
        self.__valorMercadoClub = valorMercadoClub
        self.__valorMercadoJugadores = valorMercadoJugadores
        self.__valorMercadoTop18 = valorMercadoTop18
        
    @property
    def nombreEquipo(self):
        return self.__nombreEquipo

    @nombreEquipo.setter
    def nombreEquipo(self,valor):
        self.__nombreEquipo = valor

    @property
    def tamanioPlantilla(self):
        return self.__tamanioPlantilla

    @tamanioPlantilla.setter
    def tamanioPlantilla(self,valor):
        self.__tamanioPlantilla = valor
    @property
    def mediaEdadJugadores(self):
        return self.__mediaEdadJugadores

    
    @property
    def valorMercadoClub(self):
        return self.__valorMercadoClub

    @valorMercadoClub.setter
    def valorMercadoClub(self,valor):
        self.__valorMercadoClub = valor

    @property
    def valorMercadoJugadores(self):
        return self.__valorMercadoJugadores

    @valorMercadoJugadores.setter
    def valorMercadoJugadores(self,valor):
        self.__valorMercadoJugadores = valor

    @property
    def valorMercadoTop18(self):
        return self.__valorMercadoTop18

    @valorMercadoTop18.setter
    def valorMercadoTop18(self,valor):
        self.__valorMercadoTop18 = valor

    def __str__(self):
        return 'Nombre del equipo: '+str(self.__nombreEquipo)+',tamanio de la plantilla: '+str(self.__tamanioPlantilla)+',Media de edad de jugadores: '+str(self.__mediaEdadJugadores)+',Valor en el mercado del club: '+str(self.__valorMercadoClub)+',Valor en el mercado de los jugadores: '+str(self.__valorMercadoJugadores)+',Valor en el mercado del top 18: '+str(self.__valorMercadoTop18)


#clase Almacen
class Almacen():
    datos = []

    def __init__(self,datos):
        self.datos = datos



    @property
    def datos(self):
        return self.__datos

    @datos.setter
    def datos(self,valor):
        self.__datos = valor
        
    def altaEquipo(self,EquipoFutbol):
         exito = False
         i = 0
         while exito is False and i < len(self.datos):
             if self.datos[i] == EquipoFutbol:
                 exito = True
             else:
                 i += 1
         
         if exito is False:
             self.datos.append(EquipoFutbol)
             print("OK")
         else:
             print("DUPLICADO") 

    def bajaEquipo(self,ClaveEquipoFutbol):
        exito = False
        i = 0
        while exito is False and i < len(self.datos):
            if self.datos[i].id == ClaveEquipoFutbol:
                self.datos.remove(self.datos[i])
                exito = True
            else:
                i+=1
        if exito is True:
            print("OK")
        else:
            print("NO LOCALIZADO")

    def listadoEquipos(self):
        print("{:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8}".format("ID del equipo","Nombre del equipo","Nombre de la competicion","Tamanio plantilla","Media de edad","Valor del club","Valor jugaodres","Valor Top 18"))
        for v in self.datos:
            id_equipo,nombre,nombre_comp,tamanio,media,valor,valor_jug,valor_top = v
            print("{:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8} {:^8}".format(id_equipo,nombre,nombre_comp,tamanio,media,valor,valor_jug,valor_top))       

#Main
p1 = EquipoFutbol(1,"Sevilla","LaLiga",25,32,167,123,145)
p2 = EquipoFutbol(2,"Betis","LaLiga",26,32,167,132,156)
listaEquipos = []
datos = Almacen(listaEquipos)
datos.altaEquipo(p1)
datos.altaEquipo(p2)
datos.bajaEquipo(3)
