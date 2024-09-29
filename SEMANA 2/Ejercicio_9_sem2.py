# Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
# texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o minúsculas.

def eliminar_vocales(cadena):
    vocales = "aeiouAEIOU"
    return ''.join([letra for letra in cadena if letra not in vocales])

entrada = input("Ingresa un pequeño texto: ")
salida = eliminar_vocales(entrada)
print(salida)