# Programa que lee un número y dice si es primo.

if num == 1:
    print("El número 1 no es primo.")
else:
    for i in range(2, num):
        if num % i == 0:
            print("El número no es primo.")