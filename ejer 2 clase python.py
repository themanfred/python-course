'''
2) Haga una función que calcule el valor de x en la ecuación
c = ax + b si se tiene que a = 10, b = 3.3 y c = 2 y regrese el valor 
'''

print('El valor de x en la funcion c = ax +b donde a = 10, b = 3.3 y c = 2 es:')

a=10
b=3.3
c=2
def valor(a,b,c):
    x = (c-b)/a
    return x
print(valor(a,b,c))