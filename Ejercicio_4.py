# Escribir un programa que lea un entero positivo, N, introducido por el usuario y después muestre en pantalla la suma de todos los 
# enteros desde 1 hasta N. La suma de los N primeros enteros positivos puede ser calculada de la siguiente forma

numero = int(input("Ingresa un número entero positivo: "))
suma = (numero * (numero + 1)) / 2

print(f"La suma de los números desde el 1 hasta el {numero} es: {suma}")