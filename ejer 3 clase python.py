'''
3) Haga una función que pida al usuario dos números,
y que eleve el primer número a la potencia del segundo número.

'''
num1 = int(input("Digite un numero: "))
num2 = int(input("Digite otro numero: "))

def potencia(num1,num2):
    return pow(num1,num2)

print(potencia(num1,num2))