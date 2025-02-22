import SpaceInvaders
from common import *

def Colision(obj1, obj2, tamanyoObj1, tamanyoObj2):
    if obj1[0] < obj2[0] + tamanyoObj2[0] and obj1[0] + tamanyoObj1[0] > obj2[0] and obj1[1] < obj2[1] + tamanyoObj2[1] and obj1[1] + tamanyoObj1[1] > obj2[1]:
        return True
    return False

def EliminarAlien(lst, posRayo, tamanyoAlien, tamanyoRayo, rayoJugadorImpactado):
    for i in lst:
        alienVivo = not Colision(i, posRayo, tamanyoAlien, tamanyoRayo)
        if not alienVivo:
            del i
            SpaceInvaders.rayoJugadorImpactado = True
            posRayo[1] = (-tamanyoRayo[1]) - 10
            break
    return lst

def EliminarCualquierAlien(posRayo, tamanyoAliens, tamanyoRayo ,*listas):
    for l in range(len(listas)):
        EliminarAlien(listas[l], posRayo, tamanyoAliens[l], tamanyoRayo)
    return [listas]
