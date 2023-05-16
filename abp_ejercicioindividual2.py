class Ninja():
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

class Maestro():
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

class Villano():
    def __init__(self, nombre, organizacion, poder):
        self.nombre = nombre
        self.organizacion = organizacion
        self.poder = poder

    def atacar_aldea(self, aldea):
        print(f"{self.nombre} ataca la aldea {aldea}")

    def reclutar_miembros(self, miembro):
        print(f"{self.nombre} recluta a {miembro} en la organización {self.organizacion}")

    def incrementar_poder(self,aumento):
        print(f"{self.nombre} incrementa su poder a {aumento+self.poder}")

class Traidor():
    def __init__(self,nombre,aldea,mision_exitosa,mision_fallida=None):
        self.nombre=nombre
        self.aldea=aldea
        self.mision_exitosa=mision_exitosa
        self.mision_fallida=mision_fallida

    def actualizar_misiones(self,exitosas,fallidas):
        self.mision_exitosa+=exitosas
        self.mision_fallida+=fallidas
    
    def infiltrarse(self,espia_aldea):
        self.aldea=espia_aldea
        print(f"{self.nombre} se a inflitrado en {espia_aldea}")
    
    
    def cambio_bando(self, cambia):
        if cambia:
            print("cambio de bando")

tomas=Villano("Pain","akatsuki",8000)
tomas.reclutar_miembros("sasuke")
tomas.incrementar_poder(500)
pedro=Traidor("pedro","Arena",True)
pedro.cambio_bando(True)
