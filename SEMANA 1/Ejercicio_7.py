# Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:----
# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de introducir una opción inválida, el programa informará de que no es correcta.

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

print("Operaciones:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")

opcion = int(input("Ingrese el número de la operación a realizar: "))

if opcion == 1:
    print(f"La suma es: {numero_1 + numero_2}")
elif opcion == 2:
    print(f"La resta es: {numero_1 - numero_2}")
elif opcion == 3:
    print(f"El producto es: {numero_1 * numero_2}")
else:
    print("Opción no válida")