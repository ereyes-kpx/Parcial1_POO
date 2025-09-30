#Autor: samuel Esteban Reyes Uribe
class Registrar:
    def __init__(self,ID):
        self.ID = str(ID)
        
    def RegistrarLi(self):
        NombreLi=input("cual es el nombre de el libro: ")
        Estado=input("en que estado se encuentra el libro: ")
        return NombreLi, Estado, 
    def RegistrarUsuario(self):
        NombreUs=input("cual es el nombre de el usuario: ")
        Edad=int(input("cual es la edad del usuario: "))
        docID=input("cual es el documento del usuario: ")
        return NombreUs, Edad, docID



class Libros():
    def __init__(self, Id, NombreLi, EstadoLi):
        self.Id = Id
        self.Nombre = NombreLi
        self.Estado = EstadoLi

    def RegistrarLi(self,Id,Nombre):
        self.Nombre = input ("cual es el nombre de su libro")



class Usuarios:
    def __init__(self, Nombre, Edad, Id, Carrera):
        self.Nombre = Nombre
        self.Edad = Edad
        self.Id = Id
        self.Carrera = Carrera
    
    @property
    def Id(self):
        return self._Id
    @property
    def Nombre(self):
        return self._Nombre
    @property
    def Estado(self):
        return self._Edad
    @property
    def Categoria(self):
        return self._Categoria
    
  
libro1 = Registrar("01")

libro1.RegistrarLi()
Usuario1 = Registrar("02")

Usuario1.RegistrarUsuario()
