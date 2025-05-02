from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = 'GASEOSO'
    TERRESTRE = 'TERRESTRE'
    ENANO = 'ENANO'

class Planeta:
    def __init__(self, nombre, cantidadSatélites, masa, volumen, diámetro, distanciaSol, tipoPlaneta, esObservable):
        self.nombre = nombre
        self.cantidadSatélites = cantidadSatélites
        self.masa = masa
        self.volumen = volumen
        self.diámetro = diámetro
        self.distanciaSol = distanciaSol
        self.tipoPlaneta = tipoPlaneta
        self.esObservable = esObservable
    
    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidadSatélites}")
        print(f"Masa del planeta = {self.masa:.4e} kg")
        print(f"Volumen del planeta = {self.volumen:.5e} km³")
        print(f"Diámetro del planeta = {self.diámetro} km")
        print(f"Distancia al sol = {self.distanciaSol} km")
        print(f"Tipo de planeta = {self.tipoPlaneta.value}")
        print(f"Es observable = {True if self.esObservable else False}")
    
    def calcularDensidad(self):
        return self.masa / self.volumen

    def esPlanetaExterior(self):
        límite = (149597870*3.4)
    
        if (self.distanciaSol>límite):
            return True
        else:
            return False
    # 
planeta1 = Planeta("Tierra", 1, 5.9736E24, 1.08321E12, 12742, 150000000, TipoPlaneta.TERRESTRE, True)
planeta1.imprimir()

print(f"Densidad del planeta = {planeta1.calcularDensidad():.15e} kg/km³")
print(f"Es planeta exterior = {True if planeta1.esPlanetaExterior() else False}")
print()

planeta2 = Planeta("Júpiter", 79, 1.899E27, 1.4313E15, 139820, 750000000, TipoPlaneta.GASEOSO, True)
planeta2.imprimir()

print(f"Densidad del planeta = {planeta2.calcularDensidad():.16e} kg/km³")
print(f"Es planeta exterior = {True if planeta2.esPlanetaExterior() else False}")
