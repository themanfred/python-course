''''
4) Haga una función que calcule el valor medio de seis
números y regrese el valor medio, éstos números deben de ser introducidos por el usuario. 

'''
n=0
suma=0
def medio(n,suma):
    for i in range(6):
        n = int(input("Digite un numero: "))
        suma+=n
    promedio = suma/6
    return promedio
print(medio(n,suma))


