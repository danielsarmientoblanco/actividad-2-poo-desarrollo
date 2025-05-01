class Persona:
    def __init__(self, nombre, apellidos, numeroDocumentoIdentidad, añoNacimiento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numeroDocumentoIdentidad = numeroDocumentoIdentidad
        self.añoN= añoNacimiento        
        
    def MostrarDatos(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Número de documento de identidad = {self.numeroDocumentoIdentidad}")
        print(f"Año de nacimiento = {self.añoNacimiento}")
        print()
        
persona1 = Persona("Pedro", "Pérez", "1053121010", 1998)
persona2 = Persona("Luis", "León", "1053223344", 2001)
persona1.MostrarDatos()
persona2.MostrarDatos()
