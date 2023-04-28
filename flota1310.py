import pygame
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
        return(f'El vehículo {self.marca} está en lat,lng ({self.latitud},{self.longitud}) a {self.velocidad} km/h')
    def __init__(self,marca="", velocidad=0, latitud=0.0, longitud=0.0):
        self.velocidad = velocidad
        self.latitud = latitud
        self.longitud = longitud
        self.marca = marca
        print("El objeto ha sido creado")
#FINCLASE
#ESTO ES EL MAIN
#objeto.velocidad=123
lista = []
while(True):
    objeto = Vehiculo()
    objeto.velocidad = input("Ingrese velocidad")
    objeto.marca = input("Ingrese marca")
    print(objeto)
    lista.append(objeto)
    print(lista)
#FIN MAIN