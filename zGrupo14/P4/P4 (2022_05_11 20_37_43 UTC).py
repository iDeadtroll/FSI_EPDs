import statistics as stat
from functools import reduce

#Diccionario del tamanio de las plantillas
diccionario={0:24,1:26,2:29,3:27,4:27}
print(diccionario)

#Funcion Filter
avg=stat.mean(diccionario.values())
print(avg)

res=filter(lambda x: (x[0], x[1]>avg), diccionario.items())
print(res)
print(list(res))
#Sacamos la media de jugadores que tienen los 5 primeros equipos
#Funcion Map
mapeo=dict(map(lambda x: (x[0], x[1]+30), diccionario.items()))
print(mapeo)
#Para probar la funcion map hemos añadido 30 jugadores a cada equipo
#Funcion reduce

res=reduce(lambda x, y: x+y, diccionario.values())
print(res)
#Sacamos el total de todos los jugadores que hay en los 5 equipos 