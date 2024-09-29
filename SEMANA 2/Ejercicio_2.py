# Escriba un programa en Python para construir el siguiente patrón.

n = 5  

# Patrón ascendente
for i in range(1, n + 1):
    print('* ' * i)

# Patrón descendente
for i in range(n - 1, 0, -1):
    print('* ' * i)