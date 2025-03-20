# Ejemplo de aplicación principal en Flask
from flask import Flask, render_template, request
from modules.modulo1 import lista_peliculas, frase_y_pelicula
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
        frase_random = selector_random(frase_y_pelicula)
        opciones = creador_opciones(frase_y_pelicula, frase_random)
        print("w"*100)
        print(opciones)
        if request.method == "get":
            respuesta = request.form.get('respuesta')
            if checkear_resultado(respuesta, frase_y_pelicula):  
                    score += 1
    return render_template('juego.html',frase_random=frase_random, opciones=opciones, num_frases=num_frases, score=score) 

@app.route('/resultados') #pagina de resultados
def resultados():
    return render_template('resultados.html')

@app.route('/intentos') #pagina de intentos
def intentos():
    return render_template('intentos.html') 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)