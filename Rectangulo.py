from FigurasGeometricas import FigurasGeometricas
class Rectangulo(FigurasGeometricas):
    def __init__(self, ancho, largo):
        self.largo = largo
        self.ancho = ancho
    def area_rectangulo(self):
        return self.largo * self.ancho
        
    