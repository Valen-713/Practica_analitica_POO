from FigurasGeometricas import FigurasGeometricas

class Rombo(FigurasGeometricas):
    def _init_(self, nombre):
        super()._init_(nombre)
    @property
    def diagonalMayor(self):
        return self._diagonalMayor
    
    @diagonalMayor.setter
    def diagonalMayor(self,diagonalMayor:float):
        self._diagonalMayor=diagonalMayor
    
    @property
    def diagonalMenor(self) -> float:
        return self._diagonalMenor
    
    @diagonalMenor.setter
    def diagonalMenor(self,diagonalMenor: float):
        self._diagonalMenor = diagonalMenor 

    def area_rombo(self):
        return (self.diagonalMayor * self.diagonalMenor) / 2