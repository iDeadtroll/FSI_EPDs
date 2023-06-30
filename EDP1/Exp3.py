# El primer numero indica ingresos, el segundo gastos.
cuentas = {"sevilla" : [300,450], "madrid" : [400,300], "segovia" : [500,350], "valencia" : [450,300]}
print("Diccionario cuentas:\n", cuentas)


#Actulizar el valor de la clave 'sevilla'
cuentas['sevilla']=[400,500]
print('Cuentas actualizado:\n',cuentas)
#Mostrar lista de claves
claves= list(cuentas.keys())
print("\nLista de claves del diccionario:\n",claves)

#Mostrar lista con las 2 primeras claves
print("\nLista con las 2 primeras claves:\n",claves[:2])

#Mostrar lista con las 2 ultimas claves
print("\nLista con las 2 ultimas claves:\n",claves[-2:])

#Mostrar lista con primera y tercera clave
print("\nLista con primera y tercera clave:\n",claves[::2])

#Mostrar lista con segunda y cuarta clave
print("\nLista con segunda y cuarta clave:\n",claves[1::2])

#Mostrar lista con primera y ultima clave
print("\nLista con primera y ultima clave:\n",claves[::len(claves)-1])

#Mostra primera clave del dicionario
print("\nPrimera clave:\n",claves[0])

#Mostra ultima clave del dicionario
print("\nUltima clave:\n",claves[len(claves)-1])

#Claves del diccionario
print("\nClaves del diccionario:")
for i in claves:
    print("\t",i)

#Claves del diccionario en una sola linea
print("\nClaves en una sola linea:\n", " ".join(ciudad for ciudad in claves))



#Mostrar valores de la clave "valencia"
print("\nValores de la clave 'valencia'\n",cuentas["valencia"])

#Mostrar primer valor de la clave "valencia"
print("\nPrimer valor de la clave 'valencia'\n",cuentas["valencia"][0])

#Mostrar los valores de las claves 'sevilla' y 'segovia'
cuentasMadridYSegovia = [cuentas["madrid"],cuentas["segovia"]]
print("\nValores de las claves 'sevilla' y 'segovia':\n",cuentasMadridYSegovia)

#Agregar valor a la clave "sevilla"
print("\nAgregar valor a la clave 'sevilla':")
print("\tAntes: ",cuentas["sevilla"])
cuentas["sevilla"] = cuentas["sevilla"] + [True]
print("\tDespues: ",cuentas["sevilla"])

#Lista de valores del diccionario
valores = list(cuentas.values())
print("\nLista de valores del diccionario:\n", valores)

#Primer elemento de la lista de valores
print("\nPrimer elemento de la lista de valores:\n", valores[0])

#Primer elemento del primer elemento de la lista de valores
print("\nPrimer elemento del primer elemento de la lista de valores:\n", valores[0][0])

#Lista de los primeros elementos de la lista de valores
primerosElementos = list(valores[0] for valores in cuentas.values())
print("\nPrimeros elementos de la lista de valores:\n", primerosElementos)

#Lista de los ultimos elementos de la lista de valores
ultimosElementos = list(valores[len(valores)-1] for valores in cuentas.values())
print("\nUltimos elementos de la lista de valores:\n", ultimosElementos)

#Lista de valores del diccionario
index = 0
print("\nLista de valores del diccionario:")
for ciudad in cuentas.values():
    print("\t",ciudad)

#Sumar los valores, correspondientes a los ingresos
sumaIngresos = cuentas['sevilla'][0] + cuentas['madrid'][0] + cuentas['segovia'][0] + cuentas['valencia'][0]
print("\nSuma de ingresos de",",".join(ciudad for ciudad in cuentas.keys()),f"\n{sumaIngresos}\n")

#Sumar los valores, correspondientes a los gastos.
sumaGastos = cuentas["sevilla"][1] + cuentas["madrid"][1] + cuentas["segovia"][1] + cuentas["valencia"][1]
print("Suma de gastos de",",".join(ciudad for ciudad in cuentas.keys()),f"\n{sumaGastos}\n")

#Mostrar cuentas Madrid METODO facil 1.
print('Cuentas de Madrid' , '\nIngresos:', cuentasMadridYSegovia[0][0], '\nGastos: ', cuentasMadridYSegovia[0][1])

#Mostrar cuantas Madrid METODO dificil 2.
print("Ingresos y gastos de Madrid:")
print(f'Ingresos {list(cuentas.keys())[1].title()}: ', cuentas["madrid"][0],f'\nGastos {list(cuentas.keys())[1].title()}: ', cuentas["madrid"][1],"\n")



for ciudad in cuentas.keys():
    print(f"Ingresos {ciudad.title()}:",cuentas[ciudad][0])


print('Cuentas: ', ', '.join(ciudad.title() for ciudad in cuentas.keys()))
print('\n'.join(f'\t{clave}{valor}' for clave, valor in cuentas.items()))


