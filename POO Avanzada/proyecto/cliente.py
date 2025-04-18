class Cliente:
    
    """Clase de tipo cliente Base
    """    
    
    def __init__(self,id,nombre,email,direccion):
        """Constructor de la clase cliente

        :param id: numero de identificación del cliente.
        :type id: str
        :param nombre: nombre del cliente
        :type nombre: str
        :param email: email del cliente
        :type email: str
        :param direccion: dirección del cliente
        :type direccion: str
        """        
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion
        
    def get_id_cliente(self):
        
        """Devuelve el self.__id

        :return: devuelve self.__id
        :rtype: str
        """    
        return self.__id
        
    
    def set_id_cliente(self,id_nuevo):
        """Cambiar el valor del id por el id_nuevo

        :param id_nuevo: valor nuevo del atributo self.__id
        :type id_nuevo: str
        """        
        self.__id = id_nuevo
        
        
               
    def get_nombre_cliente(self):
        """Devuelve el nombre del cliente al ser un atributo privado.

        :return: nombre del cliente
        :rtype: str
        """        
        
        return self.__nombre
    
    def set_nombre_cliente(self,nombre_nuevo):
        """Cambia el nombre de cliente

        :param nombre_nuevo: Valor que va a tomar self.__nombre
        :type nombre_nuevo: str
        """        
        self.__nombre = nombre_nuevo
           
    def get_email(self):
        """Devuelve el valor de email

        :return: valor de self.__email
        :rtype: str
        """        
        
        return self.__email
    
    def set_email(self,email_nuevo):
        """Cambia el valor de self.__email

        :param email_nuevo: Valor del email nuevo
        :type email_nuevo: str
        """        
        self.__email = email_nuevo
        
    def get_direccion(self):
        """Devuelve el valor de direccion
        :return: Devuelve el valor de la dirección.
        :rtype: str
        """        
          
        return self.__direccion
    
    def set_direccion(self,direccion_nueva):
        """Cambia el valor de self.__direccion

        :param direccion_nueva:valor del atributyo self.__direccion
        :type direccion_nueva: str
        """        
        self.__direccion = direccion_nueva
       
              

    def __str__(self):
      
        """Devuelve los valores del objeto cliente formateado.

        :return: Devuelve los valores del objeto producto formateados.
        :rtype: str
        """               

        return(f'ID: {self.__id}\nNombre: {self.__nombre}\nE-mail: {self.__email}\nDirección: {self.__direccion}')
    
    
        