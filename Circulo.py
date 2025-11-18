from FigurasGeometricas import FigurasGeometricas
class Circulo(FigurasGeometricas):
    def __init__(self, radio):
        self.radio = radio
        self.pi = 3.1416
    def area_circulo(self):
        return self.radio**2 *self.pi
    