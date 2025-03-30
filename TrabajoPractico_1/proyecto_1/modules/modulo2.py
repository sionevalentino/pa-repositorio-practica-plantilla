#Funciones para la parte de juego de adivinar la frase

from random import sample, choice, shuffle 
from modules.modulo1 import frase_y_pelicula
from flask import Flask, request


def selector_random (frase_y_pelicula): #funcion para seleccionar una frase random de la lista de frases
    frase_random = sample(frase_y_pelicula[0], k = 1) #seleccionar una frase random de la lista de frases
    return frase_random[0]

def creador_opciones(frase_y_pelicula, frase_random): #funcion para crear las opciones de respuesta y chequeaarla
    opciones = []
    opcion_correcta = frase_y_pelicula[1][frase_y_pelicula[0].index(frase_random)] 
    opciones_random = (sample(frase_y_pelicula[1], k=2))   
    while opcion_correcta in opciones_random:
        opciones_random = (sample(frase_y_pelicula[1], k=2))
    opciones.extend(opciones_random)
     
    opciones.append(opcion_correcta)
    shuffle(opciones_random)

    return (opciones, opcion_correcta)

 #retorna las opciones de respuesta y la correcta
'''
def checkear_resultado (respuesta, frase_y_pelicula, frase_random): #funcion para chequear si la respuesta del usuario es correcta
    for pelicula in frase_y_pelicula[1]:
        pepe = pelicula
        if pelicula == respuesta and frase_random == frase_y_pelicula[0][frase_y_pelicula[1].index(pelicula)]:
            return True           
        else :
            return False'''
        
'''def checkear_resultado (respuesta, frase_y_pelicula, frase_random): #funcion para chequear si la respuesta del usuario es correcta
    index = frase_y_pelicula[0].index(frase_random)
    pelicula_correcta = frase_y_pelicula[1][index]
    if respuesta == pelicula_correcta:
        return True
    else:
        return False'''

'''def checkear_resultado (respuesta, opcion_correcta): #funcion para chequear si la respuesta del usuario es correcta
    if respuesta == opcion_correcta:
        return True
    else:
        return False'''