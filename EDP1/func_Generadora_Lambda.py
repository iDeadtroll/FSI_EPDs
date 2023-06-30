# Generamos una lista de 'n' elementos
# El valor de cada elemento sera el resultado de la funcion lambda
def generador(n):             #Funcion Generadora
    i = 0                     #Variable Iterable
    while i < n:              #Criterio de parada del generador
        yield i
        i += 1                #Funcion generadora

mi_generador = generador(5)  #Funcion generadora recibe en 'numero' de elementos

cuadrado = lambda x: x ** 2  #Funcion lambda que utiliza el

for i in mi_generador:       #Recorrido de elementos de generados por la funcion generadora.
    print(cuadrado(i))
