#ESTO ES UNA CLASE
class Vehiculo:
    def acelerar(self) -> None:
        self.velocidad += 10
    def frenar(self):
        self.velocidad -= 10
    def avanzar(self):
        self.latitud += (self.velocidad/10)+5
    def retroceder(self):
        self.latitud -= (self.velocidad/10)+5
    def __str__(self):
        return(f'El vehículo está en lat,lng ({self.latitud},{self.longitud} {self.velocidad})')
    def __init__(self,marca="", velocidad=0, latitud=0.0, longitud=0.0):
        self.velocidad = velocidad
        self.latitud = latitud
        self.longitud = longitud
        self.marca = marca
        print("El objeto ha sido creado")
#FINCLASE
#ESTO ES EL MAIN
objeto = Vehiculo()
#objeto.velocidad=123
print(objeto)
diccionario = {'nombre': "holamundo"}
print(diccionario)
#FIN MAIN