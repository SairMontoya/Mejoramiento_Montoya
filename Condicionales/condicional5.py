#Programa que lee una edad y dice si la persona es mayor de edad.

def edad():
    edad = int(input("Introduce tu edad: "))
    if edad >= 18:
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
edad()