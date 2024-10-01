class Punto:
    def __init__(self, x=0, y=0):
        # Inicializamos las coordenadas x e y, con valores por defecto 0
        self.x = x
        self.y = y
    
    def mover(self, nueva_x, nueva_y):
        # Método para mover el punto a nuevas coordenadas
        self.x = nueva_x
        self.y = nueva_y
    
    def mostrar(self):
        # Método para mostrar las coordenadas actuales del punto
        print(f"Punto en coordenadas ({self.x}, {self.y})")
    
    def calcular_distancia(self, otro_punto):
        # Método para calcular la distancia entre el punto actual y otro punto
        distancia = ((self.x - otro_punto.x)**2 + (self.y - otro_punto.y)**2)**0.5
        return distancia

def ingresar_coordenadas():
    # Función para pedir coordenadas por teclado
    try:
        x = float(input("Ingrese la coordenada x: "))
        y = float(input("Ingrese la coordenada y: "))
        return Punto(x, y)
    except ValueError:
        print("Error: Ingrese valores numéricos válidos para las coordenadas.")
        return ingresar_coordenadas()  # Vuelve a pedir las coordenadas si hay error

if __name__ == "__main__":
    # Ingresar el primer punto por teclado
    print("Ingrese las coordenadas del primer punto:")
    punto1 = ingresar_coordenadas()
    
    # Ingresar el segundo punto por teclado
    print("\nIngrese las coordenadas del segundo punto:")
    punto2 = ingresar_coordenadas()
    
    # Mostrar la posición inicial de ambos puntos
    print("\nPosiciones iniciales de los puntos:")
    punto1.mostrar()
    punto2.mostrar()
    
    # Calcular la distancia entre los dos puntos
    distancia = punto1.calcular_distancia(punto2)
    print(f"\nLa distancia entre los dos puntos es: {distancia:.2f}")
    
    # Mover el primer punto a nuevas coordenadas ingresadas por el usuario
    print("\nIngrese nuevas coordenadas para mover el primer punto:")
    nueva_x = float(input("Ingrese la nueva coordenada x: "))
    nueva_y = float(input("Ingrese la nueva coordenada y: "))
    punto1.mover(nueva_x, nueva_y)
    
    print("\nDespués de mover el primer punto:")
    punto1.mostrar()