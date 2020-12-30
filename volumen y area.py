#El área y volumen de una esfera se calcula con las siguientes fórmulas:
#área =  LaTeX: 4\pi r^24 π r 2
#volumen = LaTeX: \frac{4\pi r^3}{3}4 π r 3 3
#Escribe un programa que pida el valor del radio y muestre su área y su volumen.

print("Digita el radio del ciculo")

r=int(input())
pi =3.14

vol= (4*pi*pow(r,3))/3
area = 3*pi*pow(r,2)

print("El volumen es ", vol, " y el area es ", area)
