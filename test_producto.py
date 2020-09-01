import unittest
from producto import Producto
from parameterized import parameterized
from productoServices import ProductoService
from repository import Repositorios


class TestProducto(unittest.TestCase):

    def test_uso_property(self):
        producto = Producto()
        producto.descripcion = 'acer A515'
        producto.precio = 500000
        producto.tipo = 'computadoras'
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'acer A515',
                                                 '_precio': 500000,
                                                 '_tipo': 'computadoras'})

    def test_constructor_con_valores_iniciales(self):
        producto = Producto("Lenovo 450", 300000, 'computadoras')
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'Lenovo 450',
                                                 '_precio': 300000,
                                                 '_tipo': 'computadoras'})

    @parameterized.expand([
            ("lenovo t490", 6000000, 'computadoras'),
            ("samsung s10", 200000, 'celular'),
            ("samsung s20", 400000, 'celular'),
            ("acer", 6000500, 'computadoras'),
            ("HP", 6000000, 'computadoras'),
        ])
    # Agregar un producto
    def test_add_producto(self, descripcion, precio, tipo):
        producto = Producto(descripcion, precio, tipo)
        productoKey = ProductoService().add_producto(producto)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             producto. __dict__)

    # @parameterized.expand([
    #     ("HP Omen", 790000, 'computadoras')
    # ])
    # # Eliminar un producto
    # def test_delete_producto(self, descripcion, precio, tipo):
    #     producto = Producto(descripcion, precio, tipo)
    #     key = ProductoService().add_producto(producto)
    #     ProductoService().delete_producto(key)
    #     self.assertEqual(Repositorios.productosList.get(key), None)
    #     print(ProductoService().get_productosList())

    @parameterized.expand([
        ("lenovo t490", 6000000, 'computadoras')
    ])
    # Verificar la exeption al modificar un book con un legajo que no existe
    def test_delete_producto_value_error(self, descripcion, precio, tipo):
        long_list = len(Repositorios.productosList)
        with self.assertRaises(ValueError):
            ProductoService().delete_producto(long_list+1)

    # @parameterized.expand([
    #    ("lenovo t490", 6000000, 'laptop', 1)
    # ])
    # def test_update_producto(self, productoKey, descripcion, precio, tipo):
        # produ = Producto(descripcion, precio, tipo)
        # ProductoService().update_producto(productoKey, produ)
        # self.assertDictEqual(Repositorios.productosList[productoKey],
        #                      produ.__dict__)

    @parameterized.expand([
        ("ascendente", {
         0: {'_descripcion': 'samsung s10',
             '_precio': 200000, '_tipo': 'celular'},
         1: {'_descripcion': 'samsung s20',
             '_precio': 400000, '_tipo': 'celular'},
         2: {'_descripcion': 'lenovo t490',
             '_precio': 6000000, '_tipo': 'computadoras'},
         3: {'_descripcion': 'HP',
             '_precio': 6000000, '_tipo': 'computadoras'},
         4: {'_descripcion': 'acer',
             '_precio': 6000500, '_tipo': 'computadoras'}}),
        ("descendente", {
         0: {'_descripcion': 'acer',
             '_precio': 6000500, '_tipo': 'computadoras'},
         1: {'_descripcion': 'lenovo t490',
             '_precio': 6000000, '_tipo': 'computadoras'},
         2: {'_descripcion': 'HP',
             '_precio': 6000000, '_tipo': 'computadoras'},
         3: {'_descripcion': 'samsung s20',
             '_precio': 400000, '_tipo': 'celular'},
         4: {'_descripcion': 'samsung s10',
             '_precio': 200000, '_tipo': 'celular'}}),
    ])
    def test_insertion_sort_precio(self, tipo_orden, list_ordenada):
        lista_ordenada = ProductoService().\
         insertion_sort_precio(Repositorios.productosList, tipo_orden)
        self.assertDictEqual(lista_ordenada, list_ordenada)
    
    @parameterized.expand([
        (200000, {'_descripcion':
         'samsung s10', '_precio': 200000, '_tipo': 'celular'}),
        (400000, {'_descripcion':
         'samsung s20', '_precio': 400000, '_tipo': 'celular'}),
    ])
    # Busqueda binaria
    def test_busqueda_binaria(self, precio_buscado, producto):
        busqueda = (ProductoService().
                    busqueda_binaria(Repositorios.productosList, precio_buscado))
        self.assertDictEqual(busqueda, producto)


if __name__ == '__main__':
    unittest.main()
