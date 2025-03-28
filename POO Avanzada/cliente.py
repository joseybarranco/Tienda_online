class Cliente:
    """Clase de tipo cliente Base
    """    
    def __init__(self,id,nombre,email,direccion):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion
        """Constructor de la clase Cliente,
        Sus argumentos son nombre, id,email,direccion
          :param arg1: id del cliente
          :param arg2: nombre del cliente
          :param arg3: email del cliente
          :param arg4: dirección del cliente
          :type arg1: string
          :type arg2: string
          :type arg3: string
          :type arg4: string
          :return: none
          :rtype: none
        """    
    def get_id_cliente(self):
        """ Devuelve el valor del id del cliente al ser un atributo privado
        **parameters**, **types**, **return** and **return types**::
          :param arg1: none
          :type arg1: none
          :return: return valor de atributo id
          :rtype: the return type string
        """    
        return self.__id
        
    
    def set_id_cliente(self,id_nuevo):
        self.__id = id_nuevo
        """Cambia el valor de id del objeto cliente.
            :param arg1: Valor que va a tomar el nuevo id.
            :type arg1: string
        """        
               
    def get_nombre_cliente(self):
        """Devuelve el nombre del cliente al ser un atributo privado.

        Returns:
           string:nombre del cliente
        """        
        return self.__nombre
    
    def set_nombre_cliente(self,nombre_nuevo):
        self.__nombre = nombre_nuevo
        """:param arg1:Valor que va a tomar el nombre nuevo
            :type arg1:string
        """    
    def get_email(self):
        """Devuelve el valor del nombre de cliente al ser un atributo privado

        Returns:
            string: email del cliente
        """        
        return self.__email
    
    def set_email(self,email_nuevo):
        self.__email = email_nuevo
        """:param arg1: Valor del email nuevo
        """        
    def get_direccion(self):
        """_summary_

        Returns:
            string: devuelve el valor que tiene self.__direccion 
        """        
        return self.__direccion
    
    def set_direccion(self,direccion_nueva):
        self.__direccion = direccion_nueva

    def __str__(self):
        return(f'ID: {self.__id}\nNombre: {self.__nombre}\nE-mail: {self.__email}\nDirección: {self.__direccion}')
    
    
        