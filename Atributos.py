class Celular:
    def __init__(self, marca, modelo, camara) -> None:
        """constructor

        Args:
            marca (str): marca del celular
            modelo (str): modelo del tel
            camara (str): MP de la cam
        """
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    #methods
    def llamar(self):
        """método para llamar
        """
        print(f"Estás haciendo una llamada desde un {self.marca}")

    def colgar(self):
        """método para colgar llamada
        """
        print(f"Colgaste la llamada desde un {self.marca}")


if __name__ == "__main__":
    cel1 = Celular(marca="Apple", modelo="15 pro MAX", camara="48MP")
    cel2 = Celular(marca="Apple", modelo="15 lite", camara="48MP")
    cel1.llamar()
    cel2.llamar()
    cel1.colgar()