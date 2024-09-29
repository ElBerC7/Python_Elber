# Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
# en el rango de 1500 y 2700 (ambos incluidos).

result = []

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        result.append(i)

print(result)