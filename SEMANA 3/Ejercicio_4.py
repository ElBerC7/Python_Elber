class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def calcular_area(self):
        return self.largo * self.ancho

class Cuadrado(Rectangulo):
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == "__main__":
    try:
        largo_rect = float(input("Ingrese el largo del rectángulo: "))
        ancho_rect = float(input("Ingrese el ancho del rectángulo: "))
        
        lado_cuad = float(input("Ingrese el lado del cuadrado: "))
        
        rectangulo = Rectangulo(largo_rect, ancho_rect)   
        cuadrado = Cuadrado(lado_cuad)
        
        print(f"El área del rectángulo es: {rectangulo.calcular_area():.2f}")
        print(f"El área del cuadrado es: {cuadrado.calcular_area():.2f}")
    
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")