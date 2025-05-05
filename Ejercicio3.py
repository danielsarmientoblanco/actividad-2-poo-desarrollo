from enum import Enum

class TipoCombustible(Enum):
    gasolina = "Gasolina"
    diesel = "Diésel"

class TipoAutomovil(Enum):
    compacto = "Compacto"
    SUV = "SUV"

class Color(Enum):
    negro = "negro"
    azul = "azul"

class Automovil:
    def __init__(self, marca, modelo, motor, combustible, tipo, puertas, asientos, vmax, color,vactual):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.combustible = combustible
        self.tipo = tipo
        self.puertas = puertas
        self.asientos = asientos
        self.vmax = vmax
        self.color = color
        self.vactual = vactual

    def getMarca(self): return self.marca #Llama valores encapsulados 
    def getVelocidadActual(self): return self.vactual 

    def setVelocidadMaxima(self, vmax): self.vmax = vmax #Cambia valores en el encapsulado 


    def acelerar(self, inc):
        if inc < 0 or self.vactual + inc > self.vmax:
            print("No se puede acelerar.")
        else:
            self.vactual += inc
        print(f"Velocidad actual: {self.vactual} km/h")
    def desacelerar(self, dec):
        if dec < 0 or self.vactual - dec < 0:
            print("No se puede desacelerar.")
        else:
            self.vactual -= dec
        print(f"Velocidad actual: {self.vactual} km/h")
    def frenar(self):
        self.vactual = 0
        print("Vehículo frenado.")
    
    def calcular_tiempo_llegada(self, distancia):
        if self.vactual == 0:
            print("Velocidad actual es cero.")
        else:
            tiempo = distancia / self.vactual
            print(f"Tiempo estimado: {tiempo} h")
    def imprime_datos(self):
        print(f'Marca: {self.marca}-{self.modelo}\nMotor: {self.motor}L\nCombustible:{self.combustible.value}\nTipo: {self.tipo.value}\nPuestas: {self.puertas}\nAsientos: {self.asientos}\nVel. Máx: {self.vmax} km/h\nColor: {self.color.value}\nVelocidad actual: {self.vactual}km/h')
def main():
    auto = Automovil("Toyota", 2018, 1.5 , TipoCombustible.gasolina, TipoAutomovil.SUV, 4, 5, 260, Color.negro,100)
    auto.imprime_datos()
    auto.acelerar(20)
    auto.desacelerar(50)
    auto.frenar()


if __name__ == "__main__":
    main()

