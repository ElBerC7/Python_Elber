# gestion.py

from libro import Libro

class GestionBiblioteca:
    def __init__(self):
        # Inicializamos una lista vacía para almacenar los libros
        self.libros = []
    
    def agregar_libro(self, libro):
        # Agregar un libro a la lista
        self.libros.append(libro)
        print(f"Libro '{libro.titulo}' agregado con éxito.")
    
    def listar_libros(self):
        # Listar todos los libros de la biblioteca
        if not self.libros:
            print("No hay libros en la biblioteca.")
        else:
            print("\nLista de libros en la biblioteca:")
            for libro in self.libros:
                print(libro)
    
    def buscar_por_titulo(self, titulo):
        # Buscar libros por título
        libros_encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        if libros_encontrados:
            print(f"\nLibros encontrados con el título '{titulo}':")
            for libro in libros_encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros con el título '{titulo}'.")
    
    def buscar_por_autor(self, autor):
        # Buscar libros por autor
        libros_encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        if libros_encontrados:
            print(f"\nLibros encontrados del autor '{autor}':")
            for libro in libros_encontrados:
                print(libro)
        else:
            print(f"No se encontraron libros del autor '{autor}'.")