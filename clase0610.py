class Persona:
    nombre = ""
    edad = 0
    def __init__(self, nombre="", edad=0):
        self.nombre=nombre
        self.edad = edad
        pass
    def cualestuNombre(self):
        print(self.nombre)
    def setNombre(self, nombre):
        self.nombre = nombre

a = Persona()
#a.nombre="FErnanda"
a.setNombre("Fernanda")
b=Persona()
b.nombre="Javier"
a.cualestuNombre()
b.cualestuNombre()
c = Persona("Natalia",20)
c.cualestuNombre()
