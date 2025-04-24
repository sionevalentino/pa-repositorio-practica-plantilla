
class Alumnado:
    """
    Esta clase maneja la creación de estudiantes y su inscripción en cursos.   
    """
    
    def __init__ (self):
        pass
    '''
    def lista_estActualizar(nuevo_estudiante):
        from clases.estudiante import Estudiante
        from clases.facultad import Facultad
        Facultad.agregar_estudiante(nuevo_estudiante)

        datos = nuevo_estudiante.get_datos(Estudiante)
        nuevo_estudiante = f"{datos[0]},{datos[1]},{datos[2]}\n"
        
        with open('data/lista_estudiantes.txt', 'a', encoding='UTF-8') as archivo:
            archivo.write(f'\n{nuevo_estudiante}\n') 
        return print (f'El estudiante {datos[0]} {datos[1]} ha sido agregado a la lista de estudiantes_dict.')'''
 
    #Esta funcion y la de arriba funcionan en conjunto.

    def estudiante_crear(facultad, nombre, apellido, dni):
        from clases.estudiante import Estudiante    
        nuevo_estudiante = Estudiante(nombre, apellido, dni)     
        return nuevo_estudiante
        
    #Anota al estudiante en el curso solicitado, verificando.
    def enviar_solicitud_anotar_a_curso(self, facultad, curso, dni):
        from clases.facultad import Facultad  
        from clases.curso import Curso 
        estudiantes_dict = facultad.obtener_estudiantes()
        for estudiante in estudiantes_dict.values():
            nombre, apellido, dni_estudiante, cursos = estudiante.get_datos()

            if int(dni) == int(dni_estudiante):
                existe = True
                if curso not in cursos:
                    #Modifico al estudiante en la lista y le agrego el curso al que se anota
                    with open('TrabajoPractico_2/proyecto_1/data/lista_estudiantes.txt', 'r', encoding='UTF-8') as leer_archivo_estudiantes:
                        lineas = leer_archivo_estudiantes.readlines()
                    with open('TrabajoPractico_2/proyecto_1/data/lista_estudiantes.txt', 'w', encoding='UTF-8') as archivo:
                        for linea in lineas:
                            if dni in linea: 
                                datos = linea.strip().split(',')
                                nueva_linea = ','.join(datos + [curso]) + '\n' 
                                archivo.write(nueva_linea) 
                            else:
                                archivo.write(linea) 
                    #Modifico el atributo del curso y agrego el estudiante al archivo 
                    
                    with open('TrabajoPractico_2/proyecto_1/data/lista_deptos.txt', 'r', encoding='UTF-8') as leer_archivo_deptos:
                        lineas_depto = leer_archivo_deptos.readlines()
                        for linea in lineas_depto:
                            if curso in linea:
                                datos = linea.strip().split(',')
                                departamento = datos[0]
                                depto = (facultad.enviar_lista_departamentos()).get(departamento)
                                ins_curso = (depto.enviar_cursos()).get(curso)

                    
                    ins_curso.agregar_estudiante_curso (estudiantes_dict.get(f'{nombre} {apellido}'))

                    with open('TrabajoPractico_2/proyecto_1/data/lista_cursos.txt', 'r', encoding='UTF-8') as leer_archivo_cursos:
                        lineas = leer_archivo_cursos.readlines()
                    with open('TrabajoPractico_2/proyecto_1/data/lista_cursos.txt', 'w', encoding='UTF-8') as archivo:
                        for linea in lineas:
                            if curso in linea:
                                datos = linea.strip().split(',')
                                datos_estudiante = [nombre, apellido, dni_estudiante]
                                nueva_linea = ','.join(datos + datos_estudiante) + '\n' 
                                archivo.write(nueva_linea)
                            else:
                                archivo.write(linea)

                    return print (f'El estudiante {nombre} {apellido} ha sido anotado en el curso {curso}.')
                else :
                    return print (f'El estudiante {nombre} {apellido} ya está anotado en el curso {curso}.')
            else:
                existe = False
        if not existe:
            return print (f'El estudiante con DNI {dni} no existe en la lista de estudiantes.')       

