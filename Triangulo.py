from FigurasGeometricas import FigurasGeometricas
class Triangulo(FigurasGeometricas):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area_triangulo(self):
        return self.base * self.altura /2
    
    
    