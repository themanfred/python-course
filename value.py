'''
Cree un programa que reciba un número entero,
éste entero representa un período de tiempo expresado en segundos,
imprima el equivalente en días, horas, minutos y segundos.

'''
#Por ejemplo: 300,000 segundos serían 3 días, 11 horas, 20 minutos y 0 segundos.


num = int(input('Digite un numero entero: '))
original = num
#dividir por el numero de segundos y despues  "restar" o guardar un nuevo valor de num para determinar la siguiente unidad
dias = num // (24*3600)
num = num%(24*3600)
horas = num//3600
num = num%3600
minutos = num//60
seg = num%60



print(f"{original} segundos serian {dias} dias, {horas} horas, {minutos} minutos, {seg} segundos")