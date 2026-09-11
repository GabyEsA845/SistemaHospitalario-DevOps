from datetime import date

class Consulta:
    def __init__(self, paciente, medico, motivo, fecha=None):
        self.paciente = paciente
        self.medico = medico
        self.motivo = motivo
        self.fecha = fecha or date.today()

    def __repr__(self):
        return f"Consulta({self.paciente} con {self.medico}, {self.fecha})"