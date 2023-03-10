cuentas = {("sevilla",41013) : [300,450,True],
           ("madrid",18650) : [400,300,False],
           ("segovia",28901) : [500,350,False],
           ("segovia",28902) : [450,500,True]}
# el primer elemento indica ingresos, el segundo gastos y tercero si la diferencia es negativa.
if cuentas[("segovia",28901)][2] or cuentas[("segovia",28902)][2]:
    print ("Alguna de las cuentas de Segovia es negativa")
else:
    print ("Todas las cuentas de Segovia son positivas")
mensaje = "Sevilla (41013) " + ("no " if (cuentas[("sevilla",41013)][2]) else "") + "tiene su cuenta positiva"
print (mensaje)
listas_claves = list()
for claves in cuentas.keys():
    listas_claves.append(claves)
