class Producto:
    """Clase de tipo producto Base.
    Los atributos de la clase son privados.

    """
    #Constructor
    def __init__(self,id,nombre,precio,stock):
        """Constructor de la clase producto.

        :param id: id del producto
        :type id: str
        :param nombre: nombre del producto
        :type nombre: str
        :param precio: precio del producto
        :type precio: float
        :param stock: stock del producto
        :type stock: int
        """
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    #Getter y Setter
    def get_id_producto(self):
        """Devuelve el id del producto

        :return: Devuelve el valor de self.__id
        :rtype: str
        """
        return self.__id
    
    def set_id_producto(self,id_nuevo):
        """Cambia el valor del id por el de id_nuevo

        :param id_nuevo: valor del id nuevo
        :type id_nuevo: str
        """        
        self.__id = id_nuevo

    def get_nombre_producto(self):
        """Devuelve el nombre del producto

        :return: Devuelve el valor de self.__nombre
        :rtype: str
        """
        return self.__nombre
    
    def set_nombre_producto(self,nombre_nuevo):
        """Cambia el valor de self.__nombre por el de nombre_nuevo.

        :param nombre_nuevo: valor que va a tomar self.__nombre.
        :type nombre_nuevo: str
        """
        self.__nombre = nombre_nuevo

    def get_precio(self):
        """Devuelve el valor de self.__precio

        :return: Devuelve el valor de self.__precio
        :rtype: float
        """        
        return self.__precio
    
    def set_precio(self,precio_nuevo):
        """Cambia el valor de self.___precio por el de precio_nuevo.

        :param precio_nuevo: valor que va a tomar self.__precio
        :type precio_nuevo: float
        """        
        self.__precio = precio_nuevo

    def get_stock(self):
        """Devuelve el valor de self.__stock

        :return: Devuelve el valor de self.__stock
        :rtype: int
        """        
        return self.__stock
    
    def set_stock(self,stock_nuevo):
        """Cambia el valor de self.__stock por el de stock_nuevo.

        :param stock_nuevo: Valor que va a tomar self.__stock
        :type stock_nuevo: int
        """        
        self.__stock = stock_nuevo

    #STR
    def __str__(self):
        """Devuelve los valores del objeto producto formateado.

        :return: Devuelve los valores del objeto producto formateados.
        :rtype: str
        """        
        return (f'ID: {self.__id}\nNombre: {self.__nombre}\nPrecio: {self.__precio}\nStock: {self.__stock}')
    
    def actualizar_stock(self,cantidad):
        self.set_stock(cantidad)