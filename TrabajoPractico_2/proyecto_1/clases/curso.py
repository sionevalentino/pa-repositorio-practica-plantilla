
class Curso:
    def __init__(self, nombre, titular):
        self.__nombre = nombre
        self.__titular = titular
        self.__estudiantes = []
    
    def agregar_estudiante_curso(self, estudiante):
        self.__estudiantes.append(estudiante)

    def get_datos(self):
        return [self.__nombre, self.__titular, self.__estudiantes]
