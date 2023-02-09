# Diccionario donde tenemos "nombre de localidad" como clave de la lista a la que esta asociada dicha clave.
# El primer numero de la lista indica ingresos, el segundo gastos.

cuentas = {"sevilla" : [300,450], "madrid" : [400,300], "segovia" : [500,350], "valencia" : [450,300]}

cuentasMadridYSegovia = [cuentas['madrid'], cuentas['segovia']]
cuentas["sevilla"] = cuentas["sevilla"] + [True]
sumaIngresos = cuentas['sevilla'][0] + cuentas['madrid'][0] + cuentas['segovia'][0] + cuentas['valencia'][0]
ingresosMadridYSegovia = cuentas['madrid'][0] + cuentas['segovia'][0]
gastosMadridYSevilla = cuentas['madrid'][1] + cuentas['sevilla'][1]
ingresosMenosGastosSevilla = cuentas['sevilla'][0]- cuentas['sevilla'][1]



print(cuentasMadridYSegovia)
print(cuentas)
print(sumaIngresos)
print(ingresosMadridYSegovia)
print(gastosMadridYSevilla)
print(ingresosMenosGastosSevilla)