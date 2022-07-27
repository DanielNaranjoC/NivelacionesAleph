# Ecuación ax + b = c, x = (c - b) / a

a = float(input("Ingrese el valor de a: "))
if a != 0:
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    x = (c - b) / a
    print("x=", x)
else:
    print("a es igual a cero, no es una ecuación.")

