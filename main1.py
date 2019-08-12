from producto import *
from carrito import *
from usuario import *
import os


global lstProductos
lstProductos = list()

def AgregarCarrito():
    pass

def Listarusuarios():
    pass

def CrearProducto():
    print("Registro de producto")
    cod = input("Codigo: ")
    nom = input("Nombre: ")
    pre = input("Precio: ")
    stock = input("Stock: ")
    pro = Productos(cod,nom,pre,stock)
    print(pro)
    lstProductos.append(pro)

def ListarProductos():
    for p in lstProductos:
        print(p.codigo," - ",p.nombre," - ",p.precio," - ",p.stock)


def LlenarCarrito():
    rpta = ""
    cantidad=0
    incial=False
    carro = Carrito()
    while rpta != 'N':
        print("Catalogo de productos")
        for p in lstProductos:
            print(p.codigo," - ",p.nombre," - ",p.precio," - ",p.stock)
        product = input("Elija un producto: ")
        for i in lstProductos:
            if i.codigo == product:
                print(i)        
                cantidad = int(input("Ingrese la cantidad: "))
                i.verificarStock(cantidad)
                print(i) 
                carro.AgregarCarrito(product)
                print("En mi canasta hay: ",carro)
                incial=True
                break
        if incial==False:
            print("No hay ese producto...")
        rpta = input("Desea algo mas? ")
        os.system('cls')


def menu():
    op = 0
    salir = 5
    while op !=salir:
        print("Menu")
        print("1.-Agregar Usuarios")
        print("2.-Listar Usuarios")
        print("3.-Agregar productos")
        print("4.-Listar productos")
        op =input("Digite la Opcion:")

        if op =="1":
            LlenarCarrito()
        elif op =="2":
            Listarusuarios()
        elif op =="3":
            CrearProducto()
        elif op =="4":
            ListarProductos()
        else:
            exit()    
            
menu()            

