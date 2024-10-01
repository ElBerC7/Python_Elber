def obtener(notas):
    try:
        vect = [round(float(grade.strip())) for grade in notas.split(',')]
        return vect
    except ValueError:
        print("Error: Asegúrese de ingresar números válidos en formato decimal, separados por comas.")
        return None

if __name__ == "__main__":
    while True:
        notas = input("Ingrese las calificaciones en decimal separadas por comas: ")
        salida = obtener(notas)
        if salida is not None:
            print("Lista de calificaciones redondeadas:", salida)
            break