'''
Descripción
Dado un conjunto de 1<=N<=1000 elementos enteros, determina la diferencia mínima entre cualquier pareja posible.

Entrada
En la primera línea el entero N. En la segunda línea y seprados por un espacio, los N datos enteros.

Explicación de la salida
La diferencia mínima en el ejemplo se logra restando 21 y 20

'''
#diferencia minima se ecuentra una vez que se identifica los dos numeros mas grandes
#se resta el mayour- segundo_mayor

#Condicion de 1<=N<=1000 elementos enteros


n = int(input())
if n>=1 and n <=1000:
    dif2 = []
    numeros = list(map(int,input().split()))
    for i in range(1,n):
        dif2=0
        sig = numeros[i]
        desp = numeros[i-1]
        if sig> desp:
            dif1 =sig - desp
        else:
            dif1 =desp - sig
        dif2.append(int(dif1))
        

        print(dif2)
        setdif2= set(dif2)
        
print(setdif2)
        
        
            

        #restar cada elemento contodolos los otros elementos en la lista.
        #identifica cual es el mayor de cualquier dos numeros
        #guardar la diferencia
        #compara esa diferencia con la siguiente

           
