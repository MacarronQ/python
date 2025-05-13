# Paso 1: Pedimos los coeficientes
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

# Paso 2: Verificamos que a no sea cero
if a == 0:
    print("No es una ecuación de segundo grado porque a = 0.")
else:
    # Paso 3: Calculamos el discriminante
    D = b**2 - 4*a*c
    print(f"El discriminante es: {D}")

    # Paso 4: Analizamos los casos
    if D > 0:
        # Raíces reales diferentes
        raizD = D**0.5  # usamos ** en lugar de math.sqrt
        x1 = (-b + raizD) / (2*a)
        x2 = (-b - raizD) / (2*a)
        print("La ecuación tiene dos raíces reales y diferentes:")
        print("x1 =", x1)
        print("x2 =", x2)

    elif D == 0:
        # Raíz doble
        x = -b / (2*a)
        print("La ecuación tiene una raíz real doble:")
        print("x =", x)

    else:
        # Raíces complejas (no reales)
        parte_real = -b / (2*a)
        parte_imaginaria = (-D)**0.5 / (2*a)
        print("La ecuación tiene dos raíces complejas:")
        print("x1 =", parte_real, "+", parte_imaginaria, "i")
        print("x2 =", parte_real, "-", parte_imaginaria, "i")


        