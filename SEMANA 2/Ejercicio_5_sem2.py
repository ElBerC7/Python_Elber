# Escribe un programa que encuentre la suma de todos los números primos menores que 100.

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def suma_primos_menores(limite):
    suma = 0
    for num in range(2, limite):
        if es_primo(num):
            suma += num
    return suma

limite = 100
resultado = suma_primos_menores(limite)
print(resultado)