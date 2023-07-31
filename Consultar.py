
import random
from classmedico import *
from classpaciente import *
from classhorario import *
from classconsultorio import *


def mostrar_menu():
    print("Menu")
    print("1. Nombre y contraseña")
    print("2. Agendar día")
    print("3. Consultorio")
    print("4. Salir")

c=True
while c:
    mostrar_menu()
    opcion = input("Ingrese el número de opción: ")

    if opcion =="1":
        nombre = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa unacontraseña: ")
        
    elif opcion == "2":
        dia = input("Ingrese el día de la semana: ")
    
    elif opcion =="3":
        opcion = int(input("Ingrese el número del consultorio: "))
        Consultorio = ["55", "88", "87", "41", "57"]
        
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")




