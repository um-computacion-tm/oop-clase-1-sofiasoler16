
import unittest

from objetos import Materia, Profesor, Alumno

class test_materia(unittest.TestCase):
    def test_init_materia(self):
        alumno1 = Alumno("6006", "Lorito", ["Matematica", "Lengua"])
        alumno2 = Alumno("62008", "Sofia Soler", ["Matematica"])

        materia1 = Materia("Matematica", "Juliana Gonzalez", [alumno1, alumno2])

        self.assertEqual(materia1.__nombre__, "Matematica")
        self.assertEqual(materia1.__profesores__, "Juliana Gonzalez")

    def test_obtener_nombre_profesores(self):
        alumno1 = Alumno("6006", "Lorito", ["Matematica", "Lengua"])
        alumno2 = Alumno("62008", "Sofia Soler", ["Matematica"])

        materia1 = Materia("Matematica", "Juliana Gonzalez", [alumno1, alumno2])

        self.assertEqual(materia1.obtener_profesores(), "Juliana Gonzalez")   

    def test_cambiar_nombre(self):
        alumno1 = Alumno("6006", "Lorito", ["Matematica", "Lengua"])
        alumno2 = Alumno("62008", "Sofia Soler", ["Matematica"])

        materia1 = Materia("Matematica", "Juliana Gonzalez", [alumno1, alumno2])

        materia1.cambiar_nombre("Lengua")

        self.assertEqual(materia1.__nombre__, "Lengua") 

    def test_obtener_alumnos(self):
        alumno1 = Alumno("6006", "Lorito", ["Matematica", "Lengua"])
        alumno2 = Alumno("62008", "Sofia Soler", ["Matematica"])

        materia1 = Materia("Historia", "Carlitos Paez Sosa", [alumno1, alumno2])

        self.assertEqual(alumno1.__nombre__, "Lorito")
        self.assertEqual(materia1.obtener_objeto_alumnos(), [alumno1, alumno2])

    def test_obtener_nombres_alumnos(self):
        alumno1 = Alumno("6006", "Lorito", ["Matematica", "Lengua"])
        alumno2 = Alumno("62008", "Sofia Soler", ["Matematica"])

        materia1 = Materia("Historia", "Carlitos Paez Sosa", [alumno1, alumno2])

        self.assertEqual(alumno1.__nombre__, "Lorito")
        self.assertEqual(materia1.obtener_nombre_alumnos(), ["Lorito", "Sofia Soler"])


class test_profesores(unittest.TestCase):
    def test_init_profesor(self):
        profesor1 = Profesor("Juliana Gonzalez", "Titular", "6458")

        self.assertEqual(profesor1.__nombre__, "Juliana Gonzalez")
        self.assertEqual(profesor1.__cargo__, "Titular")
        self.assertEqual(profesor1.__legajo__, "6458")

    def test_obtener_cargo_nombre_legajo_profesor(self):
        profesor1 = Profesor("Juliana Gonzalez", "Titular", "6458")

        self.assertEqual(profesor1.obtener_legajo(), "6458")   
        self.assertEqual(profesor1.obtener_cargo(), "Titular")   
        self.assertEqual(profesor1.obtener_nombre(), "Juliana Gonzalez")   


class test_alumno(unittest.TestCase):
    def test_init_alumno(self):
        alumno1 = Alumno("6006", "Lorito", ["Matematica", "Lengua"])

        self.assertEqual(alumno1.__nombre__, "Lorito")
        self.assertEqual(alumno1.__legajo__, "6006")
        self.assertEqual(alumno1.__materias__, ["Matematica", "Lengua"])

    def test_obtener_cargo_nombre_legajo_alumno(self):
        alumno1 = Alumno("6006", "Lorito", ["Matematica", "Lengua"])

        self.assertEqual(alumno1.obtener_legajo(), "6006")   
        self.assertEqual(alumno1.obtener_nombre(), "Lorito")   
        self.assertEqual(alumno1.obtener_materias_cursando(), ["Matematica", "Lengua"]) 



if __name__ == '__main__':
    unittest.main()
