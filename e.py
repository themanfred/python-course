'''
Escriba un programa que calcule el diámetro, el perímetro y el área de un círculo, el programa debe de desplegar
un menú con una opción para cada cálculo, cada cálculo debe de ser una función,
los resultados de cada cálculo deben de ser impresos.
'''
import math
pi=math.pi
n=0
def diametro():     
    radio = int(input('radio-> '))
    diametro = radio*2
    return diametro
    
def circumferencia():     
    radio = int(input('radio-> '))
    circumferencia = radio*2*pi
    return circumferencia
    
def area():     
    radio = int(input('radio-> '))
    area = radio**2*pi
    return area
while n!=4:
    print('\t MENU')
    print('1.Calcular el diametro de un circulo: ')
    print('2.Calcular la circumferencia de un circulo:')
    print('3.Calcular la area de un circulo:')
    print('4.Salir')
    n = int(input('Opcion-> :'))
    
    if n==1:
       print(f'El diametro es {diametro()}')
    elif n==2:
        print(f'La circumferencia es {circumferencia()}')     
    elif n==3:
        print(f'El area es {area()}')

    
        


        





    

