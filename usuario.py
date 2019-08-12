class Usuario:
    def __init__(self,u,nc,c,tu):
        self.usuario=u
        self.nomcompleto=nc
        self.clave=c
        self.tipousuario=tu
    def __str__(self):
        tmp ="Usuario: " +str(self.usuario)
        tmp += "\nNombre: "+str(self.nomcompleto)
        tmp += "\nClave: "+str(self.clave)
        tmp += "\nTipoUsario: "+str(self.tipousuario)
        return tmp