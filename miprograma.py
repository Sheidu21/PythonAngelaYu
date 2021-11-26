# mi primer programa de Python

# import complex math module
import cmath
# nombre = input("¿Cómo se llama? ")
a = input("Escrfibe el coeficiente quadratico ")
b = input("Escrfibe el coeficiente lineal")
c = input("Escrfibe el coeficiente constante ")

a = int(a)
b = int(b)
c = int(c)

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))