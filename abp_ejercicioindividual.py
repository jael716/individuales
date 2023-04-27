class Ninja(Personaje):
    def __init__(self, nombre, aldea, rango):
        self.nombre = nombre
        self.aldea = aldea
        self.rango = rango

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo}")

    def defender(self):
        print(f"{self.nombre} se defiende")

    def realizar_mision(self, mision):
        print(f"{self.nombre} realiza la misión: {mision}")

class Maestro(Personaje):
    def __init__(self, nombre, especialidad, alumnos):
        self.nombre = nombre
        self.especialidad = especialidad
        self.alumnos = alumnos

    def entrenar_alumnos(self):
        print(f"{self.nombre} entrena a sus alumnos en {self.especialidad}")

    def mejorar_especialidad(self):
        print(f"{self.nombre} mejora su especialidad en {self.especialidad}")

    def liderar_equipo(self, mision):
        print(f"{self.nombre} lidera al equipo en la misión: {mision}")

class Villano(Personaje):
    def __init__(self, nombre, organizacion, poder):
        self.nombre = nombre
        self.organizacion = organizacion
        self.poder = poder

    def atacar_aldea(self, aldea):
        print(f"{self.nombre} ataca la aldea {aldea}")

    def reclutar_miembros(self, miembro):
        print(f"{self.nombre} recluta a {miembro} en la organización {self.organizacion}")

    def incrementar_poder(self):
        print(f"{self.nombre} incrementa su poder")