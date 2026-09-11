from src.pacientes import Paciente

def test_crear_paciente():
    p = Paciente("Juan Pérez", 34)
    assert p.nombre == "Juan Pérez"
    assert p.historial == []

def test_agregar_consulta():
    p = Paciente("Ana Gómez", 28)
    p.agregar_consulta("Consulta general")
    assert len(p.historial) == 1