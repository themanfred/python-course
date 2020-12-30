word= '''“La clase de python me sigue aburriendo,
el maestro es cruel y despiadado, desalmado,
ya que siempre pone ejercicios muy difíciles,
y en clase, el blah blah blah del maestro me duerme,
es muy aburrido, mejor apago la cámara, cierro el micrófono y me duermo”.
'''
import os
try:
    ensayo = open('Ensayo.txt', 'w')
    ensayo.write(word)
    lista= word.split()
    for i in range(len(lista)):
        ensayo.write(lista[i].upper(), end=' ')
    ensayo.close()
except IOError:
    print('no mames carnal')


