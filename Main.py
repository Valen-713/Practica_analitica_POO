from FigurasGeometricas import FigurasGeometricas
from Triangulo import Triangulo
from Cuadrado import Cuadrado
from Circulo import Circulo
from Rectangulo import Rectangulo

nombre=input("Que figura desea usar")
print("La figura seleccionada es ",nombre)

#Instancia clase padre figura geometrica
fg= FigurasGeometricas(nombre)
#Llamo la funcion para calcuar el area
fg.area()

tr=Triangulo()
print("El area del ", fg.nombre , "es" ,tr.area())

cd = Cuadrado()
print("El area del ", fg.nombre , "es" ,cd.area())

cr = Circulo()


rc = Rectangulo()
rc.nombre=fg.nombre
Valor_area = rc.area()
print("El area del " , rc.nombre, "es" , Valor_area)


    


