# Practica Control de exepciones: https://www.youtube.com/watch?v=2MaAs7XU2T0&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=21
def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


op1 = (int(input("Introduce el primer numero: ")))

op2 = (int(input("Introduce el segundo numero: ")))

operacion = input("Introduce la operacion a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operacion no contemplada")

print("Operacion ejecutada. Continuacion de ejecocion del programa ")