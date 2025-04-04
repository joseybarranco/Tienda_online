from cliente import Cliente
from producto import Producto

class Pedido:
    """Clase de tipo Pedido Base.
    """    
    def __init__(self,id:str,cliente:Cliente,productos:list,fecha:str):
        """Constructor de la clase Pedido

        :param id: Valor del id de pedido
        :type id: str
        :param cliente: Valores del objeto Cliente
        :type cliente: Cliente
        :param productos: lista de Objetos Producto
        :type productos: list
        :param fecha: Fecha del pedido
        :type fecha: str
        """        
        self.__id = id
        self.__cliente = cliente
        self.__productos = productos
        self.__fecha = fecha
        
    def get_id_pedido(self):
        """Devuelve el id del pedido.

        :return: Devuelve self.__id
        :rtype: str
        """        
        return self.__id
    
    def set_id_pedido(self,id_nuevo):
        """Cambia el valor del id del producto por id_nuevo

        :param id_nuevo: Valor que toma self.__id
        :type id_nuevo: str
        """        
        self.__id = id_nuevo

    def get_cliente(self):
        """Devuelve los valores de objeto cliente que hace el pedido.

        :return: Devuelve el objeto Cliente.
        :rtype: Cliente
        """        
        return self.__cliente

    def set_cliente(self,cliente):
        """Cambiar el Cliente que ha hecho el pedido

        :param cliente: Valores del objeto Cliente
        :type cliente: Cliente
        """        
        self.__cliente = cliente


    def get_productos(self):
        """Devuelve la lista que contiene los productos del pedido.

        :return: Devuelve la lista de objetos Producto.(self.__preoductos)
        :rtype: List
        """        
        return self.__productos
        
    def set_productos(self,producto:list):
        """Cambia o añade un producto a la lista de productos

        :param producto: Valores del objeto producto que vas a añadir a la lista.
        :type producto: list
        """        
        self.__productos.append(producto)  
        print('Producto añadido al pedido.')

    def get_fecha(self):
        """Devuelve la fecha que se hace el pedido

        :return: Devuelve self.__fecha
        :rtype: str
        """        
        return self.__fecha
    
    def set_fecha(self,fecha_nueva):
        """Cambia la fecha del pedido.

        :param fecha_nueva: Cambia el valor de self.__fecha por el de fecha_nueva.
        :type fecha_nueva: str
        """        
        self.__fecha = fecha_nueva

    def __str__(self):
        """Devuelve los valores del objeto Pedido formateado.

        :return: Devuelve los valores del objeto Pedido formateado
        :rtype: str
        """        
        return (f'ID: {self.__id}\nCliente: {self.get_cliente()}\nProductos: {self.get_productos()}\nFecha: {self.__fecha}')

    def añadir_producto(self,producto:Producto):
        """Añade un objeto producto en la lista self.__productos
        :param producto: Valor del objeto Producto que vas a añadir a la lista.
        :type producto: Producto
        """        
        self.__productos.append(producto)

    def calcular_total(self):
        """Calcula el total del importe de los productos que hay en el pedido.

        :return:Cantidad del precio total de la suma de todos los productos del pedido.
        :rtype: float
        """        
        for producto in self.__productos:
            total += producto.get_precio() * producto.get_stock()
        return total
    



    
