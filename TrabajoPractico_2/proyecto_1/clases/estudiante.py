from clases.persona import Persona

class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.cursos = {}

    def get_datos(self):
        datos = [self.nombre, self.apellido, self.dni, self.cursos]
        return datos
    
    def cargar_cursos(self, dict_cursos):
        cursos = dict_cursos
    
          
    

    '''def __repr__(self):
        return f"Estudiante(nombre={self.nombre}, apellido={self.apellido}, dni={self.dni}, cursos={self.cursos})"'''