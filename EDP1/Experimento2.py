# el primer numero indica ingresos, el segundo gastos.
cuentas = [(300, 450), (400, 300), (500, 350), (450, 300)]

#Vector "cuentas" dando saltos de 2 en 2
impares = cuentas[::2]

#Vector "cuentas" dando saltos de 2 en 2, empesando desde la posicion 1
pares = cuentas[1::2]

#Vector "cuentas", de donde solo nos quedamos con 2 dos primeros componentes
dosPrimeros = cuentas[:2]

#Vector "cuentas", de donde solo nos quedamos con 2 dos ultimos componentes
dosUltimos = cuentas[-2:]

#Vector "cuentas", donde saltamos toda la longitud del vector "cuentas" para mostrar el primer componente y el ultimo
primeroYultimo = cuentas[::len(cuentas) - 1]

#Muestra los elementos del vector "cuentas" en orden inverso
ultimoAlPrimero = cuentas[::-1]

print(impares)
print(pares)
print(dosPrimeros)
print(dosUltimos)
print(primeroYultimo)
print(ultimoAlPrimero)