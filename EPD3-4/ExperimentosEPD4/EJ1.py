# Ejericio para aplicar operaciones CRUD (Crear Leer Actualizar Borrar)

# Priemro hacermos una clase  cliente valor
def menu():
    print('1. Añadir cliente')
    print('2. Eliminar cliente')
    print('3. Mostrar cliente a partir de su NIF')
    print('4. Listar todos los clientes')
    print('5. List clientes preferentes')
    print('6. Terminar')
    opt = input("Elija una opcion:")
    # match opt:
    #     case "1":


        # case "1":
        # case "1":
        # case "1":
        # case "1":


class Cliente:

    def __init__(self, nombre, direccion, telefono, correo, vip):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.vip = vip


cliente_a = Cliente("Juan Pérez", "Calle Falsa 123", "555-1234", "juan.perez@email.com")

print(cliente_a)



