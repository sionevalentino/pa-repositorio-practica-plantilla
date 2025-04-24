from clases.estudiante import Estudiante
from clases.profesor import Profesor
from clases.departamento import Departamento
from clases.curso import Curso
from clases.facultad import Facultad

'''def cargar_listas():
    with open ('data/lista_cursos.txt', 'r') as archivo_cursos:
        ins_cursos = []
        for curso in archivo_cursos:
            nombre, titular = curso.split(',')
            nuevo_curso = Curso(nombre, titular)
            ins_cursos.append(nuevo_curso)

    with open ('data/lista_estudiantes.txt', 'r') as archivo_est, open ('data/lista_cursos.txt', 'r') as archivo_cursos:
        ins_estudiantes = []
        cursos_estudiante = []

        for estudiante in archivo_est:
            nombre, apellido, dni, *cursos = estudiante.split(',')
        
            for curso in cursos:
                    for obj_curso in ins_cursos:
                        if curso == obj_curso.nombre:
                            cursos_estudiante.append(obj_curso)

            obj_estudiante = Estudiante(nombre, apellido, dni, cursos_estudiante)
            ins_estudiantes.append(obj_estudiante)
    
    #Creo los deptos sin asignarle el director porque no existe todavia ese objeto
    with open('data/lista_deptos.txt', 'r') as archivo_deptos:
        ins_departamentos = []
        depto_dict = {} 

        for depto in archivo_deptos:
            nombre, director_nombre = depto.split(',')
            nuevo_depto = Departamento(nombre, None) 
            ins_departamentos.append(nuevo_depto)
            depto_dict[nombre] = nuevo_depto  

    with open('data/lista_profesores.txt', 'r') as archivo_profesores:
        ins_profesores = []
        profesor_dict = {} 
        for profe in archivo_profesores:
            nombre, apellido, dni, depto_nombre = profe.split(',')
            nuevo_profesor = Profesor(nombre, apellido, dni, depto_dict[depto_nombre])
            ins_profesores.append(nuevo_profesor)
            profesor_dict[f"{nombre} {apellido}"] = nuevo_profesor
    
    return ins_estudiantes, ins_profesores, ins_departamentos, ins_cursos'''

#Se me ocurre que en vez de devolver solo listas, devolver diccionarios y asi poder referenciar
#dentro del programa a los objetos por su nombre

#Tengo que agregar el profesor a la lista de profesores en depto
#y todavia asignarle el director a los departamentos

#todos los que son objetos se guarden como objetos y no como strings


#la otra manera de hacerlo, hay que revisar las clases para ver si se puede hacer

def cargar_listas():

    #Datos profesores 
    profesores_dict = {}
    #Datos cursos
    cursos_dict = {}
    #Datos estudiantes
    estudiantes_dict = {}
    #Datos departamentos
    depto_dict = {}

    
    with open(f'TrabajoPractico_2_parte1/proyecto_1/data/lista_cursos.txt', 'r', encoding = 'UTF-8') as archivo_cursos, \
         open(f'TrabajoPractico_2_parte1/proyecto_1/data/lista_estudiantes.txt', 'r', encoding = 'UTF-8') as archivo_est, \
         open(f'TrabajoPractico_2_parte1/proyecto_1/data/lista_deptos.txt', 'r', encoding = 'UTF-8') as archivo_deptos, \
         open(f'TrabajoPractico_2_parte1/proyecto_1/data/lista_profesores.txt', 'r', encoding = 'UTF-8') as archivo_profesores:
        
        #CURSOS
        for curso in archivo_cursos:
            datos = curso.strip().split(',')
            if len(datos) < 4:  # Asegúrate de que haya al menos 4 valores
                print(f"Línea inválida en archivo_cursos: {curso}")
                continue
            nombre, titular_nombre, titular_apellido, dni = datos[:4]
            titular = Profesor(titular_nombre, titular_apellido, dni, None)
            nuevo_curso = Curso(nombre, titular)
            cursos_dict[nombre] = nuevo_curso

        #ESTUDIANTES
        for estudiante in archivo_est:
            cursos_estudiante = {}

            # Verifico si el estudiante tiene cursos asignados o no
            if len(estudiante.strip().split(',')) == 3:
                tiene_cursos = False
                nombre, apellido, dni = estudiante.strip().split(',')
            else:
                tiene_cursos = True
                nombre, apellido, dni, *cursos = estudiante.strip().split(',')          
                for curso in cursos:
                    if curso in cursos_dict:
                        cursos_estudiante[f'{curso}'] = cursos_dict.get(f'{curso}')
            
            obj_estudiante = Estudiante(nombre, apellido, dni)
            
            if tiene_cursos:
                obj_estudiante.cargar_cursos(cursos_estudiante)  

            estudiantes_dict[f"{nombre} {apellido}"] = obj_estudiante


        #DEPARTAMENTOS
        for depto in archivo_deptos:
            cursos_depto_dict = {}
            if len(depto.strip().split(',')) == 3:
                nombre, director_nombre, director_apellido  = depto.strip().split(',')
                tiene_cursos = False
            else:
                nombre, director_nombre, director_apellido, *cursos = depto.strip().split(',')
                for curso in cursos:
                    if curso in cursos_dict:
                        tiene_cursos = True
                        cursos_depto = cursos_dict[curso]
                        cursos_depto_dict[curso] = cursos_depto

            director = profesores_dict.get(f"{director_nombre} {director_apellido}") 
            nuevo_depto = Departamento(nombre, director)

            if tiene_cursos:
                nuevo_depto.cargar_cursos(cursos_depto_dict) #cargar cursos al depto
            depto_dict[nombre] = nuevo_depto
            


        #PROFESORES
        for profe in archivo_profesores:
            nombre, apellido, dni, depto_nombre = profe.strip().split(',')
            departamento = depto_dict.get(depto_nombre)
            nuevo_profesor = Profesor(nombre, apellido, dni, departamento)
            profesores_dict[f"{nombre} {apellido}"] = nuevo_profesor

        archivo_cursos.seek(0) #Vuelvo al inicio del archivo para volver a leerlo
        archivo_deptos.seek(0) 
        archivo_profesores.seek(0) 
        archivo_est.seek(0) 

        ########  (Vuelvo a correr para que se complete el objeto profesor en otros objetos)  #########

        #CURSOS
                
        for curso in archivo_cursos:
            nombre, titular_nombre, titular_apellido = (curso.strip().split(','))[:3]
            titular = profesores_dict.get(f'{titular_nombre} {titular_apellido}')
            cursos_dict[nombre] = Curso(nombre, titular)
            profesores_dict[f'{titular_nombre} {titular_apellido}'] = titular 


        #ESTUDIANTES
        for estudiante in archivo_est:
            cursos_estudiante = {}

            # Verifico si el estudiante tiene cursos asignados o no
            if len(estudiante.strip().split(',')) == 3:
                tiene_cursos = False
                nombre, apellido, dni = estudiante.strip().split(',')
            else:
                tiene_cursos = True
                nombre, apellido, dni, *cursos = estudiante.strip().split(',')          
                for curso in cursos:
                    if curso in cursos_dict:
                        cursos_estudiante[f'{curso}'] = cursos_dict.get(f'{curso}')
            
            obj_estudiante = Estudiante(nombre, apellido, dni)
            
            if tiene_cursos:
                obj_estudiante.cargar_cursos(cursos_estudiante)  

            estudiantes_dict[f"{nombre} {apellido}"] = obj_estudiante


        #DEPARTAMENTOS
        for depto in archivo_deptos:
            cursos_depto_dict = {}
            if len(depto.strip().split(',')) == 3:
                nombre, director_nombre, director_apellido  = depto.strip().split(',')
                tiene_cursos = False
            else:
                nombre, director_nombre, director_apellido, *cursos = depto.strip().split(',')
                for curso in cursos:
                    if curso in cursos_dict.keys():
                        tiene_cursos = True
                        cursos_depto = cursos_dict[curso]
                        cursos_depto_dict[curso] = cursos_depto

            director = profesores_dict.get(f"{director_nombre} {director_apellido}") 
            nuevo_depto = Departamento(nombre, director)

            if tiene_cursos:
                nuevo_depto.cargar_cursos(cursos_depto_dict) #cargar cursos al depto
            depto_dict[nombre] = nuevo_depto
            

        
    return estudiantes_dict, profesores_dict, depto_dict, cursos_dict
