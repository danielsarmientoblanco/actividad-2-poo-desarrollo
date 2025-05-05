from enum import Enum

class tipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODISESEL"
    GAS_NATURAL = "GAS NATURAL"

class tipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"


class tipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"
    

class Automovil:
    def __init__(self, marca, modelo, motor, tipoCombustible, tipoAutomovil, numeroPuertas, cantidadAsientos, velocidadMax, color):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipoCombustible = tipoCombustible
        self.tipoAutomovil = tipoAutomovil
        self.numeroPuertas = numeroPuertas
        self.cantidadAsientos = cantidadAsientos
        self.velocidadMax = velocidadMax
        self.color = color
        self.velocidadActual = 0
    

    def getMarca(self):
        return self.marca
    
    def getModelo(self):
        return self.modelo

    def getMotor(self):
        return self.motor
    
    def getTipoCombustible(self):
        return self.tipoCombustible
    
    def getTipoAutomovil(self):
        return self.tipoAutomovil

    def getNumeroPuertas(self):
        return self.numeroPuertas

    def getCantidadAsientos(self):
        return self.cantidadAsientos
    
    def getVelocidadMax(self):
        return self.velocidadMax
    
    def getColor(self, color):
        self.color = color
    
    def getVelocidadActual(self):
        return self.velocidadActual


    def setMarca(self, marca):
        self.marca = marca
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def setMotor(self, motor):
        self.motor = motor
    
    def setTipoCombustible(self, tipoCombustible):
        self.tipoCombustible = tipoCombustible
    
    def setTipoAutomovil(self, tipoAutomovil):
        self.tipoAutomovil = tipoAutomovil

    def setNumeroPuertas(self, numeroPuertas):
        self.numeroPuertas = numeroPuertas

    def setCantidadAsientos(self, cantidadAsientos):
        self.cantidadAsientos = cantidadAsientos
    
    def setVelocidadMax(self, velocidaMax):
        self.velocidadMax = velocidaMax
    
    def setColor(self, color):
        self.color = color
    
    def setVelocidadActual(self, velocidadActual):
        self.velocidadActual = velocidadActual
    
    def acelerar(self, incrementoVelocidad):
        if (self.velocidadActual + incrementoVelocidad < self.velocidadMax):
            self.velocidadActual = self.velocidadActual + incrementoVelocidad
        else:
            print("No se puede incrementar a una velocidad superior a la máxima del automóvil")
    
    def desacelerar(self, decrementoVelocidad):
        if ((self.velocidadActual - decrementoVelocidad) > 0):
            self.velocidadActual = self.velocidadActual - decrementoVelocidad
        else:
            print("No se puede decrementar a una velocidad negativa.")
    
    def frenar(self):
        self.velocidadActual = 0
    
    def calcularTiempoLlegada(self, distancia):
        return distancia/self.velocidadActual

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipoCombustible.value}")
        print(f"Tipo de automóvil = {self.tipoAutomovil.value}")
        print(f"Número de puertas = {self.numeroPuertas}")
        print(f"Cantidad de asientos = {self.cantidadAsientos}")
        print(f"Velocidad máxima = {self.velocidadMax}")
        print(f"Color = {self.color.value}")

auto1 = Automovil("Ford", 2018, 3, tipoCom.DIESEL, tipoA.EJECUTIVO, 5, 6, 250, tipoColor.NEGRO)

auto1.imprimir()
auto1.setVelocidadActual(100)
print(f"Velocidad actual = {auto1.velocidadActual}")
auto1.acelerar(20)
print(f"Velocidad actual = {auto1.velocidadActual}")
auto1.desacelerar(50)
print(f"Velocidad actual = {auto1.velocidadActual}")
auto1.frenar()
print(f"Velocidad actual = {auto1.velocidadActual}")
auto1.desacelerar(20)
