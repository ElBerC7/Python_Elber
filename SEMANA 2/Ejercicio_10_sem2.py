# Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como 8/9/1636 o Septiembre 8, 1636

def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto",
        "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    
    # Caso: fecha en formato numérico MM/DD/AAAA
    if '/' in fecha:
        mes, dia, año = fecha.split('/')
        return f"{año}-{int(mes):02}-{int(dia):02}"

    # Caso: fecha en formato de texto como 'Septiembre 8, 1636'
    else:
        fecha = fecha.replace(',', '')
        mes_palabra, dia, año = fecha.split(' ')
        mes_numero = meses.index(mes_palabra) + 1  # mes a su valor numérico
        return f"{año}-{mes_numero:02}-{int(dia):02}"

fecha_usuario = input("Ingrese la fecha (en formato MM/DD/AAAA o 'Mes Día, Año'): ")

resultado = convertir_fecha(fecha_usuario)
print(f"Fecha en formato AAAA-MM-DD: {resultado}")