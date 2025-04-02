from cliente import Cliente
from producto import Producto

class Reseña(Producto,Cliente):
    """Clase de tipo Reseña que hereda de las clases Producto y Cliente.
    :param Producto: objeto de la clase Producto
    :type Producto: Producto
    :param Cliente: objeto de la clase Cliente
    :type Cliente: Cliente
    """

    #Constructor
    def __init__(self, id, producto:Producto, cliente:Cliente,comentario,puntuacion):
        """_summary_

        :param id: Valor del id del objeto Reseña.
        :type id: str
        :param producto: Valor del objeto Producto del que trata la reseña.
        :type producto: Producto
        :param cliente: Valor del objeto Cliente que va a hacer la reseña.
        :type cliente: Cliente
        :param comentario: Valor del comentario de la reseña
        :type comentario: str
        :param puntuacion: Valor de la puntuación de la reseña 1-5.
        :type puntuacion: float
        """        
        
        Producto.__init__(self,producto.get_id_producto(),producto.get_nombre_producto(),producto.get_precio(),producto.get_stock())
        """Hereda los atributos y métodos de la clase Producto.
        """        
        Cliente.__init__(self,cliente.get_id_cliente(),cliente.get_nombre_cliente(),cliente.get_email(),cliente.get_direccion())
        """Hereda los atributos y métodos de la clase Cliente.
        """        
        self.__id = id
        self.__comentario = comentario
        self.__puntuacion = None


    #Getter y Setter
    def get_id(self):
        """Devuelve el id de la Reseña.

        :return: Devuelve el valor de self.__id
        :rtype: str
        """        
        return self.__id
    
    def get_comentario(self):
        """Devuelve el comentario de la reseña

        :return: Devuelve el valor de self.__comentario
        :rtype: str
        """        
        return self.__comentario
    
    def get_puntuacion(self):
        """Devuelve la puntuación de la reseña.

        :return: Devuelve el valor de self.__puntuacion
        :rtype: float
        """        
        return self.__puntuacion
    
    def set_id(self,id_nuevo):
        """Cambia el valor del id de la reseña por id_nuevo.

        :param id_nuevo: Valor que va a tomar self.__id
        :type id_nuevo: str
        """        
        self.__id = id_nuevo

    def set_comentario(self,comentario_nuevo):
        """Cambia el valor del comentario de la reseña.

        :param comentario_nuevo: Valor que va a tomar self.__comentario
        :type comentario_nuevo: str
        """        
        self.__comentario = comentario_nuevo

    def set_puntuacion(self,puntuacion_nueva):
        """Cambia el valor de la puntuación de la reseña.
            Comprueba que está entre 1 y 5.

        :param puntuacion_nueva: Valor que toma self.__puntuación
        :type puntuacion_nueva: float
        """        
        if 1<= puntuacion_nueva <= 5:
            self.__puntuacion = puntuacion_nueva
            print('Puntuación añadida correctamente.')
        else:
            print('La puntuación debe ser entre 1 y 5.')

    #STR

    def __str__(self):
        """Devuelve los atributos del objeto Reseña formateado
           
        :return: Devuelve los valores del objeto Reseña formateado
        :rtype: str
        """    
        return(f'ID Reseña {self.__id} del Producto con ID {self.get_id_producto()} hecho por el cliente {self.get_id_cliente()} tiene de comentario {self.__comentario} y una puntuación de {self.__puntuacion}.')
        