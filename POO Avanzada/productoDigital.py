from producto import Producto

class ProductoDigital(Producto):
    def __init__(self, id, nombre, precio, stock,formato,tamaño):
        super().__init__(id, nombre, precio, stock)
        self.__formato = formato
        self.__tamaño = tamaño

    #Getter y Setter

    def get_formato(self):
        return self.__formato
    
    def set_formato(self,formato_nuevo):
        self.__formato = formato_nuevo

    def get_tamaño(self):
        return self.__tamaño
    
    def set_tamaño(self,tamaño_nuevo):
        self.__tamaño = tamaño_nuevo

    #STR

    def __str__(self):
        return (f'ID: {self.get_id_producto()}\nNombre: {self.get_nombre_producto()}\nPrecio: {self.get_precio()}\nStock: {self.get_stock()}\nFormato: {self.__formato}\nTamaño: {self.__tamaño}')
    
    