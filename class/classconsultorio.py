
def Consultorio(self, Consultorio):
        Consultorio = ["55", "88", "87", "41", "57"]
        print("Consultorios disponibles:")
        contador=1
        for Consul in Consultorio:
            print(f"{contador}. {Consul}")   
            contador+=1
        continuar=True
        while continuar :
            print("") 
            opcion = int(input("Ingrese el número del consultorio: "))
            # Verificamos si el número de opción es válido
            if opcion >= 1 and opcion <= len(Consultorio):
                Consultorio_elegido = Consultorio[opcion-1]
                print(f"Ha seleccionado el Consultorio numero: {Consultorio_elegido }.")
                return True
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")
                return None
            break
       

   
