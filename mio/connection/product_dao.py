from connection import Conexion
from product import Producto


class ProductDAO:
    _SELECCIONAR = 'SELECT * FROM producto ORDER BY id_producto'
    _INSERTAR = 'INSERT INTO producto(nombre, precio) VALUES (%s, %s)'
    _ACTUALIZAR = 'UPDATE producto SET nombre=%s, precio=%s WHERE id_producto=%s'
    _ELIMINAR = 'DELETE FROM producto WHERE id_producto=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2])
                productos.append(producto)
            return productos

    @classmethod
    def insertar(cls, producto):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (producto.nombre, producto.precio)
                cursor.execute(cls._INSERTAR, valores)
                return cursor.rowcount

    @classmethod
    def actualizar(cls, producto):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (producto.nombre, producto.precio,
                           producto.id_producto)
                cursor.execute(cls._ACTUALIZAR, valores)
                return cursor.rowcount

    @classmethod
    def eliminar(cls, producto):
        with Conexion.obtenerConexion():
            with Conexion.obtenerCursor() as cursor:
                valores = (producto.id_producto,)
                cursor.execute(cls._ELIMINAR, valores)
                return cursor.rowcount
