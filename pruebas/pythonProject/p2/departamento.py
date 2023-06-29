
class Departamento:
    def __init__(self, id, description):
        self.id = id
        self.description = description

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def description(self):
        return self.__description;

    @description.setter
    def description(self, description):
        self.__description = description

    def toString(self):
        return str(self.id) + self.description
