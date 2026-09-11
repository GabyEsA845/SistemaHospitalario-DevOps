class Paciente:
    def __init__(self, nombre, edad, historial=None):
        self.nombre = nombre
        self.edad = edad
        self.historial = historial or []

    def agregar_consulta(self, consulta):
        self.historial.append(consulta)

    def __repr__(self):
        return f"Paciente({self.nombre}, {self.edad} años)"