
print("departamento de confeccion")
print("1. Ingresar producto")
print("2. Mostrar invetario en fabrica")
print("0. Salir")
opcion=int(input("digita una opcion: "))
opcion=100

listaProductos=[]
while opcion!=0:

    opcion=int(input("digita una opcion: "))
    if opcion==1:
        print("vamos a ingresar un nuevo producto: ")
        producto=input("Digita el producto que ingresa a fabricacion: ")
        #agragar un producto a la lista de productos
        listaProductos.append(producto)
    elif opcion==2:
        print("vamos mostrando el inventario : ")  
        print(listaProductos)
    elif opcion==0:
        print("gracias, hasta pronto") 
    else:
        print("opcion invalida..") 
print ("adios, fin del programa")
