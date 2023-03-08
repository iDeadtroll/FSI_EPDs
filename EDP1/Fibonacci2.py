# EJ1. (30 min.) Implemente la función de Fibonacci:
# a) Utilizando recursividad y sin utilizar estructuras de datos.
# b) Utilizando recursividad y un diccionario para memorizar los resultados ya calculados.
# Recuerde que:
#  Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
#  Fibonacci(0) = 0
#  Fibonacci(1) = 1

# a) Utilizando recursividad y sin utilizar estructuras de datos.
n = int(input("Ingrese un valor: "))
if n<0:
    print("Valor no valido")
else:
    def fibo(n):
        if n==0 or n==1:
            return n
        else:
            return fibo(n-1) + fibo(n-2)

    print(fibo(n))

