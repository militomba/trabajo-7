from producto import Producto
from repository import Repositorios


class ProductoService():

    def get_productosList(self):
        print("Listar Productos")
        return Repositorios.productosList

    def crearProducto(self):
        print("\n---CREAR PRODUCTO")
        descripcion = input("ingrese la descripcion del producto: ")
        precio = int(input("ingrese el precio: "))
        tipo = input("ingrese el tipo de libro: ")
        return Producto(descripcion, precio, tipo)

    '#AGREGAR PRODUCTO'
    def add_producto(self, producto=None):
        print("\n----AGREGAR PRODUCTO")
        if producto is None:
            producto = self.crearProducto
        lastKey = -1
        for productoKey in Repositorios.productosList:
            lastKey = productoKey
        lastKey = int(lastKey) + 1
        Repositorios.productosList[lastKey] = producto.__dict__
        return lastKey

    '#ACTUALIZAR PRODUCTO'
    def update_producto(self, productoKey=None, producto=None):
        print("\n----MODIFICAR PERSONA")
        if productoKey is None:
            productoKey = int(input("Ingrese una llave: "))
        if producto is None:
            producto = self.crearProducto
        Repositorios.productosList[productoKey] = producto.__dict__

    '#algoritmo insertion'
    def insertion_sort_precio(self, lista, tipo_orden):
        lista_ordenada = lista.copy()
        if tipo_orden == "ascendente":
            for i in range(0, len(lista_ordenada)):
                valorNuevo = lista_ordenada[i]
                posicion = i - 1
                while posicion >= 0 and \
                    lista_ordenada[posicion]["_precio"] > \
                        valorNuevo["_precio"]:
                    lista_ordenada[posicion + 1] = lista_ordenada[posicion]
                    posicion = posicion - 1
                lista_ordenada[posicion + 1] = valorNuevo

        if tipo_orden == "descendente":
            for i in range(0, len(lista_ordenada)):
                valorNuevo = lista_ordenada[i]
                posicion = i - 1
                while posicion >= 0 and \
                    lista_ordenada[posicion]["_precio"] < \
                        valorNuevo["_precio"]:
                    lista_ordenada[posicion + 1] = lista_ordenada[posicion]
                    posicion = posicion - 1
                lista_ordenada[posicion + 1] = valorNuevo
        return lista_ordenada

    '#ELIMINAR PRODUCTO'
    def delete_producto(self, productoKey=None):
        print("\n----ELIMINAR PERSONA")
        if productoKey not in Repositorios.productosList:
            raise ValueError("La llave no existe")
        del Repositorios.productosList[productoKey]
    
    'BUSQUEDA BINARIA'
    def busqueda_binaria(self, lista_ordenada, precio):
        lista_ordenada = self.insertion_sort_precio(lista_ordenada, "descendente")
        medio = int(len(lista_ordenada)/2)
        while lista_ordenada[medio]["_precio"] != precio:
            if lista_ordenada[medio]["_precio"] < precio:
                medio = int(medio/2)
            if lista_ordenada[medio]["_precio"] >  precio:
                medio += int(medio/2)
            if lista_ordenada[medio]["_precio"] ==  precio:
                return lista_ordenada[medio]

