# calculos.py
import operaciones

def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def ingresar_numeros():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        return a, b
    except ValueError:
        print("Error: Asegúrese de ingresar valores numéricos válidos.")
        return ingresar_numeros()  # Volver a solicitar los números si hay un error

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            a, b = ingresar_numeros()
            resultado = operaciones.suma(a, b)
            print(f"Resultado de la suma: {resultado}")
        
        elif opcion == "2":
            a, b = ingresar_numeros()
            resultado = operaciones.resta(a, b)
            print(f"Resultado de la resta: {resultado}")
        
        elif opcion == "3":
            a, b = ingresar_numeros()
            resultado = operaciones.multiplicacion(a, b)
            print(f"Resultado de la multiplicación: {resultado}")
        
        elif opcion == "4":
            a, b = ingresar_numeros()
            resultado = operaciones.division(a, b)
            print(f"Resultado de la división: {resultado}")
        
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")