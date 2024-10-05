import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return "El punto está sobre el origen"
        elif self.x == 0:
            return "El punto está sobre el eje Y"
        elif self.y == 0:
            return "El punto está sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "El punto está en el primer cuadrante"
        elif self.x < 0 and self.y > 0:
            return "El punto está en el segundo cuadrante"
        elif self.x < 0 and self.y < 0:
            return "El punto está en el tercer cuadrante"
        elif self.x > 0 and self.y < 0:
            return "El punto está en el cuarto cuadrante"

    def vector(self, otro_punto):
        return Punto(otro_punto.x - self.x, otro_punto.y - self.y)

    def distancia(self, otro_punto):
        return math.sqrt((otro_punto.x - self.x) ** 2 + (otro_punto.y - self.y) ** 2)

class Rectangulo:
    def __init__(self, punto_inicial=Punto(), punto_final=Punto()):
        self.punto_inicial = punto_inicial
        self.punto_final = punto_final

    def base(self):
        return abs(self.punto_final.x - self.punto_inicial.x)

    def altura(self):
        return abs(self.punto_final.y - self.punto_inicial.y)

    def area(self):
        return self.base() * self.altura()

# Función para ingresar las coordenadas de un punto
def ingresar_punto(nombre_punto):
    try:
        x = float(input(f"Ingrese la coordenada X del punto {nombre_punto}: "))
        y = float(input(f"Ingrese la coordenada Y del punto {nombre_punto}: "))
        return Punto(x, y)
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido.")
        return ingresar_punto(nombre_punto)

# Función para determinar qué punto está más lejos del origen
def mas_lejos_del_origen(punto1, punto2, punto3):
    origen = Punto(0, 0)
    distancia1 = punto1.distancia(origen)
    distancia2 = punto2.distancia(origen)
    distancia3 = punto3.distancia(origen)

    distancias = [(distancia1, "A"), (distancia2, "B"), (distancia3, "C")]
    max_distancia = max(distancias, key=lambda x: x[0])
    return max_distancia[1], max_distancia[0]

# Ejemplo de uso con entrada por teclado
if __name__ == "__main__":
    # Ingresar los puntos A, B, C y D
    A = ingresar_punto("A")
    B = ingresar_punto("B")
    C = ingresar_punto("C")
    D = ingresar_punto("D")

    # Imprimir los puntos
    print(f"\nPunto A: {A}")
    print(f"Punto B: {B}")
    print(f"Punto C: {C}")
    print(f"Punto D: {D}")

    # Consultar a qué cuadrante pertenecen los puntos A, C y D
    print(f"\nCuadrante de A: {A.cuadrante()}")
    print(f"Cuadrante de C: {C.cuadrante()}")
    print(f"Cuadrante de D: {D.cuadrante()}")

    # Consultar los vectores AB y BA
    vector_AB = A.vector(B)
    vector_BA = B.vector(A)
    print(f"\nVector AB: {vector_AB}")
    print(f"Vector BA: {vector_BA}")

    # Consultar la distancia entre los puntos A y B, y B y A
    distancia_AB = A.distancia(B)
    distancia_BA = B.distancia(A)
    print(f"\nDistancia entre A y B: {distancia_AB:.2f}")
    print(f"Distancia entre B y A: {distancia_BA:.2f}")

    # Determinar cuál de los puntos A, B o C se encuentra más lejos del origen
    punto_mas_lejos, distancia_mas_lejos = mas_lejos_del_origen(A, B, C)
    print(f"\nEl punto {punto_mas_lejos} está más lejos del origen con una distancia de {distancia_mas_lejos:.2f}")

    # Crear un rectángulo utilizando los puntos A y B
    rectangulo = Rectangulo(A, B)
    print(f"\nBase del rectángulo: {rectangulo.base()}")
    print(f"Altura del rectángulo: {rectangulo.altura()}")
    print(f"Área del rectángulo: {rectangulo.area()}")