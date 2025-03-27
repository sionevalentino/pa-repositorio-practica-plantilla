# Ejemplo de aplicación principal en Flask
from flask import Flask, render_template, request, session
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

@app.route('/juego', methods = ['GET', 'POST']) #pagina de juego
def juego():
    num_intentos = request.form.get('num_intentos', type=int)
    score = 0
    frase_random = selector_random(frase_y_pelicula, num_intentos)
    opciones = []
    respuestas = []
    
    for i in range(num_intentos):
        
        opciones.append(creador_opciones(frase_y_pelicula, frase_random[i]))       
        respuesta = request.form.get(f'respuesta_{i}')
        print('w'*100)
        print(respuesta)
        respuestas.append(respuesta)
        resultado = checkear_resultado(respuesta, frase_y_pelicula, frase_random[i])
        print('w'*100)
        print(resultado)
        if  checkear_resultado(respuesta, frase_y_pelicula, frase_random[i]):  
            score += 1
    session['score'] = score
    session['num_intentos'] = num_intentos

           
    return render_template('juego.html', frase_random=frase_random, opciones=opciones, num_intentos=num_intentos, score=score), score 

@app.route('/resultados', methods=['GET', 'POST']) #pagina de resultados
def resultados():
    score = session.get('score')
    num_intentos = session.get('num_intentos')
    porcentaje_aciertos = (score / num_intentos) * 100 if num_intentos > 0 else 0

    return render_template('resultados.html', num_intentos=num_intentos, score=score, porcentaje_aciertos=porcentaje_aciertos)

@app.route('/intentos') #pagina de intentos
def intentos():
    return render_template('intentos.html') 

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)