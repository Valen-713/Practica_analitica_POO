from FigurasGeometricas import FigurasGeometricas
from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Triangulo import Triangulo
from Cilindro import Cilindro
from Paralelograma import Paralelograma
from Trapecio import Trapecio
from Rombo import Rombo

Menu_funciones = True 
while Menu_funciones:
    print("______Carcular Areas______")
    print("1.Area Circulo")
    print("2.Area Cuadrado")
    print("3.Area Rectangulo")
    print("4.Area Triangulo")
    print("5.Area Cilindro")
    print("6.Area Paralelograma")
    print("7.Area Trapecio")
    print("8.Area Rombo")
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
        
    elif opcion ==3:
        largo = float(input("Digite un valor de largo: "))
        ancho = float(input("Digite un valor de ancho: "))
        rc = Rectangulo(largo, ancho)
        resultado = rc.area_rectangulo()
        print("El area del rectangulo es: ", resultado)
        
    elif opcion ==4:
        base = float(input("Digite un valor de base: "))
        altura = float(input("Digite un valor de altura: "))
        tr = Triangulo(base , altura)
        resultado = tr.area_triangulo()
        print("El area del triangulo es: ", resultado)

    elif opcion ==5:
        altura=float(input("Digite un valor de altura: "))
        radio=float(input("Digite un valor de radio: "))
        cl = Cilindro("Cilindro")
        cl.radio = radio
        cl.altura = altura
        resultado = cl.area_cilindro()
        print("El area del cilindro es: ", resultado)

    elif opcion ==6:
        base=float(input("Digite un valor de base: "))
        Altura=float(input("Digite un valor de altura: "))
        pl = Paralelograma("Paralelograma")
        pl.base = base
        pl.altura = Altura
        resultado = pl.area_paralelograma()
        print("El area del paralelograma es: ", resultado)

    elif opcion ==7:
        basemayor=float(input("Digite un valor de base mayor: "))
        basemenor=float(input("Digite un valor de base menor: "))
        Altura=float(input("Digite un valor de altura: "))
        tp = Trapecio("Trapecio")
        tp.baseMayor = basemayor
        tp.baseMenor = basemenor
        tp.altura = Altura
        resultado = tp.area_trapecio()
        print("El area del trapecio es: ", resultado)

    elif opcion ==8:
        diagonalmayor=float(input("Digite un valor de diagonal mayor: "))
        diagonalmenor=float(input("Digite un valor de diagonal menor: "))
        rb = Rombo("Rombo")
        rb.diagonalMayor = diagonalmayor
        rb.diagonalMenor = diagonalmenor
        resultado = rb.area_rombo()
        print("El area del rombo es: ", resultado)




    