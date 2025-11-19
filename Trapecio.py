from FigurasGeometricas import FigurasGeometricas

class Trapecio(FigurasGeometricas):
    def __init__(self, nombre):
        super().__init__(nombre)

    @property
    def baseMayor(self):
        return self._baseMayor
    
    @baseMayor.setter
    def baseMayor(self,baseMayor:float):
        self._baseMayor=baseMayor
    
    @property
    def baseMenor(self) -> float:
        return self._baseMenor
    
    @baseMenor.setter
    def baseMenor(self,baseMenor: float):
        self._baseMenor = baseMenor
    
    @property
    def altura(self) -> float:
        return self._altura
    
    @altura.setter
    def altura(self,altura: float):
        self._altura = altura

    def area_trapecio(self):
        return (self.baseMayor + self.baseMenor) * self.altura / 2
    
    


    