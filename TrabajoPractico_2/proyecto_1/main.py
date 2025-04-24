from clases.facultad import Facultad
from clases.estudiante import Estudiante
from clases.profesor import Profesor
from clases.departamento import Departamento
from clases.curso import Curso
from clases.alumnado import Alumnado
from modules.listaAobjeto import cargar_listas


facultad = Facultad()


'''Objeto facultad que contiene listas de estudiantes, profesores y departamentos'''



opcion = 0
while opcion != 6:

    estudiantes, profesores, departamentos, cursos = cargar_listas()
    facultad.actualizar_datos(estudiantes, profesores, departamentos)

    print(f'''
    ########################################
    # Sistema de Informacion Universitaria #
    ########################################
        
    Elige una opción
        
    1 - Inscribir alumno
    2 - Contratar profesor
    3 - Crear departamento nuevo
    4 - Crear curso nuevo
    5 - Inscribir estudiante a un curso
    6 - Salir 
    ''')

    opcion = int(input('Opcion: '))
    if opcion == 1 :
        nombre = input('Nombre: ')
        apellido = input('Apellido: ')
        dni = input('DNI: ')
        facultad.inscribir_estudiante(nombre, apellido, dni)
        print(f"Alumno {nombre} {apellido} con DNI {dni} inscrito correctamente.")


    elif opcion == 2: 
        nombre= input('Nombre: ')
        apellido= input('Apellido: ')
        dni= input('DNI: ')
        departamento = input('Departamento al que lo asigna: ')
        facultad.contratar_profesor(nombre, apellido, dni, departamento)
        print(f"Profesor {nombre} {apellido} con DNI {dni} contratado en el departamento {departamento}.")


    elif opcion == 3:
        # Listar profesores disponibles
        print("\nProfesores disponibles:")
        facultad.listar_profesores()
        nombre_depto = input('Nombre del departamento: ')
        director_nombre = input('Nombre del director: ')
        director_apellido = input('Apellido del director: ')
        facultad.crear_departamento(nombre_depto, director_nombre, director_apellido)
        print("\nDepartamentos existentes:")
        facultad.listar_deptos_existentes()
    
    
    elif opcion == 4 :
        # Listar profesores disponibles
        print("\nProfesores disponibles:")
        facultad.listar_profesores()
        nombre_curso = input('Nombre del curso: ')
        nombre_titular = input('Nombre del titular: ')
        apellido_titular = input('Apellido del titular: ')
        dni_titular = input('DNI del titular: ')
        departamento = input('Departamento al que lo asigna: ')

        dict_departamentos = facultad.enviar_lista_departamentos()
        ins_departamento = dict_departamentos[departamento]

        nuevo_curso = ins_departamento.agregar_curso(facultad,nombre_curso, nombre_titular, apellido_titular, dni_titular, departamento)
        
        print(f"\nCursos existentes en el departamento {departamento}:")
        ins_departamento.listar_cursos()


    elif opcion == 5:
        # Listar estudiantes disponibles
        print("\nEstudiantes disponibles:")
        facultad.listar_estudiantes()
        dni_estudiante = input('DNI del estudiante: ')
        nombre_curso = input('Nombre del curso: ')
        estudiante_en_curso = facultad.anotar_estudiante_a_curso(facultad, nombre_curso, dni_estudiante)

    elif opcion == 6:
        print('Saliendo...')
        break

    else:
        print('Opción no válida. Por favor, elige una opción válida.')
        opcion = int(input('Ingrese nuevamente la opcion: '))
        

   
