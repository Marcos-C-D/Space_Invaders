### Common module ###

import pygame, sys, math
from random import randrange

TECLA_ARRIBA = [pygame.K_w, pygame.K_UP]
TECLA_ABAJO = [pygame.K_s, pygame.K_DOWN]
TECLA_DERECHA = [pygame.K_d, pygame.K_RIGHT]
TECLA_IZQUIERDA = [pygame.K_a, pygame.K_LEFT]
TECLA_ACCION1 = [pygame.K_SPACE]

TECLAS_MOVIMIENTO = TECLA_ARRIBA + TECLA_ABAJO + TECLA_DERECHA + TECLA_IZQUIERDA

TECLA_ARRIBA = [pygame.K_w, pygame.K_UP]
TECLA_ABAJO = [pygame.K_s, pygame.K_DOWN]
TECLA_DERECHA = [pygame.K_d, pygame.K_RIGHT]
TECLA_IZQUIERDA = [pygame.K_a, pygame.K_LEFT]

TECLAS_MOVIMIENTO = TECLA_ARRIBA + TECLA_ABAJO + TECLA_DERECHA + TECLA_IZQUIERDA

NEGRO = (0, 0, 0)
GRIS = (127, 127, 127)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0)
CIAN= (0, 255, 255)
MAGENTA = (255, 0, 255)
COLOR_CLASICA = (105, 58, 14)
BRONCE = (255, 127, 59)
PLATA = (192, 192, 192)
ORO = (255, 255, 0)

def CerrarJuego(): # Cerrar el juego
    pygame.quit()
    sys.exit()

def EsperarCualquierTecla(): # Esperar a que se pulse cualquier tecla
    espera = True
    while espera:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                espera = False

def InicializarPygame(anchoPantalla, altoPantalla, tamanyoFuente): # Iniciar el juego
    pygame.init()
    ventana = pygame.display.set_mode((anchoPantalla, altoPantalla))
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont(None, tamanyoFuente)
    return ventana, reloj, fuente

def LimpiarPantalla(ventana, color = BLANCO): # Limpiar la pantalla
    ventana.fill(color)
    pygame.display.flip()

def ImprimirTexto(texto, coordenadas, ventana, fuente, color = ROJO): # Imprimir un cierto texto
    TextoPintar =  fuente.render(texto, True, color)
    ventana.blit(TextoPintar, coordenadas)

def CargarImaenes(ImagenesDireccion): # Cargar varias imagenes
    imagenes = []
    for direccion in ImagenesDireccion:
        imagenes.append(pygame.image.load(direccion))
    return imagenes

def RedimensionarImagenes(imagenes, tamanyoX, tamanyoY = None): # Redimensionar imagenes
    if not tamanyoY:
        tamanyoY = tamanyoX

    for indice in range(len(imagenes)):
        imagenes[indice] = pygame.transform.scale(imagenes[indice], (tamanyoX, tamanyoY))
    return imagenes

def GenerarPosicionAleatoria(minX, maxX, minY, maxY): # Generar posicion aleatoria
    x = randrange(minX, maxX)
    y = randrange(minY, maxY)
    return x, y

def Distancia(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def NormalizarVector(vector):
    modulo = math.sqrt(vector[0]**2 + vector[1]**2)
    return (vector[0] / modulo, vector[1] / modulo)


