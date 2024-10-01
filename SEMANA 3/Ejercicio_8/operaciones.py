# operaciones.py

def suma(a, b):
    try:
        return a + b
    except TypeError:
        return "Error: Tipo de dato no válido para suma."

def resta(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Tipo de dato no válido para resta."

def multiplicacion(a, b):
    try:
        return a * b
    except TypeError:
        return "Error: Tipo de dato no válido para multiplicación."

def division(a, b):
    try:
        if b == 0:
            return "Error: No es posible dividir entre cero."
        return a / b
    except TypeError:
        return "Error: Tipo de dato no válido para división."