from typing import Sequence


student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
    return sum(sequence) / len(sequence)


#Imprimir el promedio del estudiante, llamando la funcion average e ingresando a grades de studen
print(average(student["grades"]))


#El siguiente ejemplo es lo mismo de arriba pero con diferente sintaxis.

#Se crear una clase, def __init__ es para inicializar la clase
#self es la palabra comun para realizar el dot notation donde se asignarán los valores
#self.name define el valor de la case Student
class Student:
    def __init__(self):
        self.name="Rolf"
        self.grades= (89, 90, 93, 78, 90)

    def average(self):
        return sum(self.grades) / len(self.grades)


#se creó una variable donde se va a llamar la clase de arriba
student = Student()
#Se imprime la variable donde se asignó la clase, y por medio de dot notation se accede al valor
print(student.name)
print(student.grades)
#Para imprimir la segunda función que está dentro de la clase Student
#Se llama a la clase, posteriormente la funcion, y dentro de la funcion la variable donde se agregó la clase
print(Student.average(student))
#La misma forma de imprimir la segunda función dentro de la clase Student
print(student.average())



#Tambien se pueden agregar más parametros dentro de la clase, no solo se puede usar self

class Student2:
    def __init__(self, name, grades):
        self.name="Rolf"
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

student2 = Student2("Bob", (100,100,100))
print(student2.name)
print(student2.average_grade())