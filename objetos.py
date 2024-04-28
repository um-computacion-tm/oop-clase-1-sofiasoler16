
class Profesor:
    def __init__(self, nombre, cargo, legajo):
        self.__nombre__ = nombre
        self.__cargo__ = cargo
        self.__legajo__ = legajo

    def obtener_nombre(self):
        return self.__nombre__

    def obtener_cargo(self):
        return self.__cargo__

    def obtener_legajo(self):
        return self.__legajo__
    

class Alumno:
    def __init__(self, legajo, nombre, materias:list):
        self.__legajo__ = legajo
        self.__nombre__ = nombre
        self.__materias__ = materias

    def obtener_legajo(self):
        return self.__legajo__
    
    def obtener_nombre(self):
        return self.__nombre__

    def obtener_materias_cursando(self):
        return self.__materias__
    
class Materia:
    def __init__(self, nombre, profesores, alumnos:list[Alumno]):
        self.__nombre__ = nombre
        self.__profesores__ = profesores
        self.__alumnos__ = alumnos

    def obtener_profesores(self):
        return self.__profesores__

    def cambiar_nombre(self, nombre):
        self.__nombre__ = nombre

    def obtener_objeto_alumnos(self):
        for nombre in self.__alumnos__:
            print(nombre.obtener_nombre())

        return self.__alumnos__
    
    def obtener_nombre_alumnos(self):
        nombres = []
        for nombre in self.__alumnos__:
            nombres.append(nombre.obtener_nombre())

        return nombres


