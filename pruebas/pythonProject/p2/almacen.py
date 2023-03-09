class Almacen:
    def __init__(self):
        self.__departamentos = []

    @property
    def departamentos(self):
        return self.__departamentos

    @departamentos.setter
    def departamentos(self, departamentos):
        self.departamentos = departamentos

    def addDepartamento(self, departamento):
        self.departamentos.append(departamento)

    def removeDepartamento(self, departamento):
        self.departamentos.remove(departamento)
