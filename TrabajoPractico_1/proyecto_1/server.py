# Ejemplo de aplicación principal en Flask
from flask import Flask, render_template, request
from modules.modulo1 import lista_peliculas
from modules.modulo2 import selector_random, creador_opciones, checkear_resultado
from modules.config import app

# Página de inicio
@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/lista_peliculas', methods=['GET']) #pagina con nombre de las peliculas
def obtener_lista_pelicula():
    return render_template('lista_peliculas.html', lista_peliculas=lista_peliculas) 

@app.route('/juego', methods = ['GET', 'POST']) #pagina de juego
def juego():
    num_frases = request.form.get('num_intentos', type=int)
    score = 0
    while num_frases != 0:
        num_frases -= 1
        if request.methods == 'GET':
            frase_random = selector_random(lista_peliculas)
            opciones = creador_opciones(lista_peliculas, frase_random)
            respuesta = request.form.get('respuesta')
            if checkear_resultado(respuesta, lista_peliculas):  
                score += 1
    return render_template('juego.html') 

@app.route('/resultados') #pagina de resultados
def resultados():
    return render_template('resultados.html')

@app.route('/intentos') #pagina de intentos
def intentos():
    return render_template('intentos.html') 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)