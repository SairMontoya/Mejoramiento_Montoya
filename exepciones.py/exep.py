[6:01 p. m., 18/7/2023] Danielaxde:     try:
        # Calcula el discriminante
        discriminante = b**2 - 4*a*c
        
        # Comprueba si el discriminante es negativo
        if discriminante < 0:
            raise ValueError("El discriminante es negativo, la función cuadrática no tiene soluciones reales.")
        
        # Calcula las soluciones
        x1 = (-b + discriminante**0.5) / (2*a)
        x2 = (-b - discriminante**0.5) / (2*a)
        
        return x1, x2
    
    except ValueError as error:
        print("Error:", str(error))


# Ejemplo de uso
a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

soluciones = calcular_funcion_cuadratica(a, b, c)
if soluciones:
    print("Las soluciones son:", soluciones)
[6:01 p. m., 18/7/2023] Danielaxde: Y este es el segundo
[6:01 p. m., 18/7/2023] Danielaxde: def calcular_funcion_cuadratica(a, b, c):
    assert isinstance(a, (int, float)), "El coeficiente 'a' debe ser un número."
    assert isinstance(b, (int, float)), "El coeficiente 'b' debe ser un número."
    assert isinstance(c, (int, float)), "El coeficiente 'c' debe ser un número."
    
    # Calcula el discriminante
    discriminante = b**2 - 4*a*c
    
    # Comprueba si el discriminante es negativo
    assert discriminante >= 0, "El discriminante es negativo, la función cuadrática no tiene soluciones reales."
    
    # Calcula las soluciones
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    
    return x1, x2


# Ejemplo de uso
a = float(input("Ingresa el coeficiente a: "))
b = float(input("Ingresa el coeficiente b: "))
c = float(input("Ingresa el coeficiente c: "))

try:
    soluciones = calcular_funcion_cuadratica(a, b, c)
    print("Las soluciones son:", soluciones)
except AssertionError as error:
    print("Error:", str(error))