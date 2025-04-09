# módulo para organizar funciones o clases utilizadas en nuestro proyecto
# Crear tantos módulos como sea necesario para organizar el código
#modulo para ordenar la informacion delarchivo de pelicul
def crear_lista_peliculas(archivo):
    lista_peliculas = set()
    frase_y_pelicula = [[] , []] #lista de listas
    with open (archivo, "r", encoding='UTF-8') as archivo:
        	
        for renglon in archivo:
            frase, peli= renglon.strip('\n').split(';') #separar frase y pelicula 
            frase_y_pelicula[0].append(frase)
            frase_y_pelicula[1].append(peli)
            lista_peliculas.add(peli) #peliculas unicas/sinrepe
        lista_peliculas = sorted(lista_peliculas) #orden alfabetico
    return lista_peliculas, frase_y_pelicula 