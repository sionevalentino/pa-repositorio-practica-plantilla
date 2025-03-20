#Funciones para la parte de juego de adivinar la frase

from random import choice #funcion para elegir un elemento random de la lista
from modules.modulo1 import frase_y_pelicula
from flask import Flask, request

'''def selector_random (lista):
    frases_usadas = set()
    frases_disponibles = [frase for frase in lista[1] if frase not in frases_usadas]
    if not frases_disponibles:  # Si ya se usaron todas las frases
        return ('no quedan mas frases para jugar')

    frase_random = choice(frases_disponibles)
    frases_usadas.add(frase_random)
    return frase_random
'''

def selector_random (frase_y_pelicula): 
    frases_usadas = set()
    frases = set()
    
    for elementos in list:
        frases.add(elementos[0])
    frase_random = choice(frases)
    
    while frase_random in frases_usadas:
        frase_random = choice(frases)
    frases_usadas.add(frase_random)
    return frase_random

def creador_opciones(frase_y_pelicula, frase_random):
    opciones = []
    for linea in frase_y_pelicula:
        if frase_random == linea[0]: 
            opcion_correcta=frase_y_pelicula[frase_y_pelicula.index(linea)][1]
            opciones.append(opcion_correcta)
            break
    
    return opciones

def checkear_resultado (respuesta, frase_y_pelicula): #funcion para chequear si la respuesta del usuario es correcta
    frase_random = selector_random(frase_y_pelicula )
    for tupla in list:
        if respuesta in tupla and frase_random in tupla:
            return True
        else :
            return False
