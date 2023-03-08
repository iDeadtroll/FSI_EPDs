def cociente(dividendo, divisor):
    if dividendo - divisor == 0:
        return 1
    else:
        dividendo = dividendo - divisor
        result = cociente(dividendo, divisor)
        result = result + 1

        return result

div = cociente(144,12)
print(div)