def fibonacci(penultimo, ultimo, n):
    print(ultimo)
    if n > 1:
        actual = ultimo + penultimo
        fibonacci(ultimo, actual, n-1)

def fibo(n):
    fibonacci(0, 1, n)

fibo(7)
