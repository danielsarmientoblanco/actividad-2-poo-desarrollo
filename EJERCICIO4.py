import math 

pi = math.pi

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcularArea(self):
        return pi*((self.radio)**2)
    
    def calcularPerimetro(self):
        return 2*pi*(self.radio)
    

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return float(self.base*self.altura)
    
    def calcularPerimetro(self):
        return float((2*self.base)+(2*self.altura))
    


class Cuadrado:
    def __init__(self, lado):
        self.lado = lado
    
    def calcularArea(self):
        return float((self.lado)*(self.lado))
    
    def calcularPerimetro(self):
        return float((4*self.lado))


class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return float(self.base*self.altura*0.5)
    
    def calcularHipotenusa(self):
        return float(((((self.base)**2)+((self.altura)**2))**(0.5)))
    
    def calcularPerimetro(self):
        return float((self.base + self.altura + self.calcularHipotenusa()))
    
    def determinarTipoTriangulo(self):
        if (self.base == self.altura and (self.base == self.calcularHipotenusa()) and (self.altura == self.calcularHipotenusa())):
            print("Es un triángulo equilátero")
        
        elif (self.base != self.altura and (self.base!= self.calcularHipotenusa()) and (self.altura != self.calcularHipotenusa())):
            print("Es un triángulo escaleno")
        
        else:
            print("Es un triángulo isósceles")

class PruebaFiguras:
    @staticmethod
    def main():
        fig1 = Circulo(2)
        fig2 = Rectangulo(1, 2)
        fig3 = Cuadrado(3)
        fig4 = TrianguloRectangulo(3, 5)
        
        print(f"El área del círculo es = {fig1.calcularArea()}")
        print(f"El perímetro del círculo es = {fig1.calcularPerimetro()}")
        print()
        print(f"El área del rectángulo es = {fig2.calcularArea()}")
        print(f"El perímetro del rectángulo es = {fig2.calcularPerimetro()}")
        print()
        print(f"El área del cuadrado es = {fig3.calcularArea()}")
        print(f"El perímetro del cuadrado es = {fig3.calcularPerimetro()}")
        print()
        print(f"El área del triángulo es = {fig4.calcularArea()}")
        print(f"El perímetro del triángulo es = {fig4.calcularPerimetro()}")
        
        fig4.determinarTipoTriangulo()


if __name__ == "__main__":
    PruebaFiguras.main()
    
    
