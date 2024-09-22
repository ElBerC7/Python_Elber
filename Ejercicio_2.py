# Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que porcentaje de propina desea dejar al mesero.
# Su programa debe devolver la cantidad de dinero a dejar como propina.

consumo = float(input("¿Cuánto fue su consumo en el restaurante? "))
porcentaje = float(input("¿Qué porcentaje de propina desea dejar? "))
propina = consumo * (porcentaje / 100)
print(f"La propina es: {propina} soles")