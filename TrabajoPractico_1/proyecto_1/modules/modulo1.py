# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
#modulo para ordenar la informacion delarchivo de pelicul

with open ("TrabajoPractico_1/proyecto_1/data/frases_de_peliculas.txt", "r", encoding='UTF-8') as archivo:
    lista_peliculas = set()
    frase_y_pelicula = [[],[]] #lista de listas	
    for renglon in archivo:
        frase, peli= renglon.strip('\n').split(';') #separar frase y pelicula 
        frase_y_pelicula[0].append(frase)
        frase_y_pelicula[1].append(peli)
        lista_peliculas.add(peli) #peliculas unicas/sinrepe
    lista_peliculas = sorted(lista_peliculas) #orden alfabetico
