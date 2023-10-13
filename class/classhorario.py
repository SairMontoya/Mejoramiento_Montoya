class Horario:
    def __init__(self):
        self.horario = {}
        self.dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def agregar_horario_disponible(self, dia_semana):
        dia_semana = dia_semana.append()
        if dia_semana not in self.dias_semana:
            print("Error: Día de la semana inválido.")
            return
        if dia_semana not in self.horario:
            self.horario[dia_semana] = []

        self.horario[dia_semana].append

