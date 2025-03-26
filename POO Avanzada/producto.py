class Producto:

    #Constructor
    def __init__(self,id,nombre,precio,stock):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    #Getter y Setter
    def get_id_producto(self):
        return self.__id
    
    def set_id_producto(self,id_nuevo):
        self.__id = id_nuevo

    def get_nombre_producto(self):
        return self.__nombre
    
    def set_nombre_producto(self,nombre_nuevo):
        self.__nombre = nombre_nuevo

    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio_nuevo):
        self.__precio = precio_nuevo

    def get_stock(self):
        return self.__stock
    
    def set_stock(self,stock_nuevo):
        self.__stock = stock_nuevo

    #STR
    def __str__(self):
        return (f'ID: {self.__id}\nNombre: {self.__nombre}\nPrecio: {self.__precio}\nStock: {self.__stock}')
    
    def actualizar_stock(self,cantidad):
        self.set_stock(cantidad)