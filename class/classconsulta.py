class Consulta:
    
    def __init__(self, paciente, medico, horario, consultorio):
        self.paciente = paciente
        self.medico = medico
        self.horaio = horario
        self.consultorio = consultorio
        
    def setpaciente(self,paciente):
        self.__paciente = paciente
    def getpaciente(self):
        return self.__paciente
    
    def setmedico(self,medico):
        self.__medico=medico
    def getmedico(self):
        return self.__medico
    
    def sethorario(self,horario):
        self.__horario = horario
    def gethorario(self):
        return self.__horario
    def setconsultorio(self,consultorio):
        self.__consultorio=consultorio
    def getconsultorio(self):
        return self.__consultorio


