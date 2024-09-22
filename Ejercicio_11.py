# Escriba un programa Python que se encargue de eliminar los elementos duplicados de la siguiente lista. Su programa debe retornar 
# otra lista sin los duplicados.
# Lista original: [1, 1, 2, 3, 4, 4, 5, 1]
# Lista procesada: [1, 2, 3, 4, 5]

lista_original = [1, 1, 2, 3, 4, 4, 5, 1]
lista_sin_duplicados = []

for elemento in lista_original:
    if elemento not in lista_sin_duplicados:
        lista_sin_duplicados.append(elemento)

print(lista_sin_duplicados)