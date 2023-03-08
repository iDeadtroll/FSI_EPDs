# Multiplicacion como sucesion de sumas, donde "valor" es el valor que queremos multiplicar
#  y n el numeros de veces que sumamos dicho valor.
def multi(valor, n):
    if n == 0:
        return 0
    else:

        result = multi(valor, n - 1)
        result = result + valor

        return result

producto = multi(4,2)
print(producto)
