# Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
# ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos números.
# Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
# números pares e impares.

# Programa en Python para contar números pares e impares ingresados por el usuario

pares = 0
impares = 0
numeros_ingresados = []

while True:
    desea_ingresar = input("¿Desea ingresar un número? (SI/NO): ").upper()
    if desea_ingresar == 'NO':
        break
    
    numero = int(input("Ingrese el número: "))
    numeros_ingresados.append(numero)
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar resultados
print("\nNúmeros ingresados:", numeros_ingresados)
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)