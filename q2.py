A = [[1,2,3],
    [11,22,33],
    [2,3,9]]

B = [[7,0,1],[1,2,3],[4,0,8]]

resultado = [
 [0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]
 ]
def mulAxB():
    global A,B, resultado
    print(f'La matriz A xB:')
    lenA= len(A)
    for i in range(lenA):
     lensubA = len(A[i])
     for j in range(lensubA):
         resultado[i][j] = A[i][j] *B[i][j]
         print(f'|{resultado[i][j]}|',end='')
     print('')
     
def mulAmasB():
    global A,B, resultado
    print(f'La matriz A +B:')
    lenA= len(A)
    for i in range(lenA):
     lensubA = len(A[i])
     for j in range(lensubA):
         resultado[i][j] = A[i][j] +B[i][j]
         print(f'|{resultado[i][j]}|', end='')
     print('')
mulAxB()
mulAmasB()