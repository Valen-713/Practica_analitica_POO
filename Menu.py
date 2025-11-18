from FigurasGeometricas import FigurasGeometricas
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Triangulo import Triangulo


Menu_funciones = True 
while Menu_funciones:
    print("______Carcular Areas______")
    print("1.Area Circulo")
    print("2.Area Cuadrado")
    print("3.Area Rectangulo")
    print("4.Area Triangulo")
    opcion=int(input("Selecciona una opcion: "))
 
       
    if opcion ==1:
        radio = float(input("Digite el numero de radio del circulo: "))
        cr = Circulo(radio)
        resultado = cr.area_circulo()
        print("El area del circulo es: ", resultado)
        
    elif opcion ==2:
        lado = float(input("Digite un valor de lado: "))
        cd = Cuadrado(lado)
        resultado = cd.area_cuadrado()
        print("El area del cuadrado es: ", resultado)
        
        

    