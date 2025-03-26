from cliente import Cliente
from producto import Producto

class Pedido:
    def __init__(self,id:str,cliente:Cliente,productos:list,fecha:str):
        self.__id = id
        self.__cliente = cliente
        self.__productos = productos
        self.__fecha = fecha
        
    def get_id_pedido(self):
        return self.__id
    
    def set_id_pedido(self,id_nuevo):
        self.__id = id_nuevo

    def get_cliente(self):
        return self.__cliente

    def set_cliente(self,cliente):
        self.__cliente = cliente


    def get_productos(self):
        return self.__productos
        
    def set_productos(self,producto:list):
        self.__producto = producto
        print('Producto añadido al pedido.')

    def get_fecha(self):
        return self.__fecha
    
    def set_fecha(self,fecha_nueva):
        self.__fecha = fecha_nueva

    def __str__(self):
        return (f'ID: {self.__id}\nCliente: {self.get_cliente()}\nProductos: {self.get_productos()}\nFecha: {self.__fecha}')

    def añadir_producto(self,producto:Producto):
        self.__productos.append(producto)

    def calcular_total(self):
        for producto in self.__productos:
            total += producto.get_precio() * producto.get_stock()
        return total
    



    
