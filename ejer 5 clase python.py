'''
5)Haga una función que calcule el tiempo que
tardó una persona en recorrer 20 kms a una velocidad media de 1 km/hora. (Vm = d/t)

'''

print("Una persona al recorrer 20 kms a una velocidad media de 1 km/hora. \nTiene el tiempo (Vm = d/t)")
Vm=1
d=20
def tiempo(Vm, d):
    t = d/Vm
    return t

print(f'El tiempo es {tiempo(Vm, d)} horas')