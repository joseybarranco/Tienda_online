from producto import Producto

class ProductoDigital(Producto):
    """Clase de Producto Digital que hereda de la clase producto.
    Todos los atributos son privados.

    :param Producto: objeto de la clase Producto
    :type Producto: Producto
    """
    def __init__(self, id, nombre, precio, stock,formato,tamaño):
        """Constructor de la clase ProductoDigital

        :param id: id del producto
        :type id: str
        :param nombre: nombre del producto
        :type nombre: str
        :param precio: Precio del producto
        :type precio: float
        :param stock: Stock del producto
        :type stock: int
        :param formato: formato del producto (mp3,avi,...)
        :type formato: str
        :param tamaño: tamaño digital del producto en Mb
        :type tamaño: str
        """        
        super().__init__(id, nombre, precio, stock)
        """Hereda los atributos y métodos de la clase Producto.
        """        
        self.__formato = formato
        self.__tamaño = tamaño

    #Getter y Setter

    def get_formato(self):
        """Devuelve el valor del formato del producto digital.

        :return: Devuelve el valor de self.__formato
        :rtype: str
        """        
        return self.__formato
    
    def set_formato(self,formato_nuevo):
        """Cambia el valor de self.__formato por el de formato_nuevo.

        :param formato_nuevo: Valor que va a tomar self.__formato
        :type formato_nuevo: str
        """        
        self.__formato = formato_nuevo

    def get_tamaño(self):
        """Devuelve el valor del tamaño del producto digital.

        :return: Devuelve el valor de self.__tamaño
        :rtype: str
        """        
        return self.__tamaño
    
    def set_tamaño(self,tamaño_nuevo):
        """Cambia el valor de self.__tamaño por el de tamaño_nuevo.

        :param formato_nuevo: Valor que va a tomar self.__tamaño
        :type formato_nuevo: str

        """        
        self.__tamaño = tamaño_nuevo

    #STR

    def __str__(self):
        """Devuelve los valores del objeto ProductoDigital formateados.

        :return: Devuelve los valores del objeto ProductoDigital
        :rtype: str
        """        
        return (f'ID: {self.get_id_producto()}\nNombre: {self.get_nombre_producto()}\nPrecio: {self.get_precio()}\nStock: {self.get_stock()}\nFormato: {self.__formato}\nTamaño: {self.__tamaño}')
    
    