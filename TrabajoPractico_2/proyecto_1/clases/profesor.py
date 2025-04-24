from clases.persona import Persona
class Profesor(Persona):
    def __init__(self, nombre, apellido, dni, departamento):
        super().__init__(nombre, apellido, dni)
        self.departamento = departamento
        

    def crear_profesor(self, nombre, apellido, dni, departamento):
        nuevo_profesor = Profesor(nombre, apellido, dni, departamento)
        return nuevo_profesor
    def __str__(self):
        return f"{self.nombre} {self.apellido} (DNI: {self.dni}, Departamento: {self.departamento})"
