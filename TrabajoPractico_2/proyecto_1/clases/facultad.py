

class Facultad:
    
    def __init__(self):
        from clases.alumnado import Alumnado
        self.__estudiantes = {}
        self.__profesores = {}
        self.__departamentos = {}
        self.__servicio_alumnado = Alumnado()


    def actualizar_datos(self, estudiantes_dict, profesores_dict, depto_dict):
            self.__estudiantes = estudiantes_dict
            self.__profesores = profesores_dict
            self.__departamentos = depto_dict


    def anotar_estudiante_a_curso(self, facultad, curso, dni):
        self.__servicio_alumnado.enviar_solicitud_anotar_a_curso(facultad, curso, dni)


    def inscribir_estudiante(self, nombre, apellido, dni):
        nuevo_estudiante = self.__servicio_alumnado.estudiante_crear(nombre, apellido, dni)
        for estudiante in self.__estudiantes.values():
            dni_lista = estudiante.get_datos()[2]
            if dni == dni_lista:
             return print (f'El estudiante {nombre} {apellido} ya existe en la lista de estudiantes.')
            
        self.__estudiantes[f'{nuevo_estudiante.nombre} {nuevo_estudiante.apellido}'] = nuevo_estudiante
        nuevo_estudiante = f"{nombre},{apellido},{dni}"
        with open('TrabajoPractico_2/proyecto_1/data/lista_estudiantes.txt', 'a', encoding='UTF-8') as archivo:
            archivo.write(f'\n{nuevo_estudiante}') 
        return print (f'El estudiante {nombre} {apellido} ha sido agregado a la lista de estudiantes')


    def listar_profesores(self): 
        for profe in self.__profesores.values():
            print(f'{profe.nombre} {profe.apellido}')
    

    def listar_estudiantes(self):
        estudiantes=list(self.__estudiantes.values())
        for estudiante in estudiantes:
            nombre, apellido, dni = estudiante.get_datos()[:3]
            print (f'{nombre} {apellido} / DNI: {dni}')
        
        
    def obtener_estudiantes(self):
        return self.__estudiantes
    

    def contratar_profesor(self, nombre, apellido, dni, nombre_departamento):
        from clases.profesor import Profesor
        
        clave_profesor = f"{nombre} {apellido}"
        if clave_profesor in self.__profesores:
            print(f'El profesor {nombre} {apellido} ya existe en la lista de __profesores')
            return

        departamento_encontrado = self.__departamentos.get(nombre_departamento)
        if not departamento_encontrado:
            print(f"El departamento '{nombre_departamento}' no existe, no se puede asignar al profesor, cree el departamento e intente nuevamente")
            return

        nuevo_profesor = Profesor.crear_profesor(Profesor, nombre, apellido, dni, departamento_encontrado)
        self.__profesores[clave_profesor] = nuevo_profesor
        print(f'El profesor {nombre} {apellido} se contrato y fue asignado al departamento {nombre_departamento}')

        with open('TrabajoPractico_2/proyecto_1/data/lista_profesores.txt', 'a', encoding='UTF-8') as archivo:
            archivo.write(f'\n{nombre},{apellido},{dni},{nombre_departamento}')


    def crear_departamento(self, nombre_depto_nuevo, director_nombre, director_apellido):
        from clases.departamento import Departamento

        if nombre_depto_nuevo in self.__departamentos:
            print(f'El departamento {nombre_depto_nuevo} ya existe')
            return
        
        profesores_dict = self.__profesores
        director = profesores_dict.get(f'{director_nombre} {director_apellido}')
        clave_profesor = f"{director.nombre} {director.apellido}"
        if clave_profesor not in self.__profesores:
            print(f"El profesor {director.nombre} {director.apellido} no está contratado. Contrátalo antes de asignarlo a un departamento")
            return
        #Creo un objeto departamento
        dpto_nuevo = Departamento(nombre_depto_nuevo, director) 
        director.departamento = dpto_nuevo
        self.__departamentos[nombre_depto_nuevo] = dpto_nuevo

        with open('TrabajoPractico_2/proyecto_1/data/lista_deptos.txt', 'a', encoding='UTF-8') as archivo:
            archivo.write(f'\n{nombre_depto_nuevo},{director.nombre},{director.apellido}')

        print(f"Departamento {nombre_depto_nuevo} se ha creado. Su director es {director.nombre} {director.apellido}")


        
    def listar_deptos_existentes(self):
        print('Lista de departamentos de la facultad:')
        departamentos = self.__departamentos.values()
        for deptos in departamentos: #llamar al final, porque lista todos los deptos existentes
            print(f'{deptos.enviar_nombre()}')

    def enviar_lista_departamentos(self):
        return self.__departamentos

