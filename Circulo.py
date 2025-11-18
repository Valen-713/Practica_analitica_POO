from FigurasGeometricas import FigurasGeometricas
class Circulo(FigurasGeometricas):
    def __init__(self, radio, pi):
        self.radio = radio
        self.pi = 3.1416
    def area(self):
        return self.radio**2 *self.pi
    