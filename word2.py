'''
Entrada
En la primera linea un entero .
El número de monedas que dejó tu mamá.

En la siguiente linea  enteros:
, ,  , , que representan los valores de cada moneda.
Todos los números estarán separados por un espacio.

Salida
Un único entero que representa el mínimo numero de
monedas que necesitas para cumplir lo deseado.
'''
suma=0
maximo=0
N = int(input())
if N>=1 and N<=100:
    a = list(map(int,input().split()))
    for i in range(N):
        n1= a[i]
        if n1>maximo:
            maximo=n1
        if a[i]>=1 and a[i]<=100:
            suma+=a[i]
            
numeroDeMax = a.count(maximo)
numerosSinMax = N-numeroDeMax
suma_max=numeroDeMax*maximo
suma_sin_maximo= suma - (suma_max)



if suma_max> suma_sin_maximo:
    if suma_max>(suma/2):
        print(numeroDeMax)
elif suma_sin_maximo >suma_max:
    if suma_sin_maximo>(suma/2):
        print(numerosSinMax)


    
    
    
            
        