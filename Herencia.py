"""Herencia simple y por jerarquía
"""
class Persona:
    def __init__(self, nombre, edad, nacionalidad) -> None:
            self.nombre = nombre
            self.edad = edad
            self.nacionalidad = nacionalidad
    #Abstracción
    def hablar(self):
        pass
    


class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad, trabajo, salario) -> None:
         super().__init__(nombre, edad, nacionalidad)# lo que hereda
         self.trabajo = trabajo
         self.salario = salario
    def hablar(self):
        print("Hablando")


class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad, notas, universidad) -> None:
         super().__init__(nombre, edad, nacionalidad)
         self.notas = notas
         self.universidad = universidad
         

if __name__ == "__main__":
    roberto = Empleado("roberto", 43, "arg", "Programador", 500000)
    
    print(roberto.nombre)
    
    est_1 = Estudiante("Juan",20, 'col', [5,2,3], "UN")
    print(est_1.universidad)
    