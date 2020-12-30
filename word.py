'''
DescripciÃ³n
Dados dos vectores de  componentes cada uno, calcula el vector resultante
de su suma (la suma de vectores se realiza componente a componente).

Entrada
Un entero  seguido de los  enteros del primer vector y los  enteros del segundo vector.
Puedes suponer que 1 ≤  ≤ 100 y que los valores de las componentes estÃ¡n en el rango de 1 a 100.

Salida
 enteros que sean las componentes del vector suma correspondiente.
'''
n = int(input())
if n>=1 and n<=1000:
    numeros = list(map(int,input().split()))
    dif1 = numeros[0]
    for i in range(1,n):
        for j in range(1,n):
            if numeros[i] > numeros[j-1]:
                dif = numeros[i] -numeros[j-1]
                if dif1> dif:
                    dif1 =dif

            elif numeros[j-1] > numeros[i]:
                dif = numeros[j-1] -numeros[i]
                if dif1> dif:
                    dif1 =dif
            elif  numeros[i] == numeros[j-1]:
                if numeros[i-1] == numeros[j-1]:
                    dif = numeros[j-1] -numeros[i]
                    if dif1> dif:
                        dif1 =dif
                        
           
              
print(dif1)


            
        
        
        
            

