class Cliente:
    def __init__(self,id,nombre,email,direccion):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion

    def get_id_cliente(self):
        return self.__id
    
    def set_id_cliente(self,id_nuevo):
        self.__id = id_nuevo

    def get_nombre_cliente(self):
        return self.__nombre
    
    def set_nombre_cliente(self,nombre_nuevo):
        self.__nombre = nombre_nuevo

    def get_email(self):
        return self.__email
    
    def set_email(self,email_nuevo):
        self.__email = email_nuevo

    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self,direccion_nueva):
        self.__direccion = direccion_nueva

    def __str__(self):
        return(f'ID: {self.__id}\nNombre: {self.__nombre}\nE-mail: {self.__email}\nDirección: {self.__direccion}')
    
    
        