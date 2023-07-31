from usuario import*
from classmedico import *

class Paciente(usuario):
    def __init__(self, nombre, password, consultar_citas):
        usuario.__init__(self, nombre, password, consultar_citas)
        self.__consultar_citas = []
        Paciente.paciente.append(self)
    
    
    def setconsultar_citas(self,consultar_citas):
        self.__consultar_citas = consultar_citas
    def getnombre(self):
        return self.__consultar_citas
        
    def consultar_citas(self):
        for cita in self.consultar_citas:
            print(f"Paciente: {cita['paciente']}")
            print(f"horario de la cita: {cita['fecha']} {cita['hora']}")
            print("-" * 30)
            return 