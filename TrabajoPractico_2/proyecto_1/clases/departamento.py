
class Departamento:
    def __init__(self, nombre, director):
        self.__nombre = nombre
        self.__director = director
        self.__profesores = {}
        self.__cursos = {}
      
       
    def enviar_nombre(self): 
        return self.__nombre
    
    def enviar_cursos(self):
        return self.__cursos


    def listar_cursos(self):
        if self.__cursos == {}:
            print(f"El departamento {self.__nombre} no tiene cursos asignados.")
        else:
            for curso in self.__cursos.values():
                print(f"{(curso.get_datos())[0]}")


    def cargar_cursos(self, dict_cursos):
        self.__cursos = dict_cursos
    

    def agregar_curso(self, facultad, nombre_curso, titular_nombre, titular_apellido, titular_dni, departamento):
        from clases.curso import Curso
        from clases.profesor import Profesor
        from clases.facultad import Facultad
        # Verificar si el curso ya existe en el departamento
        dict_departamentos = facultad.enviar_lista_departamentos()
        ins_departamento = dict_departamentos.get(departamento)

        if ins_departamento is None:
            print(f'El departamento {departamento} no existe.')
            return
        
        if nombre_curso in ins_departamento.__cursos.keys(): 
            print(f'El curso {nombre_curso} ya existe en el departamento {departamento}.')
            return 
        
        # Profesor para el titular del curso
        titular = self.__profesores.get(f'{titular_nombre} {titular_apellido}')

        # Creo un nuevo objeto Curso
        nuevo_curso = Curso(nombre_curso, titular) #COMPOSICION 

        # Agrego el curso al diccionario de cursos del departamento
        ins_departamento.__cursos[nombre_curso] = nuevo_curso

        # Escribo el curso en el archivo de cursos
        with open('TrabajoPractico_2/proyecto_1/data/lista_cursos.txt', 'a', encoding='UTF-8') as archivo:
            archivo.write(f'\n{nombre_curso},{titular_nombre},{titular_apellido},{titular_dni}')

        with open('TrabajoPractico_2/proyecto_1/data/lista_deptos.txt', 'r', encoding='UTF-8') as leer_archivo:
            lineas = leer_archivo.readlines() 

        with open('TrabajoPractico_2/proyecto_1/data/lista_deptos.txt', 'w', encoding='UTF-8') as archivo_deptos:
            for linea in lineas:
                if departamento in linea: 
                    datos = linea.strip().split(',')
                    nueva_linea = ','.join(datos + [nombre_curso]) + '\n' 
                    archivo_deptos.write(nueva_linea) 
                else:
                    archivo_deptos.write(linea)  

        print(f'Curso {nombre_curso} agregado al departamento {departamento}.')




















    
