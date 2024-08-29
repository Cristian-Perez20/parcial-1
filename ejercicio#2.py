from datetime import datetime, timedelta

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjeta_prestamo = []

class Prestamo:
    def __init__(self, libro, fecha_prestamo, fecha_devolucion):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.fecha_limite = fecha_prestamo + timedelta(days=15)  # Plazo de 15 días para devolver el libro
        self.sancion = 0

    def verificar_sancion(self):
        # Verifica si la fecha de devolución excede la fecha límite
        if self.fecha_devolucion > self.fecha_limite:
            dias_retraso = (self.fecha_devolucion - self.fecha_limite).days
            self.sancion = dias_retraso * 5  # Por ejemplo, $5 de multa por día de retraso
            print(f"El libro '{self.libro.titulo}' tiene un retraso de {dias_retraso} días. Sanción: ${self.sancion}.")
        else:
            print(f"El libro '{self.libro.titulo}' fue devuelto a tiempo.")

class Biblioteca:
    def __init__(self):
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def registrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def prestar_libro(self, usuario, libro):
        if libro in self.libros:
            fecha_prestamo = datetime.now()
            prestamo = Prestamo(libro, fecha_prestamo, None)
            usuario.tarjeta_prestamo.append(prestamo)
            self.libros.remove(libro)
            print(f"{usuario.nombre} ha tomado prestado el libro '{libro.titulo}' el {fecha_prestamo.strftime('%Y-%m-%d %H:%M')}.")
        else:
            print(f"El libro '{libro.titulo}' no está disponible en la biblioteca.")

    def devolver_libro(self, usuario, libro):
        # Busca el préstamo correspondiente en la tarjeta del usuario
        for prestamo in usuario.tarjeta_prestamo:
            if prestamo.libro == libro and prestamo.fecha_devolucion is None:
                fecha_devolucion = datetime.now()
                prestamo.fecha_devolucion = fecha_devolucion
                prestamo.verificar_sancion()
                self.libros.append(libro)
                print(f"{usuario.nombre} ha devuelto el libro '{libro.titulo}' el {fecha_devolucion.strftime('%Y-%m-%d %H:%M')}.")
                return
        print(f"No se encontró un préstamo activo del libro '{libro.titulo}' para {usuario.nombre}.")

biblioteca = Biblioteca()

libro1 = Libro("Alicia en el país de las maravillas", "Lewis Carroll")
libro2 = Libro("La ladrona de libros", "Markus Zusak")
libro3 = Libro("1984", "George Orwell")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

usuario1 = Usuario("Kim Seok Jin")
usuario2 = Usuario("Jung Hoseok")
usuario3 = Usuario("Kim NamJoon")

biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Préstamo de libros
biblioteca.prestar_libro(usuario1, libro1)
biblioteca.prestar_libro(usuario2, libro2)

# Simular el paso del tiempo para prueba de devolución con retraso
import time
time.sleep(1)  # Simular el paso de 1 segundo

# Devolución de libros (uno a tiempo, otro con retraso)
biblioteca.devolver_libro(usuario1, libro1)  # Devuelve a tiempo
time.sleep(1)  # Simula otro segundo
biblioteca.devolver_libro(usuario2, libro2)  # Devuelve con retraso 