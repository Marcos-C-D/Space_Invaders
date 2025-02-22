import pygame
from common import *
from Funcionalidad import *

ANCHO_PANTALLA = 1000
ALTO_PANTALLA = 600
TAMANYO_FUENTE = 70
PIXEL = 4
TAMANYO_JUGADOR = (PIXEL * 11, PIXEL * 8)
TAMANYO_RAYO_JUGADOR = (PIXEL, PIXEL * 6)
TAMANYO_ALIEN1 = (PIXEL * 8, PIXEL * 8)
TAMANYO_ALIEN2 = (PIXEL * 10, PIXEL * 8)
TAMANYO_ALIEN3 = (PIXEL * 14, PIXEL * 7)
TAMANYO_ALIEN_BONUS = (PIXEL * 16, PIXEL * 7)
TAMANYO_RAYO_ALIEN = (PIXEL * 3, PIXEL * 6)
TAMANYO_MURALLA = (PIXEL * 16, PIXEL * 13)
TAMANYO_EXPLOSION = (PIXEL * 14, PIXEL * 7)

ventana, reloj, fuente = InicializarPygame(ANCHO_PANTALLA, ALTO_PANTALLA, TAMANYO_FUENTE)

direcciones = ["Robotica\\Space Invaders\\Sprites\\Alien1.1.png",
                "Robotica\\Space Invaders\\Sprites\\Alien1.2.png",

                "Robotica\\Space Invaders\\Sprites\\Alien2.1.png", 
                "Robotica\\Space Invaders\\Sprites\\Alien2.2.png",

                "Robotica\\Space Invaders\\Sprites\\Alien3.1.png", 
                "Robotica\\Space Invaders\\Sprites\\Alien3.2.png", 

                "Robotica\\Space Invaders\\Sprites\\AlienBonus.png",

                "Robotica\\Space Invaders\\Sprites\\Explosion.png",

                "Robotica\\Space Invaders\\Sprites\\Jugador.png",

                "Robotica\\Space Invaders\\Sprites\\MurallaRoja.png",
                "Robotica\\Space Invaders\\Sprites\\MurallaNaranja.png",
                "Robotica\\Space Invaders\\Sprites\\MurallaVerde.png",

                "Robotica\\Space Invaders\\Sprites\\RayoAlien.png",

                "Robotica\\Space Invaders\\Sprites\\RayoJugador.png",
    ]

imagenes = CargarImaenes(direcciones)

JUGADOR = RedimensionarImagenes([imagenes[8]], TAMANYO_JUGADOR[0], TAMANYO_JUGADOR[1])[0]
RAYO_JUGADOR = RedimensionarImagenes([imagenes[13]], TAMANYO_RAYO_JUGADOR[0], TAMANYO_RAYO_JUGADOR[1])[0]
ALIEN1 = RedimensionarImagenes(imagenes[0:2], TAMANYO_ALIEN1[0], TAMANYO_ALIEN1[1])

ventana.fill(NEGRO)

ventana.blit(imagenes[0], (ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))
pygame.display.flip()

# Jugador

posJugadorX = ANCHO_PANTALLA // 2 - TAMANYO_JUGADOR[0]
posJugadorY = 400 #ALTO_PANTALLA // 10 * 9

velJugadorX = 0
velJugadorY = 0

# Rayo Jugador

posJugadorRayoX = posJugadorX
posJugadorRayoY = (-TAMANYO_RAYO_JUGADOR[1]) - 10

velJugadorRayoY = 0

rayoJugadorImpactado = True

# Alien 1

posAlien1X = [ANCHO_PANTALLA // 2, ANCHO_PANTALLA // 2 + TAMANYO_ALIEN1[0] + PIXEL * 2]
posAlien1Y = [ALTO_PANTALLA // 6, ALTO_PANTALLA // 6 + TAMANYO_ALIEN1[1] + PIXEL * 2]

posAlien1 = [(posAlien1X[i], posAlien1Y[i]) for i in range(len(posAlien1X))]

velAlien1X = PIXEL

framesPorSprites = 60
contadorFramesSrites = 0
segundos = 0

vivo = True

velAliensY = PIXEL * 3

alienVivo = True

while vivo:

    tiempoDelta = reloj.tick_busy_loop(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CerrarJuego()
        if event.type == pygame.KEYDOWN:
            if event.key in TECLA_DERECHA and posJugadorX + TAMANYO_JUGADOR[0] + 10 < ANCHO_PANTALLA:
                velJugadorX += 5
            if event.key in TECLA_IZQUIERDA and posJugadorX - 10 > 0:
                velJugadorX += -5
            if event.key == pygame.K_SPACE and rayoJugadorImpactado:
                posJugadorRayoX = posJugadorX + TAMANYO_JUGADOR[0] // 2 - PIXEL // 2
                posJugadorRayoY = posJugadorY
                velJugadorRayoY = -5
                rayoJugadorImpactado = False

        if event.type == pygame.MOUSEBUTTONDOWN and rayoJugadorImpactado:
            posJugadorRayoX = posJugadorX + TAMANYO_JUGADOR[0] // 2 - PIXEL // 2
            posJugadorRayoY = posJugadorY
            velJugadorRayoY = -5
            rayoJugadorImpactado = False

        if event.type == pygame.KEYUP:
            if event.key in TECLA_DERECHA:
                velJugadorX -= 5
            if event.key in TECLA_IZQUIERDA:
                velJugadorX -= -5

    ventana.fill(NEGRO)

    if posJugadorX + TAMANYO_JUGADOR[0] + 10 >= ANCHO_PANTALLA and velJugadorX == 5:
        posJugadorX -= 5
    elif posJugadorX - 10 <= 0 and velJugadorX == -5:
        posJugadorX += 5
    else:
        posJugadorX += velJugadorX

    posJugadorRayoY += velJugadorRayoY

    if rayoJugadorImpactado:
        velJugadorRayoY = 0

    if posJugadorRayoY < TAMANYO_RAYO_JUGADOR[1] * -1 - 10 and not rayoJugadorImpactado:
        rayoJugadorImpactado = True

    # Eliminar Alien
    posAlien1 = EliminarAlien(posAlien1, (posJugadorRayoX, posJugadorRayoY), TAMANYO_ALIEN1, TAMANYO_RAYO_JUGADOR)
    posAlien1X = [i[0] for i in posAlien1]
    posAlien1Y = [i[1] for i in posAlien1]


    contadorFramesSrites += 1 
    if contadorFramesSrites >= framesPorSprites:
        contadorFramesSrites = 0
        segundos += 1
        for i in posAlien1X:
            i += velAlien1X
        if PIXEL * 2 in posAlien1X or ANCHO_PANTALLA - (TAMANYO_ALIEN1[0] + PIXEL * 2) in posAlien1X:
            velAlien1X *= -1
            for i in posAlien1Y:
                posAlien1Y += velAliensY

        print(segundos, velAlien1X)

    ventana.blit(RAYO_JUGADOR, (posJugadorRayoX, posJugadorRayoY))
    ventana.blit(JUGADOR, (posJugadorX, posJugadorY))
    if alienVivo:
        ventana.blit(ALIEN1[segundos % 2], (posAlien1X, posAlien1Y))
    
    pygame.display.flip()


EsperarCualquierTecla()
CerrarJuego()



