class Producto:
    def __init__(self, idproducto, nombre, precio):
        self._idproducto = idproducto
        self._nombre = nombre
        self._precio = precio

    @property
    def idproducto(self):
        return self._idproducto

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"{self.nombre} ===== (${self.precio})"
