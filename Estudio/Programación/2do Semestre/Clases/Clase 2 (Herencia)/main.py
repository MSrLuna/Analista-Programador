from Persona import persona

class profesor(persona):
    def __init__(self):
        self.contrato = None

class alumno(persona):
    def __init__(self):
        self.beca: None
        self.carrera = None