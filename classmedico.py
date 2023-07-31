from classpaciente import *
class Medico:
    def __init__(self):
        self.consultar_citas = []
        
    def consultar_citas(self, cita):
        self.consultar_citas.append(cita)
    
    def consultar_citas(self):
            print("Citas consultadas:")
            for cita in self.consultar_citas:
                print(cita)

       
