from producto import Producto
from cliente import Cliente
from productoDigital import ProductoDigital
from pedido import Pedido
from reseña import Reseña
#Variables y Constantes

lista_productos = []
diccionario_clientes = {}
lista_pedidos = []
lista_reseñas = []
#Funciones





#Programa Principal

producto1= Producto('P001','Disco Duro',100.0,10)

lista_productos.append(producto1)

producto1 = Producto('P002','Monitor',250.00,5)

lista_productos.append(producto1)

print(f'La cantidad de productos son {len(lista_productos)}')

for producto in lista_productos:
    print(producto)

cliente1 = Cliente('C001','Fran Fernandez','fran@gmail.com','Adra')

diccionario_clientes[cliente1.get_id_cliente()] = cliente1

cliente1 = Cliente('C002','David Pérez','david@gmail.com','Adra')

diccionario_clientes[cliente1.get_id_cliente()] = cliente1

print(f'La cantidad de clientes son {len(diccionario_clientes)}')
for cliente  in diccionario_clientes.values():
    print(cliente)


producto_digital1 = ProductoDigital('PD001','Canción',5.00,10,'MP4',3)

lista_productos.append(producto_digital1)

producto_digital1 = ProductoDigital('PD002','Videojuego',50.00,10,'ISO',40)

lista_productos.append(producto_digital1)

for producto in lista_productos:
    print(producto)

pedido1 = Pedido('PED001',diccionario_clientes['C001'],[],'16/03/25')
pedido1.añadir_producto(lista_productos[3])

print(pedido1)

reseña1 = Reseña('R001',lista_productos[0],diccionario_clientes['C001'],'Producto increible',None)
print(reseña1)

while True:
    print()
    print('Opción[1].Gestionar productos(añadir,listar,actualizar stock.)')
    print('Opción[2].Gestionar clientes(añadir,listar)')
    print('Opción[3].Gestionar pedidos(crear,listar,calcular total)')
    print('Opción[4].Gestionar reseñas(añadir,listar)')
    print('Opción[0]. Salir.')
    print()

    opcion = input('Escribe una de las opciones.')

    if opcion == '1':
        print()
        print('Subopción[1].Añadir Producto.')
        print('Subopción[2].Listar Productos.')
        print('Subopción[3].Actualizar el stock de un producto.')

        opcion_productos = input ('Escribe una de las opciones.')

        if opcion_productos == '1':
            tipo_producto = input('¿Qué tipo de producto quieres añadir?(Digital,Fisico)').title()
            if tipo_producto == 'Digital':
                ID_producto = input('Escribe el id del producto.')
                ID_exist = False
                for producto in lista_productos:
                    if ID_producto == producto.get_id_producto():
                        ID_exist = True
                        print('El producto ya está en la lista.')
                        break
                    
                
                if ID_exist == False:
                    nombre_producto = input('Escribe el nombre del producto.')
                    precio_producto = float(input('Escribe el precio del producto.'))
                    stock_producto = int(input('Escribe el stock del producto.'))
                    formato_producto = input('Escribe el formato del producto.')
                    tamaño_producto = float(input('Escribe el número de MB que tiene el producto.'))
                    productoDigital = ProductoDigital(ID_producto,nombre_producto,precio_producto,stock_producto,formato_producto,tamaño_producto)
                    lista_productos.append(productoDigital)
                    print('El producto digital ha sido añadido a la lista.')
            
            elif tipo_producto == 'Fisico':
                ID_producto = input('Escribe el id del producto.')
                ID_exist = False
                for producto in lista_productos:
                    if ID_producto == producto.get_id_producto():
                        ID_exist = True
                        print('El producto ya está en la lista.')
                        break

                if ID_exist == False:
                    nombre_producto = input('Escribe el nombre del producto.')
                    precio_producto = float(input('Escribe el precio del producto.'))
                    stock_producto = int(input('Escribe el stock del producto.'))
                    producto = Producto(ID_producto,nombre_producto,precio_producto,stock_producto)
                    lista_productos.append(producto)
                    print('El producto ha sido añadido a la lista.')

        elif opcion_productos == '2':
            for producto in lista_productos:
                print(producto)

        elif opcion_productos == '3':
            id_producto = input('Escribe el id del producto que quieres cambiar el stock.')
            for producto in lista_productos:
                if id_producto == producto.get_id_producto():

                    cantidad = int(input('Escribe la cantidad final de stock del producto.'))
                    producto.actualizar_stock(cantidad)
                    print('El stock ha sido actualizado.')

        else:
            print('Opción incorrecta.')

        

    elif opcion == '2':
        print()
        print('Subopción[1].Añadir clientes.')
        print('Subopción[2].Listar clientes.')
        print()

        opcion_clientes = input('Escribe una de las opciones.')

        if opcion_clientes == '1':
            id_cliente = input('Escribe el Id del cliente.')
            cliente_exist = False
            for cliente in diccionario_clientes.keys():
                if id_cliente == cliente:
                    cliente_exist = True
                    print('El cliente ya existe.')
                    break
            
            if cliente_exist == False:
                nombre_cliente = input('Escribe el nombre del cliente.')
                email_cliente = input('Escribe el E-mail del cliente.')
                direccion_cliente = input('Escribe la dirección del cliente.')
                cliente = Cliente(id_cliente,nombre_cliente,email_cliente,direccion_cliente)
                diccionario_clientes[cliente.get_id_cliente()] = cliente

        elif opcion_clientes == '2':
            for cliente  in diccionario_clientes.values():
                print(cliente)

        else:
            print('Opción incorrecta.')
            
    elif opcion == '3':
        print()
        print('Subopción[1].Crear Pedido.')
        print('Subopción[2].Listar Pedidos.')
        print('Subopción[3].Calcular total de los pedidos.')
        print()

        opcion_pedidos = input('Escribe una de las opciones.')

        if opcion_pedidos == '1':
            id_pedido = input('Escribe el id del pedido.')
            pedido_exist = False
            for pedido in lista_pedidos:
                if pedido.get_id_pedido() == id_pedido:
                    pedido_exist = True
                    print('El pedido ya existe.')

            if pedido_exist == False:
                lista_pedido_productos = []
                id_cliente = input ('Escribe el id del cliente que hace el pedido.')
                while True:
                    for producto in lista_productos:
                        print(producto)

                    producto_pedido = input('Escribe el id del producto que añades a la lista del pedido.(Salir para Continuar.)').title()
                    if producto_pedido == 'Salir':
                        break
                    else:
                        for producto in lista_productos:
                            
                            if producto_pedido == producto.get_id_producto():
                                lista_pedido_productos.append(producto)
                                print('Producto añadido correctamente.')

                            else:
                                print('El id del producto no está en la lista.')

                    
                fecha_pedido = input('Escribe la fecha de realización del pedido.')

                pedido = Pedido(id_pedido,diccionario_clientes[id_cliente],lista_pedido_productos,fecha_pedido)
                lista_pedidos.append(pedido)
                print('Pedido añadido correctamente.')

        elif opcion_pedidos == '2':
            for pedido in lista_pedidos:
                print(pedido)

        elif opcion_pedidos == '3':
            for pedido in lista_pedidos:    
                print(pedido)

            id_calcular = input('Escribe el id del pedido que quieres calcular el total.')
            for pedido in lista_pedidos:
                if id_calcular == pedido.get_id_pedido():
                    print(f'El total del pedido es {pedido.calcular_total()}€.')

        else:
            print('Opción incorrecta.')

    elif opcion == '4':
        print()
        print('Subopción[1].Añadir reseña.')
        print('Subopción[2].Listar reseñas.')
        print()

        opcion_reseñas = input('Escribe una de las opciones.')

        if opcion_reseñas == '1':
            id_reseña = input('Escribe el id de la reseña.')
            reseña_exist = False
            for reseña in lista_reseñas:
                if id_reseña == reseña.get_id():
                    print('La reseña ya existe.')
                    reseña_exist = True
            
            if reseña_exist == False:
                id_pedido_reseña = input('Escribe el id del pedido del producto que vas a hacer una reseña.')
                for pedido in lista_pedidos:
                    if pedido.get_id_pedido() == id_pedido_reseña:
                        print(pedido.get_producto())
                        id_producto_reseña = input('Escribe el id del producto que vas a hacer una reseña.')
                        for producto in pedido.get_productos():
                            if producto.get_id_producto() == id_producto_reseña:
                                comentario_reseña = input('Escribe el comentario de la reseña.')
                                puntuacion_reseña = float(input('Escribe la puntuación de la reseña.(Número flotante de entre 1 a 5)'))
                                reseña = Reseña(id_reseña,producto,pedido.get_cliente(),comentario_reseña,puntuacion_reseña)
                                lista_reseñas.append(reseña)
                                print('La reseña ha sido añadida correctamente.')

        elif opcion_reseñas == '2':
            for reseña in lista_reseñas:
                print(reseña)

        else:
            print('Opción incorrecta.')

    elif opcion == '0':
        print('Fin del programa.')
        break

    else:
        print('Opción incorrecta.')