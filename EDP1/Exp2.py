# Lista de tuplas, tuplas de dos elementos.
# Primer elemento de cada tupla indica ingresos.
# Segundo elemento de cada tuplan indica gastos.
cuentas = [(300,450),(400,300),(500,350),(450,300)]
print("Cuentas (ingresos, gastos): " , cuentas ,"\n")
impares = cuentas[::2]
print(f'\tElementos impares de cuentas: {impares}')
pares = cuentas[1::2]
print(f"\tElementos impares de cuentas: {pares}")
dosPrimeros = cuentas[:2]
print(f"\t2 primeros elementos de cuentas: {dosPrimeros}")
dosUltimos = cuentas[-2:]
print(f"\t2 ultimos elementos de cuentas: {dosUltimos}")
primeroYultimo = cuentas[::len(cuentas) - 1]
print(f"\tPrimer y ultimo elemento de cuentas: {primeroYultimo}\n")

#Listas para componer un diccionario.
salida = [impares,pares,dosPrimeros,dosUltimos,primeroYultimo]
cadena = ['Impares: ', 'Pares: ', 'Dos Primeros: ', 'Dos Ultimos: ', 'Primero y Ultimo: ']

clave = cadena
valor = salida
#Formas de componer y mostrar un dicionario.
print("Diccionario ,sin formato, usando funcion 'zip':")
diccionario = dict(zip(clave, valor))
print(diccionario)

print("\nDiccionario ,con formato, usando for x in:")
for keys, values in diccionario.items():
    print("\t",keys,values)

print("\nDiccionario ,con formato, usando for x in range:")
for x in range(len(salida)):
    print("\t",cadena[x], salida[x])

print("\nDiccionario ,con formato, usando compresion de listas:")
print('\n'.join(f'\t{clave}{valor}' for clave, valor in diccionario.items()))
