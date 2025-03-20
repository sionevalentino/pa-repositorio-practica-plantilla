# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
#modulo para ordenar la informacion delarchivo de peliculas
with open ("TrabajoPractico_1/proyecto_1/data/frases_de_peliculas.txt", "r", encoding='UTF-8') as archivo:
    lista_peliculas = set()
    lista = [] 
    for renglon in archivo:
        frase_y_pelicula = renglon.strip('\n').split(';') #separar frase y pelicula 
        
        lista.append(frase_y_pelicula) #lista que asocia pelicula con frase
       
        lista_peliculas.add(frase_y_pelicula[1]) #peliculas unicas/sinrepe
    lista_peliculas = sorted(lista_peliculas) #orden alfabetico
        