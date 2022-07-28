# ax^2 + bx + c = 0

a = float(input('Ingrese a: '))
b = float(input('Ingrese b: '))
c = float(input('Ingrese c: '))

d = b**2 - 4*a*c
# x1 = (-b + raiz(d)) / (2 a)
# x2 = (-b - raiz(d)) / (2 a)

if a == 0:
    if b != 0:
        print('La ecuación tiene una solución en los reales')
    else:
        print('No es una ecuación')
elif d == 0:
    print('La ecuación tiene una solución en los reales')
elif d > 0:
    print('La ecuación tiene dos soluciones en los reales')
else:
    print('La ecuación tiene dos soluciones en los complejos')

