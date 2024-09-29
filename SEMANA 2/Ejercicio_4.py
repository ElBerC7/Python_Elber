# Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
# pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus materias.

alumnos = []

n = int(input("¿Cuántos alumnos desea ingresar?: "))

for i in range(n):
    alumno = {}
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = []

    for j in range(3):
        nota = int(input(f"Ingrese la calificación {j+1} del alumno {nombre}: "))
        notas.append(nota)

    alumno["Alumno"] = nombre
    alumno["Notas"] = notas
    
    alumnos.append(alumno)

print("\nListado completo de alumnos y sus calificaciones:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']},\n Notas: {alumno['Notas']}\n")