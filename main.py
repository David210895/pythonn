from usuario import *
from producto import *
from carrito import *
import os

global lstusuarios,usuario,nombre,clave,tu 
global lstproductos, cod, nom, pre, stock

#USUARIO
lstusuarios =list()
usuario=""
nombre=""
clave=""
tu=""
#PRODUCTO
lstproductos=list()
cod=""
nom=""
pre=""
stock=""


def CrearUsuario():
    print("Registrando el Usuario")
    usuario=input("El Usuario:")
    nombre=input("El Nombre:")
    clave=input("La Clave:")
    tu=input("Tipo de Usuario")
    usua = Usuario(usuario,nombre,clave,tu)
    lstusuarios.append(usua)

def CrearProducto():
    print("Registro de producto")
    cod = input("Codigo: ")
    nom = input("Nombre: ")
    pre = input("Precio: ")
    stock = input("Stock: ")
    pro = Productos(cod,nom,pre,stock)
    print(pro)
    lstproductos.append(pro)

def ListarProductos():
    for p in lstproductos:
        print(p.codigo," - ",p.nombre," - ",p.precio," - ",p.stock)

def Listarusuarios():
    print("Listando Usuarios")
    for usu in lstusuarios:
        print(usu.nomcompleto,"-",usu.tipousuario)

def buscarProducto(self,codigo):
    for p in lstproductos:
        

def LlenarCarrito():
    rpta = ""
    car = Carrito()
    while rpta != 'N':
        print("Catalogo de productos")
        for prod in lstproductos:
            print(str(prod.codigo),"-",str(prod.nombre),"-",str(prod.precio),"-",str(prod.stock))
        produ = input("Ingrese el producto a añadir al carrito: ")
        car.AgregarCarrito(produ)
        print("En mi canasta hay: ",car)
        rpta = input("Desea agregar otro producto (S/N)? ")
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
            AgregarCarrito()
        elif op =="2":
            Listarusuarios()
        elif op =="3":
            CrearProducto()
        elif op =="4":
            ListarProductos()
        else:
            exit()    

menu()            













    


