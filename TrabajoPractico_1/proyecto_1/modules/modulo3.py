# Inputs del usuario
from flask import Flask, request

num_frases = request.form.get('num_intentos', type=int) #numero de frases que va a jugar el usuario
respuesta = request.form.get ('respuesta',type = str) #respuesta del usuario