import pygame
WIDTH = 800
HEIGHT = 600
ROJO = (255,0,0)
AZUL = (0,0,255)
VERDE = (0,255,0)
EJECUTANDO = True
class Player:
    def __init__(self, ejex = WIDTH/2, ejey = HEIGHT/2, radius=5, thickness=1) -> None:
        self.ejex=ejex
        self.ejey=ejey
        self.center = [self.ejex,self.ejey]
        self.radius = radius
        self.thickness = thickness
    def calculaCentro(self):
        self.center = [self.ejex,self.ejey]
class Escenario: 
    ejex = 0
    ejey = 0
    center = (ejex,ejey)
pygame.init()
ventana = pygame.display.set_mode((WIDTH,HEIGHT))
jugador=Player()
escenario = Escenario()
fondo = pygame.image.load('./fondo.png').convert()
image_rect = fondo.get_rect()

while(EJECUTANDO):
    for event in pygame.event.get():
        #Presiono ESC y quita el juego
        if(event.type== pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            EJECUTANDO=False 
    jugador.ejex, jugador.ejey = pygame.mouse.get_pos()
    ventana.blit(fondo,escenario.center)
    pygame.draw.circle(ventana,ROJO,jugador.center,jugador.radius,jugador.thickness)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
