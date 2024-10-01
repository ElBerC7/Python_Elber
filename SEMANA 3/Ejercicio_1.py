def porcentaje(fraccion):
    try:
        # Dividimos la entrada X/Y
        x, y = fraccion.split('/')
        x = int(x)
        y = int(y)
        
        # Validamos las condiciones
        if y == 0:
            raise ZeroDivisionError("Y debe ser diferente de 0")
        if x > y:
            raise ValueError("X debe ser menor o igual a Y")
                
        # Calculamos el porcentaje
        porcentaje = (x / y) * 100
        
        # Casos especiales: E y F
        if porcentaje <= 1:
            return 'E'
        elif porcentaje >= 99:
            return 'F'
        else:
            return f"{round(porcentaje)}%"
    except ValueError:
        print("Error: Ingrese una fracción válida con números enteros.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    return None

if __name__ == "__main__":
    while True:
        fraccion = input("Ingrese una fracción (X/Y): ")
        result = porcentaje(fraccion)
        if result:
            print("Resultado:", result)
            break