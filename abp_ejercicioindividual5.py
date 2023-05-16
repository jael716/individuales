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
        try:
            print(f"{self.nombre} ataca a {objetivo}")
        except TypeError as e:
            print(f"Error de tipo: {e}. Por favor, asegúrate de que el objetivo es una cadena de texto.")
        finally:
            print("Final del manejo de error de tipo en atacar.")

class Maestro(Persona):
    def __init__(self, nombre, especialidad, alumnos):
        super().__init__(nombre)
        self.especialidad = especialidad
        self.alumnos = alumnos

    def entrenar_alumnos(self):
        try:
            print(f"{self.nombre} entrena a sus alumnos en {self.especialidad}")
        except IndexError as e:
            print(f"Error de índice: {e}. Por favor, asegúrate de que todos los alumnos existen.")
        finally:
            print("Final del manejo de error de índice en entrenar_alumnos.")

class Traidor(Ninja):
    def __init__(self,nombre,aldea,mision_exitosa,mision_fallida=None):
        super().__init__(nombre, aldea, "Traidor")
        self.mision_exitosa=mision_exitosa
        self.mision_fallida=mision_fallida

    def infiltrarse(self,espia_aldea):
        try:
            self.aldea=espia_aldea
            print(f"{self.nombre} se a inflitrado en {espia_aldea}")
        except KeyError as e:
            print(f"Error de clave: {e}. Por favor, asegúrate de que la aldea existe.")
        finally:
            print("Final del manejo de error de clave en infiltrarse.")

class Villano(Traidor):
    def __init__(self, nombre, organizacion, poder):
        super().__init__(nombre, organizacion, True)
        self.poder = poder

    def atacar_aldea(self, aldea):
        try:
            print(f"{self.nombre} ataca la aldea {aldea}")
        except ValueError as e:
            print(f"Error de valor: {e}. Por favor, asegúrate de que la aldea es una cadena de texto válida.")
        finally:
            print("Final del manejo de error de valor en atacar_aldea.")

    # Sobrescribimos el método atacar
    def atacar(self, objetivo):
        try:
            print(f"{self.nombre} ataca ferozmente a {objetivo}")
        except ZeroDivisionError as e:
            print(f"Error de división por cero: {e}. Por favor, no intentes dividir por cero.")
        finally:
            print("Final del manejo de error de división por cero en atacar.")
# Crear objetos y probar métodos
ninja1 = Ninja("Naruto", "Konoha", "Genin")
ninja1.hablar()
ninja1.atacar(1234)  # Este debería causar un error de tipo

maestro1 = Maestro("Kakashi", "Sharingan", ["Naruto", "Sakura", "Sasuke"])
maestro1.hablar()
maestro1.entrenar_alumnos()

traidor1 = Traidor("Sasuke", "Konoha", True)
traidor1.hablar()
traidor1.atacar("Naruto")
traidor1.infiltrarse({"aldea": "Otogakure"})  # Este debería causar un error de clave

villano1 = Villano("Orochimaru", "Akatsuki", 9000)
villano1.hablar()
villano1.atacar("Jiraiya") 
villano1.atacar_aldea(999)  # Este debería causar un error de valor

