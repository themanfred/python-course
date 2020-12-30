'''
Input
The first line of input contains a single integer number N (1 ≤ N ≤ 105
), representing the number
of boxes in the machine. The second and last line contains N integer numbers separated by a space,
where the i − th number represents the value Bi (1 ≤ Bi ≤ 106
) drawn in the box sitting on the i − th
position of the machine.
Output
Print a single line with a single integer, representing the minimum numb
'''
import sys

n = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().strip().split()))
change=0
array2 = sorted(array.copy())

for i in range(n):
    minimum = i
    for j in range(i+1, n):
        if (array[j] < array[minimum]):
            minimum = j
    if array2 == array:
        break
    arrayTemporal = array.copy()
    temp = array[i]
    array[i] = array[minimum]
    array[minimum] = temp
    print(array)
    
    if arrayTemporal != array:
        change +=1
        print(f'change is {change}')
    

sys.stdout.write(str(change) + '\n')