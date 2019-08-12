
class Carrito:
    #Constructor
    def __init__(self):
        self.proCar = []
    def AgregarCarrito(self,productos):
        self.proCar.append(productos)
    def __str__(self):
        for producto in self.proCar:
            cadena = str(len(self.proCar))
            cadena += "\n" + str(producto)
        return cadena
    def canPro (self):
        cadena = str(len(self.proCar))
        return cadena
