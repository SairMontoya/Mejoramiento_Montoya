# Programa que lee un numero y dice si es positivo o negativo

def numero():
    num = int(input("Introduce un número: "))
    if num > 0:
        print("El número es positivo.")
    else:
        print("El número es negativo.")
numero()