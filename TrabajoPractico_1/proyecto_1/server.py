
from flask import Flask, render_template, request, session, redirect, url_for
from modules.modulo1 import lista_peliculas, frase_y_pelicula
from modules.modulo2 import selector_random, creador_opciones
from modules.config import app
from datetime import datetime

app.secret_key = 'clave'

# pagina de inicio
@app.route('/')
def index():
    return render_template('inicio.html')

@app.route('/lista_peliculas', methods=['GET']) #pagina con nombre de las peliculas
def obtener_lista_pelicula():
    return render_template('lista_peliculas.html', lista_peliculas=lista_peliculas) 

@app.route('/intentos', methods=['GET', 'POST'])  # pagina donde se ingresa nombre/intentos
def intentos():
    session['current_intento'] = 0
    session['score'] = 0  
    session['num_intentos'] = 0
    session['nombre_usuario'] = ''
    session['fecha_hora'] = datetime.now().strftime('%d/%m/%y %H:%M')

    #Creo las session si no existen, para que no se reseteen
    if 'historial_aciertos' and 'historial_desaciertos' not in session : 
        session['historial_aciertos'] = 0
        session['historial_desaciertos'] = 0
    
    if request.method == 'POST': 
        #solicito el num_intentos y los guardo en session si se envio el formulario        
        session['nombre_usuario'] = request.form.get('nombre') 
        session['num_intentos'] = request.form.get('num_intentos', type=int)
        
        return redirect(url_for('juego'))  # Redirige al juego cuando se envia la info

    return render_template('intentos.html')


@app.route('/juego', methods=['GET', 'POST'])  # pagina de juego
def juego():
    #Obtenemos los valores del juego
    num_intentos = session.get('num_intentos', 0)
    current_intento = session.get('current_intento', 0)
    score = session.get('score', 0)

    # Redirige a los resultados si se completaron los intentos
    if current_intento == num_intentos:
        return redirect(url_for('resultados'))
    
    #Para el primer intento
    if 'frase_random' not in session:
        session['frase_random'] = selector_random(frase_y_pelicula)
        session['opciones'] = creador_opciones(frase_y_pelicula, frase_random)[0]
        session['opcion_correcta'] = creador_opciones(frase_y_pelicula, frase_random)[1]
        session['mensaje'] = ''
    
                
    if request.method == 'POST':
        #recibimos los datos
        respuesta = request.form.get('respuesta')
        frase_random = session.get('frase_random')
        opciones = session.get('opciones')  
        opcion_correcta = session.get('opcion_correcta')

        #checkeamos la respuesta y guardamos el score
        if respuesta == opcion_correcta:
            score += 1
            session['historial_aciertos'] += 1          
            mensaje = "Correcto!"

        else: 
            session['historial_desaciertos'] += 1 
            mensaje = f"Incorrecto! La respuesta correcta era: {opcion_correcta}"
            
        session['mensaje'] = mensaje
        session['score'] = score
        session['current_intento'] = current_intento + 1

        #Creo frase random y opciones para el siguiente intento sin que se repitan
        frase_random = selector_random(frase_y_pelicula)
        while frase_random == session.get('frase_random'):
            frase_random = selector_random(frase_y_pelicula)
        opciones, opcion_correcta = creador_opciones(frase_y_pelicula, frase_random)
        
        #Guardo las nuevas variables en session para el siguiente intento
        session['opcion_correcta'] = opcion_correcta
        session['frase_random'] = frase_random
        session['opciones'] = opciones

        return redirect(url_for('juego'))  # Redirige al siguiente intento

    return render_template('juego.html', mensaje=session['mensaje'])

@app.route('/resultados', methods=['GET', 'POST']) #pagina de resultados
def resultados():
    nombre_usuario = session.get('nombre_usuario')
    fecha_hora = session.get('fecha_hora')
    historial_aciertos = session.get('historial_aciertos')
    historial_desaciertos = session.get('historial_desaciertos')
    score = session.get('score')
    num_intentos = session.get('num_intentos')
    porcentaje_aciertos = format((score / num_intentos) * 100, '.1f')
    
    if 'resultados_globales' not in session:
        session['resultados_globales'] = ['Nombre    Score/Intentos   Fecha y hora']        
    session['resultados_globales'].append(f'{nombre_usuario}   {score}/{num_intentos}   {fecha_hora}')
    
    
    return render_template('resultados.html', historial_aciertos=historial_aciertos, historial_desaciertos=historial_desaciertos, porcentaje_aciertos=porcentaje_aciertos, score=score, num_intentos=num_intentos)
    
@app.route('/graficas', methods=['GET']) #pagina de graficas
def graficas():
    # Obtener los datos de los resultados globales
    resultados_globales = session.get('resultados_globales', [])
    historial_aciertos = session.get('historial_aciertos')
    historial_desaciertos = session.get('historial_desaciertos')
    score = session.get('score')
    num_intentos = session.get('num_intentos') #PARA QUE USARIAS SCORE E INTENTOS EN GRAFICAS GLOBALES?

    return render_template('graficas.html',score=score, resultados_globales=resultados_globales, historial_aciertos=historial_aciertos, historial_desaciertos=historial_desaciertos, num_intentos=num_intentos)

@app.route('/resultados_globales', methods=['GET', 'POST'])
def resultados_globales():
    resultados_globales = session.get('resultados_globales', [])
    return render_template('resultados_globales.html', resultados_globales=resultados_globales )
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)