'''

'''
n = int(input(' Type a number: '))
while n!=1:
    if n%2==0:
        n/=2
        print(n, end=',')
    elif n%2!=0:
        n= (n*3)+1
        print(n, end=',')

