# EJ3. (10 min.) Utilizando comprensión de listas y el generador de rangos range(n), cree una lista con los múltiplos de 3
# entre el 1 y el 100

multiplos_de_3 = [i for i in range(1, 101) if i % 3 == 0]

print(multiplos_de_3)