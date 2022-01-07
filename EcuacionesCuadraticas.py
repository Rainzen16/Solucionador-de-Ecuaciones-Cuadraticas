import EcuacionesCuadraticas

# Este codigo de mierda funciona como quiere

a = int(input("Cual es el valor de A?: "))
b = int(input("Cual es el valor de B?: "))
c = int(input("Cual es el valor de C?: "))

d = b ** 2 - 4 * a * c  # Discriminante

if d < 0:
    print("La ecuacion no tiene soluciones reales")
elif d == 0:
    x1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
    print("Esta ecuacion tiene una sola solucion: "), x1
else:
    x1 = ((-1 * b) + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    x2 = ((-1 * b) - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
    print("El valor de x1 es: " + str(x1))
    print("El valor de x2 es: " + str(x2))
