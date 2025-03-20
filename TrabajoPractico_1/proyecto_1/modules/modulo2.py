#Funciones para la parte de juego de adivinar la frase

from random import sample, choice #funcion para elegir un elemento random de la lista
from modules.modulo1 import frase_y_pelicula
from flask import Flask, request


def selector_random (frase_y_pelicula): 
  
    frase_random = sample(frase_y_pelicula[0], k=1 ) #seleccionar una frase random de la lista de frases
    
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
    for tupla in frase_y_pelicula:
        if respuesta in tupla and frase_random in tupla:
            return True
        else :
            return False
