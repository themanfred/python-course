revEarth = 0
revTec =0
angleE=0
angleG =0
cons = (110.3/.305)
int1= (cons*.69)
int2 = (cons*.61)
bto= (cons*.69)
time =0
for i in range(4):
    
    for i in range(1):
        angleE = angleG
        angleE+=  int1
        while angleE > 360:
            if angleE > 360:
               angleE = angleE-360
               revEarth +=1
        print(f'En 1.69 años y {revEarth} revoluciones y tiempo {time:.2f}, la tierra tiene un angulo {angleE:.2f} grados')
        angleE += int2
        time +=1.69
        while angleE > 360:
            if angleE > 360:
               angleE = angleE-360
               revEarth +=1 
        print(f'En .61 años  y {revEarth} revoluciones y tiempo {time:.2f}, mas la tierra tiene un angulo {angleE:.2f} grados')
        angleE+=bto
        time +=.61
        while angleE > 360:
            if angleE > 360:
               angleE = angleE-360
               revEarth +=1
        print(f'En 1.69 años y {revEarth} revoluciones y tiempo {time:.2f}, mas la tierra tiene un angulo {angleE:.2f} grados')
        angleG=angleE
        time +=1.69
        if angleE == 110.3 or angleE == 139.39:
            print('Hay una collision!!')
    angleG = angleE       
    revTec+=1
    print(f'After {revTec} revolutions of Tec1 the Earths angle is {angleE:.2f}')
        

    
    