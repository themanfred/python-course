import math
def trig():
    x=0
    for i in range(1,11):
        y = math.sin(x) + math.cos(x)
        print(y)
        x=x+.1
    
trig()
