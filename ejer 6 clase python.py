'''
6) Escribir una funcion sum() y una función multip() que
sumen y multipliquen respectivamente 4 números.
Los números deben de ser introducidos por el usuario.

'''

num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))
num3 = int(input("Digite otro numero: "))
num4 = int(input("Digite otro numero: "))

def suma(num1,num2,num3,num4):
    suma = num1 +num2 +num3 +num4
    return suma
def multip(num1,num2,num3,num4):
    producto = num1 *num2 *num3 *num4
    return producto

print(f'La suma es {suma(num1,num2,num3,num4)} \nLa multiplicacion es {multip(num1,num2,num3,num4)}')
