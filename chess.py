import math

a= int(input("a-> "))
b= int(input("b-> "))
c= int(input("c-> "))

print(f"la ecuacion es {a}*x^2 + {b}x + {c}") 

x1 = ((-1*b) + math.sqrt(pow(b,2) - 4*a*c))/(2*a)
x2 = ((-1*b) - math.sqrt(pow(b,2) - 4*a*c))/(2*a)

print(f"Los ceros son {x1} y {x2}")