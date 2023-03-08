class StockProducto:

    def __init__(self, producto, stock = 0):
        self._producto = producto
        self._stock = stock

    @property
    def producto(self):
        return self._producto

    @producto.setter
    def nombre(self, p):
        self._producto = producto

    @property
    def precio(self):
        return self._precio

    @nombre.setter
    def nombre(self, precio):
        self._precio = precio

    def __eq__(self, other):
        if isinstance(other, Electrodomes):
            return self.nombre == other._nombre

    def __str__(self):
        return "Nombre: "