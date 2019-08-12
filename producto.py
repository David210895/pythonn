
class Productos:
    #Constructor
    def __init__(self,cod,nom,pre,sto):
        self.codigo = cod
        self.nombre = nom
        self.precio = float(pre)
        self.stock = int(sto)
    #Sobreescribir el detalle
    def __str__(self):
        tmp = "\nCodigo producto: " + str(self.codigo)
        tmp += "\nProducto: " + str(self.nombre)
        tmp += "\nPrecio: " + str(self.precio)
        tmp += "\nStock: " + str(self.stock)
        return tmp
    #yo
    def verificarStock(self, cantidad):
        if cantidad < self.stock:
            self.stock -= cantidad
        else:
            print("Stock insuficiente...")
