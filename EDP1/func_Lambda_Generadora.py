#La funcion lambda(): "suma" recibe un parametro "n"
suma = lambda n: \
    sum(i for i in range(n)) #Funcion generadora "sum()" recibe "n" y tambien lo usa como parametro para "range()"
                             # "i" variable Iterable

#La funcion lambda suma los elementos generados por la funcion generadora
print(suma(5))