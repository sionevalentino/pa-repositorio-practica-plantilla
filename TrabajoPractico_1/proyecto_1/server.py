# Ejemplo de aplicación principal en Flask
from flask import Flask, render_template, request, session, redirect, url_for
from modules.modulo1 import lista_peliculas, frase_y_pelicula
from modules.modulo2 import selector_random, creador_opciones, checkear_resultado
from modules.config import app

app.secret_key = 'clave'

# Página de inicio
@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/lista_peliculas', methods=['GET']) #pagina con nombre de las peliculas
def obtener_lista_pelicula():
    return render_template('lista_peliculas.html', lista_peliculas=lista_peliculas) 

@app.route('/intentos', methods=['GET', 'POST'])  # Página de intentos
def intentos():
    session['current_intento'] = 1
    session['score'] = 0  # Inicializa el puntaje
    session['num_intentos'] = 0  # Inicializa el número de intentos
    print("Sesión inicializada:", session)
    if request.method == 'POST':
        num_intentos = request.form.get('num_intentos', type=int)  # Número de frases que va a jugar el usuario
        session['num_intentos'] = num_intentos  # Guarda el número de intentos en la sesión
        
        return redirect(url_for('juego'))  # Redirige al juego

    return render_template('intentos.html')  # Muestra el formulario para ingresar intentos


@app.route('/juego', methods=['GET', 'POST'])  # Página de juego
def juego():
    print ('num_intentos', session['num_intentos'])
    print ('current_intento', session['current_intento'])
    num_intentos = session.get('num_intentos', 0)
    current_intento = session.get('current_intento', 0)
    score = session.get('score', 0)

    if current_intento == num_intentos:
        return redirect(url_for('resultados'))  # Redirige a resultados si se completaron los intentos

    frase_random = selector_random(frase_y_pelicula)
    opciones = creador_opciones(frase_y_pelicula, frase_random)[0]
    opcion_correcta = creador_opciones(frase_y_pelicula, frase_random)[1]

    if request.method == 'POST':
        respuesta = request.form.get('respuesta')
        if checkear_resultado(respuesta, opcion_correcta):
            score += 1
        session['score'] = score
        session['current_intento'] = current_intento + 1
        return redirect(url_for('juego'))  # Redirige al siguiente intento

    return render_template('juego.html', frase_random=frase_random, opciones=opciones, intento_actual=current_intento + 1, num_intentos=num_intentos)

@app.route('/resultados', methods=['GET', 'POST']) #pagina de resultados
def resultados():
    score = session.get('score')
    num_intentos = session.get('num_intentos')
    porcentaje_aciertos = (score / num_intentos) * 100 if num_intentos > 0 else 0
    

    return render_template('resultados.html', num_intentos=num_intentos, score=score, porcentaje_aciertos=porcentaje_aciertos)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)