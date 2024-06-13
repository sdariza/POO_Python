class Estudiante:
    def __init__(self, nombre:str, edad:int, grado:int) -> None:
        """Constructor

        Args:
            nombre (str): nombre del estudiante
            edad (int): edad del estudiante
            grado (int): grado del estudiante
        """
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
    
    
    def estudiar(self):
        print(f'El estudiante {self.nombre} está estudiando')
        
        
if __name__ == "__main__":
    name = input("Ingrese el nombre del estudiante")
    edad = int(input("Ingrese la edad del estudiante"))
    grado = int(input("Ingrese el grado del estudiante"))
    est_1 = Estudiante(nombre=name,edad=edad,grado=grado)
    print(f"""
          Nombre: {est_1.nombre}
          Edad: {est_1.edad}
          grado: {est_1.grado}
          """)
    while True:
        if "estudiar" == input().lower():
            est_1.estudiar()