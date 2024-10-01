import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        return math.pi * (self.radio ** 2)

if __name__ == "__main__":
    try:
        radio1 = float(input("Ingrese el radio del primer círculo: "))
        radio2 = float(input("Ingrese el radio del segundo círculo: "))
        
        circulo1 = Circulo(radio1)
        circulo2 = Circulo(radio2)
        
        print(f"El área del círculo con radio {circulo1.radio} es: {circulo1.calcular_area():.2f}")
        print(f"El área del círculo con radio {circulo2.radio} es: {circulo2.calcular_area():.2f}")
    
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el radio.")