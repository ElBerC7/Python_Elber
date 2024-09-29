# Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de archivo MIME correspondiente. 
# Si el nombre del archivo termina en cualquiera de estos sufijos (sin importar el uso de mayúsculas y minúsculas) :------
#.gif
#.jpg
#.jpeg
#.png
#.pdf
#.txt
#.zip
# Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene ningún sufijo, en su lugar su 
# programa deberá devolver application/octet-stream.

nombre_archivo = input("Ingrese el nombre del archivo: ").lower()

tipos_mime = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

for sufijo, mime in tipos_mime.items():
    if nombre_archivo.endswith(sufijo):
        break
else:
    mime = "application/octet-stream"

print(f"El tipo MIME es: {mime}")