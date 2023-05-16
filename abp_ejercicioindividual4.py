class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice hola")

class Ninja(Persona):
    def __init__(self, nombre, aldea, rango):
        super().__init__(nombre)
        self.aldea = aldea
        self.rango = rango

    def atacar(self, objetivo):
        print(f"{self.nombre} ataca a {objetivo}")

class Maestro(Persona):
    def __init__(self, nombre, especialidad, alumnos):
        super().__init__(nombre)
        self.especialidad = especialidad
        self.alumnos = alumnos

    def entrenar_alumnos(self):
        print(f"{self.nombre} entrena a sus alumnos en {self.especialidad}")

class Traidor(Ninja):
    def __init__(self,nombre,aldea,mision_exitosa,mision_fallida=None):
        super().__init__(nombre, aldea, "Traidor")
        self.mision_exitosa=mision_exitosa
        self.mision_fallida=mision_fallida

    def infiltrarse(self,espia_aldea):
        self.aldea=espia_aldea
        print(f"{self.nombre} se a inflitrado en {espia_aldea}")

class Villano(Traidor):
    def __init__(self, nombre, organizacion, poder):
        super().__init__(nombre, organizacion, True)
        self.poder = poder

    def atacar_aldea(self, aldea):
        print(f"{self.nombre} ataca la aldea {aldea}")

    # Sobrescribimos el método atacar
    def atacar(self, objetivo):
        print(f"{self.nombre} ataca ferozmente a {objetivo}")

# Crear objetos y probar métodos
ninja1 = Ninja("Naruto", "Konoha", "Genin")
ninja1.hablar()
ninja1.atacar("Enemigo")

maestro1 = Maestro("Kakashi", "Sharingan", ["Naruto", "Sakura", "Sasuke"])
maestro1.hablar()
maestro1.entrenar_alumnos()

traidor1 = Traidor("Sasuke", "Konoha", True)
traidor1.hablar()
traidor1.atacar("Naruto")
traidor1.infiltrarse("Otogakure")

villano1 = Villano("Orochimaru", "Akatsuki", 9000)
villano1.hablar()
villano1.atacar("Jiraiya") # Este método está sobrescrito
villano1.atacar_aldea("Konoha")