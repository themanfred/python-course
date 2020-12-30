import random

Puntos_Jugador1 = 0
Puntos_Jugador2 = 0
columnas = 0
filas = 0
tablero = []
orientacion_cartas=[]
jugador_turno = 1
par = False



def generador_Fraccion(): 

  numerador=random.randint(1,10) #Generación números aleatorios para el numerador y denominador.
  denominador=random.randint(1,10) 

  multiplicacion=random.randint(2,8) 

  fraccion=str(numerador)+'/'+str(denominador) 
  equivalente=str(numerador*multiplicacion)+'/'+str(denominador*multiplicacion) 

  return fraccion,equivalente


def TurnoJugador():

  global jugador_turno, par,Puntos_Jugador1,Puntos_Jugador2
  if jugador_turno == 1:
    if par == True:
      jugador_turno =1
      Puntos_Jugador1 +=1
    else:
      jugador_turno =2
  elif jugador_turno == 2:
    if par == True:
      jugador_turno =2
      Puntos_Jugador2 +=1
    else:
      jugador_turno =1
      



def parametrosjuego():  #Funcion que valida que el minimo de filas y columnas sea 8 y agrega los valores a la matriz

    print(f'Digite el numero de filas y columnas del juego:')

    while True:

        global filas
        global columnas
        #asegurarme que no pasa nada si pongo un numero y que me pida denuevo
        filas = int(input('Digita la dimension de filas (min. 8): '))#Digita el numero de filas
        #asegurarme que no pasa nada si pongo un numero y que me pida denuevo
        columnas = int(input('Digita la dimension de columnas (min. 8): ')) 
        #digita el numero de columnas
        mul = filas*columnas
        
        if mul % 2 == 0:
          if filas >= 2 and columnas >= 2:  #Si el numbero de filas y columnas es mayor a 8 rompe este ciclo
              break

          else:
              print("Rango no valido (min. 8)")#en caso que filas y/o colmnas es menor a 8
        else:
          print("El tablero no puede ser impar")
          return mul
  
    
    lista_fracciones=[] 

    for i in range(int(mul/2)):#For que agrega los valores generados de fracciones a una lista

      fraccion,fraccion_equivalente=generador_Fraccion()

      lista_fracciones.append(fraccion)
      lista_fracciones.append(fraccion_equivalente)
    
    random.shuffle(lista_fracciones)

    indice=0
    for i in range(filas): 
        renglon = []
        renglon2 = []
        
        for j in range(columnas):
            renglon.append(lista_fracciones[indice])
            indice+=1
              
            renglon2.append(False)#False Boca abajo
            
        orientacion_cartas.append(renglon2)
        tablero.append(renglon) #
    


def imprimir_tablero():  #Funcion que crea la matriz
    '''
    for x in range(columnas):
        print("\t\t\t" + str(x), end=" ") #imprimir el numero de la columna
    print()
'''
    for i in range(filas):
        print(str(i), end=" ") #imprimir numero de la fila

        for j in range(columnas):

            if orientacion_cartas[i][j] == False: #imprimir tablero
                print("\t\t\t*", end=" ")

            else:
                print(f"\t\t{tablero[i][j]}", end=" ")

        print()
    
    print("Jugador 1:", Puntos_Jugador1, end="\t\t\t")
    print("Jugador 2:", Puntos_Jugador1)
    print("Turno: Jugador", jugador_turno)


def cartasEquivalentes(x1,x2,y1,y2):

  global par
  if tablero[x1][y1] == tablero[x2][y2]:
    #tener a las cartas abiertas y hacer que el jugador que hizo el print
    par = True
    TurnoJugador()
  else:
      #Las cartas nos son igulas
      orientacion_cartas[x1][y1] = False #dar la vuelta de regreso
      orientacion_cartas[x2][y2] = False# dar la vuelta de regreso
      #imprimir_tablero() #mostrar el tablero 
      #mostrar que es el turno del proximo jugador
      par = False
      TurnoJugador()



def voltear_cartas():  #Funcion que se encarga de cambiar los valores "voltear cartas", dentro de la matriz
    counterDeCartas=0 #cuenta cuantas carta se han dado la vuelta

    while True:

        print("Primera Carta")

        x1 = int(input('Fila primera carta:'))
        y1 = int(input('Columna primera carta:'))
        #asegurarme que no pasa nada si pongo un numero y que me pida denuevo
        if orientacion_cartas[x1][y1] == False:  
          if x1 >= 0 and x1 < filas and y1 >= 0 and y1 < columnas:
              orientacion_cartas[x1][y1] = True
              counterDeCartas+=1 #ya se decubrio una carta
              break
          else:
              print("Rango invalido")
              continue
        else:
          print("Carta ya volteada")
          continue

    imprimir_tablero()

    while True:

        print("Segunda Carta")

        x2 = int(input('Fila segunda carta:'))
        y2 = int(input('Columna segunda carta:'))
        #asegurarme que no pasa nada si pongo un numero y que me pida denuevo
        
        if x2 >= 0 and x2 < filas and y2 >= 0 and y2 < columnas :

          if orientacion_cartas[x2][y2] == False:

              orientacion_cartas[x2][y2] = True
              counterDeCartas+=1# y ahora la segunda carta tambien haciendo un par
              break

          else:
              print("Carta ya volteada")
              continue

        else:
          print("Rango invalido")
          continue
          
    imprimir_tablero()        
    if counterDeCartas == 2:
      cartasEquivalentes(x1,x2,y1,y2)
      #llamar una funcion que me va determinar si las dos cartas son iguales open y de esa funcion se va a determinar si el jugador sigue jugando en caso de que es par o es el turno del otro
      #En caso que no es igual se va a repetir esta eccion para darle la vuelta a las cartas
     
  

def ganador():  #Función que valida ganador e imprime mensaje de felicitaciones
  global mul, Puntos_Jugador1,Puntos_Jugador2

  if Puntos_Jugador1 == Puntos_Jugador2 and (mul/2)==(Puntos_Jugador1 + Puntos_Jugador2):
      print("EMPATE")
  elif (mul/2)==(Puntos_Jugador1 + Puntos_Jugador2) and Puntos_Jugador1> Puntos_Jugador2:
        print(f'''
          __^__                                      __^__
         ( ___ )------------------------------------( ___ )
          | / |                                      | \ |
          | / |        Felicidades Jugador 1         | \ |
          |___|                                      |___|
         (_____)------------------------------------(_____)

    ''')

  elif (mul/2)==(Puntos_Jugador1 + Puntos_Jugador2) and Puntos_Jugador2> Puntos_Jugador1:
        print(f'''
          __^__                                      __^__
         ( ___ )------------------------------------( ___ )
          | / |                                      | \ |
          | / |        Felicidades Jugador 2         | \ |
          |___|                                      |___|
         (_____)------------------------------------(_____)

    ''')


def guardar_partida(): #Función que va a guardar la partida en un archivo
  pass



n = 0
while n != 3:
    print('''
                    MENU
    1)Empezar partida
    2)Continuar una partida guardada
    3)Salir

    ''')
    n = int(input('Digite una opcion:'))
    if n == 1:
        resp = ''
        parametrosjuego()
        while resp != 'fin':  #Ciclo donde se une el tablero con el voltear cartas, permite jugar mientras no se escriba fin al termino de un turno
            imprimir_tablero()

            voltear_cartas()
            resp = input(
                '¿Desea seguir jugando? (Escriba fin para terminar el juego)  '
            )

    elif n == 2:
        print('placeholder memoria')
    elif n == 3:
        print('''Hasta luego
             A____A
            |・ㅅ・|
            |っ　ｃ|
            |　　　|
            |　　　|
            |　　　|
            |　　　|
            |　　　|
             U￣￣U
        ''')








#Asigna una fraccion y que lo pueda imprimir como fraccion (n/t)
#Asignalo de manara random como elemento con valor falso
#Si el lugar asignado ya esta ocupado vuelva a hacerlo hasta que
#encuentras un lugar desocupado
'''
esa misma fraccion multiplicalo por la dividsion equivalante a uno 
que al final sea igual a la fraccion origial

Asigna ese elemento a otro 'casillero' y usar una variable
para contar la cantidad de pares que hay 

Los pares siempre son positivos

Repito el metodo de asignacion de la primera fraccion
'''
'''

'''


