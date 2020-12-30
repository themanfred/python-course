#Ejercicio3. HAGAN UN PROGRAMA QUE DIVIDA TRES NÚMEROS,
#RESTE UNA VALOR CUALQUIERA Y LO
#MULTIPLIQUE POR OTRO VALOR
print("Digite un numero: ")
num1 = int(input())
print("Digite otro numero: ")
num2 = int(input())
print("Digite otro numero: ")
num3 = int(input())

division = ((num1 / num2) / num3)

resta = division - num2

total = resta * num3

print(total)