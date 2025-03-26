from cliente import Cliente
from producto import Producto

class Reseña(Producto,Cliente):

    #Constructor
    def __init__(self, id, producto:Producto, cliente:Cliente,comentario,puntuacion):
        
        Producto.__init__(self,producto.get_id_producto(),producto.get_nombre_producto(),producto.get_precio(),producto.get_stock())
        Cliente.__init__(self,cliente.get_id_cliente(),cliente.get_nombre_cliente(),cliente.get_email(),cliente.get_direccion())
        self.__id = id
        self.__comentario = comentario
        self.__puntuacion = None


    #Getter y Setter
    def get_id(self):
        return self.__id
    
    def get_comentario(self):
        return self.__comentario
    
    def get_puntuacion(self):
        return self.__puntuacion
    
    def set_id(self,id_nuevo):
        self.__id = id_nuevo

    def set_comentario(self,comentario_nuevo):
        self.__comentario = comentario_nuevo

    def set_puntuacion(self,puntuacion_nueva):
        if 1<= puntuacion_nueva <= 5:
            self.__puntuacion = puntuacion_nueva
            print('Puntuación añadida correctamente.')
        else:
            print('La puntuación debe ser entre 1 y 5.')

    #STR

    def __str__(self):
        return(f'ID Reseña {self.__id} del Producto con ID {self.get_id_producto()} hecho por el cliente {self.get_id_cliente()} tiene de comentario {self.__comentario} y una puntuación de {self.__puntuacion}.')
    
