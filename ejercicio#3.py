class Habitacion:
    def __init__(self, tipo, precio, cantidad_disponible):
        self.tipo = tipo
        self.precio = precio
        self.cantidad_disponible = cantidad_disponible

class ServicioExtra:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Hotel:
    def __init__(self):
        self.habitaciones = []
        self.servicios_extra = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def agregar_servicio_extra(self, servicio):
        self.servicios_extra.append(servicio)

    def realizar_reserva(self, habitacion, cantidad, nombre_cliente, noches):
        try:
            if habitacion in self.habitaciones:
                if habitacion.cantidad_disponible >= cantidad:
                    habitacion.cantidad_disponible -= cantidad
                    total_habitacion = habitacion.precio * cantidad * noches
                    self.reservas.append({
                        "cliente": nombre_cliente,
                        "habitacion": habitacion.tipo,
                        "cantidad": cantidad,
                        "noches": noches,
                        "total_habitacion": total_habitacion,
                        "servicios_extra": []
                    })
                    return total_habitacion
                else:
                    raise ValueError("No hay suficientes habitaciones disponibles")
            else:
                raise ValueError("La habitación no existe en el hotel")
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def agregar_servicio_a_reserva(self, nombre_cliente, servicio, cantidad):
        try:
            for reserva in self.reservas:
                if reserva["cliente"] == nombre_cliente:
                    total_servicio = servicio.precio * cantidad
                    reserva["servicios_extra"].append((servicio.nombre, cantidad, total_servicio))
                    return total_servicio
            raise ValueError("Reserva no encontrada")
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def calcular_total_reserva(self, nombre_cliente):
        try:
            for reserva in self.reservas:
                if reserva["cliente"] == nombre_cliente:
                    total_servicios = sum(s[2] for s in reserva["servicios_extra"])
                    return reserva["total_habitacion"] + total_servicios
            raise ValueError("Reserva no encontrada")
        except ValueError as e:
            print(f"Error: {e}")
            return None

def menu():
    print("Hotel de Playa")
    print("1. Agregar habitación")
    print("2. Realizar reserva")
    print("3. Agregar servicio extra a reserva")
    print("4. Calcular total de reserva")
    print("5. Salir")

def main():
    hotel = Hotel()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Ingrese el tipo de habitación: ")
            precio = float(input("Ingrese el precio por noche: "))
            cantidad = int(input("Ingrese la cantidad disponible: "))
            hotel.agregar_habitacion(Habitacion(tipo, precio, cantidad))
            print("Habitación agregada con éxito")

        elif opcion == "2":
            print("Habitaciones disponibles:")
            for i, habitacion in enumerate(hotel.habitaciones):
                print(f"{i+1}. {habitacion.tipo} - Precio: {habitacion.precio} - Cantidad disponible: {habitacion.cantidad_disponible}")
            habitacion_seleccionada = int(input("Seleccione la habitación que desea reservar: ")) - 1
            cantidad = int(input("Ingrese la cantidad de habitaciones a reservar: "))
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            noches = int(input("Ingrese el número de noches de estancia: "))
            total = hotel.realizar_reserva(hotel.habitaciones[habitacion_seleccionada], cantidad, nombre_cliente, noches)
            if total:
                print(f"Reserva realizada con éxito. Total: {total}")

        elif opcion == "3":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            print("Servicios extra disponibles:")
            for i, servicio in enumerate(hotel.servicios_extra):
                print(f"{i+1}. {servicio.nombre} - Precio: {servicio.precio}")
            servicio_seleccionado = int(input("Seleccione el servicio extra: ")) - 1
            cantidad = int(input("Ingrese la cantidad del servicio: "))
            total_servicio = hotel.agregar_servicio_a_reserva(nombre_cliente, hotel.servicios_extra[servicio_seleccionado], cantidad)
            if total_servicio:
                print(f"Servicio agregado con éxito. Total servicio: {total_servicio}")

        elif opcion == "4":
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            total_reserva = hotel.calcular_total_reserva(nombre_cliente)
            if total_reserva:
                print(f"El total de la reserva es: {total_reserva}")

        elif opcion == "5":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()