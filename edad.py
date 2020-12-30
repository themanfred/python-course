'''
Cree un programa que registre al usuario, que
le pida al usuario su nombre, su edad, el
programa debe tener una función que valide
que el usuario sea mayor de 18 años, en
caso de que sea menor de edad, avisar en
pantalla y no registrarlo. También debe de
tener una función que sume la cantidad de
usuarios que están registrando, para terminar
el programa el usuario debe de dejar el
nombre vacío o introducir cero en la edad.

'''

sumaT=0
edadP=0
nombre='Juan'
edad=1
def usuario(nombre,edad):
    global edadP
    while nombre != ' ' or edad !=0:
        nombre = str(input('Nombre: '))
        ultP= nombre
        edad = int(input('Edad: '))
        edadP=edad
        
        if nombre == '' or edad ==0:
            break
        else:
            mayor(edadP)
            
        
def mayor(edadP):
     global sumaT
     if edadP>=18:
         sumaT+=1
     return sumaT
    
usuario =usuario(nombre,edad)       

while usuario == True :
    print(usuario)
    if mayor == True:
        print(usuario)
    else:
         break
    
print(f'La suma de usuarios registrados es {sumaT} \n ')

    

